import time
import os
import re
import csv
import random
import argparse
import urllib
import urllib.request
import itertools
import bs4
from bs4 import BeautifulSoup
import multiprocessing
from multiprocessing.dummy import Pool

artist_list = []

with open('artist_list.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        artist_list.append(line[0])

output_dir = "artists_scraped"

num_downloaded = 0
num_images = 0

def get_painting_list_by_artist(artist_name):

    try:
        artist_name = artist_name[0]
        time.sleep(3.0*random.random())  # random sleep to decrease concurrence of requests
        # go to the wikiart page that has a list of all works by a given artist
        url = "https://www.wikiart.org/en/"+artist_name+"/all-works/0"
        # get the soup of the webpage
        soup = BeautifulSoup(urllib.request.urlopen(url), "lxml")
        # set up a regex which will get the name of each painting
        regex = r'<a href="/en/'+artist_name+'/(.*?)">'
        # apply the regex to the soup
        painting_name_list = re.findall(regex, str(soup.html()))
        # get only unqique names
        painting_name_list = list(set(painting_name_list))
        #construct the url which holds the high-res images
        url_list = []
        for name in painting_name_list:
            num = str(random.randint(0,9))
            full_url = "https://uploads"+num+".wikiart.org/images/"+artist_name+"/"+name+".jpg"
            url_list.append(full_url)

        return url_list

    except Exception as e:
        print('failed to scrape %s'%artist_name, e)

def downloader(link, output_dir, failed_urls):
    global num_downloaded, num_images
    item, file = link
    filepath = file.split('/')
    savepath = '%s/%s-%s' % (output_dir, filepath[-2],filepath[-1])
    try:
        time.sleep(0.2)  # try not to get a 403
        urllib.request.urlretrieve(file, savepath)
        num_downloaded += 1
        if num_downloaded % 100 == 0:
            print('downloaded number %d / %d...' % (num_downloaded, num_images))
    except Exception as e:
        print("failed downloading " + str(file), e)
        failed_urls.append(link)


def main(artist_list, output_dir):
    start = time.time()
    global num_images
    print('gathering links to images...')
    # create a threadpool with one less than the total number of CPUs of the machine
    # this allows fast multiprocessing w/out overloading the machine
    threadpool = Pool(multiprocessing.cpu_count()-1)

    # use imap to run the function
    # different threads get different first inputs (numbers)
    # but typep and searchword are repeated
    wikiart_pages = threadpool.imap(get_painting_list_by_artist, zip(artist_list))

    # close and join the threadpool as per recommended usage
    threadpool.close()
    threadpool.join()

    # convert the wikiart iterator into
    pages = [page for page in wikiart_pages if page ]
    items = [item for sublist in pages for item in sublist]
    num_images = len(items)

    if not os.path.isdir('%s/'%(output_dir)):
        os.mkdir('%s/'%(output_dir))

    threadpool = Pool(multiprocessing.cpu_count()-1)

    failed_urls = []
    print('attempting to download %d images'%num_images)
    threadpool.starmap(downloader, zip(enumerate(items), itertools.repeat(output_dir), itertools.repeat(failed_urls)))

    # close and join the threadpool as per recommended usage
    threadpool.close()
    threadpool.join()

    print ("Took %d seconds to complete the first run."%(time.time()-start))
    print ("Attempting to gather the failed URLs")

    # Fix failed urls
    corrected_urls = []
    for i,url in enumerate(failed_urls):
        #show progress
        if i %100 == 0:
            print (str(i)+" out of " +str(len(failed_urls)))
        # extract the correct part of the url
        url = url[1]
        extracted = re.findall(r'/images/(.*?).jpg', url)
        full_url = "https://www.wikiart.org/en/" + extracted[0]

        # get the soup from the page
        soup = BeautifulSoup(urllib.request.urlopen(full_url), "lxml")
        #try jpg
        regex = r'<meta content="https://uploads[0-9].wikiart.org(.*?).jpg'
        corrected_link = re.search(regex, str(soup.html()))

        success = False
        if corrected_link:
            full_correct_url = corrected_link.group(0)[15:]
            corrected_urls.append(full_correct_url)
            success = True
        else:
            #try other file formats
            reg_list = [r'<meta content="https://uploads[0-9].wikiart.org(.*?).png',
                        r'<meta content="https://uploads[0-9].wikiart.org(.*?).jpeg',
                        r'<meta content="https://uploads[0-9].wikiart.org(.*?).Jpeg',
                        r'<meta content="https://uploads[0-9].wikiart.org(.*?).JPG',
                        r'<meta content="https://uploads[0-9].wikiart.org(.*?).PNG',]
            for regex in reg_list:
                if success == False:
                    corrected_link = re.search(regex, str(soup.html()))
                    if corrected_link:
                        full_correct_url = corrected_link.group(0)[15:]
                        corrected_urls.append(full_correct_url)
                        success = True
        if success == False:
            print("fail: "+full_url)

    print ("Downloading corrected URLs")
    threadpool = Pool(multiprocessing.cpu_count()-1)

    failed_urls_v2 = []
    threadpool.starmap(downloader, zip(enumerate(corrected_urls), itertools.repeat(output_dir), itertools.repeat(failed_urls_v2)))

    # close and join the threadpool as per recommended usage
    threadpool.close()
    threadpool.join()

    print ("Took %d seconds to complete."%(time.time()-start))


if __name__ == '__main__':
    main(artist_list, output_dir)
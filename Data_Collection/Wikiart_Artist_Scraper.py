from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import random
import re
import shutil
import requests

def get_name(url):
    # Gets the name, which starts after /jean-michel-basquiat/
    # and ends with a ., we use \. to escape the . in regex
    result = re.search('/jean-michel-basquiat/(.*)\.', url)
    return result.group(1)



driver = webdriver.Chrome('./chromedriver')

driver.get("https://www.python.org")

time.sleep(5)

counter = 1

# the first painting in the list
driver.get("https://www.wikiart.org/en/jean-michel-basquiat/portrait-of-shannon-dawson")

while counter <= 156:

    #only click to the next page after the first iteration
    if counter != 1:
        # click to the next page
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/section[1]/main/div[1]/div[2]/a[2]").click()

    img_link_list = []

    # get the image link
    img_link = driver.find_element_by_xpath("/html/body/div[2]/div[1]/section[1]/main/div[2]/aside/div[1]/img").get_attribute("src")

    # Wikiart stores smaller versions of the image by
    # appending something like !Large.jpg at the end of the URL
    # deleting this gives the full sized verison
    if img_link[-10:] == "!Large.jpg" or img_link[-10:] == "!Large.png" or img_link[-10:] == "!Large.PNG":
        img_link = img_link[:-10]

    if img_link[-11:] == "!Large.jpeg":
        img_link = img_link[:-11]


    img_link_list.append(img_link)

    # download the image
    url = img_link
    response = requests.get(url, stream=True)
    name = get_name(img_link)
    with open('./files/'+name+'.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

    counter +=1

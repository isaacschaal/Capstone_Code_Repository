# This script applies a variety of augmentations to target images.
# It applies a total of 15 color, sharpness, and contrast shifts
# and thus creates a dataset 16 times that of the original (including the oringal images)

# This script is a modified version of a script from Gwern’s StyleGAN Blog post, which can be found at
# https://www.gwern.net/Faces

# Creat the augment function
dataAugment () {
    image="$@"
    target=$(basename "$@")

    convert -blue-shift 1.1                "$image" "$target".midnight.jpg
    convert -fill red -colorize 5%         "$image" "$target".red.jpg
    convert -fill orange -colorize 5%      "$image" "$target".orange.jpg
    convert -fill yellow -colorize 5%      "$image" "$target".yellow.jpg
    convert -fill green -colorize 5%       "$image" "$target".green.jpg
    convert -fill blue -colorize 5%        "$image" "$target".blue.jpg
    convert -fill purple -colorize 5%      "$image" "$target".purple.jpg
    convert -adaptive-blur 3x2             "$image" "$target".blur.jpg
    convert -adaptive-sharpen 4x2          "$image" "$target".sharpen.jpg
    convert -brightness-contrast 10        "$image" "$target".brighter.jpg
    convert -brightness-contrast 10x10     "$image" "$target".brightercontraster.jpg
    convert -brightness-contrast -10       "$image" "$target".darker.jpg
    convert -brightness-contrast -10x10    "$image" "$target".darkerlesscontrast.jpg
    convert +level 5%                      "$image" "$target".contraster.jpg
    convert -level 5%\!                    "$image" "$target".lesscontrast.jpg
  }

# Export it
export -f dataAugment

# Apply the function to the target images
# The "photos" folder should be changed to whatever folder the images you want to process are in
find photos/ -type f | parallel --progress dataAugment


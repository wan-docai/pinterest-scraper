from urllib.request import urlretrieve
import csv

#change txt name to merge healthy/unhealthy big file
## double check save path before process
with open ('Fruits_dish_pins_test.txt') as images:
    images = csv.reader(images)
    img_count = 1
    for image in images:
        urlretrieve(image[0],
                'images/healthy/image_{0}.jpg'.format(img_count))
        img_count += 1

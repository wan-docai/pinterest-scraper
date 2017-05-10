# Pinterest Image Scraper

Now you can take the URL to any Pinterest board (or a CSV of a bunch of boards) and return a Python list of the URLs to the hi-rez versions of all of the images on the board.

## Requirements:

- Python 2.7
- Pandas (pip install pandas)
- Selenium (pip install selenium)
- [Chrome driver](https://sites.google.com/a/chromium.org/chromedriver/) ( Download and place in the directory)
- hashlib (pip install hashlib)
- cPickle 
- A [Pinterest](http://www.pinterest.com) Account

## How to Run:

```
git clone https://github.com/ankitshekhawat/pinterest-image-scraper.git
cd pinterest-image-scraper
import scraper as s
ph = s.Pinterest_Helper(<Pinterst login> , <Pinterest password>)
images = ph.runme("http://URL-to-image-board")
```

### Or if you have a CSV file with a URL to a different image board on every line:

```
...
images = ph.runme(imageboards.csv)
```

### Cache file
`runme()` also creates a cache file (cache.p) 
To download the files listed in cache use 
```
...
ph.downolad() 
```

This will download all the urls listed in the cache file to `./data/temp/`

### Custom labels
If you want to separate project, you can use labels argument in the constructor 
```
ph = s.Pinterest_Helper(<Pinterst login> , <Pinterest password>, label ='cats')
```
This will create a separate "cats.p" cache file
Using `download()` function will download the file to `./data/cats`

### Custom download directory
Use Directory argument to specify where the files should be downloaded. (Default is `./data/`)
```
ph = s.Pinterest_Helper(<Pinterst login> , <Pinterest password>, directory ='<Download DIR>')
# This will now download files to ./<Download DIR>/<Label Name>
```

### Disable initialising browser
Use `browser=False` to disable selenium browser. Useful only when just downloading the files from cache.

# Changes
- [x] Pinterest now uses /474x/ files instead of /236x/ . So changed it to 474x in the url search
- [x] Changed to Chrome driver
- [x] Using MD5 Checksum on urls to prevent re-downloading and duplicate images.
- [x] Caching using cPickle


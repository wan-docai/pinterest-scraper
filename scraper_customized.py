#!/usr/bin/env python3
# coding: utf-8
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import copy
import random
import socket
import sys
import time
import unicodedata
import urllib
from subprocess import call
from pyvirtualdisplay import Display
import os

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

try:
    from config import PINTEREST_PASSWORD, PINTEREST_USERNAME
except Exception as e:
    print(e)

def randdelay(a, b):
    time.sleep(random.uniform(a, b))


def u_to_s(uni):
    return unicodedata.normalize('NFKD', uni).encode('ascii', 'ignore')


class PinterestHelper(object):

    def __init__(self, login, pw, download=True):
        self.download = download
        # self.browser = webdriver.Firefox()
        # display = Display(visible=0, size=(800, 800))
        # display.start()
        self.browser = webdriver.Chrome()
        self.browser.get("https://www.pinterest.com")
        email_elem = self.browser.find_element_by_name('id')
        email_elem.send_keys(login)
        password_elem = self.browser.find_element_by_name('password')
        password_elem.send_keys(pw)
        password_elem.send_keys(Keys.RETURN)
        randdelay(2, 4)

    def runme(self, url, threshold=500):
        final_results = []
        previmages = []
        tries = 0
        try:
            self.browser.get(url)
            while threshold > 0:
                try:
                    results = []
                    images = self.browser.find_elements_by_tag_name("img")
                    if images == previmages:
                        tries += 1
                    else:
                        tries = 0
                    if tries > 20:
                        return final_results
                    for i in images:
                        src = i.get_attribute("src")
                        if src:
                            if src.find("/236x/") != -1 or src.find("/474x/") != 1:
                                print(src)
                                src = src.replace("/236x/", "/736x/")
                                src = src.replace("/474x/", "/736x/")
                                results.append(u_to_s(src))

                    previmages = copy.copy(images)
                    final_results = list(set(final_results + results))
                    dummy = self.browser.find_element_by_tag_name('a')
                    dummy.send_keys(Keys.PAGE_DOWN)
                    randdelay(0, 1)
                    threshold -= 1
                except StaleElementReferenceException:
                    threshold -= 1
        except (socket.error, socket.timeout):
            pass
        return final_results

    def close(self):
        """ Closes the browser """
        self.browser.close()


def main():
    if len(sys.argv) > 1:
        for i in range(2, len(sys.argv)-1):
            term = sys.argv[i]
    # else:
    #     print("\n\n[Error] Need arguments in this format:")
    #     print("pinScraper.py <search term> <destination dir[optional]>\n\n")
    #     exit()
            ph = PinterestHelper(PINTEREST_USERNAME, PINTEREST_PASSWORD)
            is_url = urllib.parse.urlparse(term)
            if is_url.scheme and is_url.netloc:
                images = ph.runme(term)
            else:
                images = ph.runme('http://pinterest.com/search/pins/?q=' + urllib.parse.quote(term))
            print(images)
            ph.close()
            with open(os.path.join(sys.argv[1], term.replace(" ", "_") + "_pins.txt"), "w") as file:
                file.write('\n'.join([i.decode('UTF-8') for i in images]))
            if len(sys.argv) > 2:
                destination = sys.argv[-1] + "/" + term.replace(" ", "_")

            print(term, destination)
            # print(term)
            call('aria2c -i ./{}_pins.txt -d {} --continue --auto-file-renaming false'.format(term.replace(" ", "_"),
                                                                                              destination),
                 shell=True)
            time.sleep(360)


if __name__ == '__main__':
    main()
    #command line input format python scraper_customized.py (directory to save url txt file) (search term #can be multiple terms and separate by "") (directory to download)

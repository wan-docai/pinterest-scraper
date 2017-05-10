from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time,random,socket,unicodedata
import string, copy, time, hashlib, requests, os.path, os
import pandas as pd
import cPickle as pickle
from urlparse import urlparse

def randdelay(a,b):
    time.sleep(random.uniform(a,b))

def u_to_s(uni):
    return unicodedata.normalize('NFKD',uni).encode('ascii','ignore')

class Pinterest_Helper(object):
    
    def __init__(self, login, pw, label='temp', directory='data',browser=True):
        self.label = label
        self.directory = './'+ directory + '/'
        if browser:
            # self.browser = webdriver.Firefox()
            self.browser = webdriver.Chrome('./chromedriver') # you need to download chrome driver
            self.browser.get("https://www.pinterest.com")            
            emailElem = self.browser.find_element_by_name('id')
            emailElem.send_keys(login)
            passwordElem = self.browser.find_element_by_name('password')
            passwordElem.send_keys(pw)
            passwordElem.send_keys(Keys.RETURN)
            randdelay(2,4)
    
    def getURLs(self, urlcsv, threshold = 500):
        tmp = self.read(urlcsv)
        results = []
        for t in tmp:
            tmp3 = self.runme(t, threshold)
            results = list(set(results + tmp3))
        random.shuffle(results)
        return results
    
    def write(self, myfile, mylist):
        tmp = pd.DataFrame(mylist)
        tmp.to_csv(myfile, index=False, header=False)


    
    def read(self,myfile):
        tmp = pd.read_csv(myfile,header=None).values.tolist()
        tmp2 = []
        for i in range(0,len(tmp)):
            tmp2.append(tmp[i][0])
        return tmp2        
        


    def runme(self,url, threshold = 500):
        final_results = []
        previmages = []
        tries = 0
        try:
            data = pickle.load( open( self.label + ".p", "rb" ) )
        except Exception as e:
            open(self.label + ".p", 'a').close()
            data ={}

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
                            if string.find(src,"/474x/") != -1:
                                print src        
                                src = string.replace(src,"/474x/","/736x/")
                                data[hashlib.md5(u_to_s(src)).hexdigest()] = u_to_s(src)
                                pickle.dump( data, open( self.label+".p", "wb" ) )                               
                                results.append(u_to_s(src))
                    previmages = copy.copy(images)
                    final_results = list(set(final_results + results))
                    dummy = self.browser.find_element_by_tag_name('a')
                    dummy.send_keys(Keys.PAGE_DOWN)
                    # images[0].send_keys(Keys.PAGE_DOWN)
                    randdelay(0,1)
                    threshold -= 1
                except (StaleElementReferenceException):
                    threshold -= 1
        except (socket.error, socket.timeout):
            pass
        return final_results

    def download(self):
        """Download all the labels in file <label>.p"""
        try:
            data = pickle.load( open( self.label + ".p", "rb" ) )
        except Exception as e:
            raise e
        else:
            try:
                os.stat(self.directory+ self.label)
            except:
                os.mkdir(self.directory+ self.label)   
            for d in (data.keys()):
                print data[d]
                if not os.path.isfile(self.directory+ self.label + '/'+ d +'.jpg'):
                    try:
                        img_data = requests.get(data[d]).content
                        with open(self.directory+ self.label+'/'+ d + '.jpg', 'wb') as handler:
                            handler.write(img_data)
                    except Exception as e:
                        print(e)
                        time.sleep(3)
                    else:
                        data.pop(d)
                        pickle.dump( data, open( self.label + ".p", "wb" ) )
                elif os.path.isfile(self.directory+ self.label + '/'+ d +'.jpg'):
                    data.pop(d)
                    pickle.dump( data, open( self.label + ".p", "wb" ) )                                            
       
 
    def scrape_old(self, url):
        results = []
        self.browser.get(url)
        images = self.browser.find_elements_by_tag_name("img")
        for i in images:
            src = i.get_attribute("src")
            if src:
                if string.find(src,"/474x/") != -1:
                    src = string.replace(src,"/474x/","/736x/")
                    results.append(u_to_s(src))
        return results
            
        
        
        
        
    
    def close(self):
        self.browser.close()
    
    
    
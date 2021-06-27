from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import sqlite3
import time
import os
import datetime
import requests
import re
import math
import webbrowser

def parsePrice():
     
    f = open('ürünlinkleri.txt')
    num_lines = sum(1 for line in open('ürünlinkleri.txt'))
    print(num_lines)
    for i in range(num_lines):
        reader = f.readline()
        print(reader)
        url=reader
        if 'tozlu.com' in url :    
            driver.get(url)
            time.sleep(5)
            title = driver.find_element(By.CSS_SELECTOR,'div.ProductName').text
            print('title: ',title)
            summit_button = driver.find_element(By.CSS_SELECTOR,'li#liTabOzellikler a')
            summit_button.click()
            time.sleep(2)
            description = driver.find_element(By.CSS_SELECTOR,'div.webTab li#liTabOzellikler div#divTabOzellikler div.detay_aciklama').text
            print('description: ',description)
            imgcount = len(driver.find_elements(By.CSS_SELECTOR,'div#ProductDetailMain div.SmallImages div.AltImgCapSmallImg img'))
            print('imgcount: ',imgcount)
            price = driver.find_element(By.CSS_SELECTOR,'div.Formline.IndirimliFiyatContent span.spanFiyat').text
            def createFolder(directory):
                try:
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                except OSError:
                    print ('Error: Creating directory. ' +  directory)
            # Example
            createFolder('./{0}/'.format(title))
            slug = driver.find_element(By.CSS_SELECTOR,'meta[property="og:url"]')
            slugattribute = slug.get_attribute('content')
            slugattribute = slugattribute.replace('https://www.tozlu.com/','')
            print('slug attribute: ',slugattribute)
            for count in range(1,imgcount+1):
                tozluimg = driver.find_element(By.CSS_SELECTOR,'div#ProductDetailMain div.SmallImages div.AltImgCapSmallImg:nth-child({0}) img'.format(count))
                imgsrc = tozluimg.get_attribute('src')               
                print('imgsrc: ',imgsrc)
                response = requests.get(imgsrc)
                imgsrc = imgsrc.replace('https://img.tozlu.com/Uploads/UrunResimleri/thumb/','')
                path2 = './{0}/{1}'.format(title, imgsrc)      
                file = open(path2, "wb")
                file.write(response.content)
                file.close()
            oku = 'readme.txt'                
            path3 = './{0}/{1}'.format(title,oku)            
            file1 = open(path3,"x")
            file1.write("""
            Title : {0}\n
            Slug  : {1}\n
            Description: {2}\n
            Price = {3}\n
            """.format(title,slugattribute,description,price))
            time.sleep(2)

            
                
               

             


            


            


            






            

while True:

    print(str(parsePrice()))
    

    
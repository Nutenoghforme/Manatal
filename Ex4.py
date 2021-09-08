#Exercise 4: Scraping Test
#Write a Python program to get the number of followers of a specific account on Twitter (taking an url as an input, for example

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

input_url = input('Enter Twitter URL: ')
print(input_url)

driver = webdriver.Chrome()
driver.get(input_url)
time.sleep(3)

elems = driver.find_elements_by_tag_name("a")
for e in elems:
    href = e.get_attributed('href'
    if href is not None and '/followers' in href :
        span1 = e.find_elements_by_tag_name('span')
        span2 = span1.find_elements_by_tag_name('span') 
        print(span2.text)
driver.close()
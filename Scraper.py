from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from os import mkdir
PATH = "chromedriver.exe"
images_url = []
timeout = 3
searchindex = []


keywords = open('keywords.txt', 'r')

for x in keywords:
    searchindex.append(x.rstrip('\n'))


driver = webdriver.Chrome(PATH)
#switch to english
driver.get("https://www.google.com")


link = driver.find_element_by_link_text("English")

link.click()

for x in searchindex:
        search = driver.find_element_by_name("q")
        search.send_keys(x)
        search.send_keys(Keys.RETURN)
        link = driver.find_element_by_link_text("Images")
        link.click()
        driver.implicitly_wait(10)
        i = 0
        while i<7:  
            #for scrolling page
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            try:
                button = driver.find_element_by_class_name('mye4qd')
                button.send_keys(Keys.RETURN)
                time.sleep(2)
            except:
                pass
            time.sleep(0.5)
            i+=1
        #parsing
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        #closing web browser
        img_tags = soup.find_all("img", class_="rg_i")
        print("number of photos found for " + x + " = " + str(len(img_tags)))
        count = 0
        mkdir(x)
        for i in img_tags:
            try :
                driver.get(i['src'])
                try:
                    element_present = EC.presence_of_element_located((By.TAG_NAME, 'img'))
                    WebDriverWait(driver, timeout).until(element_present)
                except TimeoutException:
                    print("Timed out waiting for page to load")
                driver.save_screenshot(x + "\\" + str(count) + ".png")
                count += 1
            except:
                continue
        print("number of photos downloaded = " + str(count))
        driver.get("https://www.google.com")
        print("Downloaded " + str((count / len(img_tags)) * 100) + "% of images found for " + x)

keywords.close()
driver.close()
print("Web scraping succfull")

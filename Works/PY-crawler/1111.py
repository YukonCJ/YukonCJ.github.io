import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# res = requests.get('https://www.1111.com.tw/')
# html = res.text
# soup = BeautifulSoup(html,'html.parser')
# time.sleep(5)
# title = soup.find_all('class',{'class':'block_001'})

from selenium.webdriver.common.service import Service
from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("https://www.selenium.dev/selenium/web/web-form.html")

driver = webdriver.Edge()
# service = Service(executable_path=".\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=service)
driver.get("https://www.opentable.com.tw/")
html = driver.page_source

import os
from random import randint


soup = BeautifulSoup(html,'html.parser')

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "f6jjsVPP1WowHpgwF07q mzyEVpKa0PZ1EXuWTY6J"))
)

imgs = soup.find_all('img')
for i in range(4):
    try:
        url = 'https:'+imgs[i]['src']
        print(url)
        filename = imgs[i]['alt']
        res = requests.get(url)
        img = res.content
        os.makedirs('test_open',exist_ok=True)
        with open(f'test_open/{filename}.svg','wb') as f:
            f.write(img)
        time.sleep(randint(2,6))
    except:
        pass



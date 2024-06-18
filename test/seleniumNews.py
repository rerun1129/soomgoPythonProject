import time
import pymysql
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chromedriver = 'C:/dev/chromedriver.exe'
browser = webdriver.Chrome(service=Service(chromedriver), options=chrome_options)

browser.get("https://n.news.naver.com")

browser.implicitly_wait(10)
browser.maximize_window()

# 브라우저가 실행될때까지 인터벌 주기
time.sleep(2)

elements = browser.find_elements(By.CSS_SELECTOR, 'a')
iterators = []
for e in elements:
    attribute = e.get_dom_attribute('href')
    if attribute.startswith('https://n.news.naver.com/article'):
        iterators.append(attribute)

time.sleep(5)
for iterator in iterators:
    browser.get(iterator)
    time.sleep(2)

time.sleep(5)

browser.quit()

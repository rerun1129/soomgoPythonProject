import time
from selenium.webdriver.support import expected_conditions as EC

import pymysql
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chromedriver = 'C:/dev/chromedriver.exe'
browser = webdriver.Chrome(service=Service(chromedriver), options=chrome_options)

browser.get("https://blog.naver.com/h2831991/223458670410")

browser.implicitly_wait(10)
browser.maximize_window()

# 브라우저가 실행될때까지 인터벌 주기
time.sleep(2)

# iframe 요소 찾기
iframe = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "mainFrame"))
)

# iframe으로 전환
browser.switch_to.frame(iframe)

join = ''

elements = browser.find_elements(By.CSS_SELECTOR, 'p span.se-fs-.se-ff-')
for element in elements:
    stripped_text = element.text.strip('\n')
    if stripped_text == '':
        continue
    else:
        join += stripped_text + '\n'

print(join)
browser.quit()

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# WebDriverの初期化
driver = webdriver.Chrome()

# Webページにアクセス
driver.get("https://www.bing.com/")

# 要素を取得
search_bar = driver.find_element(By.ID, 'sb_form_q')
search_bar.send_keys('python')

search_btn = driver.find_element(By.XPATH, '//label[@for="sb_form_go"]')
# search_btn.click()
# search_btn.submit()
search_btn.send_keys(Keys.ENTER)

driver.quit()

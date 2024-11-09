from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get('https://www.bing.com/')

search_bar = driver.find_element(By.ID, 'sb_form_q')
search_bar.send_keys('python')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome("C:\GIT\Skillfactory\python_selenium_sf\chromedriver")
driver.get("https://community.payoneer.com/ru/")
driver.find_element(By.XPATH,"//*[@id="search-0-searchInput"]").send_keys('facebook' + Keys.RETURN)
sleep(2)
driver.save_screenshot('sf.png')
#driver.quit()
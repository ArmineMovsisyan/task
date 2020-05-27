from selenium import webdriver
from webdriver_manager.webdriver.chromedriver import Chromedriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.joomag.com/")git stash 
elements = driver.find_elements_by_xpath('//*[contains(text(), ".get")]')
driver.switch_to.frame('_hjRemoteVarsFrame')
element = driver.find_element_by_xpath('//*[contains(text(), ".get")]')
elements.append(element)
print(len(elements))


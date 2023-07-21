from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
sr = Service("C:/Users/Priyanshi Sutariya/Desktop/selenim/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=sr)
driver.get("https://www.instagram.com")
time.sleep(100)
username = driver.find_element_by_xpath("""//*[@id="loginForm"]/div/div[1]/div/label/input""")
username.send_keys("YOUR_USERNAME")
password = driver.find_element_by_xpath("""//*[@id="loginForm"]/div/div[2]/div/label/input""")
password.send_keys("YOUR_PASSWORD")
password.send_keys(Keys.ENTER)

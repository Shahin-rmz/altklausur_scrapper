#m0
#imports
##
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
##

#m1
#login
##
driver=webdriver.Chrome("/usr/bin/chromedriver")
driver.get('https://www.altklausurendb.de/login.php')
wait1 = WebDriverWait(driver,timeout=12)
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="login_username"]').send_keys('shahin')
driver.find_element(By.XPATH,'//*[@id="login_password"]').send_keys('7aDpCS4PjxWB')
driver.find_element(By.XPATH,'/html/body/div/div/form/fieldset/input[5]').click()

time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav_top_mobile"]/a[4]').click()
print('menu')
driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/a[5]').click()
##

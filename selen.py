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
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="login_username"]').send_keys('shahin')
driver.find_element(By.XPATH,'//*[@id="login_password"]').send_keys('7aDpCS4PjxWB')
driver.find_element(By.XPATH,'/html/body/div/div/form/fieldset/input[5]').click()

time.sleep(2)
#Clicking on Discussion tab on the menu
driver.find_element(By.XPATH,'//*[@id="nav_top_mobile"]/a[4]').click()
time.sleep(1)
#click on 5th Semster
driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/a[5]').click()
time.sleep(1)
#clicking on module1 (patho) 
driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/a[1]').click()
#for loop should begin here
#choosing the year
#***this should be changed every time***#

years = driver.find_elements(By.XPATH,'//*[@id="content"]/div[2]/a')
print(years)
for year in years:
    time.sleep(1)
    year.click()
    questions = driver.find_elements(By.XPATH,'//*[@id="content"]/div[2]/a')
    #click on the first question
    driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/a[1]').click()
    for question in range(len(questions)):
        try:
            time.sleep(1)
        #question drawer
            driver.find_element(By.XPATH,'//*[@id="draw_question_header"]').click()
            time.sleep(1)
        #    #print question
            print(driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[3]/div[2]/div[1]/p[1]').text)
        #    #print A
            print(driver.find_element(By.XPATH,'//*[@id="draw_question_main"]/p[3]').text)
        #    #print loesung
            print(driver.find_element(By.XPATH,'//*[@id="draw_question_footer"]/p[1]').text)
        #    #print erklaerung
            print(driver.find_element(By.XPATH,'//*[@id="draw_question_footer"]/p[3]').text)
            #next question
            driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/a[3]').click()
        except:
            #next question
            time.sleep(1)
            driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/a[3]/i').click()
            #go to year part 
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/span[1]/span/a[1]/i').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/span[1]/span/a[1]/i').click()
##

#m0
#imports
##
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json
from pymongo import MongoClient,errors
##



##
DOMAIN = '172.18.0.2'
PORT = 27017
host = "mongodb://root:mongolak@172.18.0.2:27017"
DB_NAME = "altfragen"
client = MongoClient(host)
db = client.altfragen
csv_name = input('name the csv: ')
collection = db[csv_name]
print(client.server_info())
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
path_to_year_of_questions = input('Paste the path to the year of the questions: ')
driver.find_element(By.XPATH,path_to_year_of_questions).click()
time.sleep(1)
questions = driver.find_elements(By.XPATH,'//*[@id="content"]/div[2]/a')
driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/a[1]').click()
# get the number of question
num = 1
for question in range(len(questions)):
    dic1 = {}
    try:
        time.sleep(1)
        #question drawer
        driver.find_element(By.XPATH,'//*[@id="draw_question_header"]').click()
        time.sleep(1)
    except:
        pass
        #print question
    try:
        dic1['frage']=(driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[3]/div[2]/div[1]/p[1]').text)
        #check if there is a picture
        if driver.find_element(By.XPATH,'//*[@id="draw_question_main"]/div/img'):
            dic1['frage']= '* '+ dic1['frage']
    except:
        pass
        #print A
    try:
        dic1['option1']=(driver.find_element(By.XPATH,'//*[@id="draw_question_main"]/p[3]').text)
        if dic1['option1'] == '(A)':
            dic1['option1']=(driver.find_element(By.XPATH,'//*[@id="draw_question_main"]/p[4]').text)
    except:
        pass
        #print B
    try:

        dic1['option2']=(driver.find_element(By.XPATH,'//*[@id="draw_question_main"]/p[5]').text)
        if dic1['option2'] == '(B)':
            dic1['option2']=(driver.find_element(By.XPATH,'//*[@id="draw_question_main"]/p[6]').text)
    except:
        pass
        #print C
    try:
        dic1['option3']=(driver.find_element(By.XPATH,'//*[@id="draw_question_main"]/p[7]').text)
        if dic1['option3'] == '(C)':
            dic1['option3']=(driver.find_element(By.XPATH,'//*[@id="draw_question_main"]/p[8]').text)
    except:
        pass
        #print D
    try:
        dic1['option4']=(driver.find_element(By.XPATH,'//*[@id="draw_question_main"]/p[9]').text)
        if dic1['option4'] == '(D)':
            dic1['option4']=(driver.find_element(By.XPATH,'//*[@id="draw_question_main"]/p[10]').text)
    except:
        pass
        #print E
    try:
        dic1['option5']=(driver.find_element(By.XPATH,'//*[@id="draw_question_main"]/p[11]').text)
        if dic1['option5'] == '(E)':
            dic1['option1']=(driver.find_element(By.XPATH,'//*[@id="draw_question_main"]/p[12]').text)
    except:
        pass
#print loesung
    try:
        dic1['ans']=(driver.find_element(By.XPATH,'//*[@id="draw_question_footer"]/p[1]').text)
    except:
        pass
        #print erklaerung
    try:
        dic1['explain']=(driver.find_element(By.XPATH,'//*[@id="draw_question_footer"]/p[3]').text)
    except:
        pass
        #next question
    try:
        driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/a[3]').click()
    except:
        pass
    try:
        dic1['number']=num
        num +=1
    except:
        pass
      #  insertion = collection.insert_one(dic1)
    try:
        result = collection.insert_one(dic1)
    except:
        #next question
        result = collection.insert_one(dic1)
        num +=1
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/a[3]/i').click()
##


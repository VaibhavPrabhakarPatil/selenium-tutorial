#Navigation Example
"""from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.youtube.com/@armystudybijusir")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
"""
# Locators Example Find _element_by_(id,name,link_text,class_name) Action (.send_keys(),.click(),.text)
"""from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://apis.reebootz.com/admin")
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("Vaibhav Patil")
time.sleep(1)
driver.find_element(By.CLASS_NAME,"waves-light").click()
Extext = driver.find_element(By.CLASS_NAME,"waves-light").text
print("button text",Extext)
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
time.sleep(3)
"""

#Css Selector(Locator)(Attribute & value , ID , Class) Console check syntax $("tagname[attribute='value']")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import  time

service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
drive = webdriver.Chrome(service=service)
drive.get("https://www.rahulshettyacademy.com/AutomationPractice/")
drive.find_element(By.CSS_SELECTOR,"input[value='radio1']").click() #Attribute & value
#drive.find_element(By.CSS_SELECTOR,"#name").send_keys("Vaibhav Patil") #ID
drive.find_element(By.CSS_SELECTOR,".inputs").send_keys("Vaibhav Prabhakar Patil")#class
time.sleep(5)#this is timer







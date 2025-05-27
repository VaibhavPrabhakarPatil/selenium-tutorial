#Navigation Example
import time

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# driver.get("https://www.youtube.com/@armystudybijusir")
# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)

# Locators Example Find _element_by_(id,name,link_text,class_name) Action (.send_keys(),.click(),.text)

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# driver.get("https://apis.reebootz.com/admin")
# username_input = driver.find_element(By.ID, "username")
# username_input.send_keys("Vaibhav Patil")
# time.sleep(1)
# driver.find_element(By.CLASS_NAME,"waves-light").click()
# Extext = driver.find_element(By.CLASS_NAME,"waves-light").text
# print("button text",Extext)
# time.sleep(3)
# driver.find_element(By.LINK_TEXT,"Forgot password?").click()
# time.sleep(3)


#Css Selector(Locator)(Attribute & value , ID , Class) Console check syntax $("tagname[attribute='value']")

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import  time
# service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
# drive = webdriver.Chrome(service=service)
# drive.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# drive.find_element(By.CSS_SELECTOR,"input[value='radio1']").click() #Attribute & value
# #drive.find_element(By.CSS_SELECTOR,"#name").send_keys("Vaibhav Patil") #ID
# drive.find_element(By.CSS_SELECTOR,".inputs").send_keys("Vaibhav Prabhakar Patil")#class
# time.sleep(5)

#XPATH Locator (parents to child , parents to last child , Grand Parents to child , text, )

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
# drive = webdriver.Chrome(service=service)
# drive.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# drive.find_element(By.XPATH,"//input[@value='radio1']").click() # Button Click Example
# text1 = drive.find_element(By.XPATH,"//legend[text()='Checkbox Example']").text # text Example
# drive.find_element(By.XPATH,"//label[@for='benz']/input").click() # parents to child Example
# drive.find_element(By.XPATH,"//select[@id='dropdown-class-example']/option[last()]").click() # parents to child last () Example
# grandtext = drive.find_element(By.XPATH,"//div[@class='tableFixHead']/table/tbody/tr[3]/td[2]").text # Grand Parents to child Example
# drive.find_element(By.XPATH,"//option[starts-with@value,'option']") # start with example
# drive.find_element(By.XPATH,"*contains(@class,'npu')") # contains example input center value check
# drive.find_element(By.XPATH,"input[starts-with(@id,'nam') and contains (@name,'er-n')]") # start with and contains Example
# print(text1)
# print(grandtext)
# time.sleep(3)


#to select a multiple checkbox select (find_elements)

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
# drive = webdriver.Chrome(service=service)
# drive.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# checkboxes = drive.find_elements(By.XPATH,"//input[@type='checkbox']")
# for checkbox in checkboxes:
#     if checkbox == checkboxes[1]:
#         pass
#     else:
#         checkbox.click()
# print(len(checkboxes))
# time.sleep(10)

# static Dropdown exaples

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time
#
# service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
# drive = webdriver.Chrome(service=service)
# drive.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# static_dropdown = Select(drive.find_element(By.XPATH,"//select[@id='dropdown-class-example']"))
# static_dropdown.select_by_index(2)
# time.sleep(4)
# static_dropdown.select_by_value("option1")
# time.sleep(3)
# static_dropdown.select_by_visible_text("Option3")
# time.sleep(3)

#Dynamic Dropdown

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
# drive = webdriver.Chrome(service=service)
# drive.get("https://www.cleartrip.com/do/search/flights")
# drive.find_element(By.NAME,"from").send_keys("del")
# time.sleep(4)
# serch = drive.find_elements(By.XPATH,"//ul[@id='ui-id-1']/li/div")
# for serching in serch:
#     if serching.text == "Adelaide, AU - Adelaide (ADL)":
#         serching.click()
#     else:
#         pass
# time.sleep(3)

#Pop Alert Example

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
# drive = webdriver.Chrome(service=service)
# drive.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# drive.find_element(By.XPATH,"//input[@id='name']").send_keys("vaibhav patil")
# time.sleep(4)
# drive.find_element(By.XPATH,"//input[@id='alertbtn']").click()
# time.sleep(4)
# popup = drive.switch_to.alert
# print("Alert says:", popup.text)
# popup.accept()
# time.sleep(4)

#file upload testing & implicit-wait example

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
# drive = webdriver.Chrome(service=service)
# drive.implicitly_wait(10)
# drive.get("https://the-internet.herokuapp.com/upload")
# drive.find_element(By.XPATH,("//input[@id='file-upload']")).send_keys("C:\\Users\\vaibh\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-11-05 174344.png")
# time.sleep(4)
# drive.find_element(By.XPATH,"//input[@class='button']").click()

#mouse Action Testing & ActionChains Example

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
# drive = webdriver.Chrome(service=service)
# drive.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# action = ActionChains(drive)
# mouse_hover_button = drive.find_element(By.XPATH,"//button[@id='mousehover']")
# action.move_to_element(mouse_hover_button).perform()
# top_link = drive.find_element(By.LINK_TEXT,"Top")
# action.move_to_element(top_link).click().perform()

# mouse hover and Double Click and Right Click Example

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
#
# service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
# drive = webdriver.Chrome(service=service)
# drive.get("https://the-internet.herokuapp.com/context_menu")
# action = ActionChains(drive)
# Double_Click = drive.find_element(By.XPATH,"//div[@id='hot-spot']")
# action.context_click(Double_Click).perform() # context_Click means right click
# action.double_click(Double_Click).perform()

# Multiple Windows Handling Example

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# import time
#
# service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
# drive = webdriver.Chrome(service=service)
# drive.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# drive.find_element(By.XPATH,"//button[@id='openwindow']").click()
# print(drive.window_handles)
# time.sleep(2)
# drive.switch_to.window(drive.window_handles[1])
# drive.find_element(By.XPATH,"//li[@class='nav-item']//a[@href='about.html'][normalize-space()='About us']").click()
# drive.switch_to.window(drive.window_handles[0])

# Multiple Tab handling Example

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
# drive = webdriver.Chrome(service=service)
# drive.implicitly_wait(4)
# drive.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# drive.find_element(By.XPATH,"//a[@id='opentab']").click()
# Tab = drive.window_handles[1]
# drive.find_element(By.XPATH,"//button[@id='openwindow']").click()
# window2 = drive.window_handles[2]
# drive.switch_to.window(Tab)
# drive.find_element(By.XPATH,"//li[@class='nav-item']//a[@href='about.html'][normalize-space()='About us']").click()
# drive.switch_to.window(window2)
# drive.find_element(By.XPATH,"//a[@class='active']").click()

# Frames
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# import time
#
# service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
# drive = webdriver.Chrome(service=service)
# drive.implicitly_wait(20)
# drive.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# drive.switch_to.frame(drive.find_element(By.XPATH,"//iframe[@id='courses-iframe']"))
# drive.find_element(By.XPATH,"//div[@class='nav-outer clearfix']//nav[@class='main-menu']//div[@class='navbar-collapse collapse clearfix']//ul[@class='navigation clearfix']//li//a[@href='consulting'][normalize-space()='Job Support']").click()
# time.sleep(10)

# get Attribute Example means ex of placeholder name copy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
drive = webdriver.Chrome(service=service)
drive.get("https://www.rahulshettyacademy.com/AutomationPractice/")
placeholdernamecopy = drive.find_element(By.XPATH,"//input[@id='name']").get_attribute("placeholder")
print(placeholdernamecopy)


























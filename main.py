from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

#Verify Page Title
assert driver.title == "Swag Labs"

username_Element = driver.find_element(By.ID,"user-name")
pwd_Element=driver.find_element(By.ID,"password")
login_Button=driver.find_element(By.ID,"login-button")

username_Element.send_keys("standard_user")
pwd_Element.send_keys(By.ID,"secret_sauce")
login_Button.click()

#Add one of the item to cart
driver.implicitly_wait(10)
inventory_item=Web



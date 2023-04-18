from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://www.saucedemo.com/")

#Verify Page Title
assert driver.title == "Swag Labs"

username_Element = driver.find_element(By.ID,"user-name")
pwd_Element=driver.find_element(By.ID,"password")
login_Button=driver.find_element(By.ID,"login-button")

username_Element.send_keys("standard_user")
pwd_Element.send_keys("secret_sauce")
login_Button.click()

#Add one of the item to cart
driver.implicitly_wait(10)
inventory_item=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='inventory_item'][1]//div[@class='inventory_item_name']")))
inventory_item_name=inventory_item.text
print("Selected Item",inventory_item_name)
inventory_item.click()

add_cart=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
add_cart.click()

#Check Item is present in cart
cart_icon=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//a[@class='shopping_cart_link']")))
cart_icon.click()

if driver.find_elements(By.XPATH,"//div[@class='cart_list']/div[@class='cart_item']//div[@class='inventory_item_name' and text()='"+inventory_item_name+"']").__len__() == 1:
    print("PASSED - Item Added is present in the cart")
else:
    print("FAILED - Item Added is not present in the cart")

# Click on the left corner of the button and click on LOGOUT button
menu_button=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"react-burger-menu-btn")))
menu_button.click()
logout_button=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"logout_sidebar_link")))
logout_button.click()

driver.quit()



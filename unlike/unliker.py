import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="./geckodriver")

driver.get("http://www.facebook.com")
time.sleep(3)

email_field = driver.find_element(By.NAME, "email")
email_field.send_keys(os.environ.get('fb_email'))
pass_field = driver.find_element(By.NAME, "pass")
pass_field.send_keys(os.environ.get('fb_pass'))
pass_field.send_keys(Keys.RETURN)
time.sleep(3)

with open('pages', 'r') as pages_file:
    pages = pages_file.readlines()

removed = []
for page in pages:
    try:
        driver.get(page)
        time.sleep(4)
        try:
            follow = driver.find_element(By.XPATH, "//*[contains(text(),'Siguiendo')]")
            follow.click()
        except:
            follow = driver.find_element(By.XPATH, "//*[contains(text(),'Te gusta')]")
            follow.click()
        # import pdb; pdb.set_trace();
        time.sleep(2.5)
        label = driver.find_element(By.XPATH, "//*[contains(text(),'Dejar de seguir')]")
        label.click()
        time.sleep(2.5)
        confirm = driver.find_element(By.XPATH,  "//*[contains(text(),'Actualizar')]")
        confirm.click()
        time.sleep(4)
        removed.append(page)
    except Exception as e:
        print(f"Unable to unlike: {page}. Exception: {e}")

print(removed)
# driver.close()

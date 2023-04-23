from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime
import pytz
import random

load_dotenv()
# fixed variables
staff_email = os.getenv("YOUR_EMAIL")
APP_DATA = os.getenv("APPDATA")

# Load the Excel sheet into a Pandas dataframe
df = pd.read_excel(os.getenv('EXCEL_FILE'), sheet_name=os.getenv('SPREAD_SHEET'))


def find_profile(path, prfl_name):
    return next((os.path.join(path, fldr) for fldr in os.listdir(path) if prfl_name in fldr), None)


profiles = rf"{APP_DATA}\Mozilla\Firefox\Profiles"
profile_name = os.getenv("PROFILE_NAME") or 'default'

profile = webdriver.FirefoxProfile(find_profile(profiles, profile_name))

driver = webdriver.Firefox(profile)

# Open the Google Form
driver.get(os.getenv('FORM_URL'))

date = datetime.now(pytz.timezone('Asia/Kolkata'))
curr_date = date.strftime('%d-%m-%Y')
curr_month = date.strftime('%b-%y')

apprc_source_list = ['Facebook', 'Twitter', 'Google Review', 'Instagram']
apprc_src = random.choice(apprc_source_list)


def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


def text_input(label, value):
    if any(chctr.isdigit() for chctr in label):
        input_elem = driver.find_element(By.XPATH, f'//input[@aria-labelledby="{label}"]')
    else:
        input_elem = driver.find_element(By.XPATH, f'//input[@aria-label="{label}"]')
    try:
        input_elem.clear()
        input_elem.send_keys(value)
        time.sleep(0.1)
    except Exception as e:
        print(e)


def text_area(label, value):
    if input_elem := driver.find_element(By.XPATH, f'//textarea[@aria-labelledby="{label}"]'):
        try:
            input_elem.clear()
            input_elem.send_keys(value)
            time.sleep(0.1)
        except Exception as e:
            print(e)
    else:
        print('element not found')


def image(label, value):
    try:
        img = check_exists_by_xpath("//img[@alt='Image']")
        if not img:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(driver.find_element(By.XPATH, f'//div[@aria-label="{label}"]'))).click()
            # time.sleep(5)
            xpath = "document.querySelector('input[type=\"file\"]').style.display = ''"
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "(//iframe)[2]")))
            driver.switch_to.frame(driver.find_element(By.XPATH, "(//iframe)[2]"))
            time.sleep(1)
            driver.execute_script(xpath)
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@type='file']")))
            upload = driver.find_element(By.XPATH, "//input[@type='file']")
            upload.send_keys(value)
            time.sleep(2)
            driver.switch_to.default_content()
            time.sleep(2)
    except Exception as e:
        print(e)


def date_input(input_date):
    ddmmyyyy = input_date.split('-')
    labels = ['Day of the month', 'Month', 'Year']
    for i, val in enumerate(ddmmyyyy):
        if element := driver.find_element(By.XPATH, f"//input[@aria-label='{labels[i]}']"):
            try:
                element.send_keys(val)
            except Exception as e:
                print(e)


def drop_down(label, value):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, f'//div[@role="listbox" and @aria-labelledby="{label}"]'))).click()
    if element := driver.find_element(By.XPATH, f"//div[@role='option']//span[normalize-space()='{value}']"):
        try:
            element.click()
        except Exception as e:
            print(e)
    else:
        print('element not found')
    time.sleep(0.5)


def main():
    # Iterate through each row in the dataframe
    for index, row in df.iterrows():
        # Get the data from the dataframe
        sc_code = row['SC Code']
        customer_name = row['Customer Name']
        customer_phone = row['Customer phone']
        customer_email = row['Customer Email']
        repair_id = row['Repair order No.']
        staff = row['Staff']
        appreciation = row['Appreciation']

        image_path = os.path.join(os.getcwd(), os.getenv('IMAGE'))

        # Fill out the form with the data
        text_input('Your email', staff_email)

        # Select an option from the dropdown menu
        date_input(curr_date)
        drop_down('i9', curr_month)
        drop_down('i13', apprc_src)
        text_input('i17', sc_code)
        text_input('i21', customer_name)
        text_input('i25', customer_phone)
        text_input('i29', repair_id)
        text_input('i33', customer_email)
        text_input('i37', staff)
        text_area('i41', appreciation)
        text_area('i45', 'NA')
        image('Add file', image_path)
        # Submit the form
        submit_button = driver.find_element(By.XPATH, '//div[@role="button"]//span[text()="Submit"]')
        submit_button.click()
        time.sleep(1)
        driver.refresh()
    # Close the web driver
    driver.quit()


main()

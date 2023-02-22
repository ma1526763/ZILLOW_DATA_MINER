import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# google form link
GOOGLE_FROM_URL = os.environ['GOOGLE_FORM_LINK']
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# GOOGLE FORM FIELDS X_PATH ARE SAME EXCEPT one div
X_PATH_START = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div['
X_PATH_END = ']/div/div/div[2]/div/div[1]/div/div[1]/input'

# uploading data on Google form
def send_data_to_google_form(zillow):
    print("\nPlease wait while data is being uploaded through Google Form.")
    # creating Selenium driver
    driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    # loop though each address of house
    for i in range(len(zillow.property_street_address_list)):
        # accessing Google form
        driver.get(GOOGLE_FROM_URL)
        # wait until first element is clickable
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, f"{X_PATH_START}1{X_PATH_END}")))

        # uploading data for each question on Google form
        driver.find_element(By.XPATH, f'{X_PATH_START}1{X_PATH_END}').send_keys(zillow.property_street_address_list[i] if zillow.property_street_address_list[i] else "")
        driver.find_element(By.XPATH, f'{X_PATH_START}2{X_PATH_END}').send_keys(zillow.property_city_address_list[i] if zillow.property_city_address_list[i] else "")
        driver.find_element(By.XPATH, f'{X_PATH_START}3{X_PATH_END}').send_keys(zillow.property_state_address_list[i] if zillow.property_state_address_list[i] else "")
        driver.find_element(By.XPATH, f'{X_PATH_START}4{X_PATH_END}').send_keys(zillow.property_zipcode_address_list[i] if zillow.property_zipcode_address_list[i] else "")
        driver.find_element(By.XPATH, f'{X_PATH_START}5{X_PATH_END}').send_keys(zillow.property_latitude_list[i] if zillow.property_latitude_list[i] else "")
        driver.find_element(By.XPATH, f'{X_PATH_START}6{X_PATH_END}').send_keys(zillow.property_longitude_list[i] if zillow.property_longitude_list[i] else "")
        driver.find_element(By.XPATH, f'{X_PATH_START}7{X_PATH_END}').send_keys(zillow.property_beds_list[i] if zillow.property_beds_list[i] else "")
        driver.find_element(By.XPATH, f'{X_PATH_START}8{X_PATH_END}').send_keys(zillow.property_price_list[i] if zillow.property_price_list[i] else "")
        driver.find_element(By.XPATH, f'{X_PATH_START}9{X_PATH_END}').send_keys(zillow.property_time_info[i] if zillow.property_time_info[i] else "")
        driver.find_element(By.XPATH, f'{X_PATH_START}10{X_PATH_END}').send_keys(zillow.property_link_list[i] if zillow.property_link_list[i] else "")
        # clicking on submit button
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
        time.sleep(random.choice([0.1, 0.12, 0.15, 0.13]))

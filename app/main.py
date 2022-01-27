import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

## environment variables to be passed to docker CLI
solar_username = os.environ['MY_SOLAR_USER']
solar_password = os.environ['MY_SOLAR_PASS']
solar_loginURL = os.environ['MY_SOLAR_LOGINURL']
tg_token = os.environ['MY_TG_TOKEN']
tg_chatID = os.environ['MY_TG_CHATID']

## function to send a telegram message
def send_msg(text):
   token = tg_token
   chat_id = tg_chatID
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
   response = requests.get(url_req)

## browser automation
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get(solar_loginURL)

## interacting with login page
username_textbox=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.NAME,"username")))
username_textbox.send_keys(solar_username)
password_textbox=WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.NAME,"password")))
password_textbox.send_keys(solar_password)
login_button=WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.ID,"login-btn")))
login_button.click()

## fetching data after login
battery_percentage = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'TSoc_value')))
battery_percentage_text = battery_percentage.text
battery_percentage_float = float(battery_percentage.text)
photovoltaic_measure = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'photovoltaic-measure')))
battery_measure = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'battery-measure')))
grid_measure = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'grid-measure')))
global_state = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'GlobState_value')))
inverter_state = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'InvState_value')))
date = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="c-card-header-timestamp"] cux-card-timestamp')))

## saving strings
battery_percentage_string = "State Of Charge: "+battery_percentage.text+"%"
photovoltaic_measure_string = "Fotovoltaic Input: "+photovoltaic_measure.text
grid_measure_string = "Grid Input: "+grid_measure.text
battery_measure_string = "Battery Output: "+battery_measure.text
global_state_string = "Global State: "+global_state.text
inverter_state_string = "Inverter State: "+inverter_state.text
date_string = "Date/time: "+date.text

## sending telegram message
send_msg("\n"+battery_percentage_string+"\n"+photovoltaic_measure_string+"\n"+battery_measure_string+"\n"+grid_measure_string+"\n"+global_state_string+"\n"+inverter_state_string+"\n"+date_string)

## closing webdriver and script
driver.stop_client()
driver.close()
driver.quit()
quit()
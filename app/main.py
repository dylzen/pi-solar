import config
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def send_msg(text):
   token = config.token
   chat_id = config.chatID
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
   response = requests.get(url_req)
   print(response.json())

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get(config.login_url)
print(driver.title)

username_textbox=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.NAME,"username")))
username_textbox.send_keys(config.username)
password_textbox=WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.NAME,"password")))
password_textbox.send_keys(config.password)
login_button=WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.ID,"login-btn")))
login_button.click()

battery_percentage = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'TSoc_value')))
battery_percentage_text = battery_percentage.text
battery_percentage_float = float(battery_percentage.text)
photovoltaic_measure = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'photovoltaic-measure')))
battery_measure = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'battery-measure')))
grid_measure = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'grid-measure')))
global_state = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'GlobState_value')))
inverter_state = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'InvState_value')))
date = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="c-card-header-timestamp"] cux-card-timestamp')))

battery_percentage_string = "Percentuale batterie: "+battery_percentage.text+"%"
photovoltaic_measure_string = "Energia in input da fotovoltaico: "+photovoltaic_measure.text
battery_measure_string = "Consumo da batterie: "+battery_measure.text
grid_measure_string = "Consumo da ENEL: "+grid_measure.text
global_state_string = "Stato globale: "+global_state.text
inverter_state_string = "Stato inverter: "+inverter_state.text
date_string = "Data/ora: "+date.text

if battery_percentage_float <= 20.1:
    send_msg("Batterie quasi scariche!\n"+battery_percentage_string+"\n"+photovoltaic_measure_string+"\n"+battery_measure_string+"\n"+grid_measure_string+"\n"+global_state_string+"\n"+inverter_state_string+"\n"+date_string)
elif battery_percentage_float >= 79.9:
    send_msg("Batterie quasi piene!\n"+battery_percentage_string+"\n"+photovoltaic_measure_string+"\n"+battery_measure_string+"\n"+grid_measure_string+"\n"+global_state_string+"\n"+inverter_state_string+"\n"+date_string)

time.sleep(1800)
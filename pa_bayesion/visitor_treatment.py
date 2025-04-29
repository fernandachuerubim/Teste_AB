from selenium import webdriver
import numpy as np
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)

driver.get('http://127.0.0.1:5001/home')

clicks = 10000

for click in range(clicks):
    if np.random.random() <= 0.4:
        time.sleep(1)
        #driver.find_element('name', 'yescheckbox').click()
        driver.find_element('id', 'yesbtn').click()

    else:
        time.sleep(1)
        #driver.find_element('name', 'nocheckbox').click()
        driver.find_element('id', 'nobtn').click()


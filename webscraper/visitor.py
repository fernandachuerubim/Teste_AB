import os
import time
import numpy as np
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class visitor:
  def visitor():

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options,service=servico)
    url = os.getenv('WEB_URL')
    driver.get(url+'/home')

    clicks = 1000

    for click in range(clicks):
        button_color = driver.find_element('name', 'forwardbtn').get_attribute('value')

        if button_color == 'blue':

            if np.random.random() <= 0.30:
                driver.find_element('name', 'yescheckbox').click()
                driver.find_element('id', 'yesbtn').click()

            else:
                driver.find_element('name', 'nocheckbox').click()
                driver.find_element('id', 'nobtn').click()
        else:
            if np.random.random() <= 0.32:
                driver.find_element('name', 'yescheckbox').click()
                driver.find_element('id', 'yesbtn').click()
            else:
                driver.find_element('name', 'nocheckbox').click()
                driver.find_element('id', 'nobtn').click()
        
        time.sleep(0.2)

    return None
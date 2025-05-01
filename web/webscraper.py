from selenium import webdriver
import numpy as np
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#options = webdriver.ChromeOptions()
#service = Service()
#path_webdriver = '/mnt/0165652C522E8ECA/ProjetosDeProgramacao/AB-testing/PA-james/pa_bayesion/geckodriver'
#driver = webdriver.Chrome(options=options, service=service)
#driver = webdriver.Chrome(ChromeDriverManager().install())

#servico =  Service(EdgeChromiumDriverManager().install())
#driver = webdriver.Edge(service=servico)

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)


driver.get('http://127.0.0.1:5000/home')

clicks = 100

for click in range(clicks):
    if np.random.random() < 0.5:
        driver.find_element('name', 'yescheckbox').click()
        driver.find_element('id', 'yesbtn').click()
        sleep(1)

    else: 
        driver.find_element('name', 'nocheckbox').click()
        driver.find_element('id', 'nobtn').click()
        sleep(1)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time


email = 'jhean@gmail.com'
nome_completo = 'Jhean Bryan'
classenomeuser = coreSpriteInputRefresh Szr5J
senha = 'senha'

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('https://www.instagram.com/accounts/emailsignup/')
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('aoba')
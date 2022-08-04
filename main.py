from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time


email = 'nome@gmail.com'         #class="_2hvTZ pexuQ zyHYP" 
nome_completo = 'nome sobrenome' #class="_2hvTZ pexuQ zyHYP" 
senha = 'senha'                  #class="_2hvTZ pexuQ zyHYP" 

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#Vai no insta e cria a conta    
def criar_conta(): 
    driver.get('https://www.instagram.com/accounts/emailsignup/')
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'div.WZdjL:nth-child(4) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)').send_keys(email)        #preencher email
    driver.find_element(By.CSS_SELECTOR, 'div.WZdjL:nth-child(5) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)').send_keys(nome_completo)#preencher nome
    driver.find_element(By.CSS_SELECTOR, 'div.WZdjL:nth-child(7) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)').send_keys(senha)        #preencher senha
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.coreSpriteInputRefresh').click() #gerar nome de usuário
    driver.find_element(By.CSS_SELECTOR, 'div.bkEs3:nth-child(1) > button:nth-child(1)').click() #clicar em cadastre-se


#Faz login no gmail para coletar o código do insta
def pegar_codigo_gmail():
    driver.get('https://www.gmail.com')
    driver.find_element(By.CSS_SELECTOR, '#identifierId').send_keys('email.com')
    #impossível prosseguir, gmail não aceita login
    
pegar_codigo_gmail()

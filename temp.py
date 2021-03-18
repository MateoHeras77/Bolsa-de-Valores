# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = '/Users/mateoherasvera/Desktop/Librerias/chromedriver'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://finance.yahoo.com/')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#yfin-usr-qry'.replace(' ', '.'))))\
    .send_keys('AMZN')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="header-desktop-search-button"]')))\
    .click()


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="quote-nav"]/ul/li[4]/a')))\
    .click()


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[2]')))\

texto_columnas = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[2]')
texto_columnas = texto_columnas.text
print(texto_columnas)
tiempo_hoy = texto_columnas.split('\n')[1:-1]

res = [] 

for ele in tiempo_hoy: 
	# split for elements 
	res.append(ele.split()) 

print(res)



horas = list()
temp = list()
v_viento = list()

for i in range(0, len(res), 4):
    horas.append(res[i])

df = pd.DataFrame({'Horas': horas, 'Temperatura': temp, 'V_viento(km_h)':v_viento})
print(df)
df.to_csv('tiempo_hoy.csv', index=False)

driver.quit()






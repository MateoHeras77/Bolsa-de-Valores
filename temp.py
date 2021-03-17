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
driver.get('https://es.investing.com/')


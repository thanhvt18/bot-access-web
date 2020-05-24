from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from extension import dir_path
import os

driver = ''
if os.name == 'posix':
    driver = webdriver.Chrome(f'{dir_path}/drivers/mac/chromedriver')
elif os.name:
    driver = webdriver.Chrome(f'{dir_path}/drivers/linux/chromedriver')


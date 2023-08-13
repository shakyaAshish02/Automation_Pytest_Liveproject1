import pandas as pd
import time

#import wait as wait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as con
#from time import sleep
#import undetected_chromedriver as UC
#from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
#from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pytest
#chrome.exe --remote-debugging-port=9988 --user-data-dir="C:\Users\ashis\Desktop\Media"
opt = Options()

opt.add_experimental_option("debuggerAddress", "localhost:9988")

d=webdriver.Chrome(executable_path="C:\\Users\\ashis\\PycharmProjects\\pythonProject4\\chromedriver.exe",chrome_options=opt)
a = ActionChains(d)

mouse=d.find_element(By.XPATH,"//span[normalize-space()='Menu']")
a.move_to_element(mouse).perform()
time.sleep(1)
#d.find_element(By.XPATH,"//a[@class='pull-left ml10']//i[@class='fa fa-bars']").click()
d.find_element(By.XPATH,"//li[@class='jobseeker_menu greenbg']//a[contains(text(),'Edit Profile')]").click()
#d.find_element(By.XPATH,"//*[@id="topmenu"]/span")
time.sleep(1)
d.find_element(By.XPATH,"//a[normalize-space()='4. Resume']").click()
time.sleep(2)
d.find_element(By.XPATH,"//a[normalize-space()='Upload new resume']").click()

d.find_element(By.XPATH,"//input[@name='file']").send_keys("C:\\Users\\ashis\\Downloads\\Ashishshakya_resume1.pdf")
time.sleep(2)
d.find_element(By.XPATH,"//input[@title='Save']").click()
d.find_element(By.XPATH,"//input[@title='Save']").click()
d.find_element(By.XPATH,"//a[contains(text(),'Back to home')]").click()
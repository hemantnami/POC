from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from faker import Faker
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
fake = Faker()


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#browser = webdriver.Chrome(r"C:\Users\lenovo\Downloads\chromedriver_win32\chromedriver.exe")

browser.get('http://demo.automationtesting.in/Register.html')
browser.find_element(By.XPATH, '//*[@ng-model="FirstName"]').send_keys(fake.name())
browser.find_element(By.XPATH, '//*[@ng-model="LastName"]').send_keys(fake.name())
browser.find_element(By.XPATH, '//*[@ng-model="Adress"]').send_keys(fake.name())
browser.find_element(By.XPATH, '//*[@ng-model="EmailAdress"]').send_keys(fake.name())
browser.find_element(By.XPATH, '//*[@ng-model="Phone"]').send_keys(fake.name())
browser.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input').click()

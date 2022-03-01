from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from faker import Faker
from HTMLParser import HTMLParser
from BeautifulSoup import  BeautifulSoup

fake = Faker()

def handle_endtag(self, tag):
    print("Encountered an end tag :", tag)


browser = webdriver.Chrome(r"C:\Users\lenovo\Downloads\chromedriver_win32\chromedriver.exe")

browser.get('http://demo.automationtesting.in/Register.html')
browser.find_element(By.XPATH, '//*[@ng-model="FirstName"]').send_keys(fake.name())
browser.find_element(By.XPATH, '//*[@ng-model="LastName"]').send_keys(fake.name())
browser.find_element(By.XPATH, '//*[@ng-model="Adress"]').send_keys(fake.name())
browser.find_element(By.XPATH, '//*[@ng-model="EmailAdress"]').send_keys(fake.name())
browser.find_element(By.XPATH, '//*[@ng-model="Phone"]').send_keys(fake.name())
browser.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input').click()

source_code = '"""<span class="UserName"><a href="#">Martin Elias</a></span>"""'
soup = BeautifulSoup(source_code)
print (soup.find('span',{'class':'UserName'}).text)
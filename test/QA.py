import random
import string
import time
from datetime import datetime, timedelta

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
'''
These below methods/functions  help us to generate the data
'''
def generate_name():
    # Generating a random name using string.ascii_letters
    return ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 10)))

def generate_email():
    # Generating a random email address
    domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'example.com']
    return f"{generate_name().lower()}@{random.choice(domains)}"

def gen_phone():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)

    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}-{}-{}'.format(first, second, last)

# Test data generation
attributes = {
    "Name": generate_name(),
    "Email": generate_email(),
}
'''
Based on the keyword that we are providing the through the module it excute respective the block

'''
def test(value):
    if value in("name" , "FirstName" ,"lastname"):
        driver.find_element(By.XPATH, '//*[@ng-model="FirstName"]').send_keys(generate_name())
    elif value in("last","LastName","lastname"):
        driver.find_element(By.XPATH, '//*[@ng-model="LastName"]').send_keys(generate_name())
    elif value in("mail","email","EmailAddress"):
        driver.find_element(By.XPATH, '//*[@ng-model="EmailAdress"]').send_keys(generate_email())
    elif value in("Telephone","Phone","Mobile","MobileNumber"):
        driver.find_element(By.XPATH, '//*[@ng-model="Phone"]').send_keys(gen_phone())
    elif value=="multidropdown":
        driver.find_element(By.ID, 'msdd').click()
        list = ["English", "French", "Spanish", "Dutch", "Greek", "Hebrew"]
        for i in list:

            driver.find_element(By.XPATH, '//li//a[text()="' + i + '"]').click()
    elif value == "singledropdown":
        s = Select(driver.find_element(By.ID, 'Skills'))
        s.select_by_index(20)


driver.get("https://demo.automationtesting.in/Register.html")
test("FirstName")
test("LastName")
test("EmailAddress")
test("Phone")
test("multidropdown")
test("singledropdown")


time.sleep(5)

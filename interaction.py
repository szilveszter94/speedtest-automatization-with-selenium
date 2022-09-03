from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# import selenium
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "D:\Development\chromedriver.exe"

service_path = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service_path)

# open speedtest website
speedtest_url = "https://www.speedtest.net/"

driver.get(speedtest_url)

# click to accept cookies
time.sleep(3) # time.sleep = waiting (x second)
driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()

time.sleep(50)
try:
    driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                  '8]/div/div/div[2]/a').click()
except NoSuchElementException:
    pass
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                              '3]/div/div/div[1]/div/div/div[2]/div[2]/a').click()
time.sleep(1)
download_speed = driver.find_element(By.XPATH,
                                     '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div['
                                     '1]/div[2]/div/div[2]/div/div[2]/span').text
upload_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                             '/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[2]/span').text

time.sleep(5)
# print the result
print(f"Download speed: {download_speed}, Upload speed: {upload_speed}")

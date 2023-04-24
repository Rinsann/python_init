from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(
    r"C:\Users\Rin\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Hello, World!")
search_box.submit()
driver.quit()

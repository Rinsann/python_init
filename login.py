from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:/WebDriver/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')  # 忽略 SSL 握手问题
driver = webdriver.Chrome(service=service, options=options)
driver.get(
    "https://account.geekbang.org/login?redirect=https%3A%2F%2Ftime.geekbang.org%2F")
wait = WebDriverWait(driver, 10)
username = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
username.send_keys('your_username')
password = driver.find_element(By.NAME, 'password')
password.send_keys('your_password')
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
driver.quit()

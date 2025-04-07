from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("C:/Users/Angel/Desktop/VVPS/index.html") 

def perform_login(username, password):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(0.5)

# Тест 1: Валиден вход
def test_valid_login():
    perform_login("admin", "1234")
    assert "success.html" in driver.current_url
    driver.back()

# Тест 2: Грешна парола
def test_invalid_password():
    perform_login("admin", "wrong")
    msg = driver.find_element(By.ID, "message").text
    assert "Грешно потребителско име или парола" in msg

# Тест 3: Грешно потребителско име
def test_invalid_username():
    perform_login("user", "1234")
    msg = driver.find_element(By.ID, "message").text
    assert "Грешно потребителско име или парола" in msg

# Тест 4: Празно потребителско име
def test_empty_username():
    perform_login("", "1234")
    msg = driver.find_element(By.ID, "message").text
    assert "Моля, попълнете всички полета" in msg

# Тест 5: Празна парола
def test_empty_password():
    perform_login("admin", "")
    msg = driver.find_element(By.ID, "message").text
    assert "Моля, попълнете всички полета" in msg

# Тест 6: И двете полета празни
def test_both_fields_empty():
    perform_login("", "")
    msg = driver.find_element(By.ID, "message").text
    assert "Моля, попълнете всички полета" in msg

# Тест 7: Само интервали
def test_spaces_only():
    perform_login("   ", "   ")
    msg = driver.find_element(By.ID, "message").text
    assert "Моля, попълнете всички полета" in msg

# Тест 8: Поставяне чрез клавиш Enter
def test_enter_key_submit():
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234" + Keys.ENTER)
    time.sleep(1)
    assert "success.html" in driver.current_url
    driver.back()

test_valid_login()
test_invalid_password()
test_invalid_username()
test_empty_username()
test_empty_password()
test_both_fields_empty()
test_spaces_only()
test_enter_key_submit()

driver.quit()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    login_button = driver.find_element(By.NAME, 'login-button')
    login_button.click()
    time.sleep(3)
    driver.quit()

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    login_credentials_label = driver.find_element(By.ID, 'login_credentials')
    login_credentials_text = login_credentials_label.text
    print(f'{login_credentials_text}')
    driver.quit()

if __name__ == '__main__':
    main()
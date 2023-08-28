#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

def main():
    driver = webdriver.Firefox()
    driver.get("https://inthou.pl/")
    time.sleep(3)
    driver.refresh()
    time.sleep(3)
    driver.quit()

if __name__ == '__main__':
    main()
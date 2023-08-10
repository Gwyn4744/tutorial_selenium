#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver


def main():
    driver = webdriver.Firefox()
    driver.get("https://www.google.pl")
    driver.quit()

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver


def main():
    driver = webdriver.Firefox()
    driver.get("https://www.google.pl")
    page_url = driver.current_url
    print(f'Typ page_url: {type(page_url)}')
    print(f'Adres URL strony: {page_url}')
    driver.quit()

if __name__ == '__main__':
    main()
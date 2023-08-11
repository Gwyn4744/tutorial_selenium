#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver


def main():
    driver = webdriver.Firefox()
    driver.get("https://www.google.pl")
    page_title = driver.title
    print(f'Typ page_title: {type(page_title)}')
    print(f'Tytuł strony: {page_title}')
    driver.quit()

if __name__ == '__main__':
    main()
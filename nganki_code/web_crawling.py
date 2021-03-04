#!/usr/bin/env python3
"""
Module include all functions and classes pertaining to web scraping.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
from urllib.error import HTTPError
from urllib.error import URLError
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDWait
from selenium.webdriver.support import expected_conditions as EC
import re
import requests

## MODULE OPTIONS ##
parser = 'html5lib'

# Define Selenium options
options = Options()
options.headless = True
path = '/usr/bin/chromedriver' # Will have to be made more flexible
driver = webdriver.Chrome(options=options, executable_path=path)

class ChfAnleihen:
    """
    Class of all swiss bonds.
    """
    def __init__(self, isin, emittent, waehrung, verfall, coupon):
        self.isin = isin
        self.emittent = emittent
        self.waehrung = waehrung
        self.verfall = verfall
        self.coupon = coupon

def scrape_six_bonds(url='https://www.six-group.com'):
    """
    Scrape bond data from the six-group.com website.
    """
    req = requests.get('https://www.six-group.com')
    link = BS(req.text, parser).find('a', href=re.compile('bonds'))['href']
    link = requests.get(link)
    link = BS(link.text, parser).find(
            'a', href=re.compile('bonds.+prices')
            )['href']
    # Using Selenium to navigate the page's JavaScript
    driver.get(link) # Add an implicit wait below
    # Need to figure out a way to get Selenium to choose the right search options
    # Continue here
    #(RUN ON IPYTHON)elem = driver.find_element_by_xpath("//select[@name='Dropdown']")
    page = driver.page_source
    bs = BS(page, parser)
    
    return driver.get(link)

if __name__ == '__main__':
    print(scrape_six_bonds())
    print(driver.page_source)
    pass

from bs4 import BeautifulSoup
import json 
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.trustpilot.com/categories/vitamin_and_supplements_store"

# Creating the instance of Chrome WebDriver
driver = webdriver.Chrome()
driver.get(url)

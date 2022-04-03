import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import date

chromeOptions = Options()
chromeOptions.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chromeOptions)

companyName = ""
rating = ""
totalReviews = ""
catDescription = ""

for pages in range(1, 10):
    driver.get("https://uk.trustpilot.com/categories/fitness_and_nutrition_service?page={}".format(pages))
    for i in range(1, 20):
        companyName += "\n" + ''.join(driver.find_element(by=By.XPATH,\
            value='//*[@id="__next"]/div/main/div/div[2]/section/div[1]/div[2]/div[{}]/a/div/div[2]/p'.format(i))\
                .text)
        rating += "\n" + ''.join(driver.find_element(by=By.XPATH,\
            value='//*[@id="__next"]/div/main/div/div[2]/section/div[1]/div[2]/div[{}]/a/div/div[2]/div/p/span[1]'\
                .format(i)).text).replace("TrustScore ", "")
        totalReviews += "\n" + ''.join(driver.find_element(by=By.XPATH,\
            value='//*[@id="__next"]/div/main/div/div[2]/section/div[1]/div[2]/div[{}]/a/div/div[2]/div/p'\
                .format(i)).text.split(" ")[3])
        catDescription += "\n" + ''.join(driver.find_element(by=By.XPATH,\
            value='//*[@id="__next"]/div/main/div/div[2]/section/div[1]/div[2]/div[{}]/div[2]/div/div'.format(i))\
                .text)

driver.close()

reviewsDataset = pd.DataFrame({
    "Company Name": companyName.split("\n"),
    "TrustScore Rating": rating.split("\n"),
    "Total Reviews": totalReviews.split("\n"),
    "Category Description": catDescription.split("\n"),
    "Extraction Date": date.today()
    })

reviewsDataset = reviewsDataset.iloc[1:]

# Writing to CSV
reviewsDataset.to_csv("trust_pilot_dataset.csv")

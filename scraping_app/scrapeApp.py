from bs4 import BeautifulSoup
import pandas as pd
import requests
import io

topCompanies = ''

for pages in range(1,5):
    URL = "https://www.trustpilot.com/categories/vitamin_and_supplements_store?page={}".format(pages)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    tags = soup.find_all("p")
    for element in tags:
        topCompanies += ';' + ''.join(element.find_all(text=True))

df = pd.DataFrame([x.split('\n') for x in topCompanies.split(';')])
print(df)



 

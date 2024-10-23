import requests
from bs4 import BeautifulSoup

crgslist_response = requests.get("https://newyork.craigslist.org/search/zip#search=1~gallery~0~100")

crgslist_soup_html = BeautifulSoup(crgslist_response.text, "html.parser")

crgslist_text = crgslist_soup_html.get_text()

freeStuff = []

def getTitles(soupdata):
    titles = soupdata.select(".title")
    if titles:
        for t in titles:
            freeStuff.append(t.get_text())

getTitles(crgslist_soup_html)

freeText = " ".join(freeStuff)

crgslist_data = open('crgslist_free.txt', 'w')
crgslist_data.write(freeText)
crgslist_data.close()
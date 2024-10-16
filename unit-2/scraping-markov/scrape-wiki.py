import requests
from bs4 import BeautifulSoup

website_response = requests.get("https://www.wikihow.com/Become-a-Professional-Artist")
website_soup_html = BeautifulSoup(website_response.text, "html.parser")

def getSpecificElements(soupdata, element_name):  
  website_data = open('scraped-data-artist.txt', 'w')
  elements = soupdata.select(element_name)

  if elements:
    for t in elements:
       plaintext = t.text.strip()
       website_data.write(str(plaintext))
    website_data.close()

getSpecificElements(website_soup_html, ".step")




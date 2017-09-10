# Import modules
import requests
from bs4 import BeautifulSoup

# Crawl Subastar Website
response = requests.get('http://www.subastar.com.co/index.php/informes-de-precios/precios-sede-monteria')
html = BeautifulSoup(response.text, 'html.parser')

# Get pdf links of each auction
pdf_links = [a_tag['href'] for a_tag in html.select("table.easyfolderlisting tr td a")]

# Get all pdf's from the website and save them locally
for pdf_link in pdf_links:
    filename = pdf_link.split("/")[-1]
    day, month, year = filename.replace(".pdf", "").split("-")
    year = year[-2:] # Some years come in 4 chars (e.g. 2015) some only in the last 2 (e.g. 15). This is to normalize data.
    response = requests.get(pdf_link)
    with open('../pdfs/{0}-{1}-{2}.pdf'.format(year, month, day), 'wb') as f:
        f.write(response.content)
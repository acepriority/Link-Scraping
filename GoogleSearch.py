import requests
from bs4 import BeautifulSoup

# item to search for
item = "car"

# search engine URL
url = f"https://www.google.com/search?q={item} dealers"

# request the page content
page = requests.get(url)

# parse the page content using BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# find all the links on the page
links = soup.find_all("a")

# filter the links to only include dealer links
dealer_links = [link["href"] for link in links if "dealer" in link.get_text().lower()]

# print the dealer links
for link in dealer_links:
    print(link)

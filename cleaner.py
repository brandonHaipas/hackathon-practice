import requests
from bs4 import BeautifulSoup


url = "https://www.toctoc.com"

response = requests.get(url)

if response.status_code == 200: 
    soup = BeautifulSoup(response.content, "html.parser")
    for EachPart in soup.select("#card-body"):
        print(EachPart)

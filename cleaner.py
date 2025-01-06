from bs4 import BeautifulSoup
import requests
import json

url = "https://www.toctoc.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, features="html.parser")

assets = soup.find("script", {"id" : "__NEXT_DATA__"}, recursive=True)
assets_json = json.loads(assets.get_text(strip=True))

assets_list = assets_json['props']['pageProps']['listaDestacados'][0]['lista']

print(assets_json)
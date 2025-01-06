from bs4 import BeautifulSoup
import requests
import json

url = "https://www.toctoc.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, features="html.parser")

assets = soup.find("script", {"id" : "__NEXT_DATA__"}, recursive=True)
assets_json = json.loads(assets.get_text(strip=True))

assets_list = assets_json['props']['pageProps']['listaDestacados'][0]['lista']
assets_list1 = assets_json['props']['pageProps']['listaDestacados'][1]['lista']
assets_list2 = assets_json['props']['pageProps']['listaDestacados'][2]['lista']
assets_list+=assets_list1
assets_list += assets_list2

def get_highlighted_properties(number_of_properties, type_of_property):
    decode_dict = { 'nueva':'Venta Nuevo', 'arriendo':'Arriendo', 'usada':'Venta Usado'}
    output = []
    count = 0
    max = min(number_of_properties, len(assets_list))
    for elem in assets_list:
        if elem['tipoOperacion'] == decode_dict[type_of_property] and count < max:
            output.append(elem)
            count +=1
    return output
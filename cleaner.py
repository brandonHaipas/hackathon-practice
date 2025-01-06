import requests
from bs4 import BeautifulSoup

url = "https://www.toctoc.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    ofertas = []
    
    # Extraer ofertas del carrusel
    for each_part in soup.select(".card-body"):
        oferta = {}
        
        # Extraer título o nombre de la oferta
        titulo = each_part.select_one("a[alt], h2")
        if titulo:
            oferta["titulo"] = titulo.get("alt") or titulo.text.strip()
        
        # Extraer descripción de la oferta (si existe)
        descripcion = each_part.select_one("h3")
        if descripcion:
            oferta["descripcion"] = descripcion.text.strip()
        
        # Extraer enlace asociado a la oferta
        enlace = each_part.select_one("a[href]")
        if enlace:
            oferta["enlace"] = enlace.get("href")
        
        # Extraer imagen de la oferta (opcional)
        imagen = each_part.select_one("div[style*='background-image'], img")
        if imagen:
            if imagen.has_attr("style"):
                oferta["imagen"] = imagen["style"].split("url(")[-1].strip(")")
            elif imagen.has_attr("src"):
                oferta["imagen"] = imagen["src"]
        
        if oferta:  # Agregar solo ofertas completas
            ofertas.append(oferta)
    
    # Mostrar resultados ordenados
    '''
    for i, oferta in enumerate(ofertas):
        print(f"Oferta {i+1}:")
        print(f"  Título: {oferta.get('titulo', 'N/A')}")
        print(f"  Descripción: {oferta.get('descripcion', 'N/A')}")
        print(f"  Enlace: {oferta.get('enlace', 'N/A')}")
        print(f"  Imagen: {oferta.get('imagen', 'N/A')}")
        print()
       
    '''
    
        
else:
    print(f"Error al acceder a la página. Código de estado: {response.status_code}")

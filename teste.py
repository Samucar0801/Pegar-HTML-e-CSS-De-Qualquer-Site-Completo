import requests
from bs4 import BeautifulSoup

# URL do site que você quer visualizar o HTML
url = 'https://muriloribeiro003.github.io/'

# Faz uma requisição HTTP para obter o HTML do site
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Obtém o conteúdo HTML bruto
    html_content = response.text

    # Opcional: formatar o HTML para uma melhor visualização
    soup = BeautifulSoup(html_content, 'html.parser')
    formatted_html = soup.prettify()

    # Exibir o HTML formatado
    print(formatted_html)
else:
    print(f"Erro ao acessar o site. Status code: {response.status_code}")

import requests
from bs4 import BeautifulSoup
import re

def download_css(url):
    response = requests.get(url)
    if response.status_code == 200:
        css_content = response.text
        print(f"Conteúdo do CSS de {url}:")
        print(css_content)
        print("\n" + "="*80 + "\n")

        # Procura por @import no CSS para arquivos adicionais
        imports = re.findall(r'@import ["\'](.*?)["\'];', css_content)
        for imported_css in imports:
            # Completa o link se for relativo
            if not imported_css.startswith('http'):
                imported_css = url.rsplit('/', 1)[0] + '/' + imported_css
            download_css(imported_css)  # Baixa o CSS importado recursivamente
    else:
        print(f"Erro ao baixar o CSS: {url}")

# URL inicial
url = 'https://muriloribeiro003.github.io/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    css_links = [link.get('href') for link in soup.find_all('link', rel='stylesheet')]

    for css_link in css_links:
        if not css_link.startswith('http'):
            css_link = url + css_link
        download_css(css_link)  # Baixa o CSS inicial e os importados
else:
    print(f"Erro ao acessar o site. Status code: {response.status_code}")

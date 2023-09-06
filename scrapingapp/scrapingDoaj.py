import requests
import random
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Clase6:
    def funcion_clase6(self, search_kw):

        home_link = "https://doaj.org/"
        data = []
        
        url = f'{home_link}/search/articles?ref=homepage-box&source=%7B"query"%3A%7B"bool"%3A%7B"must"%3A%5B%7B"range"%3A%7B"index.date"%3A%7B"gte"%3A"1672531200000"%2C"format"%3A"epoch_millis"%7D%7D%7D%2C%7B"query_string"%3A%7B"query"%3A"{search_kw}"%2C"default_operator"%3A"AND"%7D%7D%5D%7D%7D%2C"track_total_hits"%3Atrue%7D'
        
        user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.51 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.51 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.51 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.32 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.32 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.32 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/101.0",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/101.0",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/101.0"
                # Agrega más User Agents según tus necesidades
        ]

        headers = {
            "User-Agent": random.choice(user_agents)
        }
        time.sleep(2)
        headers["User-Agent"] = random.choice(user_agents)
        response = requests.get(url, headers=headers)
        #print(url)

        if response.status_code == 200:

            #print("entro")
            edge_options = Options()
            edge_options.headless = True
            driver = webdriver.Edge(options=edge_options) 
            driver.get(response.url)
            time.sleep(random.uniform(1, 2))
            page_content = driver.page_source
            soup = BeautifulSoup(page_content, 'html.parser')

            result_items = soup.find_all('li', class_='card search-results__record')
            titulo = ''
            autor = ''
            resumen = ''
            fuente = ''
            result_items = result_items[:10]
            #print(result_items)

            for result in result_items:

                titulo_elem = result.find('h3',class_='search-results__heading')
                autor_elem = result.find('ul',class_='inlined-list').find('li')
                
                # Encuentra el elemento <aside> dentro de la estructura
                fuen_elem = result.find('aside', class_='col-sm-4 search-results__aside')
                fuente_elem = fuen_elem.find('ul').find_all('li')[2].get_text(strip=True) 

                link_elem = result.find('aside',class_='col-sm-4 search-results__aside').find('a', href=True)      

                # Encuentra la fecha dentro del elemento <aside>
                fecha = result.find('p', class_='label').text.strip()
                patron_fecha = r'\b(|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4}\b'
                fecha = re.search(patron_fecha, fecha)
                if fecha:
                    fecha = fecha.group()
                else:
                    fecha = "No encontrado"
                    
                titulo = titulo_elem.get_text(strip=True) if titulo_elem else 'NO ENCONTRADO'
                        
                resumen_elements = result.find('div', class_='search-results__body').find_all('p') 
                if resumen_elements:
                    resumen = resumen_elements[0].get_text(strip=True)
                    resumen = resumen.replace("\n", "; ")
                 
                else:
                    resumen = "No encontrado"

                link = link_elem['href'] if link_elem else 'NO ENCONTRADO'
                autor = autor_elem.get_text(strip=True) if autor_elem else 'NO ENCONTRADO'
                fuente = fuente_elem if fuente_elem else 'NO ENCONTRADO'
                Ncitas = 'NO ENCONTRADO'
                tipo_docu = 'ARTICULO'
                version = 'NO APLICA'

                # Agrega los datos a la lista
                data.append({'Título de la investigación:': titulo, 'Autor:': autor, 'Descripción:': resumen, 'Fuente:': fuente, 'Fecha de publicación:': fecha, 'Enlace del documento:': link, 'Número de citas:': Ncitas, 'Tipo de documento consultado:': tipo_docu, 'Cantidad de versiones del documento:': version })
                # Imprime la información del resultado actual
                print('Título de la investigación:', titulo)
                print('Autor:' , autor)
                print('Descripción:' , resumen)
                print('Fuente:' , fuente)
                print('Fecha de publicación:' , fecha)
                print('Enlace del documento:' , link)
                print('Número de citas:' , Ncitas)
                print('Tipo de documento consultado:' , tipo_docu)
                print('Cantidad de versiones del documento:' , version)
                print('-' * 50)

            driver.quit()

        else:
            print("Error al hacer la solicitud:", response.status_code) 
            print("------------------------------------------------------------------------")  

        return data
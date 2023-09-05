import requests
import re
import random
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Clase5:
    def funcion_clase5(self, search_kw):

        data=[]

        home_link = "https://ieeexplore.ieee.org"

        # URL de la página de arXiv que deseas scrapear
        url = home_link+"/search/searchresult.jsp?queryText="+search_kw+"&highlight=true&returnType=SEARCH&matchPubs=true&refinements=ContentType:Journals&refinements=ContentType:Magazines&refinements=ContentType:Early%20Access%20Articles&refinements=ContentType:Books&refinements=ContentType:Courses&refinements=ContentType:Standards&returnFacets=ALL&openAccess=true"

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

        # Realiza una solicitud GET a la página
        headers["User-Agent"] = random.choice(user_agents)
        response = requests.get(url, headers=headers)

        # Verifica si la solicitud fue exitosa
        if response.status_code == 200:
            #print("entro")
            webdriver_path = 'msedgedriver.exe'
            edge_options = webdriver.EdgeOptions()
            edge_options.use_chromium = True
            driver = webdriver.Edge(options=edge_options)
            driver.get(response.url)
            time.sleep(random.uniform(1, 2))
            page_content = driver.page_source

            # Parsea el contenido HTML usando BeautifulSoup
            soup = BeautifulSoup(page_content, 'html.parser')
            result_items = soup.find_all('div', class_='col result-item-align px-3')

            try:
                cookie_popup = driver.find_element(By.CLASS_NAME, 'cc-window')
                if cookie_popup.is_displayed():
                    cookie_popup.find_element(By.CLASS_NAME, 'cc-btn').click()
            except:
                pass

            #print(result_items)
            result_items = result_items[:10]

            for result in result_items:

                titulo = ""
                titulo_elem = ""
                autor = ""
                autor_elem = ""
                resumen = ""
                fuente_ext = ""
                fuente = ""
                fecha = ""
                fech_elem = ""
                link_elem = ""
                link = ""
                link2 = ""
                num_cit = ""
                tipo_docu = ""
                version = ""
                repositorio = ""
                citations_elem = ""
                cant_ver = ""
                cant_text = ""
                citations_match = ""
                citations_text = ""

                titulo_elem = result.find('h3', class_='text-md-md-lh').find('a', class_='fw-bold')
                autor_elem = result.find_all('span', class_='text-base-md-lh')
                fuente_ext = result.find('a', href=True)
                fech_elem = result.find('div', class_='publisher-info-container').find_all('span')[0]
                link_elem = soup.find('ul', class_='List List--horizontal').find('a', class_='stats_PDF_10029336 u-flex-display-flex',  href=True)
                citations_elem = soup.find('a', href=True, text=re.compile(r'^Papers \(\d+\)$'))
            
                if citations_elem:
                    citations_text = citations_elem.get_text()
                    citations_match = re.search(r'\((\d+)\)', citations_text)
                    if citations_match:
                        num_cit = citations_match.group(1)   
                else:
                    num_cit = 'NO ENCONTRADO'

                cant_ver = result.find('div', class_='publisher-info-container').find_all('span')[1]

                if cant_ver:
                    cant_text = cant_ver.get_text(strip=True)
                    version = cant_text.replace("|Volume: ", "").replace(",Issue", "").strip()  # Dividir por ":" y obtener el segundo elemento
                else:
                    version = 'NO ENCONTRADO'

                titulo = titulo_elem.get_text(strip=True) if titulo_elem else 'NO ENCONTRADO'
                autor = ', '.join([span.get_text(strip=True) for span in autor_elem]) if autor_elem else 'NO ENCONTRADO'
                fuente = fuente_ext.get_text(strip=True) if fuente_ext else 'NO ENCONTRADA'
                fecha = fech_elem.get_text(strip=True) if fech_elem else 'NO ENCONTRADO'
                link = link_elem['href'] if link_elem else 'NO ENCONTRADO'
                link2 = 'https://ieeexplore.ieee.org'+link 
                tipo_docu = 'PDF'
                resumen = 'NO ENCONTRADO'
                repositorio="IEEE"


                # Agrega los datos a la lista
                data.append({'Título de la investigación:': titulo, 'Autor:': autor, 'Descripción:': resumen, 'Fuente:': fuente, 'Fecha de publicación:': fecha, 'Enlace del documento:': link2, 'Número de citas:': num_cit, 'Tipo de documento consultado:': tipo_docu, 'Cantidad de versiones del documento:': version, 'Repositorio': repositorio})
                # Imprime la información del resultado actual
                print('Título de la investigación:', titulo)
                print('Autor:' , autor)
                print('Descripción:' , resumen)
                print('Fuente:' , fuente)
                print('Fecha de publicación:' , fecha)
                print('Enlace del documento:' , link2)
                print('Número de citas:' , num_cit)
                print('Tipo de documento consultado:' , tipo_docu)
                print('Cantidad de versiones del documento:' , version) 
                print('Repositorio:' , repositorio) 
                print('-' * 50)   
            
            driver.quit()

        else:
            print("Error al hacer la solicitud:", response.status_code) 
            print("------------------------------------------------------------------------")   

        return data
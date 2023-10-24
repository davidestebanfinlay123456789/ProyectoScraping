import requests
import random
import time
import re
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Clase6:
    def funcion_clase6(self, search_kw, busAut, anoIni, anoFin, tipo_docu):
        # Obtén la fecha actual
        fecha_actual = datetime.datetime.now()

        # Extrae el año de la fecha actual
        ano = fecha_actual.year
        home_link = "https://doaj.org"
        data = []
        none=0
        
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
        #cantidad 50-100-200
        can_res = 50
        
        if busAut!="":
            if tipo_docu=='todos':
                tipo_docu = 'TODOS'
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                url = f'{home_link}/search/articles?ref=homepage-box&source=%7B"query"%3A%7B"query_string"%3A%7B"query"%3A"{search_kw}%20AND%20{busAut}"%2C"default_operator"%3A"AND"%2C"default_field"%3A"bibjson.author.name"%7D%7D%2C"size"%3A"{can_res}"%2C"sort"%3A%5B%7B"created_date"%3A%7B"order"%3A"desc"%7D%7D%5D%2C"track_total_hits"%3Atrue%7D'
            elif tipo_docu=='articulo':
                tipo_docu = 'ARTICULO'
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                url = f'{home_link}/search/articles?ref=homepage-box&source=%7B"query"%3A%7B"query_string"%3A%7B"query"%3A"{search_kw}%20AND%20{busAut}"%2C"default_operator"%3A"AND"%2C"default_field"%3A"bibjson.author.name"%7D%7D%2C"size"%3A"{can_res}"%2C"sort"%3A%5B%7B"created_date"%3A%7B"order"%3A"desc"%7D%7D%5D%2C"track_total_hits"%3Atrue%7D'
            elif tipo_docu=='revista':
                tipo_docu = 'REVISTA'
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                url = f'{home_link}/search/journals?ref=homepage-box&source=%7B"query"%3A%7B"query_string"%3A%7B"query"%3A"{busAut}"%2C"default_operator"%3A"AND"%2C"default_field"%3A"bibjson.publisher.name"%7D%7D%2C"track_total_hits"%3Atrue%7D'
            elif tipo_docu=='documento':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                none=1    
        else:
            if tipo_docu=='todos':
                tipo_docu = 'TODOS'
                #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada sin tener en cuenta el tipo de documento")
                url = f'{home_link}/search/articles?ref=homepage-box&source=%7B"query"%3A%7B"query_string"%3A%7B"query"%3A"{search_kw}"%2C"default_operator"%3A"AND"%7D%7D%2C"track_total_hits"%3Atrue%7D'
            elif tipo_docu=='articulo':
                tipo_docu = 'ARTICULO'
                #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo articulos")
                url = f'{home_link}/search/articles?ref=homepage-box&source=%7B"query"%3A%7B"query_string"%3A%7B"query"%3A"{search_kw}"%2C"default_operator"%3A"AND"%7D%7D%2C"track_total_hits"%3Atrue%7D'
            elif tipo_docu=='revista':
                tipo_docu = 'REVISTA'
                #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo revistas")
                url = f'{home_link}/search/journals?ref=homepage-box&source=%7B"query"%3A%7B"query_string"%3A%7B"query"%3A"{search_kw}"%2C"default_operator"%3A"AND"%7D%7D%2C"track_total_hits"%3Atrue%7D'

            elif tipo_docu=='documento':
                #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo documentos")
                none=1
        


        if none==0:

            # Realiza una solicitud GET a la página
            response = requests.get(url)

            # Verifica si la solicitud fue exitosa
            print("------------------------------------------------------------------------")
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
                result_items = result_items[:10]
                #print(result_items)

                for result in result_items:
                    titulo_elem = result.find('h3',class_='search-results__heading')
                    if titulo_elem is not None:
                        titulo = titulo_elem.get_text(strip=True) 
                    else:
                        titulo = "No encontrado"

                    autor_elem1 = result.find('ul',class_='inlined-list')
                    if autor_elem1 is not None:
                        autor_elem2 = autor_elem1.find_all('li')
                        if len(autor_elem2) > 0:
                            autores = [autor.get_text(strip=True) for autor in autor_elem2] 
                            autor = ' '.join(autores)
                        else:
                            autor = "No encontrado"
                    else:
                        autor = "No encontrado"

                    link_elem1 = result.find('aside',class_='col-sm-4 search-results__aside')  
                    if link_elem1 is not None:
                        link_elem2 = link_elem1.find('a', href=True)  
                        if link_elem2 is not None:
                            link = link_elem2['href'] 
                            fuente = link
                        else:
                            link = "No encontrado"
                            fuente = "No encontrado"
                    else:
                        link = "No encontrado"
                        fuente = "No encontrado"
                              
                    if tipo_docu=='ARTICULO':
                        fecha_elem = result.find('p', class_='label')
                        if fecha_elem:
                            fecha = fecha_elem.text.strip()
                            patron_fecha = r'\b(|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4}\b'
                            fecha_match = re.search(patron_fecha, fecha)
                            if fecha_match:
                                fecha = fecha_match.group()
                            else:
                                fecha = "No encontrado"
                        else:
                            fecha = "No encontrado"
                    elif tipo_docu=='REVISTA':
                        fecha_elem = result.find('aside', class_='col-sm-4 search-results__aside').find_all('li')[0]
                        if fecha_elem:
                            fecha = fecha_elem.text.strip()
                            patron_fecha = r'\b(|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4}\b'
                            fecha_match = re.search(patron_fecha, fecha)
                            if fecha_match:
                                fecha = fecha_match.group()
                            else:
                                fecha = "No encontrado"
                        else:
                            fecha = "No encontrado"
                    elif tipo_docu=='TODOS':
                        fecha_elem = result.find('p', class_='label')
                        if fecha_elem:
                            fecha = fecha_elem.text.strip()
                            patron_fecha = r'\b(|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4}\b'
                            fecha_match = re.search(patron_fecha, fecha)
                            if fecha_match:
                                fecha = fecha_match.group()
                            else:
                                fecha = "No encontrado"
                        else:
                            fecha = "No encontrado"
                            
                            
                    resumen_elements1 = result.find('div', class_='search-results__body')
                    if resumen_elements1 is not None:
                        resumen_elements2 = resumen_elements1.find_all('p') 
                        if len(resumen_elements2) > 0: 
                            resumen = resumen_elements2[0].get_text(strip=True)
                            resumen = resumen.replace("\n", "; ")
                        else:
                            resumen = "No encontrado"
                    else:
                        resumen = "No encontrado"
                    
                    num_cit = 'No encontrado'
                    version = 'No encontrado'
                    repositorio = 'Doaj'

                    cadena_limpia = re.sub(r'[^0-9-]', ' ', fecha)
                    # Elimina espacios en blanco a la izquierda
                    cadena_limpia = cadena_limpia.lstrip()
                    fec = int(cadena_limpia)

                    if anoIni=='':
                        ini=1990
                    else:
                        ini = int(anoIni)
                    if anoFin=='':
                        fin= int(ano)
                    else:
                        fin = int(anoFin)

                    if ini <= fec <= fin:
                        if  titulo!= "No encontrado":
                            data.append({'Título de la investigación:': titulo, 'Autor:': autor, 'Descripción:': resumen, 'Fuente:': fuente, 'Fecha de publicación:': fecha, 'Enlace del documento:': link, 'Número de citas:': num_cit, 'Tipo de documento consultado:': tipo_docu, 'Cantidad de versiones del documento:': version, 'Repositorio': repositorio })
                    '''
                    # Imprime la información del resultado actual
                    print('Título de la investigación:', titulo)
                    print('Autor:' , autor)
                    print('Descripción:' , resumen)
                    print('Fuente:' , fuente)
                    print('Fecha de publicación:' , fecha)
                    print('Enlace del documento:' , link)
                    print('Número de citas:' , num_cit)
                    print('Tipo de documento consultado:' , tipo_docu)
                    print('Cantidad de versiones del documento:' , version)
                    print('-' * 50)'''

                driver.quit()

            else:
                print("Error al hacer la solicitud:", response.status_code) 
                print("------------------------------------------------------------------------")  

        return data
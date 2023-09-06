import requests
import re
import random
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Clase6:
    def funcion_clase6(self, search_kw):

        data=[]

        home_link = "https://www.base-search.net"

        # URL de la página de arXiv que deseas scrapear
        url = home_link+"/Search/Results?lookfor="+search_kw+"&type=all&sort=score%20desc,dctitle_sort%20asc&oaboost=1&refid=dcddes&filter[]=f_dcyear:2021"

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

        print("------------------------------------------------------------------------")

        if response.status_code == 200:
            
            #print("entro")
            edge_options = Options()
            edge_options.headless = True
            driver = webdriver.Edge() 
            driver.get(response.url)
            time.sleep(random.uniform(1, 2))
            page_content = driver.page_source

            # Parsea el contenido HTML usando BeautifulSoup
            soup = BeautifulSoup(page_content, 'html.parser')
            result_items = soup.find_all('div', class_='record-panel panel panel-default')

            print(result_items)
            result_items = result_items[:10]

            for result in result_items:

                titulo = ""
                autor = ""
                resumen = ""
                fuente = ""
                fecha1 = ""
                link = ""
                num_cit = ""
                tipo_docu = ""
                version = ""
                repositorio = ""
                

                titulo = result.find('a',class_='link1 bold').text.strip()
                titulo = titulo.replace("\n", " ")
                autor = result.find('div', class_='row row-eq-height').text.strip()
                autor= autor.replace(",","")
                resumen = result.find('div', class_='col-md-10 col-sm-9 record-column2-es text-bottom-in-flex').text.strip()
                resumen = resumen.replace("\n", "")
                fuente = result.find( 'a', class_='link1 bold', href=True)
                fecha1 = result.find('div',class_='row row-eq-height').find('div', class_='col-md-10 col-sm-9 record-column2-es text-bottom-in-flex').text.strip()
                link = result.find( 'a', class_='link1 bold', href=True)
                num_cit = "No encontrado"   
                tipo_docu = result.find('div',class_='row row-eq-height').find('div', class_='col-md-10 col-sm-9 record-column2-es text-bottom-in-flex').text.strip()
                version = "No encontrado"
                repositorio = "PudMed"

                if titulo == "" : titulo = "No encontrado"
                if autor == "" : autor = "No encontrado"
                if resumen == "" : resumen = "No encontrado"
                if fuente == "" : fuente = "No encontrado"
                if fecha1 == "" : fecha1 = "No encontrado"
                if link == "" : link = "No encontrado"
                if num_cit == "" : num_cit = "No encontrado"
                if tipo_docu == "" : tipo_docu = "No encontrado"
                if version == "" : version = "No encontrado"

                # Agrega los datos a la lista
                data.append({'Título de la investigación:': titulo, 'Autor:': autor, 'Descripción:': resumen, 'Fuente:': fuente, 'Fecha de publicación:': fecha1, 'Enlace del documento:': link, 'Número de citas:': num_cit, 'Tipo de documento consultado:': tipo_docu, 'Cantidad de versiones del documento:': version, 'repositrio': repositorio})
                # Imprime la información del resultado actual
                print('Título de la investigación:', titulo)
                print('Autor:' , autor)
                print('Descripción:' , resumen)
                print('Fuente:' , fuente)
                print('Fecha de publicación:' , fecha1)
                print('Enlace del documento:' , link)
                print('Número de citas:' , num_cit)
                print('Tipo de documento consultado:' , tipo_docu)
                print('Cantidad de versiones del documento:' , version) 
                print('Repositoio:' , repositorio) 
                print('-' * 50)   
            
            driver.quit()
            
        else:
            print("Error al hacer la solicitud:", response.status_code)    
            print("------------------------------------------------------------------------")


import requests
import re
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Clase3:
    def funcion_clase3(self, search_kw):

        #print("Función de la Clase 3 con parámetro:", search_kw)
        data=[]

        home_link = "https://scholar.google.es"

        # URL de la página de arXiv que deseas scrapear
        url = home_link+"/scholar?hl=es&as_sdt=0%2C5&q="+search_kw+"&btnG=&start="

        #print(url)

        # Realiza una solicitud GET a la página
        response = requests.get(url)

        # Verifica si la solicitud fue exitosa
        if response.status_code == 200:

            # Parsea el contenido HTML usando BeautifulSoup
            edge_options = Options()
            edge_options.headless = True
            driver = webdriver.Edge(options=edge_options)
            driver.get(response.url)
            # Esperar y obtener contenido de la página
            time.sleep(random.uniform(1, 3))
            page_content = driver.page_source

            soup = BeautifulSoup(page_content, 'html.parser')
            result_items = soup.find_all('div', class_='gs_r gs_or gs_scl')

            #print(result_items)
            result_items = result_items[:10]

            for result in result_items:

                titulo = ""
                titulo_elem = ""
                autor = ""
                resumen = ""
                fuente = ""
                fecha = ""
                fecha2 = ""
                fecha3 = ""
                link_elem = ""
                link = ""
                num_cit = ""
                Ncitas = ""
                tipo_docu = ""
                cant_ver = ""
                version = ""
                repositorio = ""

                titulo_elem = result.find('h3',class_='gs_rt').find_all('a')[0]
                titulo = titulo_elem.get_text(strip=True) 
                autor = result.find('div', class_='gs_a').text.strip()
                resumen = result.find(class_='gs_rs').text.strip()       
                fuente = result.find('a', id='tZmUqkacyaYJ')
                fecha = result.find( class_='gs_a').text.strip()
                fecha2 = re.search(r'\d{4}', fecha)
                fecha3=''
                fecha3 = fecha2.group(0) 
                link_elem = result.find( 'a', href=True)
                link = link_elem['href'] 
                num_cit = result.find('div',class_='gs_fl gs_flb').find_all('a')[2]  
                Ncitas = num_cit.get_text(strip=True)   
                tipo_docu = result.find(class_='gs_ct1')
                cant_ver = soup.find('div',class_='gs_fl gs_flb').find_all('a')[4]  
                version = cant_ver.get_text(strip=True) 
                repositorio = "Google Academico"

                if titulo == "" : titulo = "No encontrado"
                if autor == "" : autor = "No encontrado"
                if resumen == "" : resumen = "No encontrado"
                if fuente == "" : fuente = "No encontrado"
                if fecha3 == "" : fecha3 = "No encontrado"
                if link == "" : link = "No encontrado"
                if Ncitas == "" : Ncitas = "No encontrado"
                if tipo_docu == "" : tipo_docu = "No encontrado"
                if version == "" : version = "No encontrado"

                # Agrega los datos a la lista
                data.append({'Título de la investigación:': titulo, 'Autor:': autor, 'Descripción:': resumen, 'Fuente:': fuente, 'Fecha de publicación:': fecha3, 'Enlace del documento:': link, 'Número de citas:': Ncitas, 'Tipo de documento consultado:': tipo_docu, 'Cantidad de versiones del documento:': version, "Repositorio": repositorio })
                '''
                # Imprime la información del resultado actual
                print('Título de la investigación:', titulo)
                print('Autor:' , autor)
                print('Descripción:' , resumen)
                print('Fuente:' , fuente)
                print('Fecha de publicación:' , fecha3)
                print('Enlace del documento:' , link)
                print('Número de citas:' , num_cit)
                print('Tipo de documento consultado:' , tipo_docu)
                print('Cantidad de versiones del documento:' , version) 
                print('Repositorio:',repositorio)
                print('-' * 50)   '''
            
            driver.quit()
        else:
            print("Repositorio no disponible en este momento, error ", response.status_code)
            print("------------------------------------------------------------------------")
            
        return data
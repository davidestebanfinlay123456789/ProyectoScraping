import requests
import re
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Clase2:
    def funcion_clase2(self, search_kw):

        #print("Función de la Clase 2 con parámetro:", search_kw)
        data=[]

        home_link = "https://www.redalyc.org"

        # URL de la página de arXiv que deseas scrapear
        url = home_link+"/busquedaArticuloFiltros.oa?q="+search_kw

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
            result_items = soup.find_all('div', class_='wrapper')

            #print(result_items)
            result_items = result_items[:10]

            for result in result_items:

                titulo = ""
                autor = ""
                resumen = ""
                fuente_ant = ""
                fuente = ""
                fecha = ""
                fecha1 = ""
                patron = ""
                palabras_encontradas = ""
                link_elem = ""
                link = ""
                num_cit = ""
                tipo_docu = ""
                version = ""
                repositorio = ""

                titulo = result.find('span',class_='title').text.strip()
                autor = result.find('a',class_='nomRevista-hover').find('span', class_='ng-binding').text.strip()
                autor = autor.replace(",","")

                resumen = result.find('span', class_='article-contenido author ng-binding').text.strip()
                resumen = resumen.replace("\n", " ")
                resumen = resumen+"..."

                fuente_ant = result.find('a', class_='nomRevista-hover', href=True)
                fuente = fuente_ant['href']

                fecha = result.find( 'a',class_='articulo-hover ng-scope').find('span',class_='ng-binding').text.strip()
                #en esta parte traere a llamar a una sola parte de el resultado por defecto de fecha y lo almacenare en fecha1
                patron = r'\b\w+\b'  # Patrón para coincidir con palabras completas
                palabras_encontradas = re.findall(patron, fecha)
                fecha1 = palabras_encontradas[0]

                link_elem = result.find( 'a', class_='ng-scope', href=True)
                link = link_elem['href'] 

                num_cit = "No encontrado"   
                tipo_docu = result.find('div',class_='productos-articulo').find('a',class_='ng-scope').text.strip()
                version = result.find('span',class_='ng-binding ng-scope').text.strip()
                repositorio = "Redalyk"

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
                data.append({'Título de la investigación:': titulo, 'Autor:': autor, 'Descripción:': resumen, 'Fuente:': fuente, 'Fecha de publicación:': fecha1, 'Enlace del documento:': link, 'Número de citas:': num_cit, 'Tipo de documento consultado:': tipo_docu, 'Cantidad de versiones del documento:': version, "Repositorio": repositorio })
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
                print('Repositorio:',repositorio)
                print('-' * 50)   
            

        else:
            print("Error al hacer la solicitud:", response.status_code)
            print("------------------------------------------------------------------------")
    
        return data
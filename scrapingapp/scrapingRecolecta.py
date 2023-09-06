import requests
import re
import random
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Clase9:
    def funcion_clase9(self, search_kw):

        data=[]

        home_link = "https://buscador.recolecta.fecyt.es"

        # URL de la página de arXiv que deseas scrapear
        url = home_link+"/buscador-recolecta?search_api_fulltext="+search_kw+"&tipo-buscador=publicacion&document-type=&document-type-no=&Buscar=Buscar&f%5B0%5D=ano%3A2023"

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
        print("------------------------------------------------------------------------")

        if response.status_code == 200:
            
            edge_options = Options()
            edge_options.headless = True
            driver = webdriver.Edge(options=edge_options) 
            driver.get(response.url)
            time.sleep(random.uniform(1, 2))
            

            # Parsea el contenido HTML usando BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            result_items = soup.find_all('div', class_='views-row')

            #print(result_items)
            result_items = result_items[:10]
            
            for result in result_items:

                titulo = ""
                autor = ""
                resumen = ""
                fuente = ""
                fuente1 = ""
                fecha = ""
                link_elem = ""
                link = ""
                num_cit = ""
                tipo_docu = ""
                version = ""
                repositorio = ""

                fecha = result.find('span',class_='fecha').text.strip()
                fecha = fecha.replace(" ","")

                titulo = result.find('h4').text.strip()
                titulo = titulo.replace("\n", " ")

                fuente = result.find('h4').find('a', href=True)
                fuente = fuente['href'] 
                fuente1 = fuente.replace(" ","%")
                fuente = home_link+fuente1

                autor = result.find('div', class_='text-danger').text.strip()
                autor= autor.replace("\n", " ")

                resumen = result.find('div', class_='descripcionlistado').text.strip()
                resumen = resumen.replace("\n", "")
                
                link_elem = result.find( 'div', class_='identifier veren').find( 'a', href=True)
                link = link_elem['href'] 
                
                num_cit = "No encontrado"   
                tipo_docu = "No encontrado"
                version = "No encontrado"
                repositorio = "Recolecta"

                if titulo == "" : titulo = "No encontrado"
                if autor == "" : autor = "No encontrado"
                if resumen == "" : resumen = "No encontrado"
                if fuente == "" : fuente = "No encontrado"
                if fecha == "" : fecha = "No encontrado"
                if link == "" : link = "No encontrado"
                if num_cit == "" : num_cit = "No encontrado"
                if tipo_docu == "" : tipo_docu = "No encontrado"
                if version == "" : version = "No encontrado"


                # Agrega los datos a la lista
                data.append({'Título de la investigación:': titulo, 'Autor:': autor, 'Descripción:': resumen, 'Fuente:': fuente, 'Fecha de publicación:': fecha, 'Enlace del documento:': link, 'Número de citas:': num_cit, 'Tipo de documento consultado:': tipo_docu, 'Cantidad de versiones del documento:': version, 'Repositorio': repositorio})
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
                print('Repositoio:' , repositorio) 
                print('-' * 50)   
            
            driver.quit()

        else:
            print("Error al hacer la solicitud:", response.status_code)    
            print("------------------------------------------------------------------------")

        return data
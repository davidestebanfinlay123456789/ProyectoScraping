import requests
import re
import time
import random
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Clase2:
    def funcion_clase2(self, search_kw, busAut, anoIni, anoFin, tipo_docu):

        #print("Función de la Clase 2 con parámetro:", search_kw)
        data=[]
        none=0

        home_link = "https://www.redalyc.org"
    
        fecha_actual = datetime.datetime.now()
        ano = fecha_actual.year

        if busAut!="":
            if tipo_docu=='todos':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                url = home_link+"/busquedaArticuloFiltros.oa?q="+search_kw+"%20AND%20"+busAut+"%20AND%20"+str(ano)
            elif tipo_docu=='articulo':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                url = home_link+"/busquedaArticuloFiltros.oa?q="+search_kw+"%20AND%20"+busAut+"%20AND%20"+str(ano)
            elif tipo_docu=='revista':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                none=1
            elif tipo_docu=='documento':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                none=1
        else:
            if tipo_docu=='todos':
                #print("se busca el titulo de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                url = home_link+"/busquedaArticuloFiltros.oa?q="+search_kw+"%20AND%20"+str(ano)
            elif tipo_docu=='articulo':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                url = home_link+"/busquedaArticuloFiltros.oa?q="+search_kw+"%20AND%20"+str(ano)
            elif tipo_docu=='revista':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                none=1
            elif tipo_docu=='documento':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                none=1
        
        #print(url)
        if none==0:

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

                    titulo1 = result.find('span',class_='title')
                    if titulo1 is not None:
                        titulo = titulo1.text.strip()
                    else:
                        titulo = "No encontrado"

                    autor1 = result.find('a',class_='nomRevista-hover')
                    if  autor1 is not None:
                        autor2 = autor1.find('span', class_='ng-binding')
                        if  autor2 is not None:
                            autor = autor2.text.strip()
                            autor = autor.replace(",","")
                        else:
                            autor = "No encontrado"
                    else:
                        autor = "No encontrado"

                    resumen1 = result.find('span', class_='article-contenido author ng-binding')
                    if resumen1 is not None:
                        resumen = resumen1.text.strip()
                        resumen = resumen.replace("\n", " ")
                        resumen = resumen+"..."
                    else:
                        resumen = "No encontrado"

                    fuente_ant = result.find('a', class_='nomRevista-hover', href=True)
                    if  fuente_ant is not None:
                        fuente = fuente_ant['href']
                    else:
                        fuente = "No encontrado"

                    fecha1 = result.find( 'a',class_='articulo-hover ng-scope')
                    if fecha1 is not None:
                        fecha2 = fecha1.find('span',class_='ng-binding')
                        if fecha2 is not None:
                            fecha = fecha2.text.strip()
                            patron = r'\b\w+\b'  # Patrón para coincidir con palabras completas
                            palabras_encontradas = re.findall(patron, fecha)
                            fecha = palabras_encontradas[0]
                        else:
                            fecha = "No encontrado"
                    else:
                        fecha = "No encontrado"

                    link_elem = result.find( 'a', class_='ng-scope', href=True)
                    if link_elem is not None:
                        link = link_elem['href'] 
                    else:
                        link = "No encontrado"

                    num_cit = "No encontrado"   

                    tipo_docu1 = result.find('div',class_='productos-articulo')
                    if tipo_docu1 is not None:
                        tipo_docu2 = tipo_docu1.find('a',class_='ng-scope')
                        if tipo_docu2 is not None:
                            tipo_docu = tipo_docu2.text.strip()
                        else:
                            tipo_docu = "No encontrado"
                    else:
                        tipo_docu = "No encontrado"
                        

                    version1 = result.find('span',class_='ng-binding ng-scope')
                    if version1 is not None:
                        version = version1.text.strip()
                    else:
                        version = "No encontrado"

                    repositorio = "Redalyk"

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
                    print('Fecha de publicación:' , fecha1)
                    print('Enlace del documento:' , link)
                    print('Número de citas:' , num_cit)
                    print('Tipo de documento consultado:' , tipo_docu)
                    print('Cantidad de versiones del documento:' , version) 
                    print('Repositorio:',repositorio)
                    print('-' * 50) '''  
                

            else:
                print("Error al hacer la solicitud:", response.status_code)
                print("------------------------------------------------------------------------")
        
            return data
        
       
            
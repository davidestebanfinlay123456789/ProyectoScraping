import requests
import datetime
import random
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Clase9:
    def funcion_clase9(self, search_kw, busAut, anoIni, anoFin, tipo_docu):

        data=[]
        none=0

        # Obtén la fecha actual
        fecha_actual = datetime.datetime.now()

        # Extrae el año de la fecha actual
        ano = fecha_actual.year

        home_link = "https://buscador.recolecta.fecyt.es"

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

        tipo_docu = tipo_docu

        if busAut!="":
            if tipo_docu=='todos':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                url = home_link+"/buscador-recolecta?search_api_fulltext="+search_kw+"&_indexrecordidentifier=&creator="+busAut+"&repositoryname=&identifier_1=&document-type=&document-type-no=&f%5B0%5D=ano%3A"+str(ano)
            elif tipo_docu=='articulo':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                url = home_link+"/buscador-recolecta?search_api_fulltext="+search_kw+"&_indexrecordidentifier=&creator="+busAut+"&repositoryname=&identifier_1=&document-type=&document-type-no=&f%5B0%5D=ano%3A"+str(ano)+"&f%5B1%5D=subject_facet%3AArtículo%20científico%20antes%20de%20ser%20publicado%2C%20versión%20del%20editor%20%28article%29"
            elif tipo_docu=='revista':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                none=1
            elif tipo_docu=='documento':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                url = home_link+"/buscador-recolecta?search_api_fulltext="+search_kw+"&_indexrecordidentifier=&creator="+busAut+"&repositoryname=&identifier_1=&document-type=&document-type-no=&f%5B0%5D=ano%3A"+str(ano)+"&f%5B1%5D=subject_facet%3AProyecto%20fin%20de%20carrera.%20Trabajo%20final%20de%20grado%20%28bachelorThesis%29&f%5B2%5D=subject_facet%3ATesis%20doctoral%20%28doctoralThesis%29"         
        else:
            if tipo_docu=='todos':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                url = home_link+"/buscador-recolecta?search_api_fulltext="+search_kw+"&_indexrecordidentifier=&creator=&repositoryname=&identifier_1=&document-type=&document-type-no=&f%5B0%5D=ano%3A"+str(ano)
            elif tipo_docu=='articulo':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                url = home_link+"/buscador-recolecta?search_api_fulltext="+search_kw+"&_indexrecordidentifier=&creator=&repositoryname=&identifier_1=&document-type=&document-type-no=&f%5B0%5D=ano%3A"+str(ano)+"&f%5B1%5D=subject_facet%3AArtículo%20científico%20antes%20de%20ser%20publicado%2C%20versión%20del%20editor%20%28article%29"
            elif tipo_docu=='revista':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                none=1
            elif tipo_docu=='documento':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                url = home_link+"/buscador-recolecta?search_api_fulltext="+search_kw+"&_indexrecordidentifier=&creator=&repositoryname=&identifier_1=&document-type=&document-type-no=&f%5B0%5D=ano%3A"+str(ano)+"&f%5B1%5D=subject_facet%3AProyecto%20fin%20de%20carrera.%20Trabajo%20final%20de%20grado%20%28bachelorThesis%29&f%5B2%5D=subject_facet%3ATesis%20doctoral%20%28doctoralThesis%29"
        
        #print(url)

        # Realiza una solicitud GET a la página
        headers["User-Agent"] = random.choice(user_agents)
        response = requests.get(url, headers=headers)

        # Verifica si la solicitud fue exitosa
        print("------------------------------------------------------------------------")

        if none==0:

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

                    fecha1 = result.find('span',class_='fecha')
                    if fecha1 is not None:
                        fecha = fecha1.text.strip()
                        fecha = fecha.replace(" ","")
                    else:
                        fecha = "No encontrado"

                    titulo1 = result.find('h4')
                    if titulo1 is not None:
                        titulo = titulo1.text.strip()
                        titulo = titulo.replace("\n", " ")
                    else:
                        titulo = "No encontrado"

                    fuente1 = result.find('h4')
                    if fuente1 is not None:
                        fuente2 = fuente1.find('a', href=True)
                        if fuente2 is not None:
                            fuente = fuente2['href'] 
                            fuente1 = fuente.replace(" ","%")
                            fuente = home_link+fuente1
                        else:
                            fuente = "No encontrado"
                    else:
                        fuente = "No encontrado"

                    autor1 = result.find('div', class_='text-danger')
                    if autor1 is not None:
                        autor = autor1.text.strip()
                        autor = autor.replace("\n", " ")
                    else:
                        autor = "No encontrado"

                    resumen1 = result.find('div', class_='descripcionlistado')
                    if resumen1 is not None:
                        resumen = resumen1.text.strip()
                        resumen = resumen.replace("\n", "")
                    else:
                        resumen = "No encontrado"
                    
                    r=0
                    link="No encontrado"
                    link_elem = result.find( 'div', class_='identifier doi')
                    if link_elem is not None:
                        a = link_elem.find('a', class_='matomo_link', href=True)
                        if a is not None:
                            link = a['href']
                            r=1       
                    if r==0:
                        link_elem = result.find( 'div', class_='identifier handle')
                        if link_elem is not None:
                            a = link_elem.find('a', href=True)
                            if a is not None:
                                link = a['href']
                                r=1   
                    if r==0:
                        link_elem = result.find( 'div', class_='identifier veren')
                        if link_elem is not None:
                            a = link_elem.find('a', href=True)
                            if a is not None:
                                link = a['href']
                                r=1
                           
                    cadena = link
                    indice_primer_http = cadena.find("https://")
                    if indice_primer_http != -1:
                        # Buscar el siguiente "https://" después del primer enlace
                        indice_segundo_http = cadena.find("https://", indice_primer_http + 1)

                        if indice_segundo_http != -1:
                            # Extraer el segundo enlace desde el segundo "https://" hasta el final
                            segundo_enlace = cadena[indice_segundo_http:]
                            link = segundo_enlace
                        

                    num_cit = "No encontrado"   
                    version = "No encontrado"
                    repositorio = "Recolecta"

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
                    print('Repositoio:' , repositorio) 
                    print('-' * 50) '''  
                
                driver.quit()

            else:
                print("Error al hacer la solicitud:", response.status_code)    
                print("------------------------------------------------------------------------")

            return data
        
        else:
            print("este repositorio no contiene documentos con los filtros requeridos")
            return ""
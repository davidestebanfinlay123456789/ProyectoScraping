import requests
import re
import random
import time
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Clase5:
    def funcion_clase5(self, search_kw, busAut, anoIni, anoFin, tipo_docu):

        data=[]
        none=0
        # Obtén la fecha actual
        fecha_actual = datetime.datetime.now()

        # Extrae el año de la fecha actual
        year = fecha_actual.year
        canres = 25 # rango 25, 50, 100, 200

        home_link = "https://ieeexplore.ieee.org"
        
        if busAut!="":
            if anoIni=='':
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                        url = home_link+"/search/searchresult.jsp?&rowsPerPage="+str(canres)+"&searchWithin=%22First%20Name%22:"+busAut+"&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&openAccess=true"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                        
                        url = home_link+"/search/searchresult.jsp?&rowsPerPage="+str(canres)+"&searchWithin=%22First%20Name%22:"+busAut+"&returnFacets=ALL&refinements=ContentType:Early%20Access%20Articles"

                    elif tipo_docu=='revista':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        url = home_link+"/search/searchresult.jsp?&rowsPerPage="+str(canres)+"&searchWithin=%22First%20Name%22:"+busAut+"&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&openAccess=true&refinements=ContentType:Journals"

                    elif tipo_docu=='documento':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        none = 1                
                else:
                    if tipo_docu=='todos':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html sin tener en cuenta el tipo de documento establecido")
                        url = home_link+"/search/searchresult.jsp?&rowsPerPage="+str(canres)+"&searchWithin=%22First%20Name%22:"+busAut+"&ranges=1990_"+anoFin+"_Year&returnFacets=ALL"
                    elif tipo_docu=='articulo':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html pero solo de articulos")    
                        url = home_link+"/search/searchresult.jsp?&rowsPerPage="+str(canres)+"&searchWithin=%22First%20Name%22:"+busAut+"&ranges=1990_"+anoFin+"_Year&returnFacets=ALL&refinements=ContentType:Early%20Access%20Articles"

                    elif tipo_docu=='revista':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de revistas")
                        url = home_link+"/search/searchresult.jsp?&rowsPerPage="+str(canres)+"&searchWithin=%22First%20Name%22:"+busAut+"&ranges=1990_"+anoFin+"_Year&returnFacets=ALL&refinements=ContentType:Journals"
                    elif tipo_docu=='documento':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de documentos")
                        none = 1
            else:
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada sin tener en cuenta el tipo de documento")
                        url = home_link+"/search/searchresult.jsp?&rowsPerPage="+str(canres)+"&searchWithin=%22First%20Name%22:"+busAut+"&ranges="+anoIni+"_"+str(year)+"_Year&returnFacets=ALL"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo articulos")
                        url = home_link+"/search/searchresult.jsp?&rowsPerPage="+str(canres)+"&searchWithin=%22First%20Name%22:"+busAut+"&ranges="+anoIni+"_"+str(year)+"_Year&returnFacets=ALL&refinements=ContentType:Early%20Access%20Articles"
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo revistas")
                        url = home_link+"/search/searchresult.jsp?&rowsPerPage="+str(canres)+"&searchWithin=%22First%20Name%22:"+busAut+"&ranges="+anoIni+"_"+str(year)+"_Year&returnFacets=ALL&refinements=ContentType:Journals"

                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo documentos")
                        none = 1
                else:
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada sin tener en cuenta el tipo de documento")
                        url = home_link+"/search/searchresult.jsp?&rowsPerPage="+str(canres)+"&searchWithin=%22First%20Name%22:"+busAut+"&ranges="+anoIni+"_"+anoFin+"_Year&returnFacets=ALL"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo articulos")
                        url = home_link+"/search/searchresult.jsp?&rowsPerPage="+str(canres)+"&searchWithin=%22First%20Name%22:"+busAut+"&ranges="+anoIni+"_"+anoFin+"_Year&returnFacets=ALL&refinements=ContentType:Early%20Access%20Articles"
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo revistas")
                        url = home_link+"/search/searchresult.jsp?&rowsPerPage="+str(canres)+"&searchWithin=%22First%20Name%22:"+busAut+"}&ranges="+anoIni+"_"+anoFin+"_Year&returnFacets=ALL&refinements=ContentType:Journals"

                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo documentos")
                        none = 1
        else:
            if anoIni=='':
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el titulo de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                        url = home_link+"/search/searchresult.jsp?queryText="+search_kw+"&highlight=true&returnType=SEARCH&matchPubs=true&openAccess=true&returnFacets=ALL&ranges=1990_2023_Year"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                        url = home_link+"/search/searchresult.jsp?queryText="+search_kw+"&highlight=true&returnType=SEARCH&matchPubs=true&openAccess=true&returnFacets=ALL&ranges=1990_2023_Year&returnFacets=ALL&refinements=ContentType:Early%20Access%20Articles"

                    elif tipo_docu=='revista':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        url = home_link+"/search/searchresult.jsp?queryText="+search_kw+"&highlight=true&returnType=SEARCH&matchPubs=true&openAccess=true&returnFacets=ALL&ranges=1990_2023_Year&returnFacets=ALL&refinements=ContentType:Journals"

                    elif tipo_docu=='documento':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        none = 1                
                else:
                    if tipo_docu=='todos':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html sin tener en cuenta el tipo de documento establecido")
                        url = home_link+"/search/searchresult.jsp?queryText="+search_kw+"&highlight=true&returnType=SEARCH&matchPubs=true&openAccess=true&returnFacets=ALL&ranges=1990_"+anoFin+"_Year"
                    elif tipo_docu=='articulo':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html pero solo de articulos")    
                        url = home_link+"/search/searchresult.jsp?queryText="+search_kw+"&highlight=true&returnType=SEARCH&matchPubs=true&openAccess=true&returnFacets=ALL&ranges=1990_"+anoFin+"_Year&returnFacets=ALL&refinements=ContentType:Early%20Access%20Articles"

                    elif tipo_docu=='revista':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de revistas")
                        url = home_link+"/search/searchresult.jsp?queryText="+search_kw+"&highlight=true&returnType=SEARCH&matchPubs=true&openAccess=true&returnFacets=ALL&ranges=1990_"+anoFin+"_Year&returnFacets=ALL&refinements=ContentType:Journals"
                    elif tipo_docu=='documento':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de documentos")
                        none = 1
            else:
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada sin tener en cuenta el tipo de documento")
                        url = home_link+"/search/searchresult.jsp?queryText="+search_kw+"&highlight=true&returnType=SEARCH&matchPubs=true&openAccess=true&returnFacets=ALL&ranges="+anoIni+"_"+year+"_Year"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo articulos")
                        url = home_link+"/search/searchresult.jsp?queryText="+search_kw+"&highlight=true&returnType=SEARCH&matchPubs=true&openAccess=true&returnFacets=ALL&ranges="+anoIni+"_"+year+"_Year&returnFacets=ALL&refinements=ContentType:Early%20Access%20Articles"
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo revistas")
                        url = home_link+"/search/searchresult.jsp?queryText="+search_kw+"&highlight=true&returnType=SEARCH&matchPubs=true&openAccess=true&returnFacets=ALL&ranges="+anoIni+"_"+year+"_Year&returnFacets=ALL&refinements=ContentType:Journals"
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo documentos")
                        none = 1
                else:
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada sin tener en cuenta el tipo de documento")
                        url = home_link+"/search/searchresult.jsp?queryText="+search_kw+"&highlight=true&returnType=SEARCH&matchPubs=true&openAccess=true&returnFacets=ALL&ranges="+anoIni+"_"+anoFin+"_Year"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo articulos")
                        url = home_link+"/search/searchresult.jsp?queryText="+search_kw+"&highlight=true&returnType=SEARCH&matchPubs=true&openAccess=true&returnFacets=ALL&ranges="+anoIni+"_"+anoFin+"_Year&returnFacets=ALL&refinements=ContentType:Early%20Access%20Articles"
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo revistas")
                        url = home_link+"/search/searchresult.jsp?queryText="+search_kw+"&highlight=true&returnType=SEARCH&matchPubs=true&openAccess=true&returnFacets=ALL&ranges="+anoIni+"_"+anoFin+"_Year&returnFacets=ALL&refinements=ContentType:Journals"
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo documentos")
                        none = 1

        if none==0:
            # URL de la página de arXiv que deseas scrapear
            response = requests.get(url)
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
                edge_options = Options()
                edge_options.headless = True
                driver = webdriver.Edge() 
                driver.get(response.url)
                time.sleep(random.uniform(1, 3))
                page_content = driver.page_source

                # Parsea el contenido HTML usando BeautifulSoup
                soup = BeautifulSoup(page_content, 'html.parser')
                result_items = soup.find_all('div', class_='List-results-items')

                try:
                    cookie_popup = driver.find_element(By.CLASS_NAME, 'cc-window')
                    if cookie_popup.is_displayed():
                        cookie_popup.find_element(By.CLASS_NAME, 'cc-btn').click()
                except:
                    pass

                for result in result_items:

                    titulo_elem = result.find('h3', class_='text-md-md-lh')
                    if titulo_elem is not None:
                        titulo_elem1 = titulo_elem.find('a', class_='fw-bold')
                        if titulo_elem1 is not None:
                            titulo = titulo_elem1.text.strip()
                        else:
                            titulo = "No encontrado"
                    else:
                        titulo = "No encontrado"

                    autor_elem = result.find('span', class_='text-base-md-lh')
                    if autor_elem is not None:
                        autor = autor_elem.text.strip()
                    else:
                        autor="No encontrado"

                    resumen = 'No encontrado'

                    fech_elem = result.find('div', class_='publisher-info-container')
                    if fech_elem is not None:
                        fech_elem1 = fech_elem.find_all('span')
                        if len(fech_elem1) > 0:
                           fecha =  fech_elem1[0]
                           fecha = fecha.text.strip()
                        else:
                            fecha = "No encontrado"
                    else:
                        fecha = "No encontrado"

                    link_elem = result.find('ul', class_='List List--horizontal')
                    if link_elem is not None:
                        link_elem1 = link_elem.find('a',  href=True)
                        if link_elem1 is not None:
                            link = link_elem1['href']
                            link = 'https://ieeexplore.ieee.org'+link
                        else:
                            link = "No encontrado"
                    else:
                        link = "No encontrado"
                               
                    citations_elem = result.find('a', href=True, text=re.compile(r'^Papers \(\d+\)$'))

                    if citations_elem is not None:
                        citations_text = citations_elem.get_text()
                        citations_match = re.search(r'\((\d+)\)', citations_text)
                        if citations_match:
                            num_cit = citations_match.group(1)   
                    else:
                        num_cit = 'No encontrado'

                    cant_ver = result.find('div', class_='publisher-info-container').find_all('span')[1]
                    if cant_ver is not None:
                        cant_ver1 = cant_ver.find_all('span')
                        if len(cant_ver1) > 1:
                            cant_text = cant_ver1[1].get_text(strip=True)
                            version = cant_text.replace("|Volume: ", "").replace(",Issue", "").strip()  # Dividir por ":" y obtener el segundo elemento
                        else:
                            version = 'No encontrado'
                    else:
                        version = 'No encontrado'

                    fuente1 = result.find('div', class_='col result-item-align px-3')
                    if fuente1 is not None:
                        fuente2 = fuente1.find('h3', class_='text-md-md-lh')
                        if fuente2 is not None:
                            fuente3 = fuente2.find('a', class_='fw-bold',  href=True)
                            if fuente3 is not None:
                                fuente = fuente3['href']
                                fuente = 'https://ieeexplore.ieee.org'+ fuente
                            else:
                                fuente = "No encontrado"
                        else:
                            fuente = "No encontrado"
                    else:
                        fuente = "No encontrado"

                    repositorio="IEEE"

                    fecha1 =  fecha       
                    digitos = re.sub(r'\D', '', fecha1)
                    cadena_limpia = re.sub(r'[^0-9-]', ' ', digitos)
                    # Elimina espacios en blanco a la izquierda
                    cadena_limpia = cadena_limpia.lstrip()
                    fec = int(cadena_limpia)
                    fecha = str(fec)
                    
                    if anoIni=='':
                        ini=1990
                    else:
                        ini = int(anoIni)
                        print(ini)
                    if anoFin=='':
                        fin= int(year)
                        print(fin)
                    else:
                        fin = int(anoFin)
                        print(fin)

                    if ini <= fec <= fin:
                        if  titulo!= "No encontrado":
                            data.append({'Título de la investigación:': titulo, 'Autor:': autor, 'Descripción:': resumen, 'Fuente:': fuente, 'Fecha de publicación:': fecha, 'Enlace del documento:': link, 'Número de citas:': num_cit, 'Tipo de documento consultado:': tipo_docu, 'Cantidad de versiones del documento:': version, 'Repositorio': repositorio })
                                       
                    '''# Imprime la información del resultado actual
                    print('Título de la investigación:', titulo)
                    print('Autor:' , autor)
                    print('Descripción:' , resumen)
                    print('Fuente:' , fuente)
                    print('Fecha de publicación:' , fecha)
                    print('Enlace del documento:' , link)
                    print('Número de citas:' , num_cit)
                    print('Tipo de documento consultado:' , tipo_docu)
                    print('Cantidad de versiones del documento:' , version) 
                    print('Repositorio:' , repositorio) 
                    print('-' * 50) '''
                
                driver.quit()

            else:
                print("Error al hacer la solicitud:", response.status_code) 
                print("------------------------------------------------------------------------")   

            return data
        else:
            print("este repositorio no contiene documentos con los filtros requeridos")
            return ""    
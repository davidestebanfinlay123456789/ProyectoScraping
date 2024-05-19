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

class Clase3:
    def funcion_clase3(self, search_kw, busAut, anoIni, anoFin, tipo_docu):

        #print("Función de la Clase 3 con parámetro:", search_kw)
        data=[]
        none=0

        # Obtén la fecha actual
        fecha_actual = datetime.datetime.now()

        # Extrae el año de la fecha actual
        ano = fecha_actual.year

        home_link = "https://scholar.google.es"

        canres = 10 #rango 10, 20 no permite jugar con mas valores

        # URL de la página de arXiv que deseas scrapear
        url = home_link+"/scholar?hl=es&as_sdt=0%2C5&q="+search_kw+"&btnG=&start="

        if busAut!="":
            if anoIni=='':
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                        url = home_link+"/scholar?q="+search_kw+"+author:"+busAut+"&hl=es&num="+str(canres)+"&as_sdt=0,5"
                        tip_doc = "Todos"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                        url = home_link+"/scholar?q="+search_kw+"+author:"+busAut+"&hl=es&num="+str(canres)+"&as_sdt=0,5"
                        tip_doc = "Articulo"
                    elif tipo_docu=='revista':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        url = home_link+"/scholar?q="+search_kw+"+author:"+busAut+"&hl=es&num="+str(canres)+"&as_sdt=0,5"
                        tip_doc = "PDF-Articulo"
                else:
                    if tipo_docu=='todos':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html sin tener en cuenta el tipo de documento establecido")
                        url = home_link+"/scholar?q="+search_kw+"+author%3A"+busAut+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo=2003&as_yhi="+str(anoFin)
                        tip_doc = "Todos"
                    elif tipo_docu=='articulo':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html pero solo de articulos")    
                        url = home_link+"/scholar?q="+search_kw+"+author%3A"+busAut+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo=2003&as_yhi="+str(anoFin)
                        tip_doc = "Articulo"
                    elif tipo_docu=='revista':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de documentos")
                        url = home_link+"/scholar?q="+search_kw+"+author%3A"+busAut+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo=2003&as_yhi="+str(anoFin)
                        tip_doc = "PDF-Articulo"
            else:
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada sin tener en cuenta el tipo de documento")
                        url = home_link+"/scholar?q="+search_kw+"+author%3A"+busAut+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo="+str(anoIni)+"&as_yhi="+str(ano)
                        tip_doc = "Todos"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo articulos")
                        url = home_link+"/scholar?q="+search_kw+"+author%3A"+busAut+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo="+str(anoIni)+"&as_yhi="+str(ano)
                        tip_doc = "Articulo"
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo documentos")
                        url = home_link+"/scholar?q="+search_kw+"+author%3A"+busAut+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo="+str(anoIni)+"&as_yhi="+str(ano)
                        tip_doc = "PDF-Articulo"
                else:
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html sin tener en cuenta el tipo de documentos")
                        url = home_link+"/scholar?q="+search_kw+"+author%3A"+busAut+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo="+str(anoIni)+"&as_yhi="+str(anoFin)
                        tip_doc = "Todos"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo articulos")
                        url = home_link+"/scholar?q="+search_kw+"+author%3A"+busAut+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo="+str(anoIni)+"&as_yhi="+str(anoFin)
                        tip_doc = "Articulo"
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo revistas")
                        none = 1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo doumentos")
                        url = home_link+"/scholar?q="+search_kw+"+author%3A"+busAut+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo="+str(anoIni)+"&as_yhi="+str(anoFin)
                        tip_doc = "PDF-Articulo"
        else:
            if anoIni=='':
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el titulo de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                        url = home_link+"/scholar?hl=es&num="+str(canres)+"&as_sdt=0%2C5&q="+search_kw+"&btnG="
                        tip_doc = "Todos"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                        url = home_link+"/scholar?hl=es&num="+str(canres)+"&as_sdt=0%2C5&q="+search_kw+"&btnG="
                        tip_doc = "Articulo"
                    elif tipo_docu=='revista':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        url = home_link+"/scholar?hl=es&num="+str(canres)+"&as_sdt=0%2C5&q="+search_kw+"&btnG="
                        tip_doc = "PDF-Articulo"
                else:
                    if tipo_docu=='todos':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html sin tener en cuenta el tipo de documento establecido")
                        url = home_link+"/scholar?q="+search_kw+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo=2003&as_yhi="+str(anoFin)
                        tip_doc = "Todos"
                    elif tipo_docu=='articulo':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html pero solo de articulos")    
                        url = home_link+"/scholar?q="+search_kw+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo=2003&as_yhi="+str(anoFin)
                        tip_doc = "Articulo"
                    elif tipo_docu=='revista':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de documentos")
                        url = home_link+"/scholar?q="+search_kw+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo=2003&as_yhi="+str(anoFin)
                        tip_doc = "PDF-Articulo"
            else:
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada sin tener en cuenta el tipo de documento")
                        url = home_link+"/scholar?q="+search_kw+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo="+str(anoIni)+"&as_yhi="+str(ano)
                        tip_doc = "Todos"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo articulos")
                        url = home_link+"/scholar?q="+search_kw+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo="+str(anoIni)+"&as_yhi="+str(ano)
                        tip_doc = "Articulo"
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo documentos")
                        url = home_link+"/scholar?q="+search_kw+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo="+str(anoIni)+"&as_yhi="+str(ano)
                        tip_doc = "PDF-Articulo"
                else:
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html sin tener en cuenta el tipo de documentos")
                        url = home_link+"/scholar?q="+search_kw+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo="+str(anoIni)+"&as_yhi="+str(anoFin)
                        tip_doc = "Todos"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo articulos")
                        url = home_link+"/scholar?q="+search_kw+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo="+str(anoIni)+"&as_yhi="+str(anoFin)
                        tip_doc = "Articulo"
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo doumentos")
                        url = home_link+"/scholar?q="+search_kw+"&hl=es&num="+str(canres)+"&as_sdt=0%2C5&as_ylo="+str(anoIni)+"&as_yhi="+str(anoFin)
                        tip_doc = "PDF-Articulo"
        if none==0:

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

                    titulo_elem1 = result.find('h3',class_='gs_rt')
                    if titulo_elem1 is not None:
                        a = result.find('h3', class_='gs_rt').find('a')
                        if a is not None:
                            titulo = a.text.strip()
                        else:
                            titulo = "No encontrado"
                    else:
                        titulo = "No encontrado"

                    autor1 = result.find('div', class_='gs_a')
                    if autor1 is not None:
                        autor = autor1.text.strip()
                    else:
                        autor = "No encontrado"

                    resumen1 =  result.find(class_='gs_rs') 
                    if resumen1 is not None:
                        resumen = resumen1.text.strip()
                    else:
                        resumen = "No encontrado"

                    fuente1 = result.find('h3', class_='gs_rt')
                    if fuente1 is not None:
                        a = fuente1.find('a', href=True)
                        if a is not None:
                            fuente = a['href'] 
                        else:
                            fuente = "No encontrado"
                    else:
                        fuente = "No encontrado"

                    fecha1 = result.find( class_='gs_a')
                    if fecha1 is not None:
                        fecha = fecha1.text.strip()
                        match = re.search(r'\b\d{4}\b', fecha)
                        year = match.group()
                        fecha = year
                        print("-------------------------------")
                        print(year)
                        print("-------------------------------")

                    else:
                        fecha = "No encontrado"
                    
                    link_elem = result.find( 'div', class_='gs_or_ggsm')
                    if link_elem is not None:
                        a = link_elem.find( 'a', href=True)
                        if a is not None:
                            link = a['href'] 
                        else:
                            link = "No encontrado"
                    else:
                        link = "No encontrado" 

                    num_cit1 = result.find('div',class_='gs_fl gs_flb')
                    if num_cit1 is not None:
                        num_cit2 = num_cit1.find_all('a')
                        if  len(num_cit2) > 2:
                           num_cit = num_cit2[2].get_text(strip=True)
                        else:
                            num_cit = "No encontrado"
                    else:
                        num_cit = "No encontrado"
 
                    cant_ver1 = result.find('div',class_='gs_fl gs_flb')
                    if cant_ver1 is not None:
                        cant_ver2 = cant_ver1.find_all('a')  
                        if len(cant_ver2) > 4:
                            version = num_cit2[4].get_text(strip=True)
                        else:
                            version = "No encontrado"
                    else:
                        version = "No encontrado"

                    repositorio = "Google Academico"
                    
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
                    print('Repositorio:',repositorio)
                    print('-' * 50)   '''
                
                driver.quit()
            else:
                print("Repositorio no disponible en este momento, error ", response.status_code)
                print("------------------------------------------------------------------------")
                
            return data
        
        else:
            print("este repositorio no contiene documentos con los filtros requeridos")
            return ""
import requests
import re
import datetime
from bs4 import BeautifulSoup

class Clase7:
    def funcion_clase7(self, search_kw, busAut, anoIni, anoFin, tipo_docu):

        data=[]
        none=0

        # Obtén la fecha actual
        fecha_actual = datetime.datetime.now()

        # Extrae el año de la fecha actual
        ano = fecha_actual.year

        home_link = "https://eric.ed.gov"

        if busAut!="":
            if anoIni=='':
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                        url = home_link+"/?q="+search_kw+"+author%3A"+busAut
                    elif tipo_docu=='articulo':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                        url = home_link+"/?q="+search_kw+"+author%3A"+busAut+"+&ff1=pubJournal+Articles"
                    elif tipo_docu=='revista':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        none=1
                else:
                    if tipo_docu=='todos':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html sin tener en cuenta el tipo de documento establecido")
                        url = home_link+"/?q="+search_kw+"+pubyearmin%3a1953+pubyearmax%3a"+str(anoFin)+"+author%3a"+busAut
                    elif tipo_docu=='articulo':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html pero solo de articulos")    
                        url = home_link+"/?q="+search_kw+"+pubyearmin%3a1953+pubyearmax%3a"+str(anoFin)+"+author%3a"+busAut+"+&ff1=pubJournal+Articles"
                    elif tipo_docu=='revista':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de documentos")
                        none=1
            else:
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada sin tener en cuenta el tipo de documento")
                        url = home_link+"/?q="+search_kw+"+pubyearmin%3a"+str(anoIni)+"+pubyearmax%3a"+str(ano)+"+author%3a"+busAut
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo articulos")
                        url = home_link+"/?q="+search_kw+"+pubyearmin%3a"+str(anoIni)+"+pubyearmax%3a"+str(ano)+"+author%3a"+busAut+"+&ff1=pubJournal+Articles"
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo documentos")
                        none=1
                else:
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html sin tener en cuenta el tipo de documentos")
                        url = home_link+"/?q="+search_kw+"+pubyearmin%3a"+str(anoIni)+"+pubyearmax%3a"+str(anoFin)+"+author%3a"+busAut
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo articulos")
                        url = home_link+"/?q="+search_kw+"+pubyearmin%3a"+str(anoIni)+"+pubyearmax%3a"+str(anoFin)+"+author%3a"+busAut+"+&ff1=pubJournal+Articles"
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo doumentos")
                        none=1
        else:
            if anoIni=='':
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el titulo de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                        url = home_link+"/?q="+search_kw
                    elif tipo_docu=='articulo':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                        url = home_link+"?q="+search_kw+"&ff1=pubJournal+Articles"
                    elif tipo_docu=='revista':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        none=1
                else:
                    if tipo_docu=='todos':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html sin tener en cuenta el tipo de documento establecido")
                        url = home_link+"/?q="+search_kw+"+pubyearmin%3a1953+pubyearmax%3a"+str(anoFin)
                    elif tipo_docu=='articulo':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html pero solo de articulos")    
                        url = home_link+"/?q="+search_kw+"+pubyearmin%3a1953+pubyearmax%3a"+str(anoFin)+"+&ff1=pubJournal+Articles"
                    elif tipo_docu=='revista':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de documentos")
                        none=1
            else:
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada sin tener en cuenta el tipo de documento")
                        url = home_link+"/?q="+search_kw+"+pubyearmin%3a"+str(anoIni)+"+pubyearmax%3a"+str(ano)
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo articulos")
                        url = home_link+"/?q="+search_kw+"+pubyearmin%3a"+str(anoIni)+"+pubyearmax%3a"+str(ano)+"+&ff1=pubJournal+Articles"
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo documentos")
                        none=1
                else:
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html sin tener en cuenta el tipo de documentos")
                        url = home_link+"/?q="+search_kw+"+pubyearmin%3a"+str(anoIni)+"+pubyearmax%3a"+str(anoFin)
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo articulos")
                        url = home_link+"/?q="+search_kw+"+pubyearmin%3a"+str(anoIni)+"+pubyearmax%3a"+str(anoFin)+"+&ff1=pubJournal+Articles"
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo doumentos")
                        none=1

        if none==0:

            # Realiza una solicitud GET a la página
            response = requests.get(url)

            # Verifica si la solicitud fue exitosa
            print("------------------------------------------------------------------------")

            if response.status_code == 200:

                #print(url)

                # Parsea el contenido HTML usando BeautifulSoup
                soup = BeautifulSoup(response.text, "html.parser")
                result_items = soup.find_all('div', class_='r_i')

                #print(result_items)
                result_items = result_items[:10]

                for result in result_items:

                    titulo1 = result.find('a')
                    if titulo1 is not None:
                        titulo = titulo1.text.strip()
                        titulo = titulo.replace("\n", " ")
                    else:
                        titulo = "No encontrado"

                    autor1 = result.find('div', class_='r_a')
                    if autor1 is not None:
                        autor = autor1.text.strip()
                        partes = autor.split(" – ")
                        autor = partes[0]
                        autor= autor.replace(";","")
                    else:
                        autor = "No encontrado"
                    
                    resumen1 = result.find('div', class_='r_d')
                    if resumen1 is not None: 
                        resumen = resumen1.text.strip()
                        resumen = resumen.replace("\n", "")
                    else:
                        resumen = "No encontrado"
                    
                    fuente_elem = result.find( 'a', href=True)
                    if fuente_elem is not None:
                        fuente = ""+home_link
                        fuente = fuente+fuente_elem['href'] 
                    else:
                        fuente = "No encontrado"
                    
                    fecha1 = result.find('div',class_='r_a')
                    if fecha1 is not None:
                        fecha = fecha1.text.strip()
                        # Buscar patrones de cuatro dígitos (años)
                        patron = r'\b\d{4}\b'
                        fecha = re.findall(patron, fecha)
                        fecha1 = ', '.join(fecha)
                        #fecha1 = fecha1.replace(" ","")
                    else:
                        fecha = "No encontrado"

                    link_elem = result.find('div', class_='r_f')
                    if link_elem is not None:
                        link_elem1 = link_elem.find('a', href=True)
                        if link_elem1 is not None:
                            link = home_link+'/'+link_elem1['href']
                        else:
                            link = "No encontrado"
                    else:
                        link = "No encontrado"

                    num_cit = "No encontrado"
                    
                    tipo_docu1 = result.find('div', class_='r_f')
                    if tipo_docu1 is not None :
                        tipo_docu = tipo_docu1.text.strip()
                        if tipo_docu == 'Peer reviewed Download full text':
                            tipo_docu='PDF' 
                        else: 
                            tipo_docu='Articulo'
                    else:
                        tipo_docu = "No encontrado" 
                    
                    version = "No encontrado"
                    repositorio = "Eric"

                    cadena_limpia = re.sub(r'[^0-9-]', ' ', str(fecha))
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
                    print('Repositorio:' , repositorio) 
                    print('-' * 50)'''
                
            else:
                print("Error al hacer la solicitud:", response.status_code)    
                print("------------------------------------------------------------------------")

            return data
        else:
            print("este repositorio no contiene documentos con los filtros requeridos")
            return ""
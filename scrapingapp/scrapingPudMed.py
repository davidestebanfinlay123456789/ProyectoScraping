import requests
import datetime
import re
from bs4 import BeautifulSoup

class Clase1:
    def funcion_clase1(self, search_kw, busAut, anoIni, anoFin, tipo_docu):

        data=[]
        none=0

        # Obtén la fecha actual
        fecha_actual = datetime.datetime.now()

        # Extrae el año de la fecha actual
        ano = fecha_actual.year
        canres = 10 #Rango 10, 20, 50, 100, 200

        home_link = "https://pubmed.ncbi.nlm.nih.gov"
        tipo_docu=tipo_docu

        if busAut!="":
            if anoIni=='':
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                        url = home_link+"/?term=%28"+search_kw+"%29+AND+%28"+busAut+"%5BAuthor%5D%29&sort=&size="+str(canres)
                    elif tipo_docu=='articulo':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                        url = home_link+"/?term=%28"+search_kw+"%29+AND+%28"+busAut+"%5BAuthor%5D%29&sort=&size="+str(canres)
                    elif tipo_docu=='revista':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        none=1
                else:
                    if tipo_docu=='todos':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html sin tener en cuenta el tipo de documento establecido")
                        url = home_link+"/?term=%28"+search_kw+"%29+AND+%28"+busAut+"%5BAuthor%5D%29&filter=years.2003-"+str(anoFin)+"&size="+str(canres)
                    elif tipo_docu=='articulo':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html pero solo de articulos")    
                        url = home_link+"/?term=%28"+search_kw+"%29+AND+%28"+busAut+"%5BAuthor%5D%29&filter=years.2003-"+str(anoFin)+"&size="+str(canres)
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
                        url = home_link+"/?term=%28"+search_kw+"%29+AND+%28"+busAut+"%5BAuthor%5D%29&filter=years."+str(anoIni)+"-"+str(ano)+"&size="+str(canres)
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo articulos")
                        url = home_link+"/?term=%28"+search_kw+"%29+AND+%28"+busAut+"%5BAuthor%5D%29&filter=years."+str(anoIni)+"-"+str(ano)+"&size="+str(canres)
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo documentos")
                        none=1
                else:
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html sin tener en cuenta el tipo de documentos")
                        url = home_link+"/?term=%28"+search_kw+"%29+AND+%28"+busAut+"%5BAuthor%5D%29&filter=years."+str(anoIni)+"-"+str(anoFin)+"&size="+str(canres)
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo articulos")
                        url = home_link+"/?term=%28"+search_kw+"%29+AND+%28"+busAut+"%5BAuthor%5D%29&filter=years."+str(anoIni)+"-"+str(anoFin)+"&size="+str(canres)
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
                        url = home_link+"/?term="+search_kw+"&size="+str(canres)
                    elif tipo_docu=='articulo':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                        url = home_link+"/?term="+search_kw+"&size="+str(canres)
                    elif tipo_docu=='revista':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        none=1
                else:
                    if tipo_docu=='todos':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html sin tener en cuenta el tipo de documento establecido")
                        url = home_link+"/?term="+search_kw+"&filter=years.2003-"+str(anoFin)+"&size="+str(canres)
                    elif tipo_docu=='articulo':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html pero solo de articulos")    
                        url = home_link+"/?term="+search_kw+"&filter=years.2003-"+str(anoFin)+"&size="+str(canres)
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
                        url = home_link+"/?term="+search_kw+"&filter=years."+str(anoIni)+"-"+str(ano)+"&size="+str(canres)
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo articulos")
                        url = home_link+"/?term="+search_kw+"&filter=years."+str(anoIni)+"-"+str(ano)+"&size="+str(canres)
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo documentos")
                        none=1
                else:
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html sin tener en cuenta el tipo de documentos")
                        url = home_link+"/?term="+search_kw+"&filter=years."+str(anoIni)+"-"+str(anoFin)+"&size="+str(canres)
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo articulos")
                        url = home_link+"/?term="+search_kw+"&filter=years."+str(anoIni)+"-"+str(anoFin)+"&size="+str(canres)
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo doumentos")
                        none=1
        #print(url)

        if none==0:

            # Realiza una solicitud GET a la página
            response = requests.get(url)

            # Verifica si la solicitud fue exitosa
            print("------------------------------------------------------------------------")

            if response.status_code == 200:

                # Parsea el contenido HTML usando BeautifulSoup
                soup = BeautifulSoup(response.text, "html.parser")
                result_items = soup.find_all('article', class_='full-docsum')

                #print(result_items)
                result_items = result_items[:10]

                for result in result_items:

                    titulo1 = result.find('div',class_='docsum-content')
                    if titulo1 is not None:
                        titulo2 = titulo1.find('a',class_='docsum-title')
                        if titulo2 is not None:
                            titulo = titulo2.text.strip()
                            titulo = titulo.replace("\n", " ")
                            titulo = titulo.replace("[", "")
                            titulo = titulo.replace("]", "")
                            titulo = titulo.replace(".", "")
                        else:
                            titulo = "No encontrado"  
                    else:
                        titulo = "No encontrado"     

                    autor1 = result.find('span', class_='docsum-authors short-authors')
                    if autor1 is not None:
                        autor = autor1.text.strip()
                        autor = autor.replace(",","")
                        autor = autor.replace("authors:",", ")
                    else:
                        autor = "No encontrado"
                    
                    resumen1 = result.find('div', class_='docsum-snippet')
                    if resumen1 is not None:
                        resumen2 = resumen1.find('div', class_='full-view-snippet')
                        if resumen2 is not None:
                            resumen = resumen2.text.strip()
                            resumen = resumen.replace("\n", "")
                        else:
                            resumen = "No encontrado"
                    else:
                        resumen = "No encontrado"

                    fuente1 = result.find( 'a', class_='docsum-title', href=True)
                    if fuente1 is not None:
                        fuente = home_link+fuente1['href'] 
                    else:
                        fuente = "No encontrado"    

                    fecha1 = result.find('div',class_='docsum-citation full-citation')
                    if fecha1 is not None:
                        fecha2 = fecha1.find('span', class_='docsum-journal-citation short-journal-citation')
                        if fecha2 is not None:
                            fecha = fecha2.text.strip()
                            fecha = fecha.replace(" ","")
                            palabras = fecha.split(".")
                            fecha = palabras[1]
                        else:
                            fecha = "No encontrado"
                    else:
                        fecha = "No encontrado"
                    
                    link = "No encontrado"
                    num_cit = "No encontrado"   
                    version = "No encontrado" 
                    repositorio = "PudMed"

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
                    print('-' * 50)  ''' 
                

            else:
                print("Error al hacer la solicitud:", response.status_code)    
                print("------------------------------------------------------------------------")

            return data
        else:
            print("este repositorio no contiene documentos con los filtros requeridos")
            return ""
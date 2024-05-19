import requests
import re
import datetime
from bs4 import BeautifulSoup

class Clase8:
    def funcion_clase8(self, search_kw, busAut, anoIni, anoFin, tipo_docu):

        data=[]
        none=0

        # Obtén la fecha actual
        fecha_actual = datetime.datetime.now()

        # Extrae el año de la fecha actual
        ano = fecha_actual.year

        home_link = "https://www.tesisenred.net"
        #canres sirve para colocarle cuantos resultados quiero que me bote la pagina
        canres = 10 #rango 5, 10, 20, 40, 60, 80, 100 pero permite jugar con mas valores

        if busAut!="":
            if anoIni=='':
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                        url = home_link+"/discover?query="+search_kw+"&filtertype_0=author&filter_relational_operator_0=contains&filter_0="+busAut+"&filtertype=accessLevel&filter_relational_operator=equals&filter=info%3Aeu-repo%2Fsemantics%2FopenAccess&rpp="+str(canres)+"&sort_by=score&order=desc"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                        none=1
                    elif tipo_docu=='revista':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        url = home_link+"/discover?query="+search_kw+"&filtertype_0=author&filter_relational_operator_0=contains&filter_0="+busAut+"&filtertype=accessLevel&filter_relational_operator=equals&filter=info%3Aeu-repo%2Fsemantics%2FopenAccess&rpp="+str(canres)+"&sort_by=score&order=desc"
                else:
                    if tipo_docu=='todos':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html sin tener en cuenta el tipo de documento establecido")
                        url = home_link+"/discover?query="+search_kw+"&scope=/&filtertype_0=accessLevel&filtertype_1=author&filter_relational_operator_1=contains&filter_relational_operator_0=equals&filter_1="+busAut+"&filter_0=info%3Aeu-repo%2Fsemantics%2FopenAccess&filtertype=dateIssued&filter_relational_operator=equals&filter=%5B2000+TO+"+str(anoFin)+"%5D&rpp="+str(canres)+"&sort_by=score&order=desc"
                    elif tipo_docu=='articulo':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html pero solo de articulos")    
                        none=1
                    elif tipo_docu=='revista':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de documentos")
                        url = home_link+"/discover?query="+search_kw+"&scope=/&filtertype_0=accessLevel&filtertype_1=author&filter_relational_operator_1=contains&filter_relational_operator_0=equals&filter_1="+busAut+"&filter_0=info%3Aeu-repo%2Fsemantics%2FopenAccess&filtertype=dateIssued&filter_relational_operator=equals&filter=%5B2000+TO+"+str(anoFin)+"%5D&rpp="+str(canres)+"&sort_by=score&order=desc"
            else:
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada sin tener en cuenta el tipo de documento")
                        url = home_link+"/discover?query="+search_kw+"&scope=/&filtertype_0=accessLevel&filtertype_1=author&filter_relational_operator_1=contains&filter_relational_operator_0=equals&filter_1="+busAut+"&filter_0=info%3Aeu-repo%2Fsemantics%2FopenAccess&filtertype=dateIssued&filter_relational_operator=equals&filter=%5B"+str(anoIni)+"+TO+"+str(ano)+"%5D&rpp="+str(canres)+"&sort_by=score&order=desc"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo articulos")
                        none=1
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo documentos")
                        url = home_link+"/discover?query="+search_kw+"&scope=/&filtertype_0=accessLevel&filtertype_1=author&filter_relational_operator_1=contains&filter_relational_operator_0=equals&filter_1="+busAut+"&filter_0=info%3Aeu-repo%2Fsemantics%2FopenAccess&filtertype=dateIssued&filter_relational_operator=equals&filter=%5B"+str(anoIni)+"+TO+"+str(ano)+"%5D&rpp="+str(canres)+"&sort_by=score&order=desc"
                else:
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html sin tener en cuenta el tipo de documentos")
                        url = home_link+"/discover?scope=%2F&query="+search_kw+"&filtertype_0=dateIssued&filtertype_1=author&filter_relational_operator_1=contains&filter_relational_operator_0=equals&filter_1="+busAut+"&filter_0=%5B"+str(anoIni)+"+TO+"+str(anoFin)+"%5D&rpp="+str(canres)+"&sort_by=score&order=desc"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo articulos")
                        none = 1
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo revistas")
                        none = 1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo doumentos")
                        url = home_link+"/discover?scope=%2F&query="+search_kw+"&filtertype_0=dateIssued&filtertype_1=author&filter_relational_operator_1=contains&filter_relational_operator_0=equals&filter_1="+busAut+"&filter_0=%5B"+str(anoIni)+"+TO+"+str(anoFin)+"%5D&rpp="+str(canres)+"&sort_by=score&order=desc"
        else:
            if anoIni=='':
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el titulo de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                        url = home_link+"/discover?scope=%2F&query="+search_kw+"&rpp="+str(canres)+"&sort_by=score&order=desc"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                        none=1
                    elif tipo_docu=='revista':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        url = home_link+"/discover?scope=%2F&query="+search_kw+"&rpp="+str(canres)+"&sort_by=score&order=desc"
                else:
                    if tipo_docu=='todos':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html sin tener en cuenta el tipo de documento establecido")
                        url = home_link+"/discover?query="+search_kw+"&scope=/&filtertype=dateIssued&filter_relational_operator=equals&filter=%5B2000+TO+"+str(anoFin)+"%5D&rpp="+str(canres)+"&sort_by=score&order=desc"
                    elif tipo_docu=='articulo':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html pero solo de articulos")    
                        none=1
                    elif tipo_docu=='revista':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de documentos")
                        url = home_link+"/discover?query="+search_kw+"&scope=/&filtertype=dateIssued&filter_relational_operator=equals&filter=%5B2000+TO+"+str(anoFin)+"%5D&rpp="+str(canres)+"&sort_by=score&order=desc"
            else:
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada sin tener en cuenta el tipo de documento")
                        url = home_link+"/discover?query="+search_kw+"&scope=/&filtertype=dateIssued&filter_relational_operator=equals&filter=%5B"+str(anoIni)+"+TO+"+str(ano)+"%5D&rpp="+str(canres)+"&sort_by=score&order=desc"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo articulos")
                        none=1
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo documentos")
                        url = home_link+"/discover?query="+search_kw+"&scope=/&filtertype=dateIssued&filter_relational_operator=equals&filter=%5B"+str(anoIni)+"+TO+"+str(ano)+"%5D&rpp="+str(canres)+"&sort_by=score&order=desc"
                else:
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html sin tener en cuenta el tipo de documentos")
                        url = home_link+"/discover?query="+search_kw+"&scope=/&filtertype=dateIssued&filter_relational_operator=equals&filter=%5B"+str(anoIni)+"+TO+"+str(anoFin)+"%5D&rpp="+str(canres)+"&sort_by=score&order=desc"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo articulos")
                        none=1
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo doumentos")
                        url = home_link+"/discover?query="+search_kw+"&scope=/&filtertype=dateIssued&filter_relational_operator=equals&filter=%5B"+str(anoIni)+"+TO+"+str(anoFin)+"%5D&rpp="+str(canres)+"&sort_by=score&order=desc"

        #print(url)
        if none==0:

            # Realiza una solicitud GET a la página
            response = requests.get(url)

            # Verifica si la solicitud fue exitosa
            print("------------------------------------------------------------------------")

            if response.status_code == 200:

                # Parsea el contenido HTML usando BeautifulSoup
                soup = BeautifulSoup(response.text, "html.parser")
                result_items = soup.find_all('div', class_='media')

                #print(result_items)
                #print(url)

                result_items = result_items[:10]
                for result in result_items:

                    titulo1 = result.find('h4', class_='media-heading')
                    if titulo1 is not None:
                        titulo = titulo1.text.strip()
                        titulo = titulo.replace("\n", " ")
                    else:
                        titulo = "No encontrado"

                    autor_elem = result.find('p', class_='author')
                    if autor_elem is not None:
                        autor_span = autor_elem.find('span', class_='ds-dc_contributor_author-authority')
                        if autor_span is not None:
                            autor = autor_span.text.strip()
                        else:
                            autor = "No encontrado"
                    else:
                        autor = "No encontrado"
                    
                    resumen = result.find('div', class_='media-body')
                    if resumen is not None:
                        # Verifica que se haya encontrado el elemento 'media-body'
                        parrafos = resumen.find_all('p')
                        if len(parrafos) > 1:
                            # Verifica que haya al menos dos párrafos
                            resumen = parrafos[1].get_text(strip=True).replace("\n", "")
                        else:
                            resumen = "No encontrado"
                    else:
                        resumen = "No encontrado"

                    fuente = home_link
                    fuente_elem = result.find('h4', class_='media-heading')
                    if fuente_elem is not None:
                        fuente_elem = result.find('a', href=True)
                        if fuente_elem is not None:
                            fuente = fuente+fuente_elem['href'] 
                        else:
                            fuente = "No encontrado"
                    else:
                        fuente = "No encontrado"

                    fecha = result.find('p', class_='author')
                    if fecha is not None:
                        fecha_texto = fecha.find('span', class_='date')
                        if fecha_texto is not None:
                            fecha_texto1 = fecha_texto.text.strip()
                            patron = r'\d{4}-\d{2}-\d{2}'
                            fecha1 = re.search(patron, fecha_texto1)
                            if fecha1 is not None:
                                fecha = fecha1.group()
                            else:
                                fecha = "No encontrado"
                        else:
                            fecha = "No encontrado"
                    else:
                        fecha = "No encontrado"


                    link = fuente
                    num_cit = "No encontrado"   
                    tipo_docu = "No encontrado"
                    version = "No encontrado"
                    repositorio = "Cora"
                    componentes_fecha = fecha.split("-")
                    com = componentes_fecha[0]
                    cadena_limpia = com.lstrip()
                    if fecha != "No encontrado":
                            fec = int(cadena_limpia)
                    else:
                            fec = 0  # o cualquier otro valor predeterminado que desees usar en caso de que la fecha no esté disponible

                    #print(str(fec)+" Fecha")
                    
                    fecha = str(fec)

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

                
            else:
                print("Error al hacer la solicitud:", response.status_code)    
                print("------------------------------------------------------------------------")
                
            return data
        else:
            print("este repositorio no contiene documentos con los filtros requeridos")
            return ""
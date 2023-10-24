import requests
import re
import datetime
from bs4 import BeautifulSoup

class Clase4:
    
    def funcion_clase4(self, search_kw, busAut, anoIni, anoFin, tipo_docu):

        data=[]
        none=0

        # Obtén la fecha actual
        fecha_actual = datetime.datetime.now()

        # Extrae el año de la fecha actual
        ano = fecha_actual.year
        canres = 25 # rango 25, 50, 100, 200

        home_link = "https://arxiv.org"

        if busAut!="":
            if anoIni=='':
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                        url = home_link+"/search/advanced?advanced=1&terms-0-operator=AND&terms-0-term="+search_kw+"&terms-0-field=title&terms-1-operator=AND&terms-1-term="+busAut+"&terms-1-field=author&classification-physics_archives=all&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date&abstracts=show&size="+str(canres)+"&order=-announced_date_first"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                        none = 1
                    elif tipo_docu=='revista':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        url = home_link+"/search/advanced?advanced=1&terms-0-operator=AND&terms-0-term="+search_kw+"&terms-0-field=title&terms-1-operator=AND&terms-1-term="+busAut+"&terms-1-field=author&classification-physics_archives=all&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date&abstracts=show&size="+str(canres)+"&order=-announced_date_first"
                else:
                    if tipo_docu=='todos':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html sin tener en cuenta el tipo de documento establecido")
                        url = home_link+"/search/advanced?advanced=&terms-0-operator=AND&terms-0-term="+search_kw+"&terms-0-field=title&terms-1-operator=AND&terms-1-term="+busAut+"&terms-1-field=author&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date=2003&date-to_date="+str(anoFin)+"&date-date_type=submitted_date&abstracts=show&size="+str(canres)+"&order=-announced_date_first"
                    elif tipo_docu=='articulo':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html pero solo de articulos")    
                        none = 1
                    elif tipo_docu=='revista':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de revistas")
                        none = 1
                    elif tipo_docu=='documento':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de documentos")
                        url = home_link+"/search/advanced?advanced=&terms-0-operator=AND&terms-0-term="+search_kw+"&terms-0-field=title&terms-1-operator=AND&terms-1-term="+busAut+"&terms-1-field=author&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date=2003&date-to_date="+str(anoFin)+"&date-date_type=submitted_date&abstracts=show&size="+str(canres)+"&order=-announced_date_first"
            else:
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada sin tener en cuenta el tipo de documento")
                        url = home_link+"/search/advanced?advanced=&terms-0-operator=AND&terms-0-term="+search_kw+"&terms-0-field=title&terms-1-operator=AND&terms-1-term="+busAut+"&terms-1-field=author&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date="+str(anoIni)+"&date-to_date="+str(ano)+"&date-date_type=submitted_date&abstracts=show&size="+str(canres)+"&order=-announced_date_first"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo articulos")
                        none = 1
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo revistas")
                        none = 1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo documentos")
                       url = home_link+"/search/advanced?advanced=&terms-0-operator=AND&terms-0-term="+search_kw+"&terms-0-field=title&terms-1-operator=AND&terms-1-term="+busAut+"&terms-1-field=author&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date="+str(anoIni)+"&date-to_date="+str(ano)+"&date-date_type=submitted_date&abstracts=show&size="+str(canres)+"&order=-announced_date_first"
                else:
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html sin tener en cuenta el tipo de documentos")
                        url = home_link+"/search/advanced?advanced=&terms-0-operator=AND&terms-0-term="+search_kw+"&terms-0-field=title&terms-1-operator=AND&terms-1-term="+busAut+"&terms-1-field=author&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date="+str(anoIni)+"&date-to_date="+str(anoFin)+"&date-date_type=submitted_date&abstracts=show&size="+str(canres)+"&order=-announced_date_first"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo articulos")
                        none = 1
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo revistas")
                        none = 1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo doumentos")
                        url = home_link+"/search/advanced?advanced=&terms-0-operator=AND&terms-0-term="+search_kw+"&terms-0-field=title&terms-1-operator=AND&terms-1-term="+busAut+"&terms-1-field=author&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date="+str(anoIni)+"&date-to_date="+str(anoFin)+"&date-date_type=submitted_date&abstracts=show&size="+str(canres)+"&order=-announced_date_first"
        else:
            if anoIni=='':
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el titulo de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                        url = home_link+"/search/?query="+search_kw+"&searchtype=all&abstracts=show&order=&size="+str(canres)
                    elif tipo_docu=='articulo':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                        none = 1
                    elif tipo_docu=='revista':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                        url = home_link+"/search/?query="+search_kw+"&searchtype=all&abstracts=show&order=&size=25"+str(canres)
                else:
                    if tipo_docu=='todos':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html sin tener en cuenta el tipo de documento establecido")
                        url = home_link+"/search/advanced?advanced=&terms-0-operator=AND&terms-0-term="+search_kw+"&terms-0-field=title&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date=2003&date-to_date="+str(anoFin)+"&date-date_type=submitted_date&abstracts=show&size="+str(canres)+"&order=-announced_date_first"
                    elif tipo_docu=='articulo':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final en html pero solo de articulos")    
                        none = 1
                    elif tipo_docu=='revista':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca autor y fechas con filtro incial desde el año que inician las busquedas en el repositrio hasta la fecha final establecida en la busqueda pero solo de documentos")
                        url = home_link+"/search/advanced?advanced=&terms-0-operator=AND&terms-0-term="+search_kw+"&terms-0-field=title&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date=2003&date-to_date="+str(anoFin)+"&date-date_type=submitted_date&abstracts=show&size="+str(canres)+"&order=-announced_date_first"
            else:
                if anoFin=='':
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada sin tener en cuenta el tipo de documento")
                        url = home_link+"/search/advanced?advanced=&terms-0-operator=AND&terms-0-term="+search_kw+"&terms-0-field=title&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date="+str(anoIni)+"&date-to_date="+str(ano)+"&date-date_type=submitted_date&abstracts=show&size="+str(canres)+"&order=-announced_date_first"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo articulos")
                        unone = 1
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final del repositorio encontrada pero solo documentos")
                        url = home_link+"/search/advanced?advanced=&terms-0-operator=AND&terms-0-term="+search_kw+"&terms-0-field=title&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date="+str(anoIni)+"&date-to_date="+str(ano)+"&date-date_type=submitted_date&abstracts=show&size="+str(canres)+"&order=-announced_date_first"
                else:
                    if tipo_docu=='todos':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html sin tener en cuenta el tipo de documentos")
                        url = home_link+"/search/advanced?advanced=&terms-0-operator=AND&terms-0-term="+search_kw+"&terms-0-field=title&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date="+str(anoIni)+"&date-to_date="+str(anoFin)+"&date-date_type=submitted_date&abstracts=show&size="+str(canres)+"&order=-announced_date_first"
                    elif tipo_docu=='articulo':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo articulos")
                        none = 1
                    elif tipo_docu=='revista':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo revistas")
                        none=1
                    elif tipo_docu=='documento':
                        #print("se busca el autor con filtro de fecha de inicial establecida en html hasta fecha final establecida en html pero solo doumentos")
                        url = home_link+"/search/advanced?advanced=&terms-0-operator=AND&terms-0-term="+search_kw+"&terms-0-field=title&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date="+str(anoIni)+"&date-to_date="+str(anoFin)+"&date-date_type=submitted_date&abstracts=show&size="+str(canres)+"&order=-announced_date_first"

        if none==0:
            #print(url)
            # Realiza una solicitud GET a la página
            response = requests.get(url)

            # Verifica si la solicitud fue exitosa
            if response.status_code == 200:

                # Parsea el contenido HTML usando BeautifulSoup
                soup = BeautifulSoup(response.text, "html.parser")
                result_items = soup.find_all('li', class_='arxiv-result')

                #print(result_items)
                
                result_items = result_items[:10]

                for result in result_items:

                    titulo_elem = result.find('p',class_='title is-5 mathjax')
                    if titulo_elem is not None:
                        titulo = titulo_elem.get_text(strip=True) 
                    else:
                        titulo = "No encontrado"

                    autor_elem = result.find('p', class_='authors')
                    if autor_elem is not None:
                        autor_text = autor_elem.get_text(strip=True)
                        autor = autor_text.split(":")[1].strip()  # Dividir por ":" y obtener el segundo elemento
                    else:
                        autor = 'No encontrado'

                    resumen_elem = result.find('span',class_='abstract-short has-text-grey-dark mathjax') 
                    if resumen_elem is not None:
                        resumen_text = resumen_elem.get_text(strip=True)
                        resumen = resumen_text.replace("▽", "").replace("More", "").strip()  # Dividir por ":" y obtener el segundo elemento
                    else:
                        resumen = 'No encontrado'

                    fuente_elem1 = result.find('p', class_='list-title is-inline-block')
                    if fuente_elem1 is not None:
                        fuente_elem2 = fuente_elem1.find('a', href=True) 
                        if fuente_elem2 is not None:
                            fuente_text = fuente_elem2.get_text(strip=True)
                            identificador = fuente_text.split(":")[1].strip()  # Dividir por ":" y obtener el segundo elemento
                            fuente = 'https://arxiv.org/abs/'+identificador
                        else:
                            fuente = 'No encontrado'
                    else:
                        fuente = 'No encontrado'

                    link_elem1 = result.find('p', class_='list-title is-inline-block')   
                    if link_elem1 is not None:
                        link_elem2 = link_elem1.find_all('a', href=True)
                        if len(link_elem2) > 1:
                            link = link_elem2[1]['href'] 
                        else:
                            link = "No encontrado"
                    else:
                        link = "No encontrado"
    
                    fech_elem = result.find('p', class_='is-size-7')
                    if fech_elem is not None:
                        fecha = fech_elem.get_text(strip=True) 
                        fecha2 = re.search(r'\d{4}', fecha)
                        fecha = fecha2.group(0) 
                    else:
                        fecha = "No encontrado"
                    
                    num_cit = 'No encontrado'
                    repositorio = 'Arxiv'

                    version1 = result.find('p',class_='is-size-7')
                    if version1 is not None:
                        version2 = version1.find_all('span', class_="has-text-black-bis has-text-weight-semibold")
                        if len(version2) > 1:
                            version = version2[1].getText(strip=True)
                        else:
                            version = "No encontrado"
                    else:
                        version = "No encontrado"

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
                    print('Fecha de publicación:' , fecha3)
                    print('Enlace del documento:' , link)
                    print('Número de citas:' , num_cit)
                    print('Tipo de documento consultado:' , tipo_docu)
                    print('Cantidad de versiones del documento:' , version) 
                    print('Repositorio:' , repositorio) 
                    print('-' * 50)   '''
                
            
            else:
                print("Error al hacer la solicitud:", response.status_code)   
                print("------------------------------------------------------------------------") 
            
            return data
        
        else:
            print("este repositorio no contiene documentos con los filtros requeridos")
            return ""
        

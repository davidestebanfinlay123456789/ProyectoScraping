import requests
import re
import datetime
from bs4 import BeautifulSoup

class Clase10:
    def funcion_clase10(self, search_kw, busAut, anoIni, anoFin, tipo_docu):

        data=[]
        none=0

        fecha_actual = datetime.datetime.now()
        ano = fecha_actual.year
        
        canres = 15 #rango 15, 30, 50
        home_link = "https://search.scielo.org"

        if busAut!="":
            if tipo_docu=='todos':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                url = home_link+"/?q=%28"+search_kw+"%29+AND+%28au%3A%28"+busAut+"%29%29&lang=es&count="+str(canres)+"&page=1&where=&filter%5Byear_cluster%5D%5B%5D="+str(ano)
                tipo_docu1 = "PDF"
            elif tipo_docu=='articulo':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                url = home_link+"/?q=%28"+search_kw+"%29+AND+%28au%3A%28"+busAut+"%29%29&lang=es&count="+str(canres)+"&page=1&where=&filter%5Btype%5D%5B%5D=research-article&filter%5Btype%5D%5B%5D=review-article&filter%5Btype%5D%5B%5D=article-commentary&where=&filter%5Byear_cluster%5D%5B%5D="+str(ano)
                tipo_docu1 = "Articulo-PDF"
            elif tipo_docu=='revista':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                url = home_link+"/?q=%28"+search_kw+"%29+AND+%28au%3A%28"+busAut+"%29%29&lang=es&count="+str(canres)+"&page=1&where=&filter%5Btype%5D%5B%5D=editorial&where=&filter%5Byear_cluster%5D%5B%5D="+str(ano)
                tipo_docu1 = "Revista-PDF"
            elif tipo_docu=='documento':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                url = home_link+"/?q=%28"+search_kw+"%29+AND+%28au%3A%28"+busAut+"%29%29&lang=es&count="+str(canres)+"&page=1&where=&filter%5Byear_cluster%5D%5B%5D="+str(ano) 
                tipo_docu1 = "PDF"
        else:
            if tipo_docu=='todos':
                #print("se busca el titulo de fecha incial del repositorio a final del repositorio y no se tiene en cuenta un tipo de documento espesifico")
                url = home_link+"/?q=&lang=pt&count="+str(canres)+"&from=0&output=site&sort=&format=summary&fb=&page=1&q="+search_kw+"&lang=es&page=1&where=&filter%5Byear_cluster%5D%5B%5D="+str(ano)
                tipo_docu1 = "PDF"
            elif tipo_docu=='articulo':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan articulos")
                url = home_link+"/?q=&lang=pt&count="+str(canres)+"&from=0&output=site&sort=&format=summary&fb=&page=1&q="+search_kw+"&lang=es&page=1&where=&filter%5Btype%5D%5B%5D=research-article&filter%5Btype%5D%5B%5D=review-article&filter%5Btype%5D%5B%5D=article-commentary&where=&filter%5Byear_cluster%5D%5B%5D="+str(ano)
                tipo_docu1 = "Articulo-PDF"
            elif tipo_docu=='revista':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                url = home_link+"/?q=&lang=pt&count="+str(canres)+"&from=0&output=site&sort=&format=summary&fb=&page=1&q="+search_kw+"&lang=es&page=1&where=&filter%5Btype%5D%5B%5D=editorial&where=&filter%5Byear_cluster%5D%5B%5D="+str(ano)
                tipo_docu1 = "Revista-PDF"
            elif tipo_docu=='documento':
                #print("se busca el autor de fecha incial del repositorio a final del repositorio y solo se buscan revistas")
                url = home_link+"/?q=&lang=pt&count="+str(canres)+"&from=0&output=site&sort=&format=summary&fb=&page=1&q="+search_kw+"&lang=es&page=1&where=&filter%5Byear_cluster%5D%5B%5D="+str(ano)
                tipo_docu1 = "PDF"

        print(url)

        if none==0:

            # Realiza una solicitud GET a la página
            response = requests.get(url)

            # Verifica si la solicitud fue exitosa
            print("------------------------------------------------------------------------")

            if response.status_code == 200:

                # Parsea el contenido HTML usando BeautifulSoup
                soup = BeautifulSoup(response.text, "html.parser")
                result_items = soup.find_all('div', class_='item')

                #print(result_items)
                result_items = result_items[:15]

                for result in result_items:

                    titulo1 = result.find('strong',class_='title')
                    if titulo1 is not None:
                        titulo = titulo1.text.strip()
                        titulo = titulo.replace("\n", " ")
                    else:
                        titulo = "No encontrado"
                    

                    autor1 = result.find('div', class_='line authors')
                    if autor1 is not None:
                        autor = autor1.text
                        autor= autor.replace("\n"," ")
                        oracion_limpia = re.sub(r'\s+', ' ', autor.strip())
                        autor = oracion_limpia
                    else:
                        autor = "No encontrado"

                    resumen1 = result.find('div', class_='user-actions')
                    if resumen1 is not None:
                        # Verifica que se haya encontrado el elemento 'media-body'
                        parrafos = resumen1.find_all('div')
                        if len(parrafos) > 2:
                            # Verifica que haya al menos dos párrafos
                            resumen = parrafos[2].get_text(strip=True).replace("\n", "")
                            resumen = resumen.replace("\n", "")
                        else:
                            resumen = parrafos[1].get_text(strip=True).replace("\n", "")
                            resumen = resumen.replace("\n", "")
                    else:
                        resumen = "No encontrado"

                    fuente1 = result.find( 'div', class_='line')
                    if fuente1 is not None:
                        fuente2 = fuente1.find('a', href=True)
                        if fuente2 is not None:
                            fuente = fuente2['href'] 
                        else:
                            fuente = "No encontrado"
                    else:
                        fuente = "No encontrado"

                    fecha1 = result.find('div',class_='line source')
                    if fecha1 is not None:
                        fecha2 = fecha1.find_all('span')
                        if len(fecha2) > 2: 
                            fecha = fecha2[2].get_text(strip=True) 
                            fecha = fecha.replace(",","")
                        else:
                            fecha = "No encontrado"
                    else:
                        fecha = "No encontrado"
                    
                    link_elem = result.find('div', class_='line versions')
                    if link_elem is not None:
                        link_elem1 = link_elem.find_all('span')
                        link = "No encontrado"  
                        for elem in link_elem1:
                            elem1 = elem.text.strip().replace("\n", "").replace(" ", "")  # Corrige el formato del texto
                            if elem1 == 'PDF:Es':
                                link_elem2 = elem.find('a', href=True)
                                if link_elem2:
                                    link = link_elem2['href']
                                break  # Sal del bucle una vez que se encuentre el enlace PDF
                            if elem1 == 'PDF:En':
                                link_elem2 = elem.find('a', href=True)
                                if link_elem2:
                                    link = link_elem2['href']
                    else:
                        link = "No encontrado"

                    num_cit = "No encontrado"   

                    version = "No encontrado"  # Inicializar la variable 'version
                    versionN1 = result.find('div', class_='line source')
                    if versionN1 is not None:
                        versionN2 = versionN1.find_all('small')
                        if len(versionN2) > 0:
                            versionN = versionN2[0].getText(strip=True)
                            version1 = result.find('div', class_='line source')
                            if version1 is not None:
                                version2 = version1.find_all('span')[3]
                                if len(version2) > 3:
                                    version = version2[3].getText(strip=True)
                                    version = versionN + ": " + version

                    # Ahora, la variable 'version' tiene un valor en caso de que ninguna condición se cumpla
                            
                    tipo_docu = tipo_docu1
                    repositorio = "Scielo"

                    print("fecha"+fecha)

                    if fecha!="No encontrado":
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
                

            else:
                print("Error al hacer la solicitud:", response.status_code)    
                print("------------------------------------------------------------------------")

            return data
        
        else:
            print("este repositorio no contiene documentos con los filtros requeridos")
            return ""
import requests
import re
from bs4 import BeautifulSoup

class Clase4:
    
    def funcion_clase4(self, search_kw):

        data=[]

        home_link = "https://arxiv.org"

        # URL de la página de arXiv que deseas scrapear
        url = home_link+"/search/?query="+search_kw+"&searchtype=all&abstracts=show&order=&size=25"

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
                titulo = ""
                titulo_elem = ""
                autor = ""
                autor2 = ""
                autor_elem = ""
                resumen = ""
                resumen_elem = ""
                resumen2 = ""
                fuente_elem = ""
                fuente = ""
                identificador = ""
                fuente_text = ""
                fecha = ""
                fecha2 = ""
                fecha3 = ""
                fech_elem = ""
                link_elem = ""
                link = ""
                num_cit = ""
                tipo_docu = ""
                version = ""
                repositorio = ""

                titulo_elem = result.find('p',class_='title is-5 mathjax')
                autor_elem = result.find('p', class_='authors')
                if autor_elem:
                    autor_text = autor_elem.get_text(strip=True)
                    autor2 = autor_text.split(":")[1].strip()  # Dividir por ":" y obtener el segundo elemento
                else:
                    identificador = 'NO ENCONTRADO'
                resumen_elem = result.find('span',class_='abstract-short has-text-grey-dark mathjax') 
                if resumen_elem:
                    resumen_text = resumen_elem.get_text(strip=True)
                    resumen2 = resumen_text.replace("▽", "").replace("More", "").strip()  # Dividir por ":" y obtener el segundo elemento
                else:
                    identificador = 'NO ENCONTRADO'
                fuente_elem = result.find('p', class_='list-title is-inline-block').find('a', href=True) 
                if fuente_elem:
                    fuente_text = fuente_elem.get_text(strip=True)
                    identificador = fuente_text.split(":")[1].strip()  # Dividir por ":" y obtener el segundo elemento
                else:
                    identificador = 'NO ENCONTRADO'
                link_elem = result.find('p', class_='list-title is-inline-block').find_all('a', href=True)[1]      
                
                fech_elem = result.find('p', class_='is-size-7')

                titulo = titulo_elem.get_text(strip=True) if resumen_elem else 'NO ENCONTRADO'
                        
                resumen = resumen2
                link = link_elem['href'] if link_elem else 'NO ENCONTRADO'

                autor = autor2
                fuente = 'https://arxiv.org/abs/'+identificador
                fecha = fech_elem.get_text(strip=True) if fech_elem else ''
                fecha2 = re.search(r'\d{4}', fecha)
                fecha3=''
                fecha3 = fecha2.group(0) if fecha else 'NO ENCONTRADA'
                
                num_cit = 'NO ENCONTRADO'
                #en esta parte traere a llamar a una sola parte de el resultado por defecto de fecha y lo almacenare en fecha1

                tipo_docu = 'PDF,OTRO'
                version = 'NO ENCONTRADO'
                repositorio="Arxiv"

                # Agrega los datos a la lista
                data.append({'Título de la investigación:': titulo, 'Autor:': autor, 'Descripción:': resumen, 'Fuente:': fuente, 'Fecha de publicación:': fecha3, 'Enlace del documento:': link, 'Número de citas:': num_cit, 'Tipo de documento consultado:': tipo_docu, 'Cantidad de versiones del documento:': version, 'Repositorio': repositorio})
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
    
        

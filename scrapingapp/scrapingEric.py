import requests
import re
from bs4 import BeautifulSoup

class Clase7:
    def funcion_clase7(self, search_kw):

        data=[]

        home_link = "https://eric.ed.gov"

        # URL de la página de arXiv que deseas scrapear
        url = home_link+"/?q="+search_kw

        # Realiza una solicitud GET a la página
        response = requests.get(url)

        # Verifica si la solicitud fue exitosa
        print("------------------------------------------------------------------------")

        if response.status_code == 200:

            print(url)

            # Parsea el contenido HTML usando BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            result_items = soup.find_all('div', class_='r_i')

            #print(result_items)
            result_items = result_items[:10]

            for result in result_items:

                titulo = ""
                autor = ""
                partes = ""
                resumen = ""
                fuente_elem = ""
                fuente = ""
                fecha = ""
                patron = ""
                fecha1 = ""
                link_elem = ""
                link = ""
                num_cit = ""
                tipo_docu = ""
                version = ""
                repositorio = ""

                titulo = result.find('a').text.strip()
                titulo = titulo.replace("\n", " ")
                autor = result.find('div', class_='r_a').text.strip()
                partes = autor.split(" – ")
                autor = partes[0]
                autor= autor.replace(";","")
                resumen = result.find('div', class_='r_d').text.strip()
                resumen = resumen.replace("\n", "")
                fuente_elem = result.find( 'a', href=True)
                fuente = ""+home_link
                fuente = fuente+fuente_elem['href'] 
                fecha = result.find('div',class_='r_a').text.strip()
                # Buscar patrones de cuatro dígitos (años)
                patron = r'\b\d{4}\b'
                fecha = re.findall(patron, fecha)
                fecha1 = ', '.join(fecha)
                #fecha1 = fecha1.replace(" ","")

                link_elem = result.find('div', class_='r_f').find( 'a', href=True)
                if link_elem is not None:
                    link = link_elem['href']
                    # Resto del código que utiliza link
                else:
                    # Manejo en caso de que link_elem sea None
                    link = "No encontrado"


                if link.startswith("http"): 
                    link = link_elem['href'] 
                if link.startswith(""):
                    link = "No encontrado"
                else:
                    link = home_link+'/'+link_elem['href'] 

                num_cit = "No encontrado"
                   
                tipo_docu = result.find('div', class_='r_f').text.strip()

                if tipo_docu == 'Peer reviewed Download full text': tipo_docu='PDF' 
                else : tipo_docu='LINK' 
                
                version = "No encontrado"
                repositorio = "Eric"

                if titulo == "" : titulo = "No encontrado"
                if autor == "" : autor = "No encontrado"
                if resumen == "" : resumen = "No encontrado"
                if fuente == "" : fuente = "No encontrado"
                if fecha1 == "" : fecha1 = "No encontrado"
                if link == "" : link = "No encontrado"
                if num_cit == "" : num_cit = "No encontrado"
                if version == "" : version = "No encontrado"


                # Agrega los datos a la lista
                data.append({'Título de la investigación:': titulo, 'Autor:': autor, 'Descripción:': resumen, 'Fuente:': fuente, 'Fecha de publicación:': fecha1, 'Enlace del documento:': link, 'Número de citas:': num_cit, 'Tipo de documento consultado:': tipo_docu, 'Cantidad de versiones del documento:': version, 'Repositorio': repositorio})
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
                print('-' * 50)   
            

        else:
            print("Error al hacer la solicitud:", response.status_code)    
            print("------------------------------------------------------------------------")

        return data
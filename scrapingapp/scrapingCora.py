import requests
import re
from bs4 import BeautifulSoup

class Clase8:
    def funcion_clase8(self, search_kw):

        data=[]

        home_link = "https://www.tesisenred.net"

        # URL de la página de arXiv que deseas scrapear
        url = home_link+"/discover?query="+search_kw+"&scope=/&filtertype=dateIssued&filter_relational_operator=equals&filter=%5B2015+TO+2023%5D"

        # Realiza una solicitud GET a la página
        response = requests.get(url)

        # Verifica si la solicitud fue exitosa
        print("------------------------------------------------------------------------")

        if response.status_code == 200:

            # Parsea el contenido HTML usando BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            result_items = soup.find_all('div', class_='media')

            #print(result_items)

            result_items = result_items[:10]
            for result in result_items:

                titulo = ""
                autor = ""
                resumen = ""
                fuente_elem = ""
                fuente = ""
                fecha = ""
                fecha1 = ""
                patron = ""
                link = ""
                num_cit = ""
                tipo_docu = ""
                version = ""
                repositorio = ""

                titulo = result.find('h4', class_='media-heading').text.strip()
                titulo = titulo.replace("\n", " ")
                autor = result.find('p', class_='author').find('span', class_='ds-dc_contributor_author-authority').text.strip()
                resumen = result.find('div', class_='media-body').find_all('p')[1]
                resumen = resumen.get_text(strip=True)
                resumen = resumen.replace("\n", "")
                fuente_elem = result.find('h4', class_='media-heading').find('a', href=True)
                fuente = ""+home_link
                fuente = fuente+fuente_elem['href'] 

                fecha = result.find('p',class_='author').find('span', class_='date').text.strip()
                patron = r'\d{4}-\d{2}-\d{2}'
                fecha1 = re.search(patron, fecha).group()

                link = "No encontrado"
                num_cit = "No encontrado"   
                tipo_docu = "No encontrado"
                version = "No encontrado"
                repositorio = "Cora"

                if titulo == "" : titulo = "No encontrado"
                if autor == "" : autor = "No encontrado"
                if resumen == "" : resumen = "No encontrado"
                if fuente == "" : fuente = "No encontrado"
                if fecha1 == "" : fecha1 = "No encontrado"
                if link == "" : link = "No encontrado"
                if num_cit == "" : num_cit = "No encontrado"
                if tipo_docu == "" : tipo_docu = "No encontrado"
                if version == "" : version = "No encontrado"


                # Agrega los datos a la lista
                data.append({'Título de la investigación:': titulo, 'Autor:': autor, 'Descripción:': resumen, 'Fuente:': fuente, 'Fecha de publicación:': fecha1, 'Enlace del documento:': link, 'Número de citas:': num_cit, 'Tipo de documento consultado:': tipo_docu, 'Cantidad de versiones del documento:': version, 'Repositrio': repositorio})
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
                print('Repositoio:' , repositorio) 
                print('-' * 50)   
            

        else:
            print("Error al hacer la solicitud:", response.status_code)    
            print("------------------------------------------------------------------------")

        return data
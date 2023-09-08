import requests
import re
from bs4 import BeautifulSoup

class Clase10:
    def funcion_clase10(self, search_kw):

        data=[]

        home_link = "https://search.scielo.org"

        # URL de la página de arXiv que deseas scrapear
        url = home_link+"/?lang=es&count=15&from=0&output=site&sort=&format=summary&fb=&page=1&q="+search_kw

        # Realiza una solicitud GET a la página
        response = requests.get(url)

        # Verifica si la solicitud fue exitosa
        print("------------------------------------------------------------------------")

        if response.status_code == 200:

            # Parsea el contenido HTML usando BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            result_items = soup.find_all('div', class_='item')

            #print(result_items)
            result_items = result_items[:10]

            for result in result_items:

                titulo = ""
                autor = ""
                resumen = ""
                fuente = ""
                fecha = ""
                link_elem = ""
                link = ""
                num_cit = ""
                tipo_docu = ""
                version = ""
                versionN = ""
                repositorio = ""

                titulo = result.find('strong',class_='title').text.strip()
                titulo = titulo.replace("\n", " ")
                autor = result.find('div', class_='line authors').text
                autor= autor.replace("\n"," ")
                oracion_limpia = re.sub(r'\s+', ' ', autor.strip())
                autor = oracion_limpia

                resumen = result.find('div', class_='user-actions').find_all('div')[2]
                resumen = resumen.getText(strip=True)
                resumen = resumen.replace("\n", "")
                fuente = result.find( 'div', class_='line').find('a', href=True)
                fuente = fuente['href'] 

                fecha = result.find('div',class_='line source').find_all('span')[2]
                fecha = fecha.get_text(strip=True) 
                fecha = fecha.replace(",","")
                
                link_elem = result.find('div', class_='line versions').find_all('span')[6].find('a', href=True)
                link = link_elem['href'] 

                num_cit = "No encontrado"   
                tipo_docu = "PDF"
                versionN = result.find('div',class_='line source').find_all('small')[0]
                versionN = versionN.getText(strip=True)
                version = result.find('div',class_='line source').find_all('span')[3]
                version = version.getText(strip=True) 
                version = versionN+": "+version

                repositorio = "Scielo"

                if titulo == "" : titulo = "No encontrado"
                if autor == "" : autor = "No encontrado"
                if resumen == "" : resumen = "No encontrado"
                if fuente == "" : fuente = "No encontrado"
                if fecha == "" : fecha = "No encontrado"
                if link == "" : link = "No encontrado"
                if num_cit == "" : num_cit = "No encontrado"
                if tipo_docu == "" : tipo_docu = "No encontrado"
                if version == "" : version = "No encontrado"


                # Agrega los datos a la lista
                data.append({'Título de la investigación:': titulo, 'Autor:': autor, 'Descripción:': resumen, 'Fuente:': fuente, 'Fecha de publicación:': fecha, 'Enlace del documento:': link, 'Número de citas:': num_cit, 'Tipo de documento consultado:': tipo_docu, 'Cantidad de versiones del documento:': version, 'Repositrio': repositorio})
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
                print('-' * 50) '''  
            

        else:
            print("Error al hacer la solicitud:", response.status_code)    
            print("------------------------------------------------------------------------")

        return data
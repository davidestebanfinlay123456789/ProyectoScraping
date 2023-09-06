import requests
from bs4 import BeautifulSoup

class Clase1:
    def funcion_clase1(self, search_kw):

        data=[]

        home_link = "https://pubmed.ncbi.nlm.nih.gov"

        # URL de la página de arXiv que deseas scrapear
        url = home_link+"/?term="+search_kw

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

                titulo = ""
                autor = ""
                resumen = ""
                fuente = ""
                fecha = ""
                palabras = ""
                link_elem = ""
                link = ""
                num_cit = ""
                tipo_docu = ""
                version = ""
                repositorio = ""

                titulo = result.find('div',class_='docsum-content').find('a',class_='docsum-title').text.strip()
                titulo = titulo.replace("\n", " ")
                autor = result.find('span', class_='docsum-authors short-authors').text.strip()
                autor= autor.replace(",","")
                resumen = result.find('div', class_='docsum-snippet').find('div', class_='full-view-snippet').text.strip()
                resumen = resumen.replace("\n", "")
                fuente = "no encontrado"
                fecha = result.find('div',class_='docsum-citation full-citation').find('span', class_='docsum-journal-citation short-journal-citation').text.strip()
                fecha = fecha.replace(" ","")
                # Separar las palabras por puntos
                palabras = fecha.split(".")
                # Obtener la primera palabra
                fecha1 = palabras[1]
                link_elem = result.find( 'a', class_='docsum-title', href=True)
                link = ""+home_link
                link = link+link_elem['href'] 
                num_cit = "No encontrado"   
                tipo_docu = "No encontrado"
                version = "No encontrado"
                repositorio = "PudMed"

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
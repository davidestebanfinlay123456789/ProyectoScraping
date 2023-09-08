import pandas as pd
from django.shortcuts import render

from .scrapingArxiv import Clase4
from .scrapingEric import Clase7
from .scrapingCora import Clase8
from .scrapingPudMed import Clase1
from .scrapingScielo import Clase10

from .models import Resultado  # Asegúrate de importar tu modelo Resultado
from django.shortcuts import render

all_data = []  # Declara una variable global para almacenar los datos

def index(request):
    return render(request, 'index.html')

def resultados(request):
    return render(request, 'resultados.html', {'data': []})

def scrape_and_export(request):
    global all_data  # Indica que estás usando la variable global
    all_data = []  # Vacía la lista al inicio de cada búsqueda

    if request.method == 'POST':

        #valores recolectados de index.html
        search_kw = request.POST['search_kw']
        buscarPor = request.POST['buscarPor']
        anoIni = request.POST['anoIni']
        anoFin = request.POST['anoFin']
        tipDoc = request.POST['tipDoc']

        
        print("search_kw " +search_kw)
        print("buscarPor " +buscarPor)
        print("anoIni " +anoIni)
        print("anoFin " +anoFin)
        print("tipDoc " +tipDoc)
        
        instancia_clase1 = Clase1()
        instancia_clase4 = Clase4()
        instancia_clase7 = Clase7()
        instancia_clase8 = Clase8()
        instancia_clase10 = Clase10()

        scraped_data = instancia_clase1.funcion_clase1(search_kw)
        all_data.extend(scraped_data)
        
        scraped_data = instancia_clase4.funcion_clase4(search_kw)
        all_data.extend(scraped_data)

        scraped_data = instancia_clase7.funcion_clase7(search_kw)
        all_data.extend(scraped_data)

        scraped_data = instancia_clase8.funcion_clase8(search_kw)
        all_data.extend(scraped_data)

        scraped_data = instancia_clase10.funcion_clase10(search_kw)
        all_data.extend(scraped_data)

        # Crear un DataFrame de pandas desde los datos recolectados
        df = pd.DataFrame(all_data)

        # Define el nombre del archivo Excel
        #excel_filename = 'resultados_busqueda.xlsx'

        # Exporta el DataFrame a un archivo Excel
        #df.to_excel(excel_filename, index=False)

        # Guarda los datos en la base de datos de Django
        for data_item in all_data:
            resultado = Resultado(
                Título_de_la_investigación=data_item['Título de la investigación:'],
                Autor=data_item['Autor:'],
                Descripción=data_item['Descripción:'],
                Fuente=data_item['Fuente:'],
                Fecha_de_publicación=data_item['Fecha de publicación:'],
                Enlace_del_documento=data_item['Enlace del documento:'],
                Número_de_citas=data_item['Número de citas:'],
                Tipo_de_documento_consultado=data_item['Tipo de documento consultado:'],
                Cantidad_de_versiones_del_documento=data_item['Cantidad de versiones del documento:']
            )
            resultado.save()

        # Obtén los resultados desde la base de datos
        ultimos_registros = Resultado.objects.order_by('-id')[:50]

        # Pasa los resultados a la plantilla y renderiza
        context = {'data': ultimos_registros}
        return render(request, 'resultados.html', context)

    return render(request, 'index.html')

def mostrar_resultados(request):
    resultados = Resultado.objects.all()  # Obtén los resultados desde la base de datos
    context = {'data': resultados}  # Pasa los resultados a la plantilla
    return render(request, 'resultados.html', context)
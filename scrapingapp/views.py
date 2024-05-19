import pandas as pd
from django.http import HttpResponse
from openpyxl import load_workbook
from datetime import datetime
from django.template.loader import get_template
from django.shortcuts import render
from .models import Busqueda,Resultado  # Asegúrate de importar tu modelo Resultado
from .scrapingPudMed import Clase1 #+funciona EnlacesFiltros 100% tiene canres revisalo 
from .scrapingRedalyc import Clase2 #+funciona 60% con filtros de pagina falta validar fecha ini y fin por filtro de resultados para el 100% y no tiene canres y esta haciendo las busquedas siempre en el año actual osea todas en 2023
from .scrapingGoogleAcademico import Clase3 #+funciona EnlacesFiltros 100% tiene canres revisalo 
from .scrapingArxiv import Clase4 #+funciona EnlacesFiltros 100% tiene canres revisalo 
from .scrapingIEEE import Clase5 #falta solo cuadrar el pdf
from .scrapingDoaj import Clase6 #+funciona 60% con filtros de pagina falta validar fecha ini y fin por filtro de resultados para el 100% y si tiene canres
from .scrapingEric import Clase7 #+funciona enlacesFiltros 100%, no maneja canres
from .scrapingCora import Clase8 #-funciona enlacesFiltros 100%, tiene canres revisalo
#from .scrapingRecolecta import Clase9 #+funciona al 60% falyan filtros de fecha, aunque la redeterminada que tiene siempre sera el año actual aparte de esto no tiene canres y esta predeterminado a 10 resultados
from .scrapingScielo import Clase10 #+funciona 60% con filtros de pagina falta validar fecha ini y fin por filtro de resultados para el 100% y si tiene canres


all_data = []  # Declara una variable global para almacenar los datos

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_resultados(request):
    return render(request, 'resultados.html', {'data': []})

def scrape_and_export(request):
    global all_data  # Indica que estás usando la variable global
    all_data = []  # Vacía la lista al inicio de cada búsqueda
    display_data = []

    if request.method == 'POST':
        #valores recolectados de index.html
        search_kw = request.POST['search_kw']
        busAut = request.POST['busAut']
        anoIni = request.POST['anoIni']
        anoFin = request.POST['anoFin']
        tipDoc = request.POST['tipDoc']

        # Obtén la fecha actual
        fecha_actual = datetime.now().date()
        # Crea una nueva instancia de Busqueda
        busqueda = Busqueda(
            fec_bus=fecha_actual,
            tem_bus=search_kw,
            aut_bus=busAut,
            year_ini=anoIni,
            year_fin=anoFin,
            tipo_doc=tipDoc
        )

        # Guarda la instancia de Busqueda en la base de datos
        busqueda.save()

        selectRepositorios = request.POST.getlist('selectRepositorios')

        print("search_kw " +search_kw)
        print("busAut " +busAut)
        print("anoIni " +anoIni)
        print("anoFin " +anoFin)
        print("tipDoc " +tipDoc)
        #print("selectRepositorios:", selectRepositorios)
        print(len(selectRepositorios))


        search_kw = search_kw.strip()
        search_kw = search_kw.replace(" ","+")
        busAut = busAut.strip()
        busAut = busAut.replace(" ","+")
        anoIni = anoIni.replace(" ","")
        anoFin = anoFin.replace(" ","")

        if search_kw is None:
            if busAut is not None:
                search_kw = busAut
        
        instancia_clase1 = Clase1()
        instancia_clase2 = Clase2()
        instancia_clase3 = Clase3()
        instancia_clase4 = Clase4()
        instancia_clase5 = Clase5()
        instancia_clase6 = Clase6()
        instancia_clase7 = Clase7()
        instancia_clase8 = Clase8()
        #instancia_clase9 = Clase9()
        instancia_clase10 = Clase10()
      
        for rep in selectRepositorios:
            if rep == "0": 
                scraped_data = instancia_clase1.funcion_clase1(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data)

                scraped_data = instancia_clase2.funcion_clase2(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data) 
                 
                scraped_data = instancia_clase3.funcion_clase3(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data)

                scraped_data = instancia_clase4.funcion_clase4(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data)

                scraped_data = instancia_clase5.funcion_clase5(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data)

                scraped_data = instancia_clase6.funcion_clase6(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data)
                
                scraped_data = instancia_clase7.funcion_clase7(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data)

                scraped_data = instancia_clase8.funcion_clase8(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data)
                
                #scraped_data = instancia_clase9.funcion_clase9(search_kw, busAut, anoIni, anoFin, tipDoc)
                #if scraped_data is not None:
                    #all_data.extend(scraped_data)
 
                scraped_data = instancia_clase10.funcion_clase10(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data)

            elif rep == "1":
                scraped_data = instancia_clase1.funcion_clase1(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data)
            elif rep == "2":
                scraped_data = instancia_clase2.funcion_clase2(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data)
            elif rep == "3":
                scraped_data = instancia_clase3.funcion_clase3(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data)
            elif rep == "4":
                scraped_data = instancia_clase4.funcion_clase4(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data)
            elif rep == "5":
                scraped_data = instancia_clase5.funcion_clase5(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data)
            elif rep == "6":
                scraped_data = instancia_clase6.funcion_clase6(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data)
            elif rep == "7":
                scraped_data = instancia_clase7.funcion_clase7(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data)
            elif rep == "8":
                scraped_data = instancia_clase8.funcion_clase8(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data)
            #elif rep == "9":
               # scraped_data = instancia_clase9.funcion_clase9(search_kw, busAut, anoIni, anoFin, tipDoc)
                #if scraped_data is not None:
                 #   all_data.extend(scraped_data)
            elif rep == "10":
                scraped_data = instancia_clase10.funcion_clase10(search_kw, busAut, anoIni, anoFin, tipDoc)
                if scraped_data is not None:
                    all_data.extend(scraped_data)
            print(rep)

        # Crear un DataFrame de pandas desde los datos recolectados
        df = pd.DataFrame(all_data)

        # Definir el nombre del archivo Excel
        excel_filename = 'resultados_busqueda.xlsx'

        # Escribir el DataFrame en un archivo Excel
        df.to_excel(excel_filename, index=False)

        # Ajustar el ancho de las columnas y configurar el ajuste de texto en el archivo Excel generado
        with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)

            # Obtener el objeto del libro de trabajo y de la hoja de trabajo
            workbook = writer.book
            worksheet = writer.sheets['Sheet1']  # Asegúrate de cambiar 'Sheet1' al nombre correcto de tu hoja si es diferente 

            # Establecer el ancho de todas las columnas en 49.86 unidades de ancho de columna de Excel
            column_width_units = 49.86
            for col_num, value in enumerate(df.columns.values):
                worksheet.set_column(col_num, col_num, column_width_units)

            # Establecer el formato de las celdas de la fila de encabezado y centrar el texto
            header_format = workbook.add_format({
                'bold': True,
                'text_wrap': True,
                'align': 'center',
                'valign': 'vcenter',
                'font_color': '#FFFFFF',
                'bg_color': '#135485',
                'border': 1,  # Agrega bordes alrededor de las celdas del encabezado
            })

            # Escribir la fila de encabezado con el formato especificado y color de fondo
            worksheet.write_row(0, 0, df.columns, header_format)

            # Agregar bordes a todas las celdas del documento
            border_format = workbook.add_format({'border': 1})
            worksheet.conditional_format(1, 0, len(df), len(df.columns) - 1, {'type': 'no_blanks', 'format': border_format})







        # Guarda los datos en la base de datos de Django
               
        for data_item in all_data:
            # Crea una instancia de Resultado
            resultado = Resultado(
                Título_de_la_investigación=data_item['Título de la investigación:'],
                Autor=data_item['Autor:'],
                Descripción=data_item['Descripción:'],
                Fuente=data_item['Fuente:'],
                Fecha_de_publicación=data_item['Fecha de publicación:'],
                Enlace_del_documento=data_item['Enlace del documento:'],
                Número_de_citas=data_item['Número de citas:'],
                Tipo_de_documento_consultado=data_item['Tipo de documento consultado:'],
                Cantidad_de_versiones_del_documento=data_item['Cantidad de versiones del documento:'],
                busqueda=busqueda  # Asocia la instancia de Busqueda al Resultado
            )
            resultado.save()

        # Modifica los nombres de las claves en tus datos
        for item in all_data:
            # Modifica los nombres de las claves en cada elemento de la lista
            item['Titulo_de_la_investigacion'] = item.pop('Título de la investigación:')
            item['Numero_de_citas'] = item.pop('Número de citas:')
            item['Tipo_de_documento_consultado'] = item.pop('Tipo de documento consultado:')
            item['Cantidad_de_versiones_del_documento'] = item.pop('Cantidad de versiones del documento:')
            # Continúa agregando las modificaciones para las demás claves
            item['Autor'] = item.pop('Autor:')
            item['Descripción'] = item.pop('Descripción:')
            item['Fuente'] = item.pop('Fuente:')
            item['Fecha_de_publicación'] = item.pop('Fecha de publicación:')
            item['Enlace_del_documento'] = item.pop('Enlace del documento:')
            item['Repositorio'] = item.pop('Repositorio')

        #print(all_data)
        # Obtén los resultados desde la base de datos
        context = {'data': all_data}

        return render(request, 'resultados.html', context)
    return render(request, 'index.html')
    

def mostrar_resultados(request):
    global all_data
    
    print(resultados)  # Obtén los resultados desde la base de datos
    context = {'data': all_data}  # Pasa los resultados a la plantilla
    return render(request, 'resultados.html', context)

def descargar_resultados(request):
    # Obtener los resultados desde la base de datos
    resultados = Resultado.objects.all()

    # Crear un DataFrame de pandas desde los resultados
    df = pd.DataFrame(all_data)  # Convertir los resultados en un DataFrame

    # Definir el nombre del archivo Excel
    excel_filename = 'resultados_busqueda.xlsx'

    # Escribir el DataFrame en un archivo Excel
    df.to_excel(excel_filename, index=False)

    # Configurar el formato del archivo Excel
    with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)

        # Obtener el objeto del libro de trabajo y de la hoja de trabajo
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']  # Asegúrate de cambiar 'Sheet1' al nombre correcto de tu hoja si es diferente 

        # Establecer el ancho de todas las columnas en 49.86 unidades de ancho de columna de Excel
        column_width_units = 49.86
        for col_num, value in enumerate(df.columns.values):
            worksheet.set_column(col_num, col_num, column_width_units)

        # Establecer el formato de las celdas de la fila de encabezado y centrar el texto
        header_format = workbook.add_format({
            'bold': True,
            'text_wrap': True,
            'align': 'center',
            'valign': 'vcenter',
            'font_color': '#FFFFFF',
            'bg_color': '#135485',
            'border': 1,  # Agregar bordes alrededor de las celdas del encabezado
        })

        # Escribir la fila de encabezado con el formato especificado y color de fondo
        worksheet.write_row(0, 0, df.columns, header_format)

        # Agregar bordes a todas las celdas del documento
        border_format = workbook.add_format({'border': 1})
        worksheet.conditional_format(1, 0, len(df), len(df.columns) - 1, {'type': 'no_blanks', 'format': border_format})

    # Leer el archivo Excel como bytes
    with open(excel_filename, 'rb') as excel_file:
        excel_bytes = excel_file.read()

    # Crear una respuesta HTTP con el archivo Excel adjunto
    response = HttpResponse(excel_bytes, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename={}'.format(excel_filename)  # Nombre del archivo adjunto

    return response

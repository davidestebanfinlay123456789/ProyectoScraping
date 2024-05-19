"""
URL configuration for projectscraping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.shortcuts import redirect
from scrapingapp.views import mostrar_index,mostrar_resultados,scrape_and_export,descargar_resultados # Importa la vista "index" de tu aplicación


urlpatterns = [
     path('index/', mostrar_index, name='mostrar_index'),
    path('scrape/', scrape_and_export, name='scrape_and_export'),
    
    path('mostrar_resultados/', mostrar_resultados, name='mostrar_resultados'),
    # Otras rutas si las tienes
    path('descargar-resultados/', descargar_resultados, name='descargar_resultados'),

]

from django.contrib import admin

from .models import Resultado

class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('Título_de_la_investigación', 'Autor', 'Fecha_de_publicación', 'Número_de_citas')

# Registra el modelo Resultado junto con la clase ResultadoAdmin
admin.site.register(Resultado, ResultadoAdmin)
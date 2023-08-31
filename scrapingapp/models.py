from django.db import models

class Resultado(models.Model):

    Título_de_la_investigación = models.CharField(max_length=255)
    Autor = models.CharField(max_length=255)
    Descripción = models.TextField()
    Fuente = models.CharField(max_length=255)
    Fecha_de_publicación = models.CharField(max_length=255)
    Enlace_del_documento = models.URLField()
    Número_de_citas = models.CharField(max_length=3)
    Tipo_de_documento_consultado = models.CharField(max_length=50)
    Cantidad_de_versiones_del_documento = models.CharField(max_length=20)
    class Meta:
        app_label = 'scrapingapp'


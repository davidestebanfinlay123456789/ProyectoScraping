from django.db import models

class Busqueda(models.Model):
    idBusqueda = models.AutoField(primary_key=True)
    fec_bus = models.DateField()
    tem_bus = models.CharField(max_length=100)
    aut_bus = models.CharField(max_length=100, blank=True)
    year_ini = models.CharField(max_length=10, blank=True, default="No establecido")
    year_fin = models.CharField(max_length=100, blank=True, default="No establecido")
    tipo_doc = models.CharField(max_length=100, blank=True, null=True, default="No establecido")

    def __str__(self):
        return f"{self.idBusqueda} - {self.tem_bus}"


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
    busqueda = models.ForeignKey(Busqueda, on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'scrapingapp'


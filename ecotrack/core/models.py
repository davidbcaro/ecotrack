from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    poblacion = models.PositiveIntegerField()
    pib = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
        db_table = "pais"
        ordering = ['id']

    def __str__(self):
        return self.nombre


class PoliticaClimatica(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion_politica = models.TextField()
    fecha_publicacion = models.DateField()

    class Meta:
        verbose_name = "Política Climática"
        verbose_name_plural = "Políticas Climáticas"
        db_table = "politica_climatica"
        ordering = ['id']

    def __str__(self):
        return self.titulo


class AcuerdoInternacional(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_firma = models.DateField()
    descripcion = models.TextField()

    class Meta:
        verbose_name = "Acuerdo Internacional"
        verbose_name_plural = "Acuerdos Internacionales"
        db_table = "acuerdo_internacional"
        ordering = ['id']

    def __str__(self):
        return self.nombre


class PaisAcuerdo(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    acuerdo = models.ForeignKey(AcuerdoInternacional, on_delete=models.CASCADE)
    fecha_adhesion = models.DateField()

    class Meta:
        verbose_name = "Adhesión de País a Acuerdo"
        verbose_name_plural = "Adhesiones de Países a Acuerdos"
        db_table = "pais_acuerdo"
        ordering = ['id']
        unique_together = ('pais', 'acuerdo')


class SectorEconomico(models.Model):
    nombre_sector = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        verbose_name = "Sector Económico"
        verbose_name_plural = "Sectores Económicos"
        db_table = "sector_economico"
        ordering = ['id']

    def __str__(self):
        return self.nombre_sector


class Emision(models.Model):
    sector = models.ForeignKey(SectorEconomico, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    fecha = models.DateField()
    cantidad_co2e = models.DecimalField(max_digits=12, decimal_places=3)

    class Meta:
        verbose_name = "Emisión"
        verbose_name_plural = "Emisiones"
        db_table = "emision"
        ordering = ['id']

    def __str__(self):
        return f"{self.pais} - {self.fecha}"


class AlertaEmision(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    umbral = models.DecimalField(max_digits=12, decimal_places=3)
    valor_emision = models.DecimalField(max_digits=12, decimal_places=3)
    fecha_alerta = models.DateField()
    estado = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Alerta de Emisión"
        verbose_name_plural = "Alertas de Emisión"
        db_table = "alerta_emision"
        ordering = ['id']

    def __str__(self):
        return f"Alerta en {self.pais} - {self.fecha_alerta}"

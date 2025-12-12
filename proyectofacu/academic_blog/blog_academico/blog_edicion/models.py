from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# 1. TABLAS NUEVAS (Para organizar Apuntes)
class Carrera(models.Model):
    nombre = models.CharField(
        max_length=200, help_text="Ej: Tecnicatura en Programación"
    )

    def __str__(self):
        return self.nombre


class Materia(models.Model):
    nombre = models.CharField(max_length=200, help_text="Ej: Programación I")
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    año = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.nombre} ({self.carrera.nombre})"


# 2. APUNTES
class Apunte(models.Model):
    TIPO_CHOICES = [
        ("resumen", "Resumen"),
        ("parcial", "Parcial"),
        ("final", "Final"),
        ("tp", "TP"),
        ("otro", "Otro"),
    ]

    titulo = models.CharField(max_length=100)
    # Vinculamos con Materia (esto crea el desplegable)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to="apuntes/%Y/%m/")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default="resumen")
    fecha_subida = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Apunte"
        verbose_name_plural = "Apuntes"
        ordering = ["-fecha_subida"]

    def __str__(self):
        return f"{self.titulo} - {self.materia.nombre}"


# 3. ARTICULOS (BLOG)
class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    bajada = models.CharField(max_length=200)
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to="noticias/%Y/%m/", blank=True, null=True)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ["-fecha_publicacion"]

    def __str__(self):
        return self.titulo


# 4. CALENDARIO (Aquí estaba el faltante)
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateTimeField()

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Calendario Académico"
        ordering = ["fecha"]

    def __str__(self):
        return f"{self.fecha.strftime('%d/%m')}: {self.titulo}"

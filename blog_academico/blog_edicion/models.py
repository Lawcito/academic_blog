from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)

    imagen_static = models.CharField(
        max_length=100,
        blank=True,
        help_text="Nombre del archivo en static/img/articulos/"
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        related_name='articulos'
    )

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha_publicacion']

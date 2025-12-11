from django.db import models
from django.contrib.auth.models import User


class Apunte(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class MaterialEstudio(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    archivo = models.FileField(upload_to='material/', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Debate(models.Model):
    titulo = models.CharField(max_length=150)
    fecha = models.DateTimeField(auto_now_add=True)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class MensajeDebate(models.Model):
    debate = models.ForeignKey(Debate, on_delete=models.CASCADE, related_name='mensajes')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['fecha']

    def __str__(self):
        return f"{self.autor.username}: {self.texto[:30]}..."

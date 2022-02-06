from django.db import models

# Create your models here.

class Avaliacao(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comentario = models.TextField()
    nota = models.DecimalField(max_digits=3, decimal_places=2)
    data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usuario.username
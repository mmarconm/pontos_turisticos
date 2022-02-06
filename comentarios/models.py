from django.db import models

# Create your models here.
class Comentario(models.Model):

    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.usuario.username
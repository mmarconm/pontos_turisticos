from django.contrib import admin

# Register your models here.
from .models import Comentario

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    ...
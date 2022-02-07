from django.contrib import admin

# Register your models here.
from .models import Endereco

@admin.register(Endereco)
class EnderecosAdmin(admin.ModelAdmin):
    ...
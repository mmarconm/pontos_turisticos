from django.contrib import admin

# Register your models here.
from .models import Atracao

@admin.register(Atracao)
class AtracaoAdmin(admin.ModelAdmin):
    ...
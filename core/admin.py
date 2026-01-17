from django.contrib import admin

from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preço')
    list_filter = ('nome', 'preço')
    search_fields = ('nome', 'preço')

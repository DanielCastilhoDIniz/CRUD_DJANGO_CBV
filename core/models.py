from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100, name='nome')
    preco = models.DecimalField(max_digits=10, decimal_places=2, name='preço')

    def __str__(self):
        return self.nome

from django.db import models



# tipo string -> CharField(precisa do tamanho máximo)
# tipo inteiro -> IntegerField()
# tipo decimal -> FloatField()
# tipo booleano -> BooleanField()

class Produto(models.Model): #O CERTO É PRODUTO NO SINGULAR
    nome = models.CharField(max_length=200)
    preco = models.FloatField()
    estoque = models.IntegerField()
    imagem = models.CharField(max_length=500, default='')   

    def __str__(self):
        return self.nome
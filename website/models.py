from django.db import models

class Registro(models.Model):
    primeiro_nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    estagio = models.TextField(max_length=120)


    def __str__(self):
        return f"{self.primeiro_nome} {self.sobrenome} - {self.cidade}"
    
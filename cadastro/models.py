from django.db import models

class CadastrarUsuario(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=50)
    sobrenome = models.CharField(verbose_name='Sobrenome',max_length=128, blank=False , null=False)
    data_nascimento = models.DateField(verbose_name='Data_Nascimento')
    email = models.EmailField(verbose_name= 'Email', unique=True)
    senha = models.CharField('<PASSWORD>ha', max_length=36)

    def __str__(self) -> str:
        return self.nome
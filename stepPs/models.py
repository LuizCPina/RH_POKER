from django.db import models

class Inscricao(models.Model):

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    pergunta1 = models.TextField(blank=True, null=True)
    pergunta2 = models.TextField(blank=True, null=True)
    pergunta3 = models.TextField(blank=True, null=True)
    nicknames = models.CharField(max_length=100, blank=True, null=True) 
    plataformas = models.CharField(max_length=100)

    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['email'], name='unique_email')
        ]

    def __str__(self):
        return self.nome
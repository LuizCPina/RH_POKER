from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20)
    nickname = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Vaga(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):

        return self.titulo
    

class Candidatura(models.Model):

    STATUS_CHOICHES = [
        ("enviada", "Enviada"),
        ("analise", "Em Análise"),
        ("aprovado", "Aprovado"),
        ("rejeitado", "Rejeitado"),
    ]

    usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICHES, default = "enviada")

    def __str__(self):
        return f"{self.usuario.user} - {self.vaga} - {self.status}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['usuario', 'vaga'],
                name='unique_candidatura'
            )
        ]
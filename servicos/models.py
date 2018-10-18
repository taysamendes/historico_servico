from django.db import models
from django.utils import timezone

class Servico(models.Model):
    estagiario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=300)
    local = models.TextField()
    responsavel = models.TextField()
    data = models.DateTimeField(default=timezone.now)
    dataServico = models.DateTimeField(blank=True, null=True)

    def procedimento(self):
        self.dataServico = timezone.now()
        self.save()

    def __str__(self):
        return self.tipo

#8187637621d4ed9228e0ca8ea2609b1f7637886c
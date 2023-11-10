from django.db import models

class Operacao(models.Model):
    num1 = models.CharField(u'Número 1', max_length=200)
    num2 = models.CharField(u'Número 2', max_length=200)
    op = models.CharField(u'Operação', max_length=2)

    result = models.CharField(u'Resultado', max_length=200)

    data = models.DateTimeField('Data de Submissão', auto_now_add=True, null=True)

    class Meta:
        ordering = ['data',]

    def __str__(self):
        return f'{self.id} em {self.data} - {self.num1} {self.op} {self.num2} = {self.result}'
    
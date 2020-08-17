from django.db import models

class Aluno(models.Model):
    nome = models.TextField(max_length=100, null=False, blank=False)

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        db_table = 'aluno'
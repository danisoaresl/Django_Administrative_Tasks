from django.db import models

# Create your mopdels here.
Class Curso(models.Model):
    niveis_de_curso = (
        (0, 'Iniciante'),
        (1, 'Intermediário'),
        (2, 'Avançado')
    )
    titulo = models.CharField(max_lengh=50)
    nivel = models.CharField(max_length=50, choices=niveis_de_curso)
    carga_horaria = models.IntegerField()
    data_do_curso = models.DateField(help_text='aaaa/mm/dd')
    descricao = models.TextField()
    
    def _str_(self):
        return f'{self.titulo}: {self.data_do_curso} - {self.carga_horaria}'
    
    class Meta:
        verbose_name = 'Cadastro de cursos'
        verbose_name_plural = 'Cadastro de cursos'
        ordering = [' -data_do_curso']
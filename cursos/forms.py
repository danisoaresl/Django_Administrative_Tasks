from django import forms
from cursos.models import Curso
from datetime import date

class CursoForm(forms.ModelForm):
    def clean data_do_curso(self):
        data_do_curso = self.cleaned_data['data_do_curso']
        hoje = date.today()
        if data_do_curso < hoje:
            raise ValidationError('Não é possível cadastrar um curso no PASSADO!')
        return data_do_curso
    

    class Meta:
        model = Curso
        fields = ['titulo', 'nivel', 'carga_horaria', 'data_do_curso', 'descricao']
        
        
    titulo = models.CharField(max_lengh=50)
    nivel = models.CharField(max_length=50, choices=niveis_de_curso)
    carga_horaria = models.IntegerField()
    data_do_curso = models.DateField(help_text='aaaa/mm/dd')
    descricao = models.TextField()
    
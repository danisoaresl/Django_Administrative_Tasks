data = models.DateTimeField(auto_now_add=True)
def _str_(self):
    return f'{self.nome} [{self.email}]'

Class Meta:
    verbose_name = 'Formulário de contato'
    verbose_name_plural = 'Formulário de contatos'
    ordering = ['data']
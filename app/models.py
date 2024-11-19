from django.db import models

class UF(models.Model):
    sigla = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural='Unidades federais'

    def __str__(self):
        return self.sigla
    

class Cidade(models.Model):
    nome = models.CharField(max_length=30)
    UF = models.ForeignKey(UF, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Cidades'

    def __str__(self):
        return f'{self.nome}/{self.UF} '


class Genero(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Gênero")
                            
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"


#Superclasse
class Pessoa(models.Model):
    nome = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, default='')
    telefone = models.CharField(default='')
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

#Superclasse e subclasse  
class PessoaFisica(Pessoa):
    cpf = models.CharField(default='')
    data_nasc = models.DateField(default='2000-01-01')

    class Meta:
        verbose_name = "Pessoa Física"
        verbose_name_plural = "Pessoas Físicas"

    def __str__(self):
        return self.nome

#Superclasse e subclasse    
class PessoaJuridica(Pessoa):
    cnpj = models.CharField(default='')
    razao_social = models.CharField(max_length=255, default='')
    data_fundacao = models.DateField(default='2000-01-01')

    class Meta:
        abstract = True
    
#Subclasse  
class Autor(PessoaFisica):
    pass

    class Meta:
        verbose_name='Autor'
        verbose_name_plural='Autores'

#Subclasse
class Editora(PessoaJuridica):
    site = models.URLField(max_length=50)

    class Meta:
        verbose_name='Editora'
        verbose_name_plural='Editoras'

    def __str__(self):
        return f'{self.nome} {self.cidade}'  

#Subclasse
class Usuario(PessoaFisica):
    pass

    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
    

class Emprestimo(models.Model):
    dataemprestimo = models.DateField(verbose_name='Data de Empréstimo')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    datadevolucao = models.DateField(verbose_name='Data de Devolução')

    class Meta:
        verbose_name = "Emprestimo"
        verbose_name_plural='Empréstimos'

    def __str__(self):
        return f'{self.dataemprestimo} {self.usuario} {self.datadevolucao}'
    
class Livro(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do livro")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor do livro")
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, verbose_name="Editora do livro")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name="Gênero do livro")
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    preco = models.IntegerField(verbose_name="Preço do livro")
    data_plub = models.DateField(verbose_name="Data de publicação do livro")
    status = models.BooleanField(verbose_name="Status do livro")

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    def __str__(self):
        return f'{self.nome} {self.autor}'

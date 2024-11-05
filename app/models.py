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
    

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    data_nasc = models.DateField(verbose_name='Data de Nascimento')
    email = models.EmailField(max_length=20)
    telefone = models.CharField(max_length=13)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Usuários'

    def __str__(self):
        return f'{self.nome} {self.cidade}'


class Genero(models.Model):
    nome = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural='Gêneros'

    def __str__(self):
        return self.nome


class Editora(models.Model):
    nome = models.CharField(max_length=50)
    site = models.URLField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Editoras'

    def __str__(self):
        return f'{self.nome} {self.cidade}'


class Autor(models.Model):
    nome = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Autores'

    def __str__(self):
        return f'{self.nome} {self.cidade}'
    

class Livro(models.Model):
    nome = models.CharField(max_length=50)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    datapublicacao = models.DateField(verbose_name='Data de Publicação')

    class Meta:
        verbose_name_plural='Livros'

    def __str__(self):
        return f'{self.nome} {self.genero} {self.autor} {self.editora} {self.preco} {self.datapublicacao}'


class Emprestimo(models.Model):
    dataemprestimo = models.DateField(verbose_name='Data de Empréstimo')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    datadevolucao = models.DateField(verbose_name='Data de Devolução')

    class Meta:
        verbose_name_plural='Empréstimos'

    def __str__(self):
        return f'{self.dataemprestimo} {self.usuario} {self.livro} {self.datadevolucao}'
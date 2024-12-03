from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
      page = "index.html"
      return render(request, page)
    def post(self, request):
       pass

class AutorView(View):
    def get(self, request):
      page = "autor.html"
      context = {
        "autores": Autor.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
    
class UfView(View):
    def get(self, request):
      page = "uf.html"
      context = {
        "ufs": UF.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class CidadeView(View):
    def get(self, request):
      page = "cidade.html"
      context = {
        "cidades": Cidade.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class EditoraView(View):
    def get(self, request):
      page = "editora.html"
      context = {
        "editoras": Editora.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
      
class GeneroView(View):
    def get(self, request):
      page = "genero.html"
      context = {
        "generos": Genero.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class LivroView(View):
    def get(self, request):
      page = "livro.html"
      context = {
        "livros": Livro.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
    
class UsuarioView(View):
    def get(self, request):
      page = "usuario.html"
      context = {
        "usuarios": Usuario.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class EmprestimoView(View):
    def get(self, request):
      page = "emprestimo.html"
      context = {
        "emprestimos": Emprestimo.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
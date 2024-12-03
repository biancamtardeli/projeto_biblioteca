from django.urls import include, path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('autor/', AutorView.as_view(), name='autor'),
    path('cidade/', CidadeView.as_view(), name='cidade'),
    path('editora/', EditoraView.as_view(), name='editora'),
    path('emprestimo/', EmprestimoView.as_view(), name='emprestimo'),
    path('genero/', GeneroView.as_view(), name='genero'),
    path('livro/', LivroView.as_view(), name='livro'),
    path('uf/', UfView.as_view(), name='uf'),
    path('usuario/', UsuarioView.as_view(), name='usuario'),
]

from django.contrib import admin
from .models import *

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class UFAdmin(admin.ModelAdmin):
    inlines = [CidadeInline]

class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1 

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',) 
    search_fields = ('nome',) 
    inlines = [LivroInline] 

class EditoraAdmin(admin.ModelAdmin):
    model = Editora
    inlines = [LivroInline] 

class GeneroAdmin(admin.ModelAdmin):
    model = Genero
    inlines = [LivroInline]

class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1 

class EmprestimoAdmin(admin.ModelAdmin):
    model = Emprestimo
    inlines = [LivroInline] 

admin.site.register(UF, UFAdmin)
admin.site.register(Cidade)
admin.site.register(Usuario)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Livro)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)


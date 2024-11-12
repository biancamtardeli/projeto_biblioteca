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
    inlines = [LivroInline] 

class GeneroAdmin(admin.ModelAdmin):
    inlines = [LivroInline]

class EmprestimoInline(admin.TabularInline):
    model = Emprestimo
    extra = 1 

class LivroAdmin(admin.ModelAdmin): 
    inlines = [EmprestimoInline] 

admin.site.register(UF, UFAdmin)
admin.site.register(Cidade)
admin.site.register(Usuario)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Emprestimo)


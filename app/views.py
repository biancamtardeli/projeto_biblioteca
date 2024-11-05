from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
        produtos = UF.objects.all()
        return render(request, 'index.html', {'produtos': produtos})
    def post(self, request):
        pass
# Create your views here.F

from django.shortcuts import render

#Devuelve la pag principal del sitio

def home(request):
    return render(request, 'index.html')
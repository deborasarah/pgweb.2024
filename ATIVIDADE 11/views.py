from django.http import HttpResponse 


def index(request):
    return HttpResponse("A view index funcionou , Wow!")

def sobre (request):
    return HttpResponse("<h1>Sistema 1.0 desenvolvido por mim<h1>")

from django.http import HttpResponse 

def contato(request):
    return  HttpResponse("<h1>Contato</h1><p>ESta é a página de contato.</p>")

from django.http import HttpResponse 

def ajuda(resquest):
    return HttpResponse("<h1>Ajuda</h1><p>Esta é a página de ajuda.<p/>")
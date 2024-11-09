from django.shortcuts import render

# Create your views here.

from siteweb.models import Posts

# Create your views here.

def home(request):
    #return render(request, 'contato.html') #mudar dps
    return render(request, 'lar.html')
def base(request):
    return render(request, 'base.html')
#def servicos(request):
 #   return render(request, 'servicos.html')
def sobre(request):
    return render(request, 'about.html')
def contato(request):
    return render(request, 'contato.html')

def servicos(request):
    template_name = 'servicos.html' # template
    posts = Posts.objects.all() # query com todas as postagens
    context = { # cria context para chamar no template
        'posts': posts
        }
    return render(request, template_name, context)

def service_detail(request, id):
    template_name = 'service-detail.html' # template
    post = Posts.objects.get(id=id) # Metodo Get
    context = { # cria context para chamar no template
        'post': post
        }
    return render(request, template_name, context) # render

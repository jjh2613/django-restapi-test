from django.shortcuts import render
from api.forms import Form
from api.models import Article

# Create your views here.
def write(request):
  if request.method == 'POST':
    form = Form(request.POST)
    if(form.is_valid()):
      form.save()
  else:
    form = Form()

  return render(request, 'write.html', {'form': form})

def list(request):
  articleList = Article.objects.all()
  return render(request, "list.html", {'articleList': articleList})

def one(request, num):
  article = Article.objects.get(id=num)
  return render(request, "getone.html", {'article': article})
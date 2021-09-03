from api.models import Article
from django.forms import ModelForm

class Form(ModelForm):
  class Meta:
    model = Article
    fields=["name", "title","contents", "url", "email"]
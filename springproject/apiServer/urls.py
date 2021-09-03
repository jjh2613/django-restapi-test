from django.urls import path
from . import views
 
app_name = 'apiServer'
urlpatterns = [
    path('', views.SampleDataView.as_view()),
    path('/<int:datum_id>', views.SampleDataView.as_view()), 
]

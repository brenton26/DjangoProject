from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='adopt_index'),
    path('<int:id>', views.adopt, name='adopt_form'),
    path('pups', views.pups, name='pups'),
    path('pups/<int:id>', views.pup_trash, name='pup_trash')
    ]

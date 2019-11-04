from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_question', views.new_question, name='new_question'),
    path('ask', views.ask, name='ask')
]
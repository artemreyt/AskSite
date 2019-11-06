from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_question', views.new_question, name='new_question'),
    path('ask', views.ask, name='ask'),
    path('question/<int:id>', views.question, name='question'),
    url(r'login/', views.login, name='login')
]

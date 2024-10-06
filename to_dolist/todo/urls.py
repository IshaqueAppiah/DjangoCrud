from django.urls import path
from . import views

urlspatterns=[
    path('list/',views.list_todo_items) 

]
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home),
    path('addClass/', views.addClass),
    path('deleteClass/<code>', views.deleteClass),
    path('editionClass/<code>', views.editionClass),
    path('editClass/', views.editClass),
]
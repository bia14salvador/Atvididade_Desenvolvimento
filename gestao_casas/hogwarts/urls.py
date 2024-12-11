from django.urls import path
from . import views

urlpatterns = [
    path('casa/', views.casa_list, name='casa_list'),
    path('casa/create/', views.casa_create, name='casa_create'),
    path('casa/update/<int:id>/', views.casa_update, name='casa_update'),
    path('casa/delete/<int:id>/', views.casa_delete, name='casa_delete'),

    path('aluno/', views.aluno_list, name='aluno_list'),
    path('aluno/create/', views.aluno_create, name='aluno_create'),
    path('aluno/update/<int:id>/', views.aluno_update, name='aluno_update'),
    path('aluno/delete/<int:id>/', views.aluno_delete, name='aluno_delete'),
]

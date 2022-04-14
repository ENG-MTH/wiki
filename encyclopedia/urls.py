from django.urls import path

from . import views

app_name = 'wiki'

urlpatterns = [
    path('wiki/create/', views.create_entry, name='create_entry'),
    path('wiki/edit/<str:title>/', views.edit_entry, name='edit_entry'),
    path('wiki/<str:title>', views.single_entery, name='single-entry'),
    path('wiki/random', views.random_entry, name='random'),

    path("", views.index, name="index"),
]

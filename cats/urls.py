from django.urls import path
from . import views

app_name = 'cats'
urlpatterns = [

    path('', views.CatListView.as_view(), name='cats'),
    path('cat/<int:pk_from_url>', views.CatDetailView.as_view(), name='cat'),

    ]
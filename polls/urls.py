from django.urls import path

from . import views

app_name = 'polls'




urlpatterns = [
    path('', views.AnkietyBukiety.as_view(), name = 'index'),
    path('funky', views.funky),
    path('danger/<str:guess>', views.danger),
    path('bounce', views.bounce),
    path('guess', views.guess),
    path('game/<slug:guess>', views.GameView.as_view()),

    # path('cats', views.CatListView(), name='cats'),
    # path('cat/<int:pk_from_url>', views.CatDetailView.as_view(), name='cat'),




    ]
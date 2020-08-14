from . import views
from django.urls import path
#class based views
urlpatterns = [
    path('', views.WikisList.as_view(), name='home'),
    path('<slug:slug>/', views.WikisDetail.as_view(), name='wiki_detail'),
]

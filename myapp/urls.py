from django.urls import path, include
from myapp import views





urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
]

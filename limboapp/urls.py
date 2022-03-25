from django.urls import path

from . import views
from django.conf import settings
# from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('upload',views.upload,name='upload'),
]
from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url('create/', views.create, name='create'),
   url('clear/', views.test, name= 'clear'),
   url('getallrooms/', views.getAllRoomPins, name = 'number of pins ')
]   
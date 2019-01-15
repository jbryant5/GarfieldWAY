from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url('create/', views.create, name='create'),
   url('clear/', views.clear, name= 'clear'),
   url('test/', views.test, name= 'test'),
   url('edit/', views.edit, name= 'edit'),
   url('getallrooms/', views.getAllRoomPins, name = 'number of pins ')
]   
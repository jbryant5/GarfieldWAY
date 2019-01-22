from django.conf.urls import url
from django.urls import path

from . import views

app_name='pins'

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url('create/', views.create, name='create'),
   url('clear/', views.clear, name= 'clear'),
   url('test/', views.test, name= 'test'),
   path('edit/<int:pin_id>', views.edit, name= 'edit'),
   url('getallrooms/', views.getAllRoomPins, name = 'number of pins ')
]   

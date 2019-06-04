from django.conf.urls import url
from . import views

app_name='pins'

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url('create/', views.create, name='create'),
   url('test/', views.test, name= 'test'),
   url(r'^edit/(?P<pin_id>[0-9]+)/$', views.edit, name= 'edit'),
   url(r'^delete/(?P<pin_id>[0-9]+)/$', views.delete, name='delete'),
   url('getallrooms/', views.getAllRoomPins, name = 'number of pins '),
   url('vote/', views.vote, name='vote'),
   url('mypinsfilter/', views.mypinsfilter, name='mypinsfilter'),
   url('typefilter/', views.typefilter, name='typefilter'),
   url('lowestroomfilter/', views.lowestroomfilter, name='lowestroomfilter'),
   url('highestroomfilter/', views.highestroomfilter, name='highestroomfilter'),
   url('recentlypublishedfilter/', views.recentlypublishedfilter, name='recentlypublishedfilter'),
   url('oldestpublishedfilter/', views.oldestpublishedfilter, name='oldestpublishedfilter'),
]   
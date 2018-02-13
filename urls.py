from django.conf.urls import url
from . import views

urlpatterns = [
 	url(r'^$', views.index, name = 'index'),
 	url(r'^contact/$', views.contact, name = 'contact'),
 	url(r'^projects/(?P<proj>\w+)$', views.projects, name = 'projects'),
]

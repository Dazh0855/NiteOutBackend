from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^getEvent$', views.getEvent, name="getEvent"),
	url(r'^getUser$', views.getUser, name="getUser"),
]

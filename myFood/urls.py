from django.conf.urls import url

from . import views

app_name = 'myFood'
urlpatterns = [
  url(r'^$', views.Index, name='index'),
]


from django.conf.urls import url

from . import views

app_name = 'myFood'
urlpatterns = [
  url(r'^$', views.IndexView.as_view(), name='index'),
]


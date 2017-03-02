from django.conf.urls import url

from . import views

app_name = 'smart_mirror'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]

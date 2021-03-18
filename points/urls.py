from django.conf.urls import url
from . import views

app_name = 'points'
urlpatterns = [
    url('', views.get_points),
]

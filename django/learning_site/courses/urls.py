from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.course_index),
    url(r'(?P<pk>\d+)/$', views.course_show),
]

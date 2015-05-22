from django.conf.urls import url
from quickstart import views

urlpatterns= [
    url(r'^quickstart/$', views.quickstart_list),
    url(r'^quickstart/(?P<pk>[0-9]+)/$', views.quickstart_detail),
]
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from quickstart import views

urlpatterns= [
    url(r'^quickstart/$', views.quickstart_list),
    url(r'^quickstart/(?P<pk>[0-9]+)/$', views.quickstart_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
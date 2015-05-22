from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from quickstart import views
from django.conf.urls import include

urlpatterns= [
    url(r'^quickstart/$', views.QuickstartList.as_view()),
    url(r'^quickstart/(?P<pk>[0-9]+)/$', views.QuickstartDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
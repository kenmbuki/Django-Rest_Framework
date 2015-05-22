#from quickstart.views import QuickstartViewSet, UserViewSet, api_root
#from rest_framework import render
from django.conf.urls import url, include
from quickstart import views
from rest_framework.routers import DefaultRouter

#from django.conf.urls import patterns, url
#from rest_framework.urlpatterns import format_suffix_patterns
#from quickstart import views
#from django.conf.urls import include



router = DefaultRouter()
router.register(r'quickstart', views.QuickstartViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]



"""
quickstart_list = QuickstartViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
quickstart_detail = QuickstartViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
quickstart_highlight = QuickstartViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^quickstart/$', quickstart-list, name='quickstart-list'),
    url(r'^quickstart/(?P<pk>[0-9]+)/$', quickstart-detail, name='quickstart-detail'),
    url(r'^quickstart/(?P<pk>[0-9]+)/highlight/$', quickstart_highlight, name='quickstart-highlight'),
    url(r'^users/$',user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^quickstart/$', views.QuickstartList.as_view(), name='quickstart-list'),
    url(r'^quickstart/(?P<pk>[0-9]+)/$', views.QuickstartDetail.as_view(), name='quickstart-detail'),
    url(r'^quickstart/(?P<pk>[0-9]+)/highlight/$', views.QuickstartHighlight.as_view(), name='quickstart-highlight'),
    url(r'^users/$',views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view(),name='user-detail'),
])

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns= [
    url(r'^quickstart/$', views.QuickstartList.as_view()),
    url(r'^quickstart/(?P<pk>[0-9]+)/$', views.QuickstartDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.api_root),
    url(r'^quickstart/(?P<pk>[0-9]+)/highlight/$', views.QuickstartHighlight.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

"""
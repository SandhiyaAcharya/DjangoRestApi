from django.conf.urls import url 
from myapi import views 
 
urlpatterns = [ 
    url(r'^api/posts$', views.list),
    url(r'^api/posts/(?P<pk>[0-9]+)$', views.detail),
    
]
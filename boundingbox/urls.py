from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from bbox import views

urlpatterns = patterns('',
                       url( r'^$', direct_to_template, {'template':'points.html'} ),
                       url( r'^point/add/$', views.addPoint, name="point_add" ),
                       url( r'^point/search/$', views.searchPoints, name="point_search" ),
)

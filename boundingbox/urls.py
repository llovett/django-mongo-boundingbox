from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from bbox import views

urlpatterns = patterns('',
#                       url( r'^$', views.addPoints, name="add_points" ),
                       url( r'^$', direct_to_template, {'template':'points.html'} ),
                       url( r'^search/%', views.searchPoints, name="search_points" ),
)

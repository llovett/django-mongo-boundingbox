from django.http import HttpResponse
from django.shortcuts import render_to_response
from bbox.models import Point

def addPoint( request ):
    lat, lng = float(request.POST['lat']), float(request.POST['lng'])
    Point.objects.create( title="test point", position=[lat,lng] )
    return HttpResponse()

def searchPoints( request ):
    lat, lng = request.GET['lat'], request.GET['lng']
    # TODO: find points in database
    return HttpResponse()

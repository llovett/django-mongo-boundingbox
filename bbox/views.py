from django.http import HttpResponse
from django.shortcuts import render_to_response
from bbox.models import Point
import json

def addPoint( request ):
    lat, lng = float(request.POST['lat']), float(request.POST['lng'])
    Point.objects.create( title="test point", position=[lat,lng] )
    return HttpResponse()

def searchPoints( request ):
    lat1, lng1 = float(request.GET['lat1']), float(request.GET['lng1'])
    lat2, lng2 = float(request.GET['lat2']), float(request.GET['lng2'])
    points = [p.position for p in Point.objects( position__within_box=[(lat1,lng1),(lat2,lng2)] )]
    
    return HttpResponse( json.dumps( points ),
                         mimetype="application/json" )

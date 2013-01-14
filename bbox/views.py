from django.http import HttpResponse
from django.shortcuts import render_to_response
from bbox.models import Point
import json
from sys import stderr
from Polygon.Shapes import Rectangle

def addPoint( request ):
    lat, lng = float(request.POST['lat']), float(request.POST['lng'])
    Point.objects.create( title="route point", position=[lat,lng] )
    return HttpResponse()

def searchPoints( request ):
    postData = json.loads(request.raw_post_data)
    rectangles = postData['rectangles']

    # bboxArea = the union of all the bounding boxes on the route
    bboxArea = None
    for i in xrange(0,len(rectangles),4):
        # Make a Rectangle out of the width/height of a bounding box
        # longitude = x, latitude = y
        theRect = Rectangle( abs(rectangles[i] - rectangles[i+2]),
                             abs(rectangles[i+1] - rectangles[i+3]) )
        theRect.shift( rectangles[i+2], rectangles[i+3] )
        bboxArea = bboxArea + theRect if bboxArea else theRect

    bboxArea = [list(t) for t in bboxArea.contour( 0 )]

    # TODO: pull objects out of database using bboxArea
    points = { "points" : [p.position for p in Point.objects( position__within_polygon=bboxArea )] }

    return HttpResponse( json.dumps(points), mimetype="application/json" )

from django.http import HttpResponse
from django.shortcuts import render_to_response
from bbox.models import Point
import json
from sys import stderr
from Polygon.Shapes import Rectangle

def addPoint( request ):
    lat, lng = float(request.POST['lat']), float(request.POST['lng'])
    Point.objects.create( title="test point", position=[lat,lng] )
    return HttpResponse()

def searchPoints( request ):
    postData = json.loads(request.raw_post_data)
    rectangles = postData['rectangles']

    # For debugging only
    stderr.write( "received %d rectangles"%(len(rectangles)/4) )

    # bboxArea = the union of all the bounding boxes on the route
    bboxArea = None
    for i in xrange(0,len(rectangles),4):
        # Make a Rectangle out of the width/height of a bounding box
        theRect = Rectangle( abs(rectangles[i+1] - rectangles[i+3]),
                             abs(rectangles[i] - rectangles[i+2]) )

        # Translate the rectangle by the SW corner of the box
        theRect.shift( rectangles[i+2], rectangles[i+3] )

        # DOUBLE the size of the rect!???? This really shouldn't be necessary
        # theRect.scale(2,2)

        # Union the bounding box
        bboxArea = bboxArea + theRect if bboxArea else theRect

    # For debugging only --- did it really work??
    stderr.write( str(bboxArea) )

    return HttpResponse()

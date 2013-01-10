from django.http import HttpResponse
from django.shortcuts import render_to_response

def addPoints( request ):
    return HttpResponse("Add-points page")

def searchPoints( request ):
    return HttpResponse("Search-points page")

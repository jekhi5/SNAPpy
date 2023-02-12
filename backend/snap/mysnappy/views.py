from django.shortcuts import render
from django.http import HttpResponse
from google.maps import Geocoder
from google.maps import GeocoderRequest

# TODO: implement spell-checking!


def landing(request):
    return render(request, "landing.html")


def map(request):
    if request.method == "GET":
        return render(request, "map.html")
    elif request.method == "POST":
        result = location_pipeline(
            request.POST["zipcode"], request.POST["radius"])
        return HttpResponse(result)


def shoppinglist(request):
    if request.method == "GET":
        # print("GET")
        return render(request, "shoppinglist.html")
    elif request.method == "POST":
        print("POST")
        return HttpResponse(request.POST['shoppingList'])


# Process the user given zipcode and radius through the following pipeline:
# 1. Request Google Maps to give us all grocery stores in the given radius
# 2. Filter those results to only include supermarkets that are known to accept SNAP
# 3. Request Google Maps to give us accessibility and pricing information for the remaining grocery stores

def location_pipeline(address, radius_string):
    coords = Geocoder().geocode(address)

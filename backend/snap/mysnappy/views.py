from decouple import config
import geocoder
from django.http import HttpResponse
from django.shortcuts import render
import store_locating_pipeline
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# TODO: implement spell-checking!

# GET endpoints for the home page


def landing(request):
    return render(request, "landing.html")

# GET endpoints for grocery finder map.


def map(request):
    if request.method == "GET":
        return render(request, "map.html")
    elif request.method == "POST":
        result = location_pipeline(
            request.POST["zipcode"], request.POST["radius"])
        return HttpResponse(result)


# endpoints for Shopping List to recipe.
def shoppinglist(request):
    # GET: serve the page
    if request.method == "GET":
        # print("GET")
        return render(request, "shoppinglist.html")

    # POST: take in the shopping list. Query the recipe api for recipes.
    # Send recipes back to the requester.
    elif request.method == "POST":
        return HttpResponse(request.POST['shoppingList'])


# Process the user given zipcode and radius through the following pipeline:
# 1. Request Google Maps to give us all grocery stores in the given radius
# 2. Filter those results to only include supermarkets that are known to accept SNAP
# 3. Request Google Maps to give us accessibility and pricing information for the remaining grocery stores
# NOTE: The user will pass in a radius in miles, however, we want to convert this to meters per the API
def location_pipeline(user_address, radius_string):
    assert (str.isdigit(radius_string))
    radius = int(radius) * 1609.344

    # The request for the coordinates
    g = geocoder.google(user_address, key=os.getenv('GOOGLE_KEY'))

    # The received coordinates
    coords = g.latlng

    if (coords == None):
        # HANDLE ERROR
        exit(1)

    lat = coords[0]
    lng = coords[1]

    print("Address: ", user_address)
    print("Radius: ", radius_string)
    print("Coords: (", lat, ", ", lng, ")")
    print()

    list_of_supermarkets = get_superparkets_in_area(lat, lng, radius)

    print("Initial list (count = ", len(list_of_supermarkets), "): ")
    for store in list_of_supermarkets:
        for key in store:
            print(key, " : ", store[key])
        print()

    print("--------------------")

    filtered_list = get_snap_stores(list_of_supermarkets)

    print("Filtered list (count = ", len(filtered_list), "): ")
    for store in filtered_list:
        for key in store:
            print(key, " : ", store[key])
        print()

    print("--------------------")

    resulting_stores = get_store_info(filtered_list)

    print("Resulting list (count = ", len(resulting_stores), "): ")
    for store in resulting_stores:
        for key in store:
            print(key, " : ", store[key])
        print()

    print("--------------------")


location_pipeline("1733 W. School St.", 0.5)

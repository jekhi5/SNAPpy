import geocoder
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .store_locating_pipeline import *
import os
import json
from dotenv import load_dotenv, find_dotenv
from py_edamam import Edamam
from random import choice

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
            request.POST["address"], request.POST["radius"])
        return JsonResponse(result)


# endpoints for Shopping List to recipe.
def shoppinglist(request):
    # GET: serve the page
    if request.method == "GET":
        return render(request, "shoppinglist.html")

    # POST: take in the shopping list. Query the recipe api for recipes.
    # Send recipes back to the requester.
    elif request.method == "POST":
        sl = request.POST['shoppingList']
        ing1 = choice(sl)
        ing2 = choice(sl)
        ing3 = choice(sl)

        e = Edamam(
            recipes_appid=os.getenv('RECIPE_ID'),
            recipes_appkey=os.getenv('RECIPE_KEY'),
        )

        result = e.search_recipe(ing1 + ' ' + ing2 + ' ' + ing3)

        print(result)
        if result['count'] > 0:
            out = result['hits'][0]

            data = {
                'hits': result['count'],
                'title': out['recipe']['label'],
                'url': out['recipe']['url']
            }

            return JsonResponse(data)

        else:
            out = {'hits': 0}
            return JsonResponse(out)


# Process the user given zipcode and radius through the following pipeline:
# 1. Request Google Maps to give us all grocery stores in the given radius
# 2. Filter those results to only include supermarkets that are known to accept SNAP
# 3. Request Google Maps to give us accessibility and pricing information for the remaining grocery stores
# NOTE: The user will pass in a radius in miles, however, we want to convert this to meters per the API


def location_pipeline(user_address, radius_string):

    try:
        user_address = ''.join(x for x in user_address if x != '"')
        radius_string = ''.join(x for x in radius_string if x != '"')
        float(radius_string)
    except ValueError:
        # HANDLE ERROR
        return {"results": []}

    radius = float(radius_string) * 1609.344

    # The request for the coordinates
    g = geocoder.google(user_address, key=os.getenv('GOOGLE_KEY'))

    # The received coordinates
    coords = g.latlng

    if (coords == None):
        # HANDLE ERROR
        return {"results": []}

    lat = coords[0]
    lng = coords[1]

    list_of_supermarkets = get_supermarkets_in_area(lat, lng, radius)

    filtered_list = get_snap_stores(list_of_supermarkets)

    return {"results": get_store_info(filtered_list)}

import re
import geocoder
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .store_locating_pipeline import *
import os
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

        sl = request.POST['shoppingList']
        ing1 = choice(sl)
        ing2 = choice(sl)
        ing3 = choice(sl)

        e = Edamam(
            recipes_appid= os.getenv('RECIPE_ID'),
            recipes_appkey=os.getenv('RECIPE_KEY'),
        )

        
        result = e.search_recipe(ing1 + ' ' + ing2 + ' ' + ing3)

        if result['count'] > 0:
            out = choice(result['hits'])

            
            data = {
                'hits'  : result['count'],
                'title' : out['recipe']['label'],
                'url'   : out['recipe']['url']
            }

            return JsonResponse(data)

        else:
            out = {'hits' : 0}
            return JsonResponse(out)

        





# Process the user given zipcode and radius through the following pipeline:
# 1. Request Google Maps to give us all grocery stores in the given radius
# 2. Filter those results to only include supermarkets that are known to accept SNAP
# 3. Request Google Maps to give us accessibility and pricing information for the remaining grocery stores
# NOTE: The user will pass in a radius in miles, however, we want to convert this to meters per the API
def location_pipeline(user_address, radius_string):
    try:
        float(radius_string)
    except:
        # HANDLE ERROR
        exit(1)

    radius = int(radius_string) * 1609.344

    # The request for the coordinates
    g = geocoder.google(user_address, key=os.getenv('GOOGLE_KEY'))

    # The received coordinates
    coords = g.latlng

    if (coords == None):
        # HANDLE ERROR
        exit(1)

    lat = coords[0]
    lng = coords[1]

    # print("Address: ", user_address)
    # print("Radius: ", radius_string)
    # print("Coords: (", lat, ", ", lng, ")")
    # print()

    list_of_supermarkets = get_supermarkets_in_area(lat, lng, radius)

    # print("Initial list (count = ", len(list_of_supermarkets), "): ")
    # for store in list_of_supermarkets:
    #     for key in store:
    #         print(key, " : ", store[key])
    #     print()

    # print("--------------------")

    filtered_list = get_snap_stores(list_of_supermarkets)

    # print("Filtered list (count = ", len(filtered_list), "): ")
    # for store in filtered_list:
    #     for key in store:
    #         print(key, " : ", store[key])
    #     print()

    # print("--------------------")

    resulting_stores = get_store_info(filtered_list)

    # print("Resulting list (count = ", len(resulting_stores), "): ")
    # for store in resulting_stores:
    #     for key in store:
    #         print(key, " : ", store[key])
    #     print()

    # print("--------------------")


location_pipeline("500 Parker St.", 2)

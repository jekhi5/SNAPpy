from django.shortcuts import render
from django.http import HttpResponse
from decouple import config
import requests

# TODO: implement spell-checking!

# GET endpoints for the home page
def landing(request):
    return render(request, "landing.html")

# GET endpoints for grocery finder map.
def map(request):
    return render(request, "map.html")

# endpoints for Shopping List to recipe.
def shoppinglist(request):
    # GET: serve the page
    if request.method == "GET":
        return render(request, "shoppinglist.html")

    # POST: take in the shopping list. Query the recipe api for recipes.
    # Send recipes back to the requester.
    elif request.method == "POST":
        # extract first four ingredients from list 
        ingredients = request.POST['shoppingList']
        #ingredients = ingredients[:3]
        #ingredients_query = ' '.join(ingredients)

        # build message payload
        payload = {
            'app_id'  : config('RECIPE_ID'),
            'app_key' : congig('RECIPE_KEY'),
            'q'       : ingredients_query
        }

        r = requests.get(
            'https://api.edamam.com/api/recipes/v2',
            params=payload
        )




        return HttpResponse(ingredients)


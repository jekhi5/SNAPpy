from django.shortcuts import render
from django.http import HttpResponse

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
        return HttpResponse(request.POST['shoppingList'])


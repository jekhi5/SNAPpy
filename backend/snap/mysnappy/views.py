from django.shortcuts import render
from django.http import HttpResponse

# TODO: implement spell-checking!

def landing(request):
    return render(request, "landing.html")

def map(request):
    if request.method == "GET":
        return render(request, "map.html")
    elif request.method == "POST":
        return HttpResponse(request.POST["map"])

def shoppinglist(request):
    if request.method == "GET":
        #print("GET")
        return render(request, "shoppinglist.html")
    elif request.method == "POST":
        print("POST")
        return HttpResponse(request.POST['shoppingList'])

from django.shortcuts import render



def landing(request):
    return render(request, "landing.html")

def map(request):
    return render(request, "map.html")

def shoppinglist(request):
    return render(request, "shoppinglist.html")

def shoppinglist_post(request):
    if request.POST:
        print(request)


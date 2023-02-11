import os
from django.shortcuts import render
from django.http import HttpResponse, FileResponse



def index(request):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'view/simple_frontend.html')

    return FileResponse(open(filename, 'rb'))


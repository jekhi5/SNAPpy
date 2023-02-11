from django.db import models

# Create your models here.

class Donor(models.Model):
    items = []
    times = {}

    def __init__(self, email, hashed_pw, location, radius):
        self.email = email
        self.hashed_pw = hashed_pw
        self.location = location
        self.radius = radius
    
    def add_items(item_list):
        items = item_list

    def set_time(times_dict):
        times = times_dict

class Needer(models.Model):
    items = []
    times = {}

    def __init__(self, email, hashed_pw, location, radius):
        self.email = email
        self.hashed_pw = hashed_pw
        self.location = location
        self.radius = radius
    
    def add_items(item_list):
        items = item_list

    def set_time(times_dict):
    times = times_dict
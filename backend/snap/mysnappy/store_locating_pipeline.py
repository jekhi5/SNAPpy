import requests
import os
import pandas as pd
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

key = os.getenv('GOOGLE_KEY')
payload = {}
headers = {}


def get_supermarkets_in_area(lat, lng, radius):
    nearby_base = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="
    latitude = str(lat)
    longitude = str(lng)
    establishment_type = "supermarket"

    nearby_url = f'{nearby_base}{latitude}%2C{longitude}&radius={radius}&type={establishment_type}&key={key}'

    nearby_response = requests.request(
        "GET", nearby_url, headers=headers, data=payload)

    nearby_json_list = nearby_response.json()["results"]

    return list(map(lambda response: {
        "name": response["name"],
        "place_id": response["place_id"],
        "vicinity": response["vicinity"],
        "latlng": (response["geometry"]["location"]["lat"], response["geometry"]["location"]["lng"])
    }, nearby_json_list))

# Perform a version of map-reduce on the given list of stores and return a list only
# containing stores that accept SNAP


def get_snap_stores(nearby_response):
    if len(nearby_response) == 0:
        return nearby_response

    snap_stores = pd.read_csv(
        '/home/emery/hack-beanpot/SNAPpy/backend/snap/mysnappy/SNAP_Store_Locations.csv')

    # Transforms input into dataframe
    nearby_response = pd.json_normalize(nearby_response)

    # Splits the address ("319 Huntington Avenue, Boston, MA" -> ["319 Huntington Ave", "Boston"])
    nearby_response[['Addresses', 'City']
                    ] = nearby_response.vicinity.str.split(", ", expand=True)
    nearby_response.Addresses = nearby_response.Addresses.str.replace(
        'Avenue', 'Ave')
    nearby_response.Addresses = nearby_response.Addresses.str.replace(
        'Street', 'St')
    nearby_response.Addresses = nearby_response.Addresses.str.replace(
        'Road', 'Rd')
    nearby_response.Addresses = nearby_response.Addresses.str.replace(
        'Drive', 'Dr')
    nearby_response.Addresses = nearby_response.Addresses.str.replace(
        'Boulevard', 'Blvd')

    # Compare the list of grocery stores in the area against the list of grocery stores that are
    # known to accept SNAP and filters out those that are not. Turns result into an array of dictionaries.
    nearby_stores = nearby_response
    snap_addresses = snap_stores['Address'].tolist()
    nearby_stores = nearby_stores[nearby_stores["Addresses"].isin(
        snap_addresses)].drop(columns=["Addresses", "City"], axis=1)
    output_list = nearby_stores.to_dict(orient='records')

    # Return result
    return output_list

# Complete a detail_place API call and return a list of JSON objects with the resulting info


def get_store_info(list_of_places):
    if len(list_of_places) == 0:
        return list_of_places

    details_base = "https://maps.googleapis.com/maps/api/place/details/json?place_id="

    fields = "%2C".join(["formatted_phone_number", "url", "website",
                        "wheelchair_accessible_entrance", "delivery", "curbside_pickup", "current_opening_hours"])

    result = list_of_places

    for data in result:
        detail_url = f'{details_base}{data["place_id"]}&fields={fields}&key={key}'
        detail_response = requests.request(
            "GET", detail_url, headers=headers, data=payload)
        print(detail_response.json())
        detail_json = detail_response.json()["result"]

        data.update(detail_json)

    return result

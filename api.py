import requests

nearby_base = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" 
latitude = "42.338110"
longitude = "-71.094780"
radius = "1000"
establishment_type = "supermarket"
key = "API_KEY"

nearby_url = f'{nearby_base}{latitude}%2C{longitude}&radius={radius}&type={establishment_type}&key={key}'

payload={}
headers = {}

nearby_response = requests.request("GET", nearby_url, headers=headers, data=payload)
nearby_json_list = nearby_response.json()["results"]

important_data = list(map(lambda response : {
    "name": response["name"],
    "place_id": response["place_id"],
    "vicinity": response["vicinity"]
    }, nearby_json_list))

details_base = "https://maps.googleapis.com/maps/api/place/details/json?place_id="
fields = "%2C".join(["formatted_phone_number", "url", "website", "wheelchair_accessible_entrance", "delivery", "curbside_pickup"])

for data in important_data:
    detail_url = f'{details_base}{data["place_id"]}&fields={fields}&key={key}'
    detail_response = requests.request("GET", detail_url, headers=headers, data=payload)

    detail_json = detail_response.json()["result"]
    
    data.update(detail_json)


for entry in important_data:
    for key in entry:
        print(key, " : ", entry[key])
    print()

import pandas as pd

# EXAMPLE INPUT
'''
    maplocs = [
        {'name': 'Whole Foods Market', 'place_id': 'ChIJJYdkPBp644kRwWFG-QDpyuY', 'vicinity': '15 Westland Avenue, Boston'},
        {'name': 'Symphony Market / Halal / postmate', 'place_id': 'ChIJ071AwRl644kRn4LD2Fx3UIM',
         'vicinity': '291 Huntington Avenue, Boston'},
        {'name': 'College Convenience', 'place_id': 'ChIJ8SPg6Bl644kR5l2NR1yHOeM',
         'vicinity': '281 Huntington Avenue, Boston'},
        {'name': "Wollaston's Market", 'place_id': 'ChIJ3V9Axxh644kRYpjOb4LAAPg',
         'vicinity': '369 Huntington Avenue, Boston'},
        {'name': 'International Halal Market', 'place_id': 'ChIJedBykSd644kR2aLQIv0sbBI',
         'vicinity': '1433 Tremont Street, Boston'},
        {'name': 'Target Grocery', 'place_id': 'ChIJn7EjihV544kRK9p_ELhNhkU', 'vicinity': '1341 Boylston Street, Boston'},
        {'name': 'Punjab Mini Mart', 'place_id': 'ChIJKwT22oh544kRg1pFKjfeTkw', 'vicinity': '1576 Tremont Street, Boston'}]
'''


def get_snap_stores(nearby_response):

    snap_stores = pd.read_csv('SNAP_Store_Locations.csv')

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


# EXAMPLE OUTPUT
'''
get_snap_stores([
    {'name': 'Whole Foods Market', 'place_id': 'ChIJJYdkPBp644kRwWFG-QDpyuY', 'vicinity': '15 Westland Avenue, Boston'}, 
    {'name': 'Symphony Market / Halal / postmate', 'place_id': 'ChIJ071AwRl644kRn4LD2Fx3UIM', 'vicinity': '291 Huntington Avenue, Boston'}, 
    {'name': 'International Halal Market', 'place_id': 'ChIJedBykSd644kR2aLQIv0sbBI', 'vicinity': '1433 Tremont Street, Boston'}, 
    {'name': 'Target Grocery', 'place_id': 'ChIJn7EjihV544kRK9p_ELhNhkU', 'vicinity': '1341 Boylston Street, Boston'}])
'''

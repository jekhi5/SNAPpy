import pandas as pd

df = pd.read_csv('SNAP_Store_Locations.csv')

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

df_maplocs = pd.json_normalize(maplocs)

# print(df_maplocs.to_string)
df_maplocs[['Address', 'City']] = df_maplocs.vicinity.str.split(", ", expand=True)
pd.set_option('display.max_columns', None)
# df_maplocs.head()
print(df_maplocs.to_string)

for row in df_maplocs:
    print(row["name"])

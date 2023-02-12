import pandas as pd

def get_snap_stores(nearby_response):

    snap_stores = pd.read_csv('SNAP_Store_Locations.csv')
    maplocs = nearby_response

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
    # print(maplocs)
    nearby_response = pd.json_normalize(nearby_response)

    nearby_response[['Addresses', 'City']] = nearby_response.vicinity.str.split(", ", expand=True)
    nearby_response.Addresses = nearby_response.Addresses.str.replace('Avenue','Ave')
    nearby_response.Addresses= nearby_response.Addresses.str.replace('Street','St')
    nearby_response.Addresses= nearby_response.Addresses.str.replace('Road','Rd')
    nearby_response.Addresses= nearby_response.Addresses.str.replace('Drive','Dr')
    nearby_response.Addresses= nearby_response.Addresses.str.replace('Boulevard','Blvd')

    nearby_stores = nearby_response
    marks_list = snap_stores['Address'].tolist()
    nearby_stores = nearby_stores[nearby_stores["Addresses"].isin(marks_list)].drop(columns=["Addresses","City"], axis=1)
    output_list = nearby_stores.to_dict(orient='records')
    print(output_list)

    return output_list

get_snap_stores( [
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
        {'name': 'Punjab Mini Mart', 'place_id': 'ChIJKwT22oh544kRg1pFKjfeTkw', 'vicinity': '1576 Tremont Street, Boston'}])
# print(df_maplocs.to_string)
# pd.set_option('display.max_columns', None)
# formatting
# print(df1)
# print(df1)

# df_maplocs.head()
# print(df_maplocs.to_string)

# for row in df_maplocs:
    # print(row["name"])

# df3 = pd.merge(df2, df1, on=['Address'], how='inner')
# print(df['Address'].where(df['Rating_Score'] < 50))

# d = (
#     df1.merge(df2,
#               on=['Address'],
#               how='left',
#               indicator=True)
#     .query('_merge == "left_only"')
#     .drop(columns='_merge')
# )
# res = pd.merge(df1,df2, indicator=True, how='left').query('_merge=="left_only"').drop('_merge', axis=1)
# df3 = pd.merge(df1, df2, how='inner', left_on='Addresses', right_on='Address')
# df3 = df1[df1['Address'].isin(df2['Addresses'])]

# print(df1)
# print(marks_list)
# filter1 = df1["Addresses"].isin([marks_list])
# print(df1["Addresses"].isin(marks_list))
# print(df1[df1["Addresses"].isin(marks_list)])
# print(df1)

# print(df1.to_dict(orient='records'))




# df1 = df1.drop('Addresses', "City", axis=1)
# print(df1)
# print(filter1)
# print(df1[filter1])



# Display Result
# print("Result:\n",res)

# print(df3)
# df1.merge(df2, on=['Address'], how='left', indicator=True)
# # df1.compare(df2, keep_shape=True, keep_equal=True)
# # df = df1.merge(df2, left_on='Address', right_on='Address', how='left')
# print(df1)
# # df1['team'].isin(df2['team']).value_counts()
# # df_common = df1.loc[df1['Address'].isin(df2['Address'])]
# print(df_common)
# print(df1)
# print(df2)

# importing geopy library


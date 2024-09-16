#!/usr/bin/env python3

import requests
import json

def calculate_commute_time(origin_coord_list:list, destination_coord_list:list, departure_time:str) -> int:
    # Load the configuration file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Access the API key
    my_api_key = config.get('google_api_key')
    origin_lat = str(origin_coord_list[0])
    origin_lon = str(origin_coord_list[1])
    dest_lat = str(destination_coord_list[0])
    dest_lon = str(destination_coord_list[1])
    
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + origin_lat + "%2C" + origin_lon + "&destinations=" + dest_lat + "%2C" + dest_lon + "&units=imperial&departure_time=" + departure_time + "&key=" + my_api_key

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    results = response.json()

    return int(results["rows"][0]["elements"][0]["duration_in_traffic"]["text"][:-5])

def main():
    
    with open('coordinate_data.json','r') as coords:
        coordinate_json = json.load(coords)

    # destination_address = "6803%20S%20Tuscon%20Way%2C%20Centennial%2C%20CO%2080112"
    dest_coords = [39.59114,-104.83695]
    departure_time = "now"
    for point in coordinate_json:
        origin = [point["latitude"],point["longitude"]]
        commute = calculate_commute_time(origin,dest_coords,departure_time)
        point["commute_time"] = commute

    with open('commute_times.json','w') as f:
        json.dump(coordinate_json,f)

if __name__ == '__main__':
    main()

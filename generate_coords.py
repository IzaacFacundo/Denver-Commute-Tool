#!/usr/bin/env python3

import numpy as np
import json

def main():
    NW_bounds = [39.737844,-105.009355]
    SE_bounds = [39.687468,-104.942057]

    grid_density = 10 # n points in one direction (n x n grid)
    point_id = 0
    points = []
    for lat in np.linspace(NW_bounds[0],SE_bounds[0],grid_density):
        for lon in np.linspace(NW_bounds[1], SE_bounds[1],grid_density):
            points.append({'point_id': point_id, 'latitude': lat, 'longitude': lon,'commute_time':0})
            point_id += 1

    with open('coordinate_data.json','w') as out:
        json.dump(points,out)        

if __name__ == '__main__':
    main()

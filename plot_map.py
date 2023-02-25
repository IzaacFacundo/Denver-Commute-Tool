import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

with open("../Denver-Commute-Tool/coordinate_data.json",'r') as c:
    coord_data_json = json.load(c)
    coord_df = pd.DataFrame(coord_data_json)






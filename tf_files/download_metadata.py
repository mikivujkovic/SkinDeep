"""
Script that downloads image metadata from ISIC archive
"""
from __future__ import print_function
import pandas as pd
import requests
import json
from collections import OrderedDict

images_data = []
images_data_frame = pd.DataFrame()


# Get all IDs from name-id pairs
ids = []
with open("images_id_name.csv") as f:
    for line in f:
        id = line[:24].strip()
        ids.append(id)

# counter for printing progress to console
count = len(ids)
counter = 1

# metadata placeholders
image_id = ""
image_name = ""
dataset = ""
age = ""
benign = ""
diagnosis = ""
confirm_type = ""
melanocytic = ""
sex = ""

# get metadata by ID
for id in ids:
    url = "https://isic-archive.com/api/v1/image/" + id
    try:
        response = requests.get(url)
        data = response.text
        data_ext = json.loads(data, object_pairs_hook=OrderedDict)
    except:
        print("no connection")
    #print(data_ext)
    try:
        image_id = id
        image_name = data_ext["name"]
        diagnosis = data_ext["meta"]["clinical"]["diagnosis"]
        benign = data_ext["meta"]["clinical"]["benign_malignant"]
        dataset = data_ext["dataset"]["name"]
        age = data_ext["meta"]["clinical"]["age_approx"]
        confirm_type = data_ext["meta"]["clinical"]["diagnosis_confirm_type"]
        melanocytic = data_ext["meta"]["clinical"]["melanocytic"]
        sex = data_ext["meta"]["clinical"]["sex"]
    except:
        pass

    # append metadata to list
    desc = [image_id, image_name, dataset, age, benign, diagnosis, confirm_type, melanocytic, sex]
    print(desc)
    print("\n")
    images_data.append(desc)
    # pprint.pprint(images_data)
    print("image: ", counter, "of: ", count)
    print("\n")
    counter = counter + 1

# save metadata to disk using pandas Dataframe
print("Saving to disk")
print("\n")
images_data_frame = images_data_frame.append(images_data)
images_data_frame.to_csv("images_data.csv")
print("Finished")
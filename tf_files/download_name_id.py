"""
Script that downloads name-ID pairs for images in ISIC archive
"""
from __future__ import print_function
import pandas as pd
import requests
import json

# dataset ids and lenghts
ids = [
    ["5627f42b9fc3c132be08d84f", 683],
    ["582b8d419fc3c1566bbcb098", 417],
    ["5627f5f69fc3c132be08d852", 1535],
    ["57eebe389fc3c12a89bb75f7", 225],
    ["581cd6059fc3c13dcd0e0930", 947],
    ["5825fd959fc3c171066d3352", 111],
    ["5627eefe9fc3c132be08d84c", 9251],
    ["54b6e869bae4785ee2be8652", 557],
    ["54ea816fbae47871b5e00c80", 60]
]

images_data = []
images_data_frame = pd.DataFrame()

# get ids and names by dataset
for id in ids:
    no = str(id[1])
    dataset = id[0]
    url = "https://isic-archive.com/api/v1/image?limit=" + no + \
    "&offset=0&sort=name&sortdir=1&datasetId=" + dataset
    try:
        response = requests.get(url)
        data = response.text
        data_ext = json.loads(data)
    except:  
        print("no connection")

    for line in data_ext:
        img_id = line["_id"]
        img_name = line["name"]
        images = [img_id, img_name]
        images_data.append(images)

# save id name pairs to disk using pandas Dataframe
images_data_frame = images_data_frame.append(images_data)
images_data_frame.columns = ["id", "name"]
images_data_frame.set_index("id", inplace=True)
images_data_frame.to_csv("images_id_name.csv")


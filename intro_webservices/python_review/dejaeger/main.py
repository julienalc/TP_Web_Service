# Solution
import json
import pandas as pd

# Step 1 Read JSON file
with open("../data.json", "r") as file:
    json_data = file.read()

# Step 2 Parse JSON
data = json.loads(json_data)

# Step 3 Extract JSON data into a list of dict
clean_data = []
for people in data:
    people_data = {
        "firstname": people["info"]["firstname"],
        "lastname": people["info"]["lastname"],
        "address": people["info"]["address"]["street"] + people["info"]["address"]["city"] + people["info"]["address"]["zipcode"],
        "age": people["info"]["age"],
        "job": people["job"]
    }
    clean_data.append(people_data)

# Step 4 Make a dataframe out of the python object (list<dict>)
df = pd.DataFrame(clean_data)

# Step 5 Display of the DF
print(df.head())
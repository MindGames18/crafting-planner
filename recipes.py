import os
import json

r_name = input("Enter the Recipe Name:")
if r_name == "":
    r_name = "anvil"

script_dir = os.path.dirname(__file__)
sub_dir = '\\jar\\assets\\minecraft\\recipes\\'
abs_file_path = script_dir + sub_dir + r_name + ".json"
read_data = open(abs_file_path).read()
data = json.loads(read_data)

count = 0

'''#finding raw materials
print("Raw materials req. for recipe are: \n")
if data["type"] == "crafting_shaped":
    for item in data["key"]:
        ing_name = data["key"][item]["item"]
        ing_name = ing_name.replace("minecraft:", "")
        ing_name = ing_name.replace("_", " ")
        print(ing_name)
    exit()

elif data["type"] == "crafting_shapeless":
    for item in data["ingredients"]:
        #print(data["ingredients"][count])
        ing_name = data["ingredients"][count]["item"]
        ing_name = ing_name.replace("minecraft:", "")
        ing_name = ing_name.replace("_", " ")
        print(ing_name)
        count = count + 1
    exit()'''


item_count = 0
ing_count = []
item_name = [0,0,0,0,0,0,0,0,0]

if data["type"] == "crafting_shaped":
    print(data["pattern"][0])
for item in data["key"]:
    item_name[item_count] = item
    item_count += 1


for i in range(8):
    print(data["pattern"][i])
    for item in data["key"]:
        print(data["key"][item])
        #if data["pattern"][i] == data["key"][item]:

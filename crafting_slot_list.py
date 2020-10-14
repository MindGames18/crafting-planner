import os
import constants as c
import json


recipe_name = []
ing_name = []
recipe_count = 0

for filename in os.listdir(c.abs_recipe_dir):
    abs_file_path = c.abs_recipe_dir + filename
    read_data = open(abs_file_path).read()  # File Handle
    data = json.loads(read_data)  # Json object

    name = data["result"]["item"]
    name = name.replace("minecraft:", "")
    recipe_name.append(name)
    print(name)

    if data["type"] == "crafting_shaped":
        for item in data["key"]:
            if type(data["key"][item]) is dict:
                print(data["key"][item]["item"],)
        print("\n")
            

'''
    # no of each raw materials needed
        for i in range(len(data["pattern"])):
            for j in range(len(data["pattern"][0])):
                crafting_slot = data["pattern"][i][j]
                print(crafting_slot)
        exit()


else:
    for item in data["ingredients"]:
        if item not in item_name:
            item_name.append(item)
        item_count += 1

    for item in data["ingredients"]:
        for i in range(len(item_name)):
            if item == item_name[i]:
                ing_count[i] += 1
'''

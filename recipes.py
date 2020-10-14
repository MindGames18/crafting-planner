import os
import json

#add a dropdown with all the recipe names
r_name = "stick"

script_dir = os.path.dirname(__file__)
sub_dir = '\\jar\\assets\\minecraft\\recipes\\'
abs_file_path = script_dir + sub_dir + r_name + ".json"
read_data = open(abs_file_path).read()
data = json.loads(read_data)

count = 0
counter = 0
item_count = 0
ing_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
item_name = []
shapeless_name = []
crafting_slot = []

# counts the number of unique items req.
if data["type"] == "crafting_shaped":
    for item in data["key"]:
        item_name.append(item)
        item_count += 1

    # no of each raw materials needed
    for i in range(len(data["pattern"])):
        for j in range(len(data["pattern"][0])):
            crafting_slot = data["pattern"][i][j]
            for k in range(item_count):
                if data["pattern"][i][j] == item_name[k]:
                    ing_count[k] += 1

else:
    for item in data["ingredients"]:
        if item not in item_name:
            item_name.append(item)
        item_count += 1

    for item in data["ingredients"]:
        for i in range(len(item_name)):
            if item == item_name[i]:
                ing_count[i] += 1
        

counter = item_count

# finding raw materials
print("Raw materials req. for recipe are: \n")
if data["type"] == "crafting_shaped":
    for item in data["key"]:
        if type(data["key"][item]) is dict:
            ing_name = data["key"][item]["item"]
            ing_name = ing_name.replace("minecraft:", "")
            ing_name = ing_name.replace("_", " ")
            print(ing_name, ing_count[item_count-counter])
            counter -= 1
        else:
            ing_name = data["key"][item][0]["item"]
            ing_name = ing_name.replace("minecraft:", "")
            ing_name = ing_name.replace("_", " ")
            print(ing_name, ing_count[item_count-counter])
            counter -= 1

elif data["type"] == "crafting_shapeless":
    for item in data["ingredients"]:
        ing_name = data["ingredients"][count]["item"]
        ing_name = ing_name.replace("minecraft:", "")
        ing_name = ing_name.replace("_", " ")
        count = count + 1
        if ing_name not in shapeless_name:
            shapeless_name.append(ing_name)
            print(shapeless_name[item_count-counter], ing_count[item_count-counter])
            counter -= 1

import os
import constants as c
import json


#recipe_name = 
ing_name = []
recipe_count = 0
newpat = [[0,0,0],[0,0,0],[0,0,0]]

for filename in os.listdir(c.abs_recipe_dir):
    abs_file_path = c.abs_recipe_dir + filename
    read_data = open(abs_file_path).read()  # File Handle
    data = json.loads(read_data)  # Json object

    name = data["result"]["item"]
    name = name.replace("minecraft:", "")

    ing_name = []
    if data["type"] == "crafting_shaped":
        if len(data["pattern"])*len(data["pattern"][0]) == 9:
            newpat = data["pattern"]
            print("size = 9")
            #print(newpat)
        else:
            print("size != 9")
            for i in range(len(data["pattern"])):
                for j in range(len(data["pattern"][0])):
                    newpat[i][j] = data["pattern"][i][j]
            #print(newpat)


        for i in range(len(newpat)):
            for j in range(len(newpat)):
                for k in data["key"]:
                        if newpat[i][j] == " " or newpat[i][j] == 0:
                            ing_name.append("NULL")
                        else:
                            ing_name.append(data["key"][k]["item"])


        print(name,"\n",ing_name)
        ing_name = []
        newpat = [[0,0,0],[0,0,0],[0,0,0]]
        exit()

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

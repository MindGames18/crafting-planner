import os
import constants as c
import json


ing_name = []
newpat = [[0,0,0],[0,0,0],[0,0,0]]
count = 0
book = {}


def slot_item(recipe_name):
    for filename in os.listdir(c.abs_recipe_dir):
        abs_file_path = c.abs_recipe_dir + filename
        read_data = open(abs_file_path).read()  # File Handle
        data = json.loads(read_data)  # Json object

        name = data["result"]["item"]
        name = name.replace("minecraft:", "")
    
        #changing all the patterns from random dimension to 3x3
        if data["type"] == "crafting_shaped":
            for i in range(len(data["pattern"])):
                for j in range(len(data["pattern"][0])):
                    newpat[i][j] = data["pattern"][i][j]

            #writting according to crafting slots in the dict   
            for i in range(len(newpat)):
                for j in range(len(newpat)):
                    if newpat[i][j] in data["key"]:
                        if type(data["key"][newpat[i][j]]) is dict:
                            ing_name.append(data["key"][newpat[i][j]]["item"])
                            count+=1
            
                        else:
                            ing_name.append(data["key"][newpat[i][j]][0]["item"])
                            count+=1
                    else:
                        ing_name.append(None)
                        count+=1

        #same for shapeless just puting in the grids
        elif data["type"] == "crafting_shapeless":
            for item in data["ingredients"]:
                if type(item) is dict:
                    ing_name.append(item["item"])
                    count+=1
                else:
                    ing_name.append(item[0]) 
                    count+=1
            for i in range(9-count):
                ing_name.append(None)

 
    book[name] = ing_name #putting everything in a dict
    
    #reseting all the values
    ing_name = []
    newpat = [[0,0,0],[0,0,0],[0,0,0]]
    count = 0
    #print(filename) just for checking where the file is breaking

    return book[recipe_name]

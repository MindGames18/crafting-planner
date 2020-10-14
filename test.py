import os
import constants as c
import json


#recipe_name = 
ing_name = []
recipe_count = 0
newpat = [[0,0,0],[0,0,0],[0,0,0]]
filename = "yellow_wool.json"
count = 0


#for filename in os.listdir(c.abs_recipe_dir):
abs_file_path = c.abs_recipe_dir + filename
read_data = open(abs_file_path).read()  # File Handle
data = json.loads(read_data)  # Json object

name = data["result"]["item"]
name = name.replace("minecraft:", "")
ing_name = []

if data["type"] == "crafting_shaped":
    for i in range(len(data["pattern"])):
        for j in range(len(data["pattern"][0])):
            newpat[i][j] = data["pattern"][i][j]

    
    for i in range(len(newpat)):
        for j in range(len(newpat)):
            if newpat[i][j] in data["key"]:
                if type(data["key"][newpat[i][j]]) is dict:
                    ing_name.append(data["key"][newpat[i][j]]["item"])
                    print(ing_name[count])
                    count+=1
            
                else:
                    ing_name.append(data["key"][newpat[i][j]][0]["item"])
                    print(ing_name[count])
                    count+=1
            else:
                ing_name.append("NULL")
                print(ing_name[count])
                count+=1
   

    print(name,"\n",ing_name)
    ing_name = []
    newpat = [[0,0,0],[0,0,0],[0,0,0]]

elif data["type"] == "crafting_shapeless":
    for item in data["ingredients"]:
        print(data["ingredients"][count]["item"])
        ing_name.append(data["ingredients"][count]["item"])
        count+=1
    for i in range(9-count):
        ing_name.append("NULL")
    print(ing_name)

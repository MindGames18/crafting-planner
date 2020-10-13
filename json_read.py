import os
import json

script_dir = os.path.dirname(__file__)
sub_dir = '\\jar\\assets\\minecraft\\recipes\\'
file_path = script_dir + sub_dir

# "w" creates new file in write mode overwrites if already exist
file_shapeless = open("file_shapeless.txt", "w")
file_shaped = open("file_shaped.txt", "w")
f_recipe = open("recipe_name.txt", "w")

for filename in os.listdir(file_path):  # reads the files in the folder
    # print(filename)
    abs_file_path = script_dir + sub_dir + filename
    read_data = open(abs_file_path).read()  # reads the file
    data = json.loads(read_data)  # loads everything in the file

    if data["type"] == "crafting_shapeless":
        file_shapeless.write(filename)
        file_shapeless.write("\n")
    else:
        file_shaped.write(filename)
        file_shaped.write("\n")
        
    if data["result"]:
        fname= data["result"]["item"]
        fname = fname.replace("minecraft:","")
        f_recipe.write(fname)
        f_recipe.write("\n")

file_shapeless.close()
file_shaped.close()
f_recipe.close()

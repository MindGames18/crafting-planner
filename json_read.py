import os
import json
import constants

'''
def recipe_loader():

    file_path = constants.script_dir + constants.recipe_dir
    
    # "w" creates new file in write mode overwrites if already exist
    shapeless = open("shapeless.txt", "w")
    shaped = open("shaped.txt", "w")
    f_recipe = open("recipe_name.txt", "w")

    for filename in os.listdir(file_path):  # reads the files in the folder
        # print(filename)
        abs_file_path = script_dir + sub_dir + filename
        read_data = open(abs_file_path).read()  # reads the file
        data = json.loads(read_data)  # loads everything in the file

        if data["type"] == "crafting_shapeless":
            shapeless.write(filename)
            shapeless.write("\n")
        else:
            shaped.write(filename)
            shaped.write("\n")

        if data["result"]:
            fname = data["result"]["item"]
            fname = fname.replace("minecraft:", "")
            f_recipe.write(fname)
            f_recipe.write("\n")

    shapeless.close()
    shaped.close()
    f_recipe.close()
'''


def recipe_loader():

    # "w" creates new file in write mode overwrites if already exist
    shapeless = list()
    shaped = list()
    f_recipe = list()
    file_names = list()

    # reads the files in the folder
    for filename in os.listdir(constants.abs_recipe_dir):

        abs_file_path = constants.abs_recipe_dir + filename
        read_data = open(abs_file_path).read()  # File Handle
        data = json.loads(read_data)  # Json object

        # Categorising into shaped and shapeless recipes
        if data["type"] == "crafting_shapeless":
            shapeless.append(filename)

        else:
            shaped.append(filename)

        # Listing all the recipes Available
        if data["result"]:
            fname = data["result"]["item"]
            fname = fname.replace("minecraft:", "")
            f_recipe.append(fname)
        tmp_file_name = filename.replace(".json", "")
        file_names.append(tmp_file_name)

    return file_names

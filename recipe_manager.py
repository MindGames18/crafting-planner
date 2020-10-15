import json
import constants
import json_read

'''
    Method to identify unique ingredients required in an item
'''


def unique_items_required(item_name):

    # Determining file path and creating the json object
    abs_file_path = constants.abs_recipe_dir + item_name + ".json"
    fhandle = open(abs_file_path).read()
    json_obj = json.loads(fhandle)

    # Initialising Lists and counter
    unique_ingredients = [None for i in range(9)]
    unique_ingredients = []

    # Code Logic for shaped and shapeless
    if json_obj["type"] == "crafting_shaped":
        for item in json_obj["key"]:
            unique_ingredients.append(json_obj["key"][item])

    else:
        for item in json_obj["ingredients"]:
            if item not in unique_ingredients:
                unique_ingredients.append(item)

    #var = 0
    #print(unique_ingredients[var],type(unique_ingredients[var]))
    print(unique_ingredients)

#unique_items_required("torch")
#unique_items_required("fire_charge")

x= json_read.recipe_loader()
print(x)

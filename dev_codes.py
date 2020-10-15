import json_read as jr
import recipe_manager as rm

###############################################
# dev code to iterate through all recipes 
# to check if any recipe fails to parse
x = jr.recipe_loader()
print(len(x))

for iterator in x:
    try:
        y = rm.unique_items_required(iterator)
    except:
        print("failed", iterator)
###############################################
import recipe_manager as rm

###############################################
# dev code to iterate through all recipes
# to check if any recipe fails to parse
x = rm.recipe_loader()
print(len(x))
i = 0

for iterator in x:
    try:
        y = rm.unique_items_required(iterator)
        # print(i)
        i += 1
    except:
        print("failed", iterator)
###############################################

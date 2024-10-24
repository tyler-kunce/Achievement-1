import pickle

def take_recipe():
    recipe_name = input("What's the recipe called? ")
    cooking_time = int(input("How long to cook this (in minutes)? "))
    input_ingredients = input("What do you need to cook it (comma-separated)? ").split(",")
    ingredients = []
    for ingredient in input_ingredients:
        ingredients.append(ingredient.strip())
    
    difficulty = calc_difficulty(cooking_time, ingredients)
    
    recipe = {
        "recipe_name": recipe_name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty
    }

    return recipe

def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    if cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    if cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    if cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "Hard"

    return difficulty

file_name = input("What's the name of the file you're opening? ")
file_name += '.bin'

try:
    recipe_file = open(file_name, "rb")
    data = pickle.load(recipe_file)
except FileNotFoundError:
    print("That file doesn't exist. Let's create one!")
    data = {"recipes_list": [], "all_ingredients": []}
except:
    print("Oh no! Something unexpected occurred.")
    data = {"recipes_list": [], "all_ingredients": []}
else:
    recipe_file.close()
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]

n = int(input("How many recipes are you entering? "))

for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe["ingredients"]:
        if not ingredient in all_ingredients:
            all_ingredients.append(ingredient)
    recipes_list.append(recipe)

data = {"recipes_list": recipes_list, "all_ingredients": all_ingredients}

file_updt = open(file_name, "wb")
pickle.dump(data, file_updt)
file_updt.close()
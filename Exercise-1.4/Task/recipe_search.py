import pickle

def display_recipe(recipe):
    print("Recipe: ", recipe["recipe_name"])
    print("Cooking Time (in minutes): ", recipe["cooking_time"])
    print("Ingredients: ")
    for ingredient in recipe["ingredients"]:
        print("+ ", ingredient)
    print("Difficulty: ", recipe["difficulty"])

def search_ingredient(data):
    print("List of ingredients:")
    for index, ingredient in enumerate(data["all_ingredients"], 1):
        print(index, ingredient)
    
    try:
        ind = int(input("Pick a number from the list of ingredients: "))
        ingredient_searched = num_list[ind][1]
        print()
    except ValueError:
        print("Invalid input")
    except:
        print("Something went wrong. Check your input again.")
    else:
        for i in data["recipes_list"]:
            if ingredient_searched in i["ingredients"]:
                display_recipe(i)

file_name = input("Enter the name of the file containing recipes: ")

try:
    file = open(file_name, "rb")
    data = pickle.load(file)
except FileNotFoundError:
    print("That file doesn't exist")
except:
    print("Oh no! Something unexpected occurred.")
else:
    file.close()
    search_ingredient(data)
recipes_list = []
ingredients_list = []

n = int(input('How many recipes are you entering? '))

def take_recipe():
    name = str(input('What is the name of your recipe? '))
    cooking_time = int(input('How long does this take to make (in minutes)? '))
    ingredients = list(input('What do you need to make it, using a comma? ').split(', '))
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}

    return recipe

for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'Easy'
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'Medium'
    if recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'Intermediate'
    if recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'Hard'

for recipe in recipes_list:
    print('Recipe: ', recipe['name'].capitalize())
    print('Cooking Time (min): ', recipe['cooking_time'])
    print('Ingredients: ')
    for ingredient in recipe['ingredients']:
        print(ingredient.capitalize())
    print('Difficulty Level: ', recipe['difficulty'])

def all_ingredients():
    print('Ingredients Required Across All Recipes')
    print('---------------------------------------')
    ingredients_list.sort()
    for ingredient in ingredients_list:
        print(ingredient.capitalize())

all_ingredients()
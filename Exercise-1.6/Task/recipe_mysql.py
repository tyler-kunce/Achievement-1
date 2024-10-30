import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'cf-python',
    passwd = 'password'
)

cursor = conn.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS task_database;')
cursor.execute('USE task_database;')
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
               id INT PRIMARY KEY AUTO_INCREMENT,
               name VARCHAR(50),
               ingredients VARCHAR(255),
               cooking_time INT,
               difficulty VARCHAR(20)
               );''')

def main_menu(conn, cursor):
    while True:
        print('-Main Menu-')
        print('1. Create a new recipe')
        print('2. Search for recipes by an ingredient')
        print('3. Update a recipe in the database')
        print('4. Delete a recipe from the database')
        print('5. Exit')

        user_input = input('Enter your option (1-5): ')

        if user_input == '1':
            create_recipe(conn, cursor)
        elif user_input == '2':
            search_recipe(conn, cursor)
        elif user_input == '3':
            update_recipe(conn, cursor)
        elif user_input == '4':
            delete_recipe(conn, cursor)
        elif user_input == '5':
            print('Exiting')
            conn.commit()
            cursor.close()
            conn.close()
            break
        else:
            print('You entered an invalid option. Try again')

def calculate_difficulty(cooking_time, ingredients):
    ingredient_len = len(ingredients)
    if cooking_time < 10 and ingredient_len < 4:
        return "Easy"
    elif cooking_time < 10 and ingredient_len >= 4:
        return "Medium"
    elif cooking_time >= 10 and ingredient_len < 4:
        return "Intermediate"
    elif cooking_time >= 10 and ingredient_len >= 4:
        return "Hard"

def create_recipe(conn, cursor):
    name = input('What\'s the name of your recipe? ')
    cooking_time = int(input('How long does it take to cook? '))
    ingredients = [str(ingredients) for ingredients in input('What\'s used to make it (separated with commas)? ').split(', ')]
    difficulty = calculate_difficulty(cooking_time, ingredients)

    ingredients_py = ', '.join(ingredients)

    sql = ('INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s);')
    val = (name, ingredients_py, cooking_time, difficulty)

    cursor.execute(sql, val)

    conn.commit()

    print("You added a Recipe")

def search_recipe(conn, cursor):
    cursor.execute('SELECT ingredients FROM Recipes;')
    results = cursor.fetchall()
    
    all_ingredients = set()
    for ingredient in results:
        ingredients = ingredient[0]
        all_ingredients.update(ingredients.split(', '))

    print("Ingredients from which to choose:")
    for ind, ingredient in enumerate(sorted(all_ingredients), start=1):
        print(f'{ind}, {ingredient}')
    
    user_input = int(input('For which ingredient\'s respective number do you choose? ')) - 1
    search_ingredient = sorted(all_ingredients)[user_input]

    search_sql = ('SELECT * FROM Recipes WHERE ingredients LIKE %s;')
    val = ('%' + search_ingredient + '%',)

    cursor.execute(search_sql, val)

    results = cursor.fetchall()

    for row in results:
        print(row)

def update_recipe(conn, cursor):
    cursor.execute('SELECT * FROM Recipes;')
    recipes = cursor.fetchall()

    print('Available recipes:')
    recipe_map = {}

    for index, recipe in enumerate(recipes, start=1):
        ingredients_list = recipe[2].split(', ')
        ingredients_cap = [ingredient.capitalize() for ingredient in ingredients_list]
        ingredients_cap_str = ', '.join(ingredients_cap)

        print(f'ID: {index}, Name: {recipe[1]}')
        print(f'''Ingredients: {ingredients_cap_str}
        Cooking Time: {recipe[3]}
        Difficulty: {recipe[4]}
        ''')

        recipe_map[index] = recipe[0]

    user_input = int(input("Enter the ID of the recipe you wish to update: "))
    recipe_id = recipe_map.get(user_input)

    if recipe_id is None:
        print('Invalid selection.')
        return

    column_update = input("Enter the column you wish to update - name, ingredients, or cooking_time: ")

    new_val = None
    if column_update == 'name':
        new_val = input('Enter the new recipe name: ')
        update_sql = 'UPDATE Recipes SET name = %s WHERE id = %s;'
        cursor.execute(update_sql, (new_val, recipe_id))
    elif column_update == 'ingredients':
        new_val = [str(new_val) for new_val in input('What\'s used to make it (separated with commas)? ').split(', ')]
        ingredients_py = ', '.join(new_val)
        update_sql = 'UPDATE Recipes SET ingredients = %s WHERE id = %s;'
        cursor.execute(update_sql, (ingredients_py, recipe_id))
    elif column_update == 'cooking_time':
        new_val = int(input('Enter the updated cooking time (in minutes): '))
        update_sql = 'UPDATE Recipes SET cooking_time = %s WHERE id = %s;'
        cursor.execute(update_sql, (new_val, recipe_id))
    else:
        print('That\'s not a column.')
        return
    
    if column_update in ['ingredients', 'cooking_time']:
        cursor.execute('SELECT cooking_time, ingredients FROM Recipes WHERE id = %s;', (recipe_id,))
        recipe = cursor.fetchone()
        new_difficulty = calculate_difficulty(int(recipe[0]), recipe[1].split(', '))
        update_sql = 'UPDATE Recipes SET difficulty = %s WHERE id = %s;'
        cursor.execute(update_sql, (new_difficulty, recipe_id))

    conn.commit()
    print('You have successfully updated the Recipe.')

def delete_recipe(conn, cursor):
    cursor.execute('SELECT id, name FROM Recipes;')
    recipes = cursor.fetchall()

    print('List of Recipes:')
    for recipe in enumerate(recipes, start=1):
        print(f'ID: {recipe[0]}, Name: {recipe[1]}')
    
    recipe_id = int(input('Enter the ID of the Recipe you wish to delete: '))

    delete_sql = 'DELETE FROM Recipes WHERE id = %s;'
    cursor.execute(delete_sql, (recipe_id,))

    conn.commit()
    print('You have successfully deleted the Recipe.')

main_menu(conn, cursor)
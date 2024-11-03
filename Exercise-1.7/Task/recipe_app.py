from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://cf-python:password@localhost/task_database')

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Recipe(Base):
    __tablename__ = 'final_recipes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return '<Recipe ID: ' + str(self.id) + '-' + self.name + '-' + self.difficulty + '>'

    def __str__(self):
        return (
            f'''{'-'*25}
            Recipe: {self.name}
            Cooking Time: {self.cooking_time} minutes
            Ingredients: {self.ingredients}
            Difficulty: {self.difficulty}
            {'-'*25}'''
        )
    
    def calculate_difficulty(self):
        ingredient_len = len(self.return_ingredients_as_list())
        if self.cooking_time < 10 and ingredient_len < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and ingredient_len >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and ingredient_len < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and ingredient_len >= 4:
            self.difficulty = "Hard"
    
    def return_ingredients_as_list(self):
        if self.ingredients:
            return self.ingredients.split(', ')
        else:
            return []
        
Base.metadata.create_all(engine)

def create_recipe():
    name = input('What\'s the name of the recipe you\'re cooking (50 characters or less, please)? ')
    if len(name) > 50 or not all(char.isalnum() or char.isspace() for char in name):
        print('That is an invalid recipe name :(')
        return
    
    ingredients = []
    num_ingredients = int(input('How many ingredients are we using? '))
    for i in range(num_ingredients):
        ingredient = input('Provide an ingredient, please: ')
        ingredients.append(ingredient)
    ingredients_str = ', '.join(ingredients)

    cooking_time = input('How long will this take (in minutes)? ')
    if not cooking_time.isnumeric():
        print('That is an invalid cooking time :(')
        return
    
    recipe_entry = Recipe(
        name = name,
        ingredients = ingredients_str,
        cooking_time = int(cooking_time)
    )
    recipe_entry.calculate_difficulty()

    session.add(recipe_entry)
    session.commit()
    print('Recipe was successfully added!')

def view_all_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print('There are no recipes')
        return
    for recipe in recipes:
        print(recipe)

def search_by_ingredients():
    recipe_count = session.query(Recipe).count()
    if recipe_count == 0:
        print('There are no recipes')
        return
    
    results = session.query(Recipe.ingredients).all()

    all_ingredients = []

    for result in results:
        ingredients_list = result[0].split(', ')
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    print('\nList of Ingredients:')
    for index, ingredient in enumerate(all_ingredients, start=1):
        print(f'{index} | {ingredient}')
    user_ingredients = input('Enter the corresponding number for the ingredients you would like to see (space-separated): ').split()

    if not all(
        index.isnumeric() and 0 < int(index) <= len(all_ingredients)
        for index in user_ingredients
    ):
        print('That is not a valid selection :(')
        return
    search_ingredients = [all_ingredients[int(index) - 1] for index in user_ingredients]
    
    conditions = []
    for ingredient in search_ingredients:
        like_term = f'%{ingredient}%'
        conditions.append(Recipe.ingredients.like(like_term))
    
    results = session.query(Recipe).filter(*conditions).all()

    if results:
        for recipe in results:
            print(recipe)
    else:
        print('There are no recipes with the ingredients you selected')

def edit_recipe():
    recipe_count = session.query(Recipe).count()
    if recipe_count == 0:
        print('There are no recipes')
        return
    
    results = session.query(Recipe.id, Recipe.name).all()

    print('\nList of Recipes:')
    for recipe in results:
        print(f'ID: {recipe.id} | Name: {recipe.name}')

    user_id = input('Enter the ID of the recipe we\'re updating: ')
    if not user_id.isnumeric() or int(user_id) not in [recipe.id for recipe in results]:
        print('That is not a valid Recipe ID. Select a option from the list provided.')
        return
    
    recipe_to_edit = session.query(Recipe).filter_by(id=int(user_id)).one()

    print(f'''
          1. Recipe Name: {recipe_to_edit.name}
          2. Ingredients: {recipe_to_edit.ingredients}
          3. Cooking Time: {recipe_to_edit.cooking_time} minutes
        ''')

    column_to_edit = input('Enter the number corresponding to the component of the recipe you would like to edit (1, 2, or 3): ')
    if column_to_edit not in ['1', '2', '3']:
        ('That is not a valid selection :(')
        return
    
    if column_to_edit == '1':
        new_name = input('Enter a new name for the recipe: ')
        if len(new_name) > 50 or not all(char.isalnum() or char.isspace() for char in new_name):
            print('That is an invalid recipe name :(')
            return
        recipe_to_edit.name = new_name

    elif column_to_edit == '2':
        new_ingredients = []
        num_ingredients = int(input('How many ingredients are we using? '))

        for i in range(num_ingredients):
            ingredient = input('Provide an ingredient, please: ')
            new_ingredients.append(ingredient)

        recipe_to_edit.ingredients = ', '.join(new_ingredients)

    elif column_to_edit == '3':
        new_time = input('Enter the new cooking time (in minutes): ')
        if not new_time.isnumeric():
            print('That is an invalid cooking time :(')
            return
        
        recipe_to_edit.cooking_time = int(new_time)

    recipe_to_edit.calculate_difficulty()

    session.commit()
    print('Recipe was successfully updated!')

def delete_recipe():
    recipe_count = session.query(Recipe).count()
    if recipe_count == 0:
        print('There are no recipes')
        return

    results = session.query(Recipe.id, Recipe.name).all()

    print('\nList of Available Recipes:')
    for recipe in results:
        print(f'ID: {recipe.id} | Name: {recipe.name}')

    user_id = input('Enter the ID of the recipe we\'re deleting: ')
    if not user_id.isnumeric() or int(user_id) not in [recipe.id for recipe in results]:
        print('That is not a valid Recipe ID. Select a option from the list provided.')
        return

    recipe_to_delete = session.query(Recipe).filter_by(id=user_id).one()

    confirmation = input(f'Are you certain want to delete {recipe_to_delete.name}? Enter "yes" or "no": ').lower()

    if confirmation == 'no':
        print('You have opted not to delete the Recipe')
        return
    elif confirmation == 'yes':
        session.delete(recipe_to_delete)
        session.commit()
        print('Recipe was successfully deleted!')
    else:
        print('Invalid option. You must enter "yes" or "no".')
        return

def main_menu():
    while True:
        print(f'''
            -Main Menu-
            1. Create a new recipe
            2. View all recipes
            3. Search for recipes by ingredients
            4. Update a recipe in the database
            5. Delete a recipe from the database
            Or type "quit" to exit the app
        ''')

        user_input = input('\nEnter your option (1-5): ')

        if user_input == '1':
            create_recipe()
        elif user_input == '2':
            view_all_recipes()
        elif user_input == '3':
            search_by_ingredients()
        elif user_input == '4':
            edit_recipe()
        elif user_input == '5':
            delete_recipe()
        elif user_input == 'quit':
            print('Exiting')
            session.commit()
            session.close()
            engine.dispose()
            break            
        else:
            print('You entered an invalid option. Try again')

main_menu()
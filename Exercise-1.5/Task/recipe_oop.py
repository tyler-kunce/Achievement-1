class Recipe(object):
    all_ingredients = set()

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = int(0)
        self.difficulty = None
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cooking_time(self):
        return self.cooking_time
    
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    def get_ingredients(self):
        return self.ingredients
    
    def add_ingredients(self, *args):
        self.ingredients = args
        self.update_all_ingredients()

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in self.all_ingredients:
                self.all_ingredients.add(ingredient)

    def search_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            return True
        else:
            return False

    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        if self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        if self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        if self.cooking_time >= 10 and len(self.ingredients) >= 4:
            self.difficulty = "Hard"
        return self.difficulty
    
    def get_difficulty(self):
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    def __str__(self):
        output = "Name: " + self.name + \
            "\nCooking Time (in minutes): " + str(self.cooking_time) + \
            "\nIngredients: " + str(self.ingredients) + \
            "\nDifficulty: " + str(self.difficulty)
        return output
    
def recipe_search(data, search_term):
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)
    
tea = Recipe("Tea")
tea.add_ingredients("Water", "Tea leaves", "Sugar")
tea.set_cooking_time(5)
tea.get_difficulty()
print(tea)

coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee grounds", "Sugar", "Water")
coffee.set_cooking_time(5)
coffee.get_difficulty()
print(coffee)

cake = Recipe("Cake")
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla essence", "Flour", "Baking Powder", "Milk")
cake.set_cooking_time(50)
cake.get_difficulty()
print(cake)

smoothie = Recipe("Banana Smoothie")
cake.add_ingredients("Bananas", "Milk", "Peanut butter", "Sugar", "Ice cubes")
cake.set_cooking_time(5)
cake.get_difficulty()
print(smoothie)

recipes_list = [tea, coffee, cake, smoothie]

print("\nRecipes with Water:")
recipe_search(recipes_list, "Water")

print("\nRecipes with Sugar:")
recipe_search(recipes_list, "Sugar")

print("\nRecipes with Bananas:")
recipe_search(recipes_list, "Bananas")
import json


def validate_input(prompt, validator):
    while True:
        try:
            value = validator(input(prompt))
            return value
        except ValueError:
            print("Invalid input, please try again.")


def validate_int(value):
    return int(value)


def validate_choice(value):
    value = int(value)
    if value not in range(1, 5):
        raise ValueError
    return str(value)


def load_recipes():
    try:
        with open("recipes.json", "r") as f:
            recipes = json.load(f)
            if not recipes["recipes"]:
                print("No recipes in my belly")
            return recipes
    except (FileNotFoundError, json.JSONDecodeError):
        with open("recipes.json", "w") as f:
            recipes = {"recipes": []}
            json.dump(recipes, f, indent=4)
            return recipes


def save_recipes(recipes):
    try:
        with open("recipes.json", "w") as f:
            json.dump(recipes, f, indent=4)
    except IOError:
        print("Failed to save recipes to file.")

    try:
        with open("recipes.txt", "w") as f:
            for index, recipe in enumerate(recipes["recipes"]):
                f.write(f"{index + 1}. {recipe['name']}\n")
                f.write("Ingredients:\n")
                for ingredient in recipe["ingredients"]:
                    f.write(f"- {ingredient}\n")
                f.write("Steps:\n")
                for step in recipe["steps"]:
                    f.write(f"- {step}\n")
                f.write("\n")
    except IOError:
        print("Failed to save recipes to file.")


def display_recipe(recipe):
    if recipe:
        print("Name:", recipe.get("name"))
        print("Ingredients:")
        for ingredient in recipe.get("ingredients"):
            print(f"- {ingredient}")
        print("Steps:")
        for step in recipe.get("steps"):
            print(f"- {step}")
    else:
        print("Recipe not found.")


def view_recipe():
    name = input("Recipe: ")
    if not name:
        return display_all_recipes()
    recipes = load_recipes()
    for index, recipe in enumerate(recipes["recipes"]):
        if recipe.get("name") == name or str(index+1) == name:
            display_recipe(recipe)
            return
    print("That's not in my belly")


def add_recipe():
    name = input("Enter the name of the recipe: ")
    ingredients = []
    while True:
        ingredient = input("Enter an ingredient (leave blank to stop adding): ")
        if not ingredient:
            break
        ingredients.append(ingredient)
    steps = []
    while True:
        step = input("Enter a step (leave blank to stop adding): ")
        if not step:
            break
        steps.append(step)
    recipes = load_recipes()
    recipe = {"name": name, "ingredients": ingredients, "steps": steps}
    recipes["recipes"].append(recipe)
    recipe_index = len(recipes["recipes"])
    save_recipes(recipes)
    print(f"{recipe_index}. recipe added to my belly")


def display_all_recipes():
    recipes = load_recipes()
    if not recipes["recipes"]:
        print("No recipes in my belly")
        return
    for index, recipe in enumerate(recipes["recipes"]):
        print(f"{index + 1}. {recipe.get('name')}")
def main():
    version = "Pre-Release 4"
    print(f"# Version {version}")
    while True:
        print()
        print("What would you like to do?")
        print("1. View a recipe")
        print("2. Add a recipe")
        print("3. Display all recipes")
        print("4. Exit")
        choice = validate_input("Enter your choice (1-4): ", validate_choice)
        if choice == "1":
            view_recipe()
        elif choice == "2":
            add_recipe()
        elif choice == "3":
            display_all_recipes()
        elif choice == "4":
            print("Goodbye!")
            return
        else:
            print("That's not a valid choice, please try again")


if __name__ == "__main__":
    main()

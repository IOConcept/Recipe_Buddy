import json


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
    with open("recipes.json", "w") as f:
        json.dump(recipes, f, indent=4)


def display_recipe(recipe):
    print("Name:", recipe.get("name"))
    print("Ingredients:")
    for ingredient in recipe.get("ingredients"):
        print("-", ingredient)
    print("Steps:")
    for step in recipe.get("steps"):
        print("-", step)


def view_recipe():
    name = input("Enter the name of the recipe: ")
    if not name:
        return display_all_recipes()
    recipes = load_recipes()
    for recipe in recipes["recipes"]:
        if recipe.get("name") == name:
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
    recipes["recipes"].append({"name": name, "ingredients": ingredients, "steps": steps})
    save_recipes(recipes)
    print("1 recipe added to my belly")


def display_all_recipes():
    recipes = load_recipes()
    if not recipes["recipes"]:
        print("No recipes in my belly")
        return
    for recipe in recipes["recipes"]:
        print(recipe.get("name"))


def export_recipes():
    recipes = load_recipes()
    if not recipes["recipes"]:
        print("No recipes in my belly")
        return
    with open("recipes.txt", "w") as f:
        for recipe in recipes["recipes"]:
            f.write(f"Name: {recipe.get('name')}\n")
            f.write("Ingredients:\n")
            for ingredient in recipe.get("ingredients"):
                f.write(f"- {ingredient}\n")
            f.write("Steps:\n")
            for step in recipe.get("steps"):
                f.write(f"- {step}\n")
            f.write("\n")
    print("Recipes exported successfully")


def main():
    while True:
        print("Menu:")
        print("1. View Recipe")
        print("2. Add a recipe")
        print("3. Export Recipes")
        print("4. Display all recipes")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_recipe()
        elif choice == "2":
            add_recipe()
        elif choice == "3":
            export_recipes()
        elif choice == "4":
            display_all_recipes()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print("# Version 20.3 Beta 3")
    main()

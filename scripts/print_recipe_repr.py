import sys

if __name__ == "__main__":
    import recipe

    recipe_instance_name = sys.argv[1]

    recipe_instance = getattr(recipe, recipe_instance_name)

    print(recipe_instance)

import importlib
import sys


def get_instance(recipe_path, instance_name):
    spec = importlib.util.spec_from_file_location("recipe", cache_path)
    imported_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(imported_module)
    instance = getattr(imported_module, instance_name)
    return instance


if __name__ == "__main__":
    recipe_path, instance_name = sys.argv[1:3]
    instance = get_instance(recipe_path, instance_name)
    print(instance)

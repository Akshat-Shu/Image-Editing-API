import os
import importlib.util as import_util

def resolve_functions(folder_path) :
    # List all .py files in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.py')]

    all_functions = {}

    # Dynamically import each file and collect its functions
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        spec = import_util.spec_from_file_location(file_name, file_path)
        module = import_util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Collect all functions from the module
        for attr_name, attr_value in vars(module).items():
            if callable(attr_value):
                all_functions[attr_name] = attr_value

    return all_functions

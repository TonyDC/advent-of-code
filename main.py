import pkgutil
import importlib

import year_2024

def main():
    for _, module_name, _ in pkgutil.iter_modules(path=year_2024.__path__, prefix=year_2024.__name__ + '.'):
        module = importlib.import_module(f'{module_name}.main')
        print(module_name, module.main())

if __name__ == '__main__':
    main()
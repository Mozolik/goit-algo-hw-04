import sys
from pathlib import Path
from colorama import Fore, Style, init

def print_tree(path: Path, indent: int = 0):
    if path.is_dir():
        print(Fore.BLUE+" " * indent + path.name)
    else:
        print(Fore.GREEN + " " * indent + path.name)
    
    if path.is_dir():
        for child in path.iterdir():
            print_tree(child, indent + 2)

def main():
    if len(sys.argv) < 2:
        print("python module_4_3.py /шлях/до/вашої/директорії")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists() or not dir_path.is_dir():
        print(f"Каталог '{dir_path}' не існує або не є директорією.")
        sys.exit(1)

    print_tree(dir_path)


if __name__ == "__main__":
    main()


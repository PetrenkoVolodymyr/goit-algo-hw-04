# from pathlib import Path
import os
from colorama import Fore
import sys


def colored_dir(adress):
    try:
        # adress = Path(adress)

        for child in os.listdir(adress):
            if os.path.isdir(str(adress) + "\\" + child):
                print(f"{Fore.BLUE} [FOLDER] {child} {Fore.RESET}")
            else:
                print(f"{Fore.RED} [FILE] {child} {Fore.RESET}")

    except:
        print("Wrong adress")

# target_folder = "D:\Projects\HTML_CSS\HWks\goit-algo-hw-04"
target_folder = sys.path[0]
colored_dir(target_folder)
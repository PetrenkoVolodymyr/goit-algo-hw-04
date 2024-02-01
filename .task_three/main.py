from pathlib import Path
import os
from colorama import Fore
import sys


def colored_dir(path):
    print(sys.path)
    try:
        adress = Path(r"D:\Projects\HTML_CSS\HWks")

        for child in os.listdir(adress):
            if os.path.isdir(str(adress) + "\\" + child):
                print(f"{Fore.BLUE} [FOLDER] {child} {Fore.RESET}")
            else:
                print(f"{Fore.RED} [FILE] {child} {Fore.RESET}")

    except:
        print("Wrong adress")


path = "D:\Projects\HTML_CSS\HWks\goit-algo-hw-04"
colored_dir(path)
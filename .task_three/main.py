import pathlib
from pathlib import Path
import os
from colorama import Fore

def colored_dir(adress):
    try:
        for child in pathlib.Path(adress).iterdir():
            if os.path.isdir(child):
                print(f"{Fore.BLUE} [FOLDER] {Path(child).name} {Fore.RESET}")
            else:
                print(f"{Fore.RED} [FILE] {Path(child).name} {Fore.RESET}")

    except:
        print("Wrong adress")

target_folder = "D:\Projects\HTML_CSS\HWks"
colored_dir(target_folder)

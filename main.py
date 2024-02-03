import pathlib
from pathlib import Path
import os
from colorama import Fore
import sys

def colored_dir(adress):
    try:
        for child in pathlib.Path(adress).iterdir():
            if os.path.isdir(child):
                print(f"{Fore.BLUE} [FOLDER] {Path(child).name} {Fore.RESET}")
            else:
                print(f"{Fore.RED} [FILE] {Path(child).name} {Fore.RESET}")

    except:
        print("Wrong adress")

def main():
    folder = sys.path[0]
    path_folder = Path(folder)
    colored_dir(path_folder)

if __name__ == '__main__':
    main()










# import pathlib
# from pathlib import Path
# import os
# from colorama import Fore
# import sys

# def colored_dir(adress):
#     try:
#         for child in pathlib.Path(adress).iterdir():
#             if os.path.isdir(child):
#                 print(f"{Fore.BLUE} [FOLDER] {Path(child).name} {Fore.RESET}")
#             else:
#                 print(f"{Fore.RED} [FILE] {Path(child).name} {Fore.RESET}")

#     except:
#         print("Wrong adress")


# target_folder = "D:\Projects\HTML_CSS\HWks"
# colored_dir(target_folder)
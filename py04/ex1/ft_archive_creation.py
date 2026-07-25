#! /usr/bin/env python3

import typing
import sys


# ========================== Read and Save Function ===========================
# Open and read file, saving its content before closing
# ------------------------------------------------------
def ft_read_and_save(argv: list) -> str | None:
    if len(argv) == 0 or len(argv) > 1:
        print("Usage: ft_archive_creation.py <file>\n")
        sys.exit()

    print("======== 📁   Cyber Archives Recovery & Preservation 📁  ========\n")
    print(f"Accessing file '{argv[0]}'")

    try:
        file_object: typing.TextIO = open(argv[0])
        file_tmp = file_object.read()
        print("----------------\n")
        print(file_tmp)
        print("\n----------------")
        file_object.close()
        print(f"File '{argv[0]}' closed.")
        return file_tmp
    except OSError as e:  # Operating System Error
        print(f"Error opening file '{argv[0]}': {e}")
        return None


# ======================== Archive Creation Function ==========================
# Write and save file, if a name file is provided
# ------------------------------------------------------
def ft_archive_creation(file_tmp: str) -> None:
    # Separate whole text file by '\n', then we add '#', and we join again them
    lst_lines = file_tmp.splitlines()
    lst_lines_trans = [(line + '#') for line in lst_lines]
    file_trans = ("\n".join(lst_lines_trans)) + '\n'

    print("\nTransform data:")
    print("----------------\n")
    print(file_trans)
    print("----------------")

    new_file = input("Enter new file name (or empty): ")
    if new_file == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file}'")
    try:
        file_object: typing.TextIO = open(new_file, 'w')
        file_object.write(file_trans)
        file_object.close()
        print(f"Data saved in file '{new_file}'.\n")
        return
    except OSError as e:
        print(f"Error writing file '{new_file}': {e}")
        return


# ============================== Program Test ================================

if __name__ == "__main__":
    file_tmp = ft_read_and_save(sys.argv[1:])
    if file_tmp is not None:
        ft_archive_creation(file_tmp)

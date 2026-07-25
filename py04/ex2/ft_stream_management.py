#! /usr/bin/env python3

import typing
import sys


# ========================== Read and Save Function ===========================
# Open and read file, saving its content before closing
# ------------------------------------------------------
def ft_read_and_save(argv: list) -> str | None:
    if len(argv) == 0 or len(argv) > 1:
        print("[STDERR]❌ Usage: ft_stream_management.py <file>\n",
              file=sys.stderr)
        return None

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
        print(f"[STDERR]❌ Error opening file '{argv[0]}': {e}",
              file=sys.stderr)
        return None


# ======================== Stream Management Function =========================
# Write and save file, if a name file is provided
# ------------------------------------------------------
def ft_stream_management(file_tmp: str) -> None:
    # Separate whole text file by '\n', then we add '#', and we join again them
    lst_lines = file_tmp.splitlines()
    lst_lines_trans = [(line + '#') for line in lst_lines]
    file_trans = ("\n".join(lst_lines_trans)) + '\n'

    print("\nTransform data:")
    print("----------------\n")
    print(file_trans)
    print("----------------")

    print("Enter new file name (or empty): ", end="", flush=True)
    # Flush »»» Forces buffer text from print appearing on the moment
    new_file = sys.stdin.readline().strip()  # capture stdin and remove '\n'
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
        print(f"[STDERR]❌ Error writing file '{new_file}': {e}",
              file=sys.stderr)
        return


# ============================== Program Test ================================

if __name__ == "__main__":
    file_tmp = ft_read_and_save(sys.argv[1:])
    if file_tmp is not None:
        ft_stream_management(file_tmp)

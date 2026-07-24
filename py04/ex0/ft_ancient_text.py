#! /usr/bin/env python3

import typing
import sys


# ====================== Parse Errors Function Creation =======================

def ft_ancient_text(argv: list) -> None:
    if len(argv) == 0 or len(argv) > 1:
        print("Usage: ft_ancient_text.py <file>\n")
        sys.exit()

    print("================ 📁  Cyber Archives Recovery 📁  =================\n")
    print(f"Accessing file '{argv[0]}'")

    try:
        file_object: typing.TextIO = open(argv[0])  # Input/Output object type
        print("----------------\n")
        print(file_object.read())  # Stream or File object
        print("\n----------------")
        file_object.close()
        print(f"File '{argv[0]}' closed.")
        return
    except OSError as e:  # Operating System Error
        print(f"Error opening file '{argv[0]}': {e}")
        return


# ============================== Program Test ================================

if __name__ == "__main__":
    ft_ancient_text(sys.argv[1:])

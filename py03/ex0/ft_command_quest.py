#! /usr/bin/env python3

import sys


# ======================= Command Function Creation ==========================

def ft_command_quest(argv: list) -> None:
    total_argv = len(argv)

    print("============ 💻  Command Quest 💻 ============")
    print(f"Program name: {argv[0]}")
    if total_argv == 1:
        print("⭕ No arguments provided!")
    else:
        i = 1
        print(f"Arguments received: {len(argv[1:])}")
        for arg in argv[1:]:  # Skip the first list element : until the end
            print(f"✅ Argument {i}: {arg}")
            i += 1
    print(f"Total sys arguments: {total_argv}\n")


# ============================== Program Test ================================

if __name__ == "__main__":
    argv = sys.argv
    ft_command_quest(argv)

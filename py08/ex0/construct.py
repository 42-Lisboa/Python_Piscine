#! /usr/bin/env python3

import sys
import os
import site


def main(is_venv: bool) -> None:
    if not is_venv:
        print("MATRIX STATUS: You're still plugged in - Pill 🟦\n")
        print(f"Current Python: {sys.executable}")  # Where python.exe stands
        print("Virtual Environment: None detected\n")
        print("⚠️  WARNING: You're in the global environment! ⚠️")
        print("👾 The machines can see everything you install. 👾\n")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\\Scripts\\activate # On Windows\n\n"
              "Then run this program again.")
    else:
        env_path = os.environ["VIRTUAL_ENV"]
        # VIRTUAL_ENV - var that holds the env path when it's activated
        env_name = os.path.basename(env_path)  # shows last path element
        package_path = site.getsitepackages()[0]  # packages locations
        print("MATRIX STATUS: Welcome to the construct - Pill 🟥\n")
        print(f"Current Python: {sys.executable}")  # Where python.exe stands
        print(f"Virtual Environment name: {env_name}")
        print(f"Virtual Environment path: {env_path}\n")
        print("✅ SUCCESS: You're in an isolated environment! ✅")
        print("📦 Safe to install packages without "
              "affecting the global system. 📦\n")
        print("Package installation path:")
        print(f"{package_path}")


if __name__ == "__main__":
    is_venv = (sys.base_prefix != sys.prefix)
    # base_prefix - always shows the path for the main global python installed
    # prefix - where python install new packages
    #  is the same as base if there's no venv activated
    main(is_venv)

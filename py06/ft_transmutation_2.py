import alchemy


print("====================== ⚛️  Transmutation 2 ⚛️  ======================")

print("Import alchemy package only")

print("Testing lead to gold: ", end="")
print(f"{alchemy.lead_to_gold()}\n")


# Import Explanation:
"""
This script imports only the top-level 'alchemy' package. It demonstrates the
power of clean architecture: it relies on the main alchemy/__init__.py file to
route, collect, and expose the lead_to_gold function from deep within its sub-
directories, providing the simplest and cleanest access for the end user.
"""

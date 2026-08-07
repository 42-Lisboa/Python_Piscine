import alchemy.transmutation.recipes


print("====================== ⚛️  Transmutation 0 ⚛️  ======================")

print("Using module alchemy/transmutation/recipes.py directly")

print("Testing lead to gold: ", end="")
print(f"{alchemy.transmutation.recipes.lead_to_gold()}\n")


# Import Explanation:
"""
This script uses an absolute import path targeting the specific module
(recipes.py) directly. By explicitly stating the full path, it bypasses the
package's internal routing, meaning Python goes straight down the directory
tree to the exact file without needing any __init__.py files to expose the
lead_to_gold function.
"""

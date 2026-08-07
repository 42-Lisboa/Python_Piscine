import alchemy.transmutation


print("====================== ⚛️  Transmutation 1 ⚛️  ======================")

print("Import transmutation sub-package directly")

print("Testing lead to gold: ", end="")
print(f"{alchemy.transmutation.lead_to_gold()}\n")


# Import Explanation:
"""
This script imports the 'transmutation' sub-package rather than a specific
file. It stops at the folder level and relies entirely on the
alchemy/transmutation/__init__.py file to act as a bridge, which successfully
pulls and exposes the lead_to_gold function from the hidden recipes module.
"""

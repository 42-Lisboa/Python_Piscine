print("=============== 💥 Kaboom 1💥 ===============")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - ❌ THIS WILL RAISE THE EXCEPTION: ImportError\n")

# The simple import try will cause an ImportError for Circular Import
from alchemy.grimoire.dark_spellbook import dark_spell_record  # noqa: ignore
print(dark_spell_record("Avada Kedrava", "arsenic, spirit, dark, soul"))

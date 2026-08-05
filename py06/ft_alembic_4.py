import alchemy


print("========================= ⚗️  Alembic 4 ⚗️  =========================")

print("Accessing the alchemy module using 'import alchemy'")

try:
    print("Testing create_air: ", end="")
    print(f"{alchemy.create_air()}\n")
    print("Testing create_earth: ", end="")
    print(f"{alchemy.create_earth()}\n")  # type: ignore
except Exception as e:
    print(f"Error - {e} ❌\n")

#! /usr/bin/env python3


# ========================= Manipulate File Function ==========================
# Open and do the action on the file: read or write content on it
# ----------------------------------------------------------------
def secure_archive(file_name: str, action: str = 'r', content="") -> tuple:
    try:
        if action == "r":
            with open(file_name, action) as file:  # Here we access the file
                data = file.read()  # Second element of tuple if 'r'
            return (True, data)
        elif action == "w":
            data = "Content successfully written to file"  # If 'w'
            with open(file_name, action) as file:  # Here we access the file
                file.write(content)
            return (True, data)
        else:
            data = f"Invalid action: '{action}'. Use 'r' or 'w'."
            return (False, data)

    except Exception as e:
        return (False, str(e))  # We gotta transform execption object


# ======================= Test Secure Archive Function ========================

def test_secure_archive() -> None:
    print("============ 🛡️   Cyber Archives Security 🛡️  ============\n")

    # Test0 - Non Existent File
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(f"❌ {secure_archive('non_existent.txt', 'r')}")

    # Test1 - Inaccessible File - chmod -r ex3/inaccessible.txt
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(f"❌ {secure_archive('inaccessible.txt', 'r')}")

    # Test2 - Regular File
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(f"✅ {secure_archive('ancient_fragment.txt', 'r')}")

    # Test3 - Writing in Regular File
    content = 'Brasil\nis gonna be\nHexa in 2030! 🏖️'
    print("\nUsing 'secure_archive' to write previous content to the file:")
    print(f"✅ {secure_archive('ancient_fragment.txt', 'w', content)}")

    # BonusTest - Read Transformed Regular File
    print("\nUsing 'secure_archive' to read from the new regular file:")
    print(f"🔄️ {secure_archive('ancient_fragment.txt')}")


# ============================== Program Test ================================

if __name__ == "__main__":
    test_secure_archive()

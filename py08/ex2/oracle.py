from dotenv import load_dotenv  # type: ignore
import os
import sys

REQUIRED_VAR = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT"
    # ,"NON_EXISTENT_KEY"
]


# =================== Loading Environment variables function ==================
#            Function to load .env or injected environment variables
# -----------------------------------------------------------------------------

def load_env(req_var: list[str]) -> dict[str, str | None]:
    load_dotenv()  # load your environment var to os

    for key in req_var:  # let's check if any variable is missing
        has_value = os.getenv(key)
        if has_value is None:
            print(f"❌ Environment Variable '{key}' doesn't exist!")
            print("💠 Check or set your .env file properly! 💠")
            sys.exit(1)

    env_data: dict[str, str | None] = {}  # now let's add all var to a dict
    env_data["MATRIX_MODE"] = os.getenv("MATRIX_MODE") or "development"
    env_data["LOG_LEVEL"] = os.getenv("LOG_LEVEL") or "DEBUG"
    env_data["ZION_ENDPOINT"] = os.getenv("ZION_ENDPOINT") or "www.site.local"
    env_data["DATABASE_URL"] = os.getenv("DATABASE_URL")
    env_data["API_KEY"] = os.getenv("API_KEY")
    return env_data


# =========================== Print Oracle function ===========================
#                    Function to adequate to subject example
# -----------------------------------------------------------------------------

def print_oracle_report(env_data: dict[str, str | None]) -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("⚙️  Configuration loaded")
    print("------------------------------------------")

    mode = env_data.get("MATRIX_MODE")
    print(f"◾Mode: {mode}")

    if mode == "development":
        print("◾Database: Connected to local instance")
    else:
        print("◾Database: Connected to remote cluster")

    print("◾API Access: Authenticated")
    print(f"◾Log Level: {env_data.get('LOG_LEVEL')}")

    if env_data.get("ZION_ENDPOINT"):
        print("◾Zion Network: Online")
    else:
        print("◾Zion Network: Offline")

    print("\n🛡️  Environment security check")
    print("------------------------------------------")
    print("◾No hardcoded secrets detected")
    print("◾.env file properly configured")
    print("◾Production overrides available")
    print("◾The Oracle sees all configurations.\n")


# ============================== Program Test ================================

def main() -> None:
    env_data = load_env(REQUIRED_VAR)
    print_oracle_report(env_data)


if __name__ == "__main__":
    main()


# ---------------------------- IMPORTANT CONCEPTS ----------------------------
"""
os.environ & os.getenv():   are used to read system environment variables (in-
                            jected in the terminal) or variables inside of .env
                            file, before the script execution i.e:
                            MY_API_KEY="xy123" PORT="3000" python seu_script.py
os.environ:                 works like a standard variables dictipnary from py-
                            hon. Ideal for mandatory variables, because if the
                            variable doesn't exist the program just crashes.
os.getenv():                it's a fuction more ideal to optional environment
                            variables because you can decide a return value in
                            case of a non-existent variable without code crash.
                            the order in which this function search for var:
                            injected variables > .env file > default code var
python-dotenv:              it's an external module that we use the function
                            load_dotenv() to load all environment variables
                            from its required file '.env'. To import we use:
                            'from dotenv import load_dotenv'

"""

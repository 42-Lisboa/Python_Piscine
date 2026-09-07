from dotenv import load_dotenv





# ---------------------------- IMPORTANT CONCEPTS ----------------------------
"""
os.environ & os.getenv():   are used to read environment variables injected in
                            the terminal or inside of .env file, before the
                            script execution i.e:
                            MY_API_KEY="xy123" PORT="3000" python seu_script.py
os.environ:                 works like a standard variables dictipnary from py-
                            hon. Ideal for mandatory variables, because if the
                            variable doesn't exist the program just crashes.
os.getenv():                it's a fuction more ideal to optional environment
                            variables because you can decide a return value in
                            case of a non-existent variable without code crash.
python-dotenv:              it's an external module that we use the function
                            load_dotenv() to load all environment variables
                            from its required file '.env'. To import we use:
                            'from dotenv import load_dotenv'

"""

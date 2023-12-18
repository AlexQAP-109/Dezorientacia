import os
from dotenv import load_dotenv

class Env():
    load_dotenv()

    valid_login = os.getenv("valid_login")
    valid_pass = os.getenv("valid_pass")

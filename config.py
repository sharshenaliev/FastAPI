from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_DB = 'hackaton'#os.environ.get("POSTGRES_DB")
POSTGRES_USER = 'postgres'#os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = ''#os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = 'localhost'#os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = '5432'#os.environ.get("POSTGRES_PORT")
SECRET_KEY = os.environ.get("SECRET_KEY")

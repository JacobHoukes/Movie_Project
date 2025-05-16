from dotenv import load_dotenv
import os

from movie_app import MovieApp
from storage.storage_json import StorageJson

load_dotenv()
api_key = os.getenv("API_KEY")

storage = StorageJson("data/data.json")
app = MovieApp(storage=storage, api_key=api_key)
app.run()

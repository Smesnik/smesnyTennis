from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = "https://tennisapi1.p.rapidapi.com/api/tennis/"
TIMEOUT = 20
BASE_DIR = Path(__file__).parent.parent



HEADERS = {
	"x-rapidapi-key": os.getenv("RAPID_API_KEY"),
	"x-rapidapi-host": "tennisapi1.p.rapidapi.com",
	"Content-Type": "application/json"
}
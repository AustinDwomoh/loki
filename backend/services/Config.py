
from logging import WARN
import os
import pathlib
from dotenv import load_dotenv
load_dotenv()
BASE_DIR = pathlib.Path(__file__).parent
LOG_BASE_DIR = BASE_DIR / "errors"

BOT_MODE = os.getenv("BOT_MODE", "production").strip().lower()
IS_PRODUCTION = BOT_MODE == "production"
IS_TESTING = BOT_MODE == "testing"
class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", 5432))
    DB_NAME = os.getenv("DB_NAME", "mydatabase")
    DB_USER = os.getenv("DB_USER", "myuser")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "mypassword")
    LOG_BASE_DIR = LOG_BASE_DIR

class LogTypes:
    ERROR = "error"
    WARN = "warn"
    INFO = "info"
    TASK = "task"
    FATAL = "fatal"
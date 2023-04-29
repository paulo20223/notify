import os
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = os.path.join(BASE_DIR, "config")

env = environ.FileAwareEnv()
TG_BOT_TOKEN = env.str('TG_BOT_TOKEN')
TG_NOTIFY_CHANNEL = env.str('TG_NOTIFY_CHANNEL')
DEBUG = env.bool("DEBUG")
ORIGINS = env.list("ORIGINS")

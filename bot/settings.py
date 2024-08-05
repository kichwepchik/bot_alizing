from dotenv import load_dotenv
from dataclasses import dataclass
import os

@dataclass
class Bots:
    bot_token: str
    admin_id: int

@dataclass
class Settings:
    bots: Bots

def get_settings(path: str):
    # Получим абсолютный путь к файлу .env
    absolute_path = os.path.abspath(path)
    if not os.path.exists(absolute_path):
        raise FileNotFoundError(f"The .env file at path '{absolute_path}' does not exist.")

    load_dotenv(absolute_path)

    bot_token = os.getenv("TOKEN")
    admin_id = os.getenv("ADMIN_ID")

    if bot_token is None:
        raise ValueError("The TOKEN variable is not set in the .env file.")
    if admin_id is None:
        raise ValueError("The ADMIN_ID variable is not set in the .env file.")

    return Settings(
        bots=Bots(
            bot_token=bot_token,
            admin_id=int(admin_id),
        )
    )

# Assuming .env file is located in the root of your project directory (same as where you run the script)
settings = get_settings('../.env')  # Обратите внимание на правильный путь
print(settings)

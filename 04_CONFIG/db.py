import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"D:\pycharm projects\test.env", override=True)

engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

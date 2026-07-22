from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

password = quote_plus(os.getenv("DB_PASSWORD"))
# f"{os.getenv('DB_USER')}:{password}@"  # USE This only line of code below in Password section
# f"{os.getenv('DB_PASSWORD')}@"

DATABASE_URL = (
    f"mysql+pymysql://"
    f"{os.getenv('DB_USER')}:{password}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)

meta = MetaData()

conn = engine.connect()

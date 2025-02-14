from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Import config
from app.utility.config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

# Database URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Database engine
engine = create_engine(DATABASE_URL)

# Local Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Models Base
Base = declarative_base()
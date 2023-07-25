from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config
from .models import Base

engine = create_engine(config.db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

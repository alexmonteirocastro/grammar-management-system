from app.core.settings import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

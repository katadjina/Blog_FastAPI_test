from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi-practice.db"
 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()


## get_db function -> Context manager provides a session from the session factory
## ensures that the session is closed after its usage. It's especially useful in the context of FastAPI.
def get_db():
    db = SessionLocal()  ## creates a new session instance. 
    try:
        yield db #yields the session back to the caller (typically a FastAPI route). 
    finally:
        db.close()    
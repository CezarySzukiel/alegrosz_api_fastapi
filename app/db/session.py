from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm.decl_api import declarative_base

SQLALCHEMY_DATYABASE_URL = "sqlite:///./inventory.db"
engine = create_engine(SQLALCHEMY_DATYABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
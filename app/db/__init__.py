from sqlalchemy.orm import session

from app.db.models import product, location, inventory
from app.db.session import engine, Base

def init_db():
    """Create the database tables."""
    Base.metadata.create_all(bind=engine)
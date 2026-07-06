from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings

# ==========================================================
# SQLAlchemy Engine
# ==========================================================

engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    future=True,
    pool_pre_ping=True,
)

# ==========================================================
# Session Factory
# ==========================================================

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

# ==========================================================
# Base Class for all ORM Models
# ==========================================================

from app.models.base import Base


# ==========================================================
# Dependency
# ==========================================================

def get_db():
    """
    Database dependency for FastAPI.
    Automatically closes the session after request.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

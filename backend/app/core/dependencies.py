from typing import Generator


def get_db() -> Generator:
    """Yield a DB session. Wire this up to your SQLAlchemy SessionLocal."""
    raise NotImplementedError

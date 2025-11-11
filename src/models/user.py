from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column

from src.models.base import Base



class User(Base):
    """
    CREATE TABLE IF NOT EXISTS users
    (
      id SERIAL PRIMARY KEY,
      name VARCHAR,
      email VARCHAR UNIQUE
    );
    """

    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    email = mapped_column(String, unique=True, index=True)
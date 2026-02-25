from typing import Optional
from eo_lib.domain.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class ProductionType(Base):
    """
    Production Type Entity.
    Categorizes different types of research production (e.g., BOOK, SOFTWARE).
    """
    __tablename__ = "production_types"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)

    def __init__(self, name: str, id: Optional[int] = None, **kwargs):
        self.id = id
        self.name = name

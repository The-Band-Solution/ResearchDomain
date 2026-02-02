from typing import Optional

from eo_lib.domain.base import Base
from sqlalchemy import Column, Integer, String

from research_domain.domain.mixins import SerializableMixin


class Language(Base, SerializableMixin):
    """
    Language Catalog Entity.
    """
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)

    def __init__(self, name: str, id: Optional[int] = None, **kwargs):
        self.id = id
        self.name = name

from typing import Optional

from eo_lib.domain.base import Base
from sqlalchemy import Column, Float, Integer, String, Text

from research_domain.domain.mixins import SerializableMixin


class Fellowship(Base, SerializableMixin):
    """
    Fellowship Model.

    Represents a scholarship or funding for a student in an advisorship.
    """

    __tablename__ = "fellowships"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    value = Column(Float, nullable=False)

    def __init__(
        self,
        name: str,
        value: float,
        description: Optional[str] = None,
        id: Optional[int] = None,
        **kwargs,
    ):
        """
        Initializes a new Fellowship instance.
        """
        super().__init__(**kwargs)
        self.id = id
        self.name = name
        self.value = value
        self.description = description

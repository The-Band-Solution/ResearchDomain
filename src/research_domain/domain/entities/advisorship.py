from datetime import date
from typing import Optional

from eo_lib.domain.entities import Initiative
from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship

from research_domain.domain.mixins import SerializableMixin


class Advisorship(Initiative, SerializableMixin):
    """
    Advisorship Model.

    A specialized Initiative that links a Student and a Supervisor (both represented as Person).
    An Advisorship has a team composed of a student and a supervisor.
    Uses Joined Table Inheritance from initiatives.
    """

    __tablename__ = "advisorships"

    id = Column(Integer, ForeignKey("initiatives.id"), primary_key=True)
    student_id = Column(Integer, ForeignKey("persons.id"), nullable=True)
    supervisor_id = Column(Integer, ForeignKey("persons.id"), nullable=True)
    fellowship_id = Column(Integer, ForeignKey("fellowships.id"), nullable=True)

    # Relationships
    student = relationship("Person", foreign_keys=[student_id])
    supervisor = relationship("Person", foreign_keys=[supervisor_id])
    fellowship = relationship("Fellowship", foreign_keys=[fellowship_id])

    @property
    def is_volunteer(self) -> bool:
        """Returns True if the advisorship is voluntary (no fellowship)."""
        return self.fellowship is None and self.fellowship_id is None

    def __init__(
        self,
        name: str,
        student_id: Optional[int] = None,
        supervisor_id: Optional[int] = None,
        fellowship_id: Optional[int] = None,
        student: Optional[object] = None,
        supervisor: Optional[object] = None,
        fellowship: Optional[object] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        description: Optional[str] = None,
        status: str = "active",
        id: Optional[int] = None,
        **kwargs,
    ):
        super().__init__(
            name=name,
            description=description,
            status=status,
            start_date=start_date,
            end_date=end_date,
            id=id,
            **kwargs,
        )
        self.student_id = student_id
        self.supervisor_id = supervisor_id
        self.fellowship_id = fellowship_id
        self.student = student
        self.supervisor = supervisor
        self.fellowship = fellowship

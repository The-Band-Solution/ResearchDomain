from datetime import date
from typing import Optional
import enum

from eo_lib.domain.entities import Initiative
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from research_domain.domain.mixins import SerializableMixin


class AdvisorshipType(enum.Enum):
    SCIENTIFIC_INITIATION = "Scientific Initiation"
    JUNIOR_SCIENTIFIC_INITIATION = "Junior Scientific Initiation"
    UNDERGRADUATE_THESIS = "Undergraduate Thesis"
    MASTER_THESIS = "Master Thesis"
    PHD_THESIS = "PhD Thesis"
    POST_DOCTORATE = "Post-Doctorate"


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
    institution_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)
    
    type = Column(Enum(AdvisorshipType), nullable=True)
    program = Column(String(500), nullable=True)
    defense_date = Column(Date, nullable=True)
    
    cancelled = Column(Boolean, default=False)
    cancellation_date = Column(Date, nullable=True)

    # Relationships
    student = relationship("Person", foreign_keys=[student_id])
    supervisor = relationship("Person", foreign_keys=[supervisor_id])
    fellowship = relationship("Fellowship", foreign_keys=[fellowship_id])
    institution = relationship("Organization", foreign_keys=[institution_id])

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
        institution_id: Optional[int] = None,
        type: Optional[AdvisorshipType] = None,
        program: Optional[str] = None,
        defense_date: Optional[date] = None,
        student: Optional[object] = None,
        supervisor: Optional[object] = None,
        fellowship: Optional[object] = None,
        institution: Optional[object] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        cancelled: bool = False,
        cancellation_date: Optional[date] = None,
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
        self.institution_id = institution_id
        self.type = type
        self.program = program
        self.defense_date = defense_date
        self.student = student
        self.supervisor = supervisor
        self.fellowship = fellowship
        self.institution = institution
        self.cancelled = cancelled
        self.cancellation_date = cancellation_date


from uuid import uuid4

from app.core.base import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Case(Base):
    __tablename__ = "cases"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4(), index=True)
    language_id = Column(UUID(as_uuid=True), ForeignKey("languages.id"))
    name_english = Column(String, index=True)
    name_native = Column(String, index=True)
    question = Column(String)

    # Relationships
    language = relationship("Language", back_populates="cases")
    word_forms = relationship("WordForm", back_populates="case")

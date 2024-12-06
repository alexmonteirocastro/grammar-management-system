from uuid import uuid4

from app.core.base import Base
from sqlalchemy import Column, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .enums import WordGender, WordNumber, WordType


class WordPattern(Base):
    __tablename__ = "word_patterns"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4(), index=True)
    language_id = Column(UUID(as_uuid=True), ForeignKey("languages.id"))
    base_word = Column(String, index=True)
    type = Column(Enum(WordType))  # type: ignore
    number = Column(Enum(WordNumber))  # type: ignore
    gender = Column(Enum(WordGender))  # type: ignore

    # Relationships
    language = relationship("Language", back_populates="word_patterns")
    word_forms = relationship("WordForm", back_populates="word_pattern")


class WordForm(Base):
    __tablename__ = "word_forms"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4(), index=True)
    word_pattern_id = Column(UUID(as_uuid=True), ForeignKey("word_patterns.id"))
    case_id = Column(UUID(as_uuid=True), ForeignKey("cases.id"))
    form = Column(String)

    # Relationships
    word_pattern = relationship("WordPattern", back_populates="word_forms")
    case = relationship("Case", back_populates="word_forms")

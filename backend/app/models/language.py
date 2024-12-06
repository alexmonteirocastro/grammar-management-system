from uuid import uuid4

from app.core.base import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Language(Base):
    __tablename__ = "languages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4(), index=True)
    name = Column(String, unique=True, index=True)
    code = Column(String(2), unique=True, index=True)

    # Relationships
    cases = relationship("Case", back_populates="language")
    word_patterns = relationship("WordPattern", back_populates="language")

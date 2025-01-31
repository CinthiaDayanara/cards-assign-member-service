from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.models.database import Base

class Member(Base):
    __tablename__ = "card_members"

    id = Column(Integer, primary_key=True, index=True)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    user_id = Column(Integer, nullable=False)

    card = relationship("Card", back_populates="members")

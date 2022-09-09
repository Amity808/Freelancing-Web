from datetime import datetime

from sqlalchemy import Column, String, Float, Boolean, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship

from .base_class import Base


class Users(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(Date)
    #profile = relationship("Profile", back_populates="users")
    #gig = relationship("Gig", back_populates="users")

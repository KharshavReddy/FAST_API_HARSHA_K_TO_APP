from sqlalchemy import Column, Integer, String 
from .database import Base


# Create Model
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    description = Column(String)
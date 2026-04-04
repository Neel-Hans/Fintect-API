from sqlalchemy.orm import Column, Integer, String, Boolean
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True)
    email= Column(String, unique=True, index=True)
    hashed_password= Column(String)
    role = Column(String) #admin/analyst/viewer
    is_active = Column(Boolean, default=True)



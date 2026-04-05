from sqlalchemy import Column, Integer, String, Boolean,DateTime
from sqlalchemy import Enum as SqlEnum
from datetime import datetime
from app.db.base import Base
from app.enums.enums import UserRole


class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True, index=True)
    email= Column(String, unique=True, index=True, nullable=False)
    name=Column(String, nullable=False)
    hashed_password= Column(String, nullable=False)
    role = Column(SqlEnum(UserRole), nullable=False, default=UserRole.VIEWER)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    def __repr__(self):
        return f"<User {self.id} {self.email}"



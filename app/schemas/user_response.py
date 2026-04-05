from pydantic import BaseModel, EmailStr
from app.enums.enums import UserRole
from datetime import datetime

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

''' model_config helps FastAPI serialize SQLAlchemy model into response schema'''







from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.register_login_schema import RegisterRequest, LoginRequest, TokenResponse
from app.schemas.user_response import UserResponse
from app.core.dependencies import get_db
from app.services.auth_service import register_user,login_user
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix='/auth', tags=["Auth"])

@router.post("/register",response_model=UserResponse)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    return register_user(db, data.name, data.email, data.password)


@router.post("/token", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token = login_user(db, form_data.username, form_data.password)
    return {"access_token": token, "token_type": "bearer"}
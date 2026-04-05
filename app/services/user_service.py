from fastapi import HTTPException

from app.models.user import User
from app.enums.enums import UserRole
from sqlalchemy.orm import Session

def update_user_role(db: Session, user_id: int, new_role: UserRole, current_user: User): #to update the user role for admin
    user = db.query(User).filter(User.id == user_id).first()



    if not user:
        raise HTTPException(404, "User not found")

    #prevent self-demotion so that admin doesn't lock the whole system
    if user.id == current_user.id:
        raise HTTPException(400, "Cannot change your own role")

    user.role = new_role
    db.commit()
    db.refresh(user)

    return user

def get_all_user(db:Session): #get the list of all users for admin
    return db.query(User).all()


def manage_user_status(db:Session, user_id: int, is_active: bool, current_user: User):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(404, "User not found")

    user.is_active = is_active

    db.commit()
    db.refresh(user)

    return user

def delete_user_service(db: Session, user_id: int, is_deleted: bool):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(404, "User not found")


    user.is_deleted = is_deleted

    db.commit()
    db.refresh(user)

    return user


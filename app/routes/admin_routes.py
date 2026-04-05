from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.enums.enums import UserRole
from app.core.dependencies import get_db, get_current_user
from app.core.rbac import require_role
from app.services.user_service import update_user_role, get_all_user, manage_user_status
from app.schemas.user_response import UserResponse

router = APIRouter(prefix="/admin/users", tags=["Admin - user Management"])
'''
The " require_role" function in rbac.py calls get_curent_user internally
hence the role check happens at the route level, separating business logic which 
in the service'''

@router.get("/", response_model=list[UserResponse])
def get_all_users_route(db:Session = Depends(get_db),
                        current_user: User = Depends(require_role([UserRole.ADMIN]))):
    return get_all_user(db)

@router.patch("/{user_id}/role",response_model=UserResponse)
def update_user_role_route(
        user_id: int,
        new_role: UserRole,
        db:Session = Depends(get_db),
        current_user: User = Depends(require_role([UserRole.ADMIN])) # <- ADMIN ONLY
):
    return update_user_role(db, user_id, new_role, current_user)

@router.patch("/{user_id}/status",response_model=UserResponse)
def manage_user_status_route(
        user_id: int,
        is_active: bool,
        db: Session = Depends(get_db),
        current_user: User = Depends(require_role([UserRole.ADMIN]))
):
    return manage_user_status(db, user_id, is_active, current_user)

'''
**How to call these:**

GET    /admin/users/                          → get all users
PATCH  /admin/users/1/role?new_role=admin     → change role
PATCH  /admin/users/1/status?is_active=false  → deactivate user
'''



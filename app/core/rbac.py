from fastapi import Depends, HTTPException
from app.enums.enums import UserRole
from app.core.dependencies import get_current_user

def require_role(roles: list):
    def checker(user=Depends(get_current_user)):
        if user.role not in roles:
            raise HTTPException(status_code=403, detail=f"Requires role: {[r.value for r in roles]}")

        return user

    return checker
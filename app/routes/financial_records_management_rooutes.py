'''
The routes in this file are for mananging the financial records
through create, update, view and delete services

The admin has access to all the services implement through RBAC
the analyst and viewer can only access the view service.

'''

from fastapi import APIRouter, Depends
from fastapi import Query #for paginated resonses
from typing import Optional
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.user import User
from app.enums.enums import UserRole,RecordCategory,RecordType
from app.core.dependencies import get_db
from app.core.rbac import require_role
from app.services.financial_records_management import create_financial_record_service, update_financial_record_service,delete_financial_record,get_financial_records_service
from app.schemas.financial_record_schema import FinancialRecordCreate, FinancialRecordUpdate, FinancialRecordResponse


router = APIRouter(prefix='/records/management', tags=["Financial Records Management"])

'''
The " require_role" function in rbac.py calls get_curent_user internally
hence the role check happens at the route level, separating business logic which 
in the service'''


@router.post("/create",summary="Create a new financial record -> Only Admin",response_model=FinancialRecordResponse,status_code=201)
def create_financial_record_route(data:FinancialRecordCreate,
                                  db: Session = Depends(get_db),
                                  current_user: User = Depends(require_role([UserRole.ADMIN]))
                                  ):

    return create_financial_record_service(data,db)

@router.get("/",summary="Get all financial records with filters pagination -> All ")
def get_financial_records_route(
        db: Session = Depends(get_db),
        current_user: User = Depends(require_role([UserRole.ANALYST, UserRole.ADMIN, UserRole.VIEWER])),
        page: int = Query(default=1, ge=1),
        page_size: int = Query(default=10, ge=1, le=100),
        customer_name: Optional[str] = Query(default=None),
        mobile_number: Optional[str] = Query(default=None),
        category: Optional[RecordCategory] = Query(default=None),
        type: Optional[RecordType] = Query(default=None),
        date_from: Optional[datetime] = Query(default=None),
        date_to: Optional[datetime] = Query(default=None)


):
    return get_financial_records_service(
        db=db,
        page=page,
        page_size=page_size,
        customer_name=customer_name,
        mobile_number=mobile_number,
        category=category,
        type=type,
        date_from=date_from,
        date_to=date_to
    )

'''

Key things:
- `Query(default=1, ge=1)` — page must be >= 1 
- `Query(default=10, ge=1, le=100)` — page size between 1 and 100 
- `require_role([UserRole.ANALYST, UserRole.ADMIN])` — both analyst and admin can view 
- No `response_model` since we return a custom pagination dict

**How to call it:**
```
GET /records/?page=1&page_size=10
GET /records/?customer_name=arjun
GET /records/?mobile_number=9876543210
GET /records/?category=salary&type=income
GET /records/?date_from=2024-01-01&date_to=2024-03-31'''

@router.delete("/{record_id}/delete",summary="Delete a financial record -> Only admin")
def delete_financial_record_service(
        record_id:int,
        db: Session = Depends(get_db),
        current_user: User = Depends(require_role([UserRole.ADMIN]))
):
    return delete_financial_record(record_id,db)


@router.patch("/{record_id}", summary="Updating a financial record -> Only admin")
def update_financial_record_route(
        record_id: int,
        data: FinancialRecordUpdate,
        db: Session = Depends(get_db),
        current_user: User = Depends(require_role([UserRole.ADMIN]))
):
    return update_financial_record_service(record_id,data,db)




from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.enums.enums import UserRole, RecordCategory, RecordType
from app.core.dependencies import  get_db
from app.core.rbac import require_role
from app.services.dashboard_summary import  (
    get_financial_summary_service,
    get_summary_customer_service,
    category_wise_summary,
    recent_activity_customer,
    monthly_trend_service,
)

from fastapi.responses import StreamingResponse
from app.services.export_service import export_all_records_csv



router = APIRouter(prefix="/dashboard/financial_summary", tags=["Dashboard Summaries"])


@router.get("/", summary="Get the overall financial summary")
def get_financial_summary_route(db: Session = Depends(get_db),
                                 current_user: User = Depends(require_role([UserRole.ANALYST, UserRole.ADMIN]))):
    return get_financial_summary_service(db)


@router.get("/customer/summary/{mobile_number}", summary="Get financial summary per customer")
def get_summary_customer_route(mobile_number: str,
                               db: Session = Depends(get_db),
                               current_user: User = Depends(require_role([UserRole.ANALYST, UserRole.ADMIN]))
                               ):
    return get_summary_customer_service(db, mobile_number)

@router.get("/category/{category}",summary="Get financial summary by category")
def get_category_wise_summary_route(category: RecordCategory,
                                    db: Session = Depends(get_db),
                                    current_user: User = Depends(require_role([UserRole.ANALYST, UserRole.ADMIN]))):
    return category_wise_summary(db, category)


@router.get("/customer/recent_activity/{mobile_number}", summary="Recent activity of a customer")
def recent_activity_customer_route(mobile_number: str,
                                   db: Session = Depends(get_db),
                                   current_user: User = Depends(require_role([UserRole.ANALYST, UserRole.ADMIN]))):
    return recent_activity_customer(db, mobile_number)



@router.get("/trends/monthly", summary="Monthly income vs expense trends")
def monthly_trend_route(db: Session = Depends(get_db),
                        current_user: User = Depends(require_role([UserRole.ANALYST, UserRole.ADMIN]))):
    return monthly_trend_service(db)


@router.get("/export/csv", summary="Export all financial records as CSV")
def export_csv_route(
        db:Session = Depends(get_db),
        current_user: User = Depends(require_role([UserRole.ANALYST, UserRole.ADMIN]))
):
    output = export_all_records_csv(db)

    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=financial_records.csv"}
    )










from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes.admin_routes import router as admin_router
from app.routes.auth_router import router as auth_router
from app.scripts.create_tables import create_tables
from app.scripts.seed_admin import seed_admin
from app.scripts.seed_financial import seed_financial_records
from app.routes.financial_records_management_rooutes import router as financial_records_management_rouutes
from app.routes.dashboard_summary_routes import router as dashboard_routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print("Creating tables...")
        create_tables()
    except Exception as e:
        print(f"Create tables error: {e}")

    try:
        print("Seeding admin...")
        seed_admin()
    except Exception as e:
        print(f"Seed admin error: {e}")

    try:
        print("Seeding financial records...")
        seed_financial_records()
    except Exception as e:
        print(f"Seed financial records error: {e}")

    yield


app = FastAPI(
    title="Fintech API",
    version="1.0.0",
    lifespan=lifespan
)

''' app.inlcude_router - expects the api router object without importing the whole module'''
app.include_router(auth_router)
app.include_router(admin_router)

app.include_router(financial_records_management_rouutes)
app.include_router(dashboard_routes)


@app.get("/")
def health_check():
    return {"status": "ok"}



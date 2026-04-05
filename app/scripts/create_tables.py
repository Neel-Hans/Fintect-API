from app.db.session import engine
from app.db.base import Base
from app.models.user import User
from app.models.financial_record import FinancialRecord

def create_tables():
    print("creating tables.....")
    Base.metadata.create_all(bind=engine)
    print("Tables created")



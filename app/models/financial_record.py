from sqlalchemy import Column, Integer, String, Float, DateTime, Text,Boolean
from sqlalchemy import Enum as SqlEnum

from datetime import datetime
from app.db.base import Base
from app.enums.enums import RecordType, RecordCategory


class FinancialRecord(Base):
    __tablename__ = "financial_records"

    id = Column(Integer, primary_key=True, index=True)
    mobile_number = Column(String, nullable=False, index=True) #for quick search based on phone number
    customer_name=Column(String, nullable=False)
    amount= Column(Float, nullable=False)
    type = Column(SqlEnum(RecordType), nullable=False)
    category= Column(SqlEnum(RecordCategory), nullable=False)
    date= Column(DateTime, nullable=False)
    notes=Column(Text, nullable=True)
    is_deleted=Column(Boolean, default=False)
    created_at=Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at=Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


    def __repr__(self):
        return f"<FinancialRecord {self.id} {self.type} {self.amount}"

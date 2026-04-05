import sys
import os
import json
from datetime import datetime

current_dir = os.path.dirname(__file__) #app/scripts/
project_root = os.path.abspath(os.path.join(current_dir, "../..")) #project root

sys.path.append(project_root)


from app.db.session import SessionLocal
from app.models.financial_record import FinancialRecord
from app.enums.enums import RecordType, RecordCategory


def seed_financial_records():
    db= SessionLocal()

    try:
        existing = db.query(FinancialRecord).first()
        if existing:
            print("Financial Records already exists")
            return

        json_path = os.path.join(project_root, "data/financial_records.json")
        print(f"JSON path: {json_path}")
        print(f"File exists: {os.path.exists(json_path)}")
        with open(json_path, "r") as f:
            records = json.load(f)

        for record in records:
            financial_record = FinancialRecord(
                customer_name=record["customer_name"],
                mobile_number=record["mobile_number"],
                amount=record["amount"],
                type= RecordType(record["type"]),
                category=RecordCategory(record["category"]),
                date=datetime.fromisoformat(record["date"]),
                notes=record.get("notes")
            )

            db.add(financial_record)

        db.commit()
        print(f"{len(records)} financial records seeded successfully")

    except Exception as e:
        db.rollback()
        print(f"error seeding financial records: {e} ")

    finally:
        db.close()

if __name__ == "__main__":
    seed_financial_records()


''''''
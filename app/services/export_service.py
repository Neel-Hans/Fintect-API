'''
This function can be used by analysts and admins to export all  the data
in a csv format for further analysis using different libraries like pandas, matplotlib

'''


import csv
import io
from sqlalchemy.orm import Session
from app.models.financial_record import FinancialRecord

def export_all_records_csv(db: Session) -> io.StringIO:
    records = db.query(FinancialRecord).filter(
        FinancialRecord.is_deleted == False
    ).order_by(FinancialRecord.date.desc()).all()


    output = io.StringIO
    writer = csv.writer(output)

    writer.writerow([
        "id","mobile_number","amount", "type",
        "category", "date", "notes"
    ])

    #data rows
    for r in records:
        writer.writerow([
            r.id,
            r.mobile_number,
            r.amount,
            r.type.value,
            r.category.value,
            r.date,
            r.notes
        ])
    output.seek(0)

    return output
import sys
import os

#fix import path( so script can find app/)
#fintech_project/app/scripts
current_dir = os.path.dirname(__file__)

#/fintech_poject/app/scripts/../.. = /project
project_root = os.path.abspath(os.path.join(current_dir, "../.."))

#adds /project to python's search path
sys.path.append(project_root)


from app.core.security import hash_password
from app.enums.enums import UserRole
from app.db.session import SessionLocal
from app.models.user import User

def seed_admin():
    db= SessionLocal()

    try:
        existing = db.query(User).filter(User.email=="neel.hans97@gmail.com").first()

        if existing:
            print("Admin already exists")
            return

        admin = User(
            name="Neel Hans",
            email="neel.hans97@gmail.com",
            hashed_password=hash_password("admin123"),
            role=UserRole.ADMIN
        )

        db.add(admin)
        db.commit()
        db.refresh(admin)
        print("Admin created successfully")

    except Exception as e:
        db.rollback()
        print(f"Error creating admin: {e}")


    finally:
        db.close()

if __name__ == "__main__":
    seed_admin()



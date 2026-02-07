from database import db

async def create_indexes():
    try:
        await db.attendance.create_index(
            [("employee_id", 1), ("date", 1)],
            unique=True
        )
        await db.employees.create_index("employee_id", unique=True)
    except Exception as e:
        print("⚠️ Index creation skipped:", e)


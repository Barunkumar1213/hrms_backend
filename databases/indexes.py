from database import db

async def create_indexes():
    # Unique attendance per employee per date
    await db.attendance.create_index(
        [("employee_id", 1), ("date", 1)],
        unique=True
    )

    # Faster queries
    await db.attendance.create_index("employee_id")
    await db.attendance.create_index("date")

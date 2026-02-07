from fastapi import APIRouter , HTTPException
from models.attendance import Attendance
from database import db
from utils.serializers import serialize_docs
from pymongo.errors import DuplicateKeyError

router = APIRouter()

@router.post("/")
async def mark_attendance(att: Attendance):
    data = att.dict()
    data["date"] = data["date"].isoformat()

    try:
        await db.attendance.insert_one(data)
        return {"message": "Attendance marked"}
    except DuplicateKeyError:
        raise HTTPException(
            status_code=400,
            detail="Attendance already marked for this employee on this date"
        )

@router.get("/{employee_id}")
async def get_attendance(employee_id: str):
    records = await db.attendance.find(
                {"employee_id": employee_id}
            ).to_list(100)
    return serialize_docs(records)
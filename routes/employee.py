from fastapi import APIRouter, HTTPException , Query
from models.employee import Employee
from database import db
from utils.serializers import serialize_docs
import math

router = APIRouter()

@router.post("/")
async def add_employee(emp: Employee):
    existing = await db.employees.find_one(
        {"employee_id": emp.employee_id}
    )
    if existing:
        raise HTTPException(status_code=400, detail="Employee already exists")

    await db.employees.insert_one(emp.dict())
    return {"message": "Employee added successfully"}

@router.get("/")
async def list_employees(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
):
    skip = (page - 1) * limit

    cursor = db.employees.find().skip(skip).limit(limit)
    employees = await cursor.to_list(length=limit)

    total = await db.employees.count_documents({})
    total_pages = math.ceil(total / limit)

    return {
        "data": serialize_docs(employees),
        "meta": {
            "page": page,
            "limit": limit,
            "total": total,
            "total_pages": total_pages,
        },
    }

@router.delete("/{employee_id}")
async def delete_employee(employee_id: str):
    result = await db.employees.delete_one(
        {"employee_id": employee_id}
    )
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {"message": "Employee deleted"}

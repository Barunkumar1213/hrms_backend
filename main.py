from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.employee import router as employee_router
from routes.attendance import router as attendance_router
from databases.indexes import create_indexes

app = FastAPI(title="HRMS Lite API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://hrms-frontend-ecru-zeta.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    try:
        await create_indexes()
        print("✅ Database indexes ensured")
    except Exception as e:
        # VERY IMPORTANT: never crash the app on startup
        print("⚠️ Index creation skipped:", e)

app.include_router(employee_router, prefix="/employees", tags=["Employees"])
app.include_router(attendance_router, prefix="/attendance", tags=["Attendance"])

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(
    title='Xử lý đăng kí học viên',
    description='Xử lý đăng kí học viên',
    version='1.0.0'
)

students = [
    {
        "full_name": "Nguyen Minh",
        "email": "canikissyou212007@gmail.com",
        "age": 18,
        "course": "python",
        "phone": "0123456789"
    }
]

class Student(BaseModel):
    full_name: str = Field(..., min_length=3)
    email: EmailStr
    age: int
    course: str
    phone: str
    
@app.post("/students")
def create_student(student: Student):
    for item in students:
        if item["email"] == student.email:
            raise HTTPException(
                status_code=400,
                detail='Email đã tồn tại trong hệ thống'
            )
            
    students.append(student.model_dump())
    
    return {
        "message": "Thêm học viên thành công",
        "student": student
    }

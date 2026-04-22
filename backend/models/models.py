from pydantic import BaseModel
from typing import Optional, List

class LessonCreate(BaseModel):
    name: str
    teacher: str
    grade: Optional[str] = None

class StudentReport(BaseModel):
    lesson_id: str
    student_id: str
    attention: int
    understand: int
    weak_points: List[str]
    suggest: str
# ===== wheel_spec.py =====
from fastapi import APIRouter, Depends, Query
from typing import Optional
from sqlalchemy.orm import Session
from app import models, schemas, database
from app.dependencies import get_current_user

router = APIRouter(prefix="/wheel", tags=["Wheel Specification"])

@router.post("/")
def create_wheel_spec(
    wheel: schemas.WheelSpecificationCreate,
    db: Session = Depends(database.get_db),
    current_user: str = Depends(get_current_user)
):
    
    print("Received Wheel Spec Data:", wheel.model_dump())

    new_spec = models.WheelSpecification(
        formNumber=wheel.formNumber,
        submittedBy=wheel.submittedBy,
        submittedDate=wheel.submittedDate,
        fields=wheel.fields.model_dump()
    )
    db.add(new_spec)
    db.commit()
    db.refresh(new_spec)

    return {
        "data": {
            "formNumber": new_spec.formNumber,
            "submittedBy": new_spec.submittedBy,
            "submittedDate": str(new_spec.submittedDate),
            "status": "Saved"
        },
        "message": "Wheel specification submitted successfully.",
        "success": True
    }

@router.get("/")
def get_all_specs(
    formNumber: Optional[str] = Query(None),
    submittedBy: Optional[str] = Query(None),
    submittedDate: Optional[str] = Query(None),
    db: Session = Depends(database.get_db),
    current_user: str = Depends(get_current_user)
):
    query = db.query(models.WheelSpecification)

    if formNumber:
        query = query.filter(models.WheelSpecification.formNumber == formNumber)
    if submittedBy:
        query = query.filter(models.WheelSpecification.submittedBy == submittedBy)
    if submittedDate:
        query = query.filter(models.WheelSpecification.submittedDate == submittedDate)

    specs = query.all()

    return {
        "data": specs,
        "message": "Filtered wheel specification forms fetched successfully.",
        "success": True
    }


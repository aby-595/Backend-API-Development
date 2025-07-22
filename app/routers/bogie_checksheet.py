from fastapi import APIRouter, Depends, Query
from typing import Optional
from sqlalchemy.orm import Session
from datetime import date
from app import models, schemas, database
from app.dependencies import get_current_user

router = APIRouter(prefix="/bogie", tags=["Bogie Checksheet"])


# ✅ Recursive serializer that handles date inside nested dicts/lists
def serialize_dates(obj):
    if isinstance(obj, dict):
        return {k: serialize_dates(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [serialize_dates(item) for item in obj]
    elif isinstance(obj, date):
        return obj.isoformat()
    else:
        return obj


@router.post("/")
def create_bogie_checksheet(
    form: schemas.BogieChecksheetCreate,
    db: Session = Depends(database.get_db),
    current_user: str = Depends(get_current_user)
):
    # ✅ Prevent duplicate formNumber
    existing = db.query(models.BogieChecksheet).filter_by(formNumber=form.formNumber).first()
    if existing:
        return {
            "success": False,
            "message": f"Form with number {form.formNumber} already exists.",
            "data": None
        }

    new_form = models.BogieChecksheet(
        formNumber=form.formNumber,
        inspectionBy=form.inspectionBy,
        inspectionDate=form.inspectionDate,
        bogieDetails=serialize_dates(form.bogieDetails.model_dump()),
        bogieChecksheet=serialize_dates(form.bogieChecksheet.model_dump()),
        bmbcChecksheet=serialize_dates(form.bmbcChecksheet.model_dump())
    )
    db.add(new_form)
    db.commit()
    db.refresh(new_form)

    return {
        "data": {
            "formNumber": new_form.formNumber,
            "inspectionBy": new_form.inspectionBy,
            "inspectionDate": str(new_form.inspectionDate),
            "status": "Saved"
        },
        "message": "Bogie checksheet submitted successfully.",
        "success": True
    }


@router.get("/")
def get_all_forms(
    formNumber: Optional[str] = Query(None),
    inspectionBy: Optional[str] = Query(None),
    inspectionDate: Optional[str] = Query(None),
    db: Session = Depends(database.get_db),
    current_user: str = Depends(get_current_user)
):
    query = db.query(models.BogieChecksheet)

    if formNumber:
        query = query.filter(models.BogieChecksheet.formNumber == formNumber)
    if inspectionBy:
        query = query.filter(models.BogieChecksheet.inspectionBy == inspectionBy)
    if inspectionDate:
        query = query.filter(models.BogieChecksheet.inspectionDate == inspectionDate)

    forms = query.all()

    # Convert SQLAlchemy model objects to dict and serialize nested dates
    data = []
    for form in forms:
        form_dict = {
            "formNumber": form.formNumber,
            "inspectionBy": form.inspectionBy,
            "inspectionDate": form.inspectionDate.isoformat(),
            "bogieDetails": serialize_dates(form.bogieDetails),
            "bogieChecksheet": serialize_dates(form.bogieChecksheet),
            "bmbcChecksheet": serialize_dates(form.bmbcChecksheet)
        }
        data.append(form_dict)

    return {
        "data": data,
        "message": "Filtered bogie checksheet forms fetched successfully.",
        "success": True
    }

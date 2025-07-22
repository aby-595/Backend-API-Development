from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models, database
from app.auth import jwt_handler
from passlib.context import CryptContext
from fastapi import Body

router = APIRouter(
    prefix="/api/users",  
    tags=["Authentication"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ===== REGISTER =====
@router.post("/register")
def register_user(user: schemas.UserRegister, db: Session = Depends(database.get_db)):
    existing_user = db.query(models.User).filter(models.User.mobile == user.mobile).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Mobile already registered")

    hashed_password = pwd_context.hash(user.password)
    new_user = models.User(
        name=user.name,
        mobile=user.mobile,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}

# ===== LOGIN =====
@router.post("/login", response_model=schemas.Token)
def login(user: schemas.UserLogin = Body(...), db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.mobile == user.phone).first()
    if not db_user or not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid mobile or password")

    token = jwt_handler.create_access_token(data={"sub": db_user.mobile})
    return {"access_token": token, "token_type": "bearer"}


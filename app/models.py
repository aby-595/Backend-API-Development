from sqlalchemy import Column, Integer, String, Date, DateTime, JSON
from app.database import Base
from datetime import datetime

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"
    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, unique=True, nullable=False)
    submittedBy = Column(String, nullable=False)
    submittedDate = Column(Date, nullable=False)
    fields = Column(JSON, nullable=False)

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheet"
    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, unique=True, nullable=False)
    inspectionBy = Column(String, nullable=False)
    inspectionDate = Column(Date, nullable=False)
    bogieDetails = Column(JSON, nullable=False)
    bogieChecksheet = Column(JSON, nullable=False)
    bmbcChecksheet = Column(JSON, nullable=False)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    mobile = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)




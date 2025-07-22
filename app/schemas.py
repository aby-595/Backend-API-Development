from pydantic import BaseModel
from typing import Optional
from datetime import date

# === WHEEL SCHEMA ===
class WheelFields(BaseModel):
    axleBoxHousingBoreDia: float
    bearingSeatDiameter: float
    condemningDia: float
    intermediateWWP: float
    lastShopIssueSize: float
    rollerBearingBoreDia: float
    rollerBearingOuterDia: float
    rollerBearingWidth: float
    treadDiameterNew: float
    variationSameAxle: float
    variationSameBogie: float
    variationSameCoach: float
    wheelDiscWidth: float
    wheelGauge: int
    wheelProfile: str

class WheelSpecificationCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: WheelFields


# === BOGIE SCHEMA ===
class BogieDetails(BaseModel):
    bogieNo: str
    makerYearBuilt: str
    incomingDivDate: str
    deficitComponents: str
    dateOfIoh: date

    class Config:
        orm_mode = True

class BogieChecksheetFields(BaseModel):
    axleGuide: str
    bogieFrameCondition: str
    bolster: str
    bolsterSuspensionBracket: str
    lowerSpringSeat: str

    class Config:
        orm_mode = True

class BMBCChecksheetFields(BaseModel):
    adjustingTube: str
    cylinderBody: str
    pistonTrunnion: str
    plungerSpring: str

    class Config:
        orm_mode = True

class BogieChecksheetCreate(BaseModel):
    formNumber: str
    inspectionBy: str
    inspectionDate: date
    bogieDetails: BogieDetails
    bogieChecksheet: BogieChecksheetFields
    bmbcChecksheet: BMBCChecksheetFields


# === USER & TOKEN ===
class UserRegister(BaseModel):
    name: str
    mobile: str
    password: str

class UserLogin(BaseModel):
    phone: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    mobile: Optional[str] = None


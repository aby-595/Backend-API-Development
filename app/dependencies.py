from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.schemas import TokenData

# Constants used for encoding/decoding JWTs
SECRET_KEY = "bmw"
ALGORITHM = "HS256"

# ✅ Must match your login path (as defined in auth.py)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        # Decode JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        mobile: str = payload.get("sub")
        if mobile is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token: subject (mobile) not found",
            )
        return mobile
    except JWTError as e:
        print("JWT Decode Error:", str(e))  # Debugging line (remove in production)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

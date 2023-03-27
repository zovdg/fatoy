from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from datetime import timedelta
from fastapi import status, HTTPException
from typing import Union

from app.db.session import get_db
from app.core.hashing import Hashing
from app.schemas.tokens import Token
from app.db.repository.login import get_user
from app.core.security import create_access_token
from app.core.config import settings

from app.db.models.users import User

from jose import JWTError, jwt


router = APIRouter()


def authenticate_user(username: str, password: str, db: Session) -> Union[bool, User]:
    user = get_user(username=username, db=db)
    print(user)
    if not user:
        return False
    if not Hashing.verify_password(password, user.hashed_password):
        return False
    return user


@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


oauth2_schema = OAuth2PasswordBearer(tokenUrl="/login/token")


def get_current_user_from_token(
    token: str = Depends(oauth2_schema), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        print("username/email extracted is", username)
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(username=username, db=db)
    if user is None:
        raise credentials_exception
    return user

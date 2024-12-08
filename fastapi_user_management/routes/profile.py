"""Token provider endpoint for JWT."""

from datetime import timedelta
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import EmailStr
from sqlalchemy.orm import Session

from fastapi_user_management import crud
from fastapi_user_management.config import SETTINGS
from fastapi_user_management.core.database import get_db
from fastapi_user_management.models.user import UserModel, UserStatusValues
from fastapi_user_management.schemas.auth import Token, TokenData
from fastapi_user_management.schemas.user import UserBase
from fastapi_user_management.routes.auth import get_current_active_user

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal Server Error"},
    },
)

@router.get("/profile", response_model=UserBase)
async def get_user_profile(
    current_user: Annotated[UserBase, Depends(get_current_active_user)],
) -> UserBase:
    """Endpoint to get the current user's profile.

    Args:
        current_user (Annotated[UserBase, Depends]: current user obtained from the token.

    Returns:
        UserBase: current user profile information.
    """
    # Returning the current user's profile
    return current_user

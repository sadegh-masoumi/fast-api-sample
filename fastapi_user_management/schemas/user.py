"""Module to define User schemas."""
from pydantic import BaseModel, EmailStr

from fastapi_user_management.models.user import UserStatusValues
from fastapi_user_management.schemas.role import RoleBase


class UserBase(BaseModel):
    """Base Schema for users."""

    fullname: str | None = None
    username: EmailStr | None = None
    status: UserStatusValues | None = None
    roles: list[RoleBase] | None = None
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    """Schema use for login request."""

    username: EmailStr
    password: str
    class Config:
        orm_mode = True


class BaseUserCreate(UserBase):
    """Schema to create new user."""

    fullname: str
    username: EmailStr
    password: str | None = None
    roles: list[RoleBase]
    class Config:
        orm_mode = True


class UserCreate(BaseUserCreate):
    """Schema to create pre-defined users."""

    fullname: str
    username: EmailStr
    password: str
    roles: list[RoleBase]
    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    """Schema to update user password."""

    new_password: str
    new_password_confirm: str

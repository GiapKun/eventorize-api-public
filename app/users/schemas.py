from datetime import datetime
from typing import List, Optional

from core.schemas import EmailStr, PhoneStr, UrlStr
from pydantic import BaseModel, Field, field_validator

from .config import settings
from .exceptions import ErrorCode as UserErrorCode


class RegisterRequest(BaseModel):
    fullname: str
    email: EmailStr
    phone: Optional[PhoneStr] = None
    password: str

    @field_validator("password")
    @classmethod
    def check_the_minimum_length_of_the_password(cls, v: str) -> str:
        if len(v) < settings.minimum_length_of_the_password:
            raise UserErrorCode.InvalidPasswordLength()
        return v


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class Response(BaseModel):
    id: str = Field(alias="_id")
    fullname: str
    email: str
    position: Optional[str] = None
    phone: Optional[str] = None
    type: str
    company: Optional[str] = None
    district: Optional[str] = None
    ward: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    facebook: Optional[str] = None
    twitter: Optional[str] = None
    linkedin: Optional[str] = None
    instagram: Optional[str] = None
    created_at: datetime
    created_by: str
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None


class ListResponse(BaseModel):
    total_items: int
    total_page: int
    records_per_page: int
    results: List[Response]


class LoginResponse(Response):
    access_token: str
    token_type: str


class EditRequest(BaseModel):
    fullname: Optional[str] = None
    phone: Optional[PhoneStr] = None
    avatar: Optional[UrlStr] = None
    position: Optional[str] = None
    company: Optional[str] = None
    district: Optional[str] = None
    ward: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    facebook: Optional[UrlStr] = None
    twitter: Optional[UrlStr] = None
    linkedin: Optional[UrlStr] = None
    instagram: Optional[UrlStr] = None

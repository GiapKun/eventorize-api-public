from datetime import datetime
from typing import Literal, Optional

from core.schemas import EmailStr, ObjectIdStr, PhoneStr, UrlStr
from pydantic import BaseModel


class Users(BaseModel):
    fullname: str
    email: EmailStr
    position: Optional[str] = None
    phone: Optional[PhoneStr] = None
    company: Optional[str] = None
    district: Optional[str] = None
    ward: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    facebook: Optional[UrlStr] = None
    twitter: Optional[UrlStr] = None
    linkedin: Optional[UrlStr] = None
    instagram: Optional[UrlStr] = None
    password: bytes
    type: Literal["admin", "user"]
    created_at: datetime
    created_by: Optional[ObjectIdStr] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[ObjectIdStr] = None
    deleted_at: Optional[datetime] = None
    deleted_by: Optional[ObjectIdStr] = None

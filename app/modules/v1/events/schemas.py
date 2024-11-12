from datetime import datetime
from typing import List, Optional

from core.schemas import ObjectIdStr, UrlStr
from pydantic import BaseModel,Field


class CreateRequest(BaseModel):
    organizer_id: ObjectIdStr
    title: str
    thumbnail: Optional[UrlStr] = None
    description: str
    link: Optional[UrlStr] = None
    start_date: datetime
    end_date: datetime
    is_online: bool
    address: Optional[str] = None
    district: Optional[str] = None
    ward: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None

class PublicResponse(BaseModel):
    id: str = Field(alias="_id")
    organizer_id: str
    title: str
    thumbnail: Optional[UrlStr] = None
    description: str
    link: Optional[UrlStr] = None
    start_date: datetime
    end_date: datetime
    is_online: bool
    address: Optional[str] = None
    district: Optional[str] = None
    ward: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None

class PublicListResponse(BaseModel):
    total_items: int
    total_page: int
    records_per_page: int
    results: List[PublicResponse]

class Response(PublicResponse):
    created_at: datetime
    created_by: str
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None


class ListResponse(BaseModel):
    total_items: int
    total_page: int
    records_per_page: int
    results: List[Response]


class EditRequest(BaseModel):
    title: Optional[str] = None
    thumbnail: Optional[UrlStr] = None
    description: Optional[str] = None
    link: Optional[UrlStr] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    is_online: Optional[bool] = None
    address: Optional[str] = None
    district: Optional[str] = None
    ward: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
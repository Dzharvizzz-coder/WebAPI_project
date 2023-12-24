from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class HotelSchemaBase(BaseModel):
    name: str
    description: str
    location: str


class HotelSchemaCreate(HotelSchemaBase):
    pass


class HotelSchemaUpdate(HotelSchemaBase):
    name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None


class HotelSchema(HotelSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime

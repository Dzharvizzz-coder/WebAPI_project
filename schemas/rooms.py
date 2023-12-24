from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class RoomSchemaBase(BaseModel):
    type: str
    number: str
    capacity: int = Field(..., ge=1)
    price_per_night: int = Field(..., ge=0)
    hotel_id: int


class RoomSchemaCreate(RoomSchemaBase):
    pass


class RoomSchemaUpdate(RoomSchemaBase):
    type: Optional[str] = None
    number: Optional[str] = None
    capacity: Optional[int] = Field(None, ge=1)
    price_per_night: Optional[float] = Field(None, ge=0)
    hotel_id: Optional[int] = None


class RoomSchema(RoomSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime

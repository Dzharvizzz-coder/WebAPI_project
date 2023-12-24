from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class BookingSchemaBase(BaseModel):
    check_in_date: date
    check_out_date: date
    room_id: int
    customer_id: int


class BookingSchemaCreate(BookingSchemaBase):
    pass


class BookingSchemaUpdate(BookingSchemaBase):
    check_in_date: Optional[date] = None
    check_out_date: Optional[date] = None
    room_id: Optional[int] = None
    customer_id: Optional[int] = None


class BookingSchema(BookingSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime

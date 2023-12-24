from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class CustomerSchemaBase(BaseModel):
    name: str


class CustomerSchemaCreate(CustomerSchemaBase):
    pass


class CustomerSchemaUpdate(CustomerSchemaBase):
    name: Optional[str] = None


class CustomerSchema(CustomerSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime

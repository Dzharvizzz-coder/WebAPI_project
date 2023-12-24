from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import crud.models.customers as crud
from api.sockets import notify_clients
from database import get_db
from schemas.customers import CustomerSchema, CustomerSchemaCreate, CustomerSchemaUpdate

router = APIRouter(prefix="/customers", tags=["customers"])


@router.post("/", response_model=CustomerSchema)
async def create_customer(customer_schema: CustomerSchemaCreate, db: Session = Depends(get_db)):
    customer = crud.create_customer(db=db, schema=customer_schema)
    await notify_clients(f"Создан Клиент '{customer.name} (ID: {customer.id})'")
    return customer


@router.get("/", response_model=List[CustomerSchema])
async def read_customers(db: Session = Depends(get_db)):
    customer = crud.read_customers(db=db)
    return customer


@router.get("/", response_model=CustomerSchema)
async def read_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = crud.read_customer(db=db, customer_id=customer_id)
    return customer


@router.patch("/", response_model=CustomerSchema)
async def update_customer(customer_id: int, customer_schema: CustomerSchemaUpdate, db: Session = Depends(get_db)):
    customer = crud.update_customer(db=db, customer_id=customer_id, schema=customer_schema)
    await notify_clients(f"Обновлён Клиент '{customer.name} (ID: {customer.id})'")
    return customer


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = crud.delete_customer(db=db, customer_id=customer_id)
    await notify_clients(f"Удалён Клиент '(ID: {customer_id})'")
    return customer


from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import crud.models.hotels as crud
from api.sockets import notify_clients
from database import get_db
from schemas.hotels import HotelSchema, HotelSchemaCreate, HotelSchemaUpdate

router = APIRouter(prefix="/hotels", tags=["hotels"])


@router.post("/", response_model=HotelSchema)
async def create_hotel(hotel_schema: HotelSchemaCreate, db: Session = Depends(get_db)):
    hotel = crud.create_hotel(db=db, schema=hotel_schema)
    await notify_clients(f"Создан Отель '{hotel.name} (ID: {hotel.id})'")
    return hotel


@router.get("/", response_model=List[HotelSchema])
async def read_hotels(db: Session = Depends(get_db)):
    hotel = crud.read_hotels(db=db)
    return hotel


@router.get("/", response_model=HotelSchema)
async def read_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = crud.read_hotel(db=db, hotel_id=hotel_id)
    return hotel


@router.patch("/", response_model=HotelSchema)
async def update_hotel(hotel_id: int, hotel_schema: HotelSchemaUpdate, db: Session = Depends(get_db)):
    hotel = crud.update_hotel(db=db, hotel_id=hotel_id, schema=hotel_schema)
    await notify_clients(f"Обновлён Отель '{hotel.name} (ID: {hotel.id})'")
    return hotel


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = crud.delete_hotel(db=db, hotel_id=hotel_id)
    await notify_clients(f"Удалён Отель '(ID: {hotel_id})'")
    return hotel


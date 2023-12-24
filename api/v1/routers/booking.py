from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import crud.models.bookings as crud
from api.sockets import notify_clients
from database import get_db
from schemas.bookings import BookingSchema, BookingSchemaCreate, BookingSchemaUpdate

router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.post("/", response_model=BookingSchema)
async def create_booking(booking_schema: BookingSchemaCreate, db: Session = Depends(get_db)):
    booking = crud.create_booking(db=db, schema=booking_schema)
    await notify_clients(f"Создано Бронирование (ID: {booking.id}) комнаты (ID: {booking.room_id}) "
                         f"отеля '{booking.room.hotel.name} (ID: {booking.room.hotel.id})'"
                         f"для клиента '{booking.customer.name} (ID: {booking.customer.id})'")
    return booking


@router.get("/", response_model=List[BookingSchema])
async def read_bookings(db: Session = Depends(get_db)):
    booking = crud.read_bookings(db=db)
    return booking


@router.get("/", response_model=BookingSchema)
async def read_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = crud.read_booking(db=db, booking_id=booking_id)
    return booking


@router.patch("/", response_model=BookingSchema)
async def update_booking(booking_id: int, booking_schema: BookingSchemaUpdate, db: Session = Depends(get_db)):
    booking = crud.update_booking(db=db, booking_id=booking_id, schema=booking_schema)
    await notify_clients(f"Обновлено Бронирование (ID: {booking.id}) комнаты (ID: {booking.room_id}) "
                         f"отеля '{booking.room.hotel.name} (ID: {booking.room.hotel.id})'"
                         f"для клиента '{booking.customer.name} (ID: {booking.customer.id})'")
    return booking


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = crud.delete_booking(db=db, booking_id=booking_id)
    await notify_clients(f"Удалёно Бронирование '(ID: {booking_id})'")
    return booking


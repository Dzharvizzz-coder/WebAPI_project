from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import crud.models.rooms as crud
from api.sockets import notify_clients
from database import get_db
from schemas.rooms import RoomSchema, RoomSchemaCreate, RoomSchemaUpdate

router = APIRouter(prefix="/rooms", tags=["rooms"])


@router.post("/", response_model=RoomSchema)
async def create_room(room_schema: RoomSchemaCreate, db: Session = Depends(get_db)):
    room = crud.create_room(db=db, schema=room_schema)
    await notify_clients(f"Создан Номер '{room.type}-{room.number}/{room.capacity} | Стоимостью: {room.price_per_night}"
                         f" (ID: {room.id})' в Отеле '{room.hotel.name} (ID: {room.hotel.id})'")
    return room


@router.get("/", response_model=List[RoomSchema])
async def read_rooms(db: Session = Depends(get_db)):
    room = crud.read_rooms(db=db)
    return room


@router.get("/", response_model=RoomSchema)
async def read_room(room_id: int, db: Session = Depends(get_db)):
    room = crud.read_room(db=db, room_id=room_id)
    return room


@router.patch("/", response_model=RoomSchema)
async def update_room(room_id: int, room_schema: RoomSchemaUpdate, db: Session = Depends(get_db)):
    room = crud.update_room(db=db, room_id=room_id, schema=room_schema)
    await notify_clients(f"Обновлён Номер '{room.type}-{room.number}/{room.capacity} | Стоимостью: {room.price_per_night}"
                         f" (ID: {room.id})' в Отеле '{room.hotel.name} (ID: {room.hotel.id})'")
    return room


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_room(room_id: int, db: Session = Depends(get_db)):
    room = crud.delete_room(db=db, room_id=room_id)
    await notify_clients(f"Удалён Номер '(ID: {room_id})'")
    return room

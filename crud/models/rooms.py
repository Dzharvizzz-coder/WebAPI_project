import crud.base as crud
from sqlalchemy.orm import Session
from models import Room
from schemas.rooms import RoomSchemaCreate, RoomSchemaUpdate


def create_room(db: Session, schema: RoomSchemaCreate):
    return crud.create_object(db=db, model=Room, schema=schema)


def read_room(db: Session, **kwargs):
    return crud.get_object(db=db, model=Room, **kwargs)


def read_room_by_id(db: Session, room_id: int):
    return crud.get_object_by_id(db=db, model=Room, obj_id=room_id)


def read_rooms(db: Session, offset: int = 0, limit: int = None, **kwargs):
    return crud.get_all_objects(db=db, model=Room, offset=offset, limit=limit, **kwargs)


def update_room(db: Session, room_id: int, schema: RoomSchemaUpdate):
    return crud.update_object(db=db, obj_id=room_id, model=Room, schema=schema)


def delete_room(db: Session, room_id: int):
    return crud.delete_object(db=db, obj_id=room_id, model=Room)


def delete_all_rooms(db: Session):
    return crud.delete_all_objects(db=db, model=Room)

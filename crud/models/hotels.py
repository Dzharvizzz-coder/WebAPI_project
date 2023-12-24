import crud.base as crud
from sqlalchemy.orm import Session
from models import Hotel
from schemas.hotels import HotelSchemaCreate, HotelSchemaUpdate


def create_hotel(db: Session, schema: HotelSchemaCreate):
    return crud.create_object(db=db, model=Hotel, schema=schema)


def read_hotel(db: Session, **kwargs):
    return crud.get_object(db=db, model=Hotel, **kwargs)


def read_hotel_by_id(db: Session, hotel_id: int):
    return crud.get_object_by_id(db=db, model=Hotel, obj_id=hotel_id)


def read_hotels(db: Session, offset: int = 0, limit: int = None, **kwargs):
    return crud.get_all_objects(db=db, model=Hotel, offset=offset, limit=limit, **kwargs)


def update_hotel(db: Session, hotel_id: int, schema: HotelSchemaUpdate):
    return crud.update_object(db=db, obj_id=hotel_id, model=Hotel, schema=schema)


def delete_hotel(db: Session, hotel_id: int):
    return crud.delete_object(db=db, obj_id=hotel_id, model=Hotel)


def delete_all_hotels(db: Session):
    return crud.delete_all_objects(db=db, model=Hotel)

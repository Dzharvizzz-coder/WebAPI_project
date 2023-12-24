import crud.base as crud
from sqlalchemy.orm import Session
from models import Booking
from schemas.bookings import BookingSchemaCreate, BookingSchemaUpdate


def create_booking(db: Session, schema: BookingSchemaCreate):
    return crud.create_object(db=db, model=Booking, schema=schema)


def read_booking(db: Session, **kwargs):
    return crud.get_object(db=db, model=Booking, **kwargs)


def read_booking_by_id(db: Session, booking_id: int):
    return crud.get_object_by_id(db=db, model=Booking, obj_id=booking_id)


def read_bookings(db: Session, offset: int = 0, limit: int = None, **kwargs):
    return crud.get_all_objects(db=db, model=Booking, offset=offset, limit=limit, **kwargs)


def update_booking(db: Session, booking_id: int, schema: BookingSchemaUpdate):
    return crud.update_object(db=db, obj_id=booking_id, model=Booking, schema=schema)


def delete_booking(db: Session, booking_id: int):
    return crud.delete_object(db=db, obj_id=booking_id, model=Booking)


def delete_all_bookings(db: Session):
    return crud.delete_all_objects(db=db, model=Booking)

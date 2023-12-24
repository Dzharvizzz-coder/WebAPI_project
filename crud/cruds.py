from .base import *
from models import Hotel, Room, Booking, Customer





def create_room(db: Session, room_data: SchemaBase):
    return create_object(db=db, model=Room, schema=room_data)


def get_room(db: Session, **kwargs):
    return get_object(db=db, model=Room, **kwargs)


def get_room_by_id(db: Session, room_id: int):
    return get_object_by_id(db=db, model=Room, obj_id=room_id)


def get_all_rooms(db: Session, offset: int = 0, limit: int = None, **kwargs):
    return get_all_objects(db=db, model=Room, offset=offset, limit=limit, **kwargs)


def update_room(db: Session, room_id: int, room_data: SchemaBase):
    return update_object(db=db, obj_id=room_id, model=Room, schema=room_data)


def delete_room(db: Session, room_id: int):
    return delete_object(db=db, obj_id=room_id, model=Room)


def delete_all_rooms(db: Session):
    return delete_all_objects(db=db, model=Room)


def create_booking(db: Session, booking_data: SchemaBase):
    return create_object(db=db, model=Booking, schema=booking_data)


def get_booking(db: Session, **kwargs):
    return get_object(db=db, model=Booking, **kwargs)


def get_booking_by_id(db: Session, booking_id: int):
    return get_object_by_id(db=db, model=Booking, obj_id=booking_id)


def get_all_bookings(db: Session, offset: int = 0, limit: int = None, **kwargs):
    return get_all_objects(db=db, model=Booking, offset=offset, limit=limit, **kwargs)


def update_booking(db: Session, booking_id: int, booking_data: SchemaBase):
    return update_object(db=db, obj_id=booking_id, model=Booking, schema=booking_data)


def delete_booking(db: Session, booking_id: int):
    return delete_object(db=db, obj_id=booking_id, model=Booking)


def delete_all_bookings(db: Session):
    return delete_all_objects(db=db, model=Booking)


def create_customer(db: Session, customer_data: SchemaBase):
    return create_object(db=db, model=Customer, schema=customer_data)


def get_customer(db: Session, **kwargs):
    return get_object(db=db, model=Customer, **kwargs)


def get_customer_by_id(db: Session, customer_id: int):
    return get_object_by_id(db=db, model=Customer, obj_id=customer_id)


def get_all_customers(db: Session, offset: int = 0, limit: int = None, **kwargs):
    return get_all_objects(db=db, model=Customer, offset=offset, limit=limit, **kwargs)


def update_customer(db: Session, customer_id: int, customer_data: SchemaBase):
    return update_object(db=db, obj_id=customer_id, model=Customer, schema=customer_data)


def delete_customer(db: Session, customer_id: int):
    return delete_object(db=db, obj_id=customer_id, model=Customer)


def delete_all_customers(db: Session):
    return delete_all_objects(db=db, model=Customer)

import crud.base as crud
from sqlalchemy.orm import Session
from models import Customer
from schemas.customers import CustomerSchemaCreate, CustomerSchemaUpdate


def create_customer(db: Session, schema: CustomerSchemaCreate):
    return crud.create_object(db=db, model=Customer, schema=schema)


def read_customer(db: Session, **kwargs):
    return crud.get_object(db=db, model=Customer, **kwargs)


def read_customer_by_id(db: Session, customer_id: int):
    return crud.get_object_by_id(db=db, model=Customer, obj_id=customer_id)


def read_customers(db: Session, offset: int = 0, limit: int = None, **kwargs):
    return crud.get_all_objects(db=db, model=Customer, offset=offset, limit=limit, **kwargs)


def update_customer(db: Session, customer_id: int, schema: CustomerSchemaUpdate):
    return crud.update_object(db=db, obj_id=customer_id, model=Customer, schema=schema)


def delete_customer(db: Session, customer_id: int):
    return crud.delete_object(db=db, obj_id=customer_id, model=Customer)


def delete_all_customers(db: Session):
    return crud.delete_all_objects(db=db, model=Customer)

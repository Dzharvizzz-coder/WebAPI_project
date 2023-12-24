from fastapi import APIRouter

from api.v1.routers.customers import router as customers_router
from api.v1.routers.hotels import router as hotels_router
from api.v1.routers.booking import router as bookings_router
from api.v1.routers.rooms import router as rooms_router

router = APIRouter(prefix='/v1')

router.include_router(customers_router)
router.include_router(hotels_router)
router.include_router(rooms_router)
router.include_router(bookings_router)

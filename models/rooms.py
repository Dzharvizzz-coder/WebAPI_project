from datetime import datetime
from sqlalchemy import Integer, String, DateTime, func, ForeignKey, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database import Base


class Room(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[str] = mapped_column(String, unique=True, index=True)
    number: Mapped[str] = mapped_column(String, unique=True, index=True)
    capacity: Mapped[int] = mapped_column(Integer, unique=True, index=True)

    price_per_night: Mapped[float] = mapped_column(Float, unique=True, index=True)

    hotel_id: Mapped[int] = mapped_column(Integer, ForeignKey("hotels.id", ondelete="CASCADE"))
    hotel: Mapped["Hotel"] = relationship(back_populates="rooms", lazy="selectin")

    bookings: Mapped["Booking"] = relationship(back_populates="room", lazy="selectin")

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())

from datetime import datetime, date
from sqlalchemy import Integer, DateTime, func, ForeignKey, Date
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    check_in_date: Mapped[date] = mapped_column(Date, unique=True, index=True)
    check_out_date: Mapped[date] = mapped_column(Date, unique=True, index=True)

    room_id: Mapped[int] = mapped_column(Integer, ForeignKey("rooms.id", ondelete="CASCADE"))
    room: Mapped["Room"] = relationship(back_populates="bookings", lazy="selectin")

    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey("customers.id", ondelete="CASCADE"))
    customer: Mapped["Customer"] = relationship(back_populates="bookings", lazy="selectin")

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())

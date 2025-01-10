from uuid import UUID as ID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import UUID

class Base(DeclarativeBase):
  id: Mapped[ID] = mapped_column(UUID, primary_key=True, default=False)
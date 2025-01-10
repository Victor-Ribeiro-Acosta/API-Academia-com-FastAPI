from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, ForeignKey
from contrib.base import Base

class CategoriaModel(Base):
  __tablename__ = 'categoria'

  ca_id: Mapped[int] = mapped_column(Integer, primary_key=True, default=False)
  nome: Mapped[str] = mapped_column(String(100))
  atleta: Mapped["AtletaModel"] = relationship("AtletaModel", back_populates = 'categoria', lazy = 'selectin')
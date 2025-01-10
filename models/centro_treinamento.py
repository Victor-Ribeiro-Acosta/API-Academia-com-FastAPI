from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, ForeignKey
from contrib.base import Base

class CTModel(Base):
  __tablename__ = 'CentroTreinamento'

  ct_id: Mapped[int] = mapped_column(Integer, primary_key=True, default=False)
  nome: Mapped[str] = mapped_column(String(100), unique = True)
  endereco: Mapped[str] = mapped_column(String(100))
  numero: Mapped[str] = mapped_column(Integer)
  cidade: Mapped[str] = mapped_column(String(100))
  atleta: Mapped["AtletaModel"] = relationship("AtletaModel", back_populates = 'CentroTreinamento' , lazy='selectin')
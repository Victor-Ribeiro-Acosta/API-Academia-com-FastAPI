from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, Integer, String, Float
from contrib.base import Base



class AtletaModel(Base):
  __tablename__ = 'atleta'

  at_id: Mapped[int] = mapped_column(Integer, primary_key = True, default=False)
  nome: Mapped[str] = mapped_column(String(100))
  cpf: Mapped[str] = mapped_column(String(11), unique=True)
  sexo: Mapped[str] = mapped_column(String(10))
  idade: Mapped[int] = mapped_column(Integer)
  peso: Mapped[float] = mapped_column(Float)
  altura: Mapped[float] = mapped_column(Float)
  
  categoria: Mapped["CategoriaModel"] = relationship("CategoriaModel", back_populates = 'atleta', lazy='selectin', foreign_keys="AtletaModel.categoria_id")
  categoria_id: Mapped[int] = mapped_column(ForeignKey('categoria.ca_id'))
  
  centro_treinamento: Mapped["CTModel"] = relationship( "CTModel", back_populates = 'atleta', lazy='selectin', foreign_keys="AtletaModel.ct_id")
  ct_id: Mapped[int] = mapped_column(ForeignKey('CentroTreinamento.ct_id'))
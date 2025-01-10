from pydantic import UUID4, Field
from typing import Annotated

from sqlalchemy.orm import Mapped
from schemas.categoria import CategoriaIn
from contrib.baseSchema import SchemaOut

class CategoriaOut(CategoriaIn, SchemaOut):
  nome: Annotated[str, Field(description='Categoria registrada')]
from typing import Annotated
from pydantic import UUID4, Field
from schemas.atleta import AtletaIn
from contrib.baseSchema import SchemaOut

class AtletaOut(AtletaIn, SchemaOut):
  nome: Annotated[str, Field(description='Atleta registrado')]
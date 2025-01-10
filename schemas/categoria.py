from typing import Annotated
from pydantic import Field
from contrib.baseSchema import BaseSchema

class CategoriaIn(BaseSchema):
  nome: Annotated[str, Field(description='Informe o nome da categoria')]
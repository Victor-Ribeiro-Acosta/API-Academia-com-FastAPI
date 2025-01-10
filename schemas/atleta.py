from typing import Annotated, Optional
from pydantic import Field, PositiveInt, PositiveFloat
from contrib.baseSchema import BaseSchema
from schemas.categoria import CategoriaIn
from schemas.centro_treinamento import CTIn

class AtletaIn(BaseSchema):
  nome: Annotated[str, Field(description='Informe o nome do atleta')]
  cpf: Annotated[str, Field(description='Informe o CPF do atleta', max_length=11)]
  sexo: Annotated[str, Field(description='Informe o sexo do atleta')]
  idade: Annotated[PositiveInt, Field(description='Informe a idade do atleta')]
  peso: Annotated[PositiveFloat, Field(description = 'Informe o peso do atleta')]
  altura: Annotated[PositiveFloat, Field(description = 'Informe a altura do atleta')]
  categoria:Annotated[CategoriaIn, Field(description='Informe a categoria do atleta')]
  centro_treinamento: Annotated[CTIn, Field(description='Informe o centro de treinamento do atleta')]


class AtletaUp(BaseSchema):
  nome: Annotated[Optional[str], Field(None, description='Editar nome do atleta')]
  idade: Annotated[Optional[PositiveInt], Field(None, description='Editar idade')]
  peso: Annotated[Optional[PositiveFloat], Field(None, description = 'Editar peso')]
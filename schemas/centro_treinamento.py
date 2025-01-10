from typing import Annotated
from pydantic import Field
from contrib.baseSchema import BaseSchema

class CTIn(BaseSchema):
  nome: Annotated[str, Field(description='Informe o nome da categoria')]
  endereco: Annotated[str, Field('Informe o endereço do centro de treinamento sem o número')]
  numero: Annotated[int, Field(description='Informe o número do centro de treinamento')]
  cidade: Annotated[str, Field(description='Informe a cidade do centro de treinamento')]
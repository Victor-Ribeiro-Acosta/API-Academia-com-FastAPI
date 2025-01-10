from typing import Annotated
from pydantic import BaseModel, Field, UUID4

class BaseSchema(BaseModel):
  class Config:
    extra = 'forbid'
    from_attributes = True

class SchemaOut(BaseModel):
  id: Annotated[UUID4, Field(description='Identificador')]

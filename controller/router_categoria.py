from uuid import uuid4
from pydantic import UUID4
from sqlalchemy.future import select
from fastapi import APIRouter, Body
from http import HTTPStatus
from dependencias import DB_dependecy
from schemas.categoria import CategoriaIn
from views.categoria import CategoriaOut
from models.categoria import CategoriaModel

router = APIRouter()

@router.post("/",
             summary="Informar Categoria",
             status_code=HTTPStatus.CREATED,
             response_model = CategoriaOut
            )
async def inserir_categoria(db_session: DB_dependecy, categoria: CategoriaIn = Body(...)):
             
             categoria_out = CategoriaOut(id=uuid4(), **categoria.model_dump())
             categoria_model = CategoriaModel(**categoria_out.model_dump())
             db_session.add(categoria_model)
             await db_session.commit()
             return categoria_out


@router.get("/",
            summary="Informar Categoria",
           status_code=HTTPStatus.OK,
           response_model = list[CategoriaOut]
           )
async def listar_categorias(db_session: DB_dependecy):
             categorias: list[CateogriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()
             return categorias


@router.get("/{id}",
            summary="Informar Categoria",
           status_code=HTTPStatus.OK,
           response_model = CategoriaOut
           )
async def listar_categorias_por_id(id: UUID4, db_session: DB_dependecy):
             categoria: CateogriaOut = (await db_session.execute(select(CategoriaModel).filter_by(id=id))).scalars().first()
             return categoria
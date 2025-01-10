from uuid import uuid4
from pydantic import UUID4
from sqlalchemy.future import select
from fastapi import APIRouter, Body
from http import HTTPStatus
from dependencias import DB_dependecy
from schemas.centro_treinamento import CTIn
from views.centro_treinamento import CTOut
from models.centro_treinamento import CTModel

router = APIRouter()

@router.post("/",
             summary="Cadastrar Centro de Treinamento",
             status_code=HTTPStatus.CREATED,
             response_model = CTOut
            )
async def inserir_categoria(db_session: DB_dependecy, ct: CTIn = Body(...)):

             ct_out = CTOut(id=uuid4(), **ct.model_dump())
             ct_model = CTModel(**ct_out.model_dump())
             db_session.add(ct_model)
             await db_session.commit()
             return ct_out


@router.get("/",
            summary="Pesquisar centro de treinamento",
           status_code=HTTPStatus.OK,
           response_model = list[CTOut]
           )
async def listar_categorias(db_session: DB_dependecy):
             ct: list[CTOut] = (await db_session.execute(select(CTModel))).scalars().all()
             return ct


@router.get("/{id}",
            summary="Pesquisar centro de treinamento por id",
           status_code=HTTPStatus.OK,
           response_model = CTOut
           )
async def listar_categorias_por_id(id: UUID4, db_session: DB_dependecy):
             ct: CTOut = (await db_session.execute(select(CTModel).filter_by(id=id))).scalars().first()
             return ct
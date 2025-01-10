from fastapi import APIRouter, Body, HTTPException
from http import HTTPStatus
from uuid import uuid4
from dependencias import DB_dependecy
from schemas.atleta import AtletaIn, AtletaUp
from views.atleta import AtletaOut
from models.atleta import AtletaModel
from models.categoria import CategoriaModel
from models.centro_treinamento import CTModel
from sqlalchemy.future import select
from pydantic import UUID4
router = APIRouter()

@router.post("/",
             summary="Cadastrar Atleta",
             status_code=HTTPStatus.OK,
             response_model = AtletaOut
            )
async def cadastrar_atleta(db_session: DB_dependecy, atleta: AtletaIn = Body(...)):

             centro_treinamento = (await db_session.execute(select(CTModel).filter_by(nome=atleta.centro_treinamento.nome)))

             if not centro_treinamento:
                          raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Centro de treinamento não encontrado!')
                          
                          
             
             categoria = (await db_session.execute(select(CategoriaModel).filter_by(nome=atleta.categoria.nome)))
             
             if not categoria:
                          raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Categoria não encontrada')

             
                          
             atleta_out = AtletaOut(id=uuid4(), **atleta.model_dump())
             atleta_model = AtletaModel(**atleta_out.model_dump())
             await db_session.commit()
             await db_session.refresh(atleta_out)
                          
             return atleta_out


@router.get("/",
            summary="Informar Categoria",
           status_code=HTTPStatus.OK,
           response_model = list[AtletaOut]
           )
async def listar_atletas(db_session: DB_dependecy):
             atletas: list[AtletaOut] = (await db_session.execute(select(AtletaModel))).scalars().all()
             
             return [AtletaOut.model_validate(atleta) for atleta in atletas]


@router.get('/{id}',
            summary="Informar id do atleta",
           status_code=HTTPStatus.OK,
           response_model = AtletaOut
           )
async def listar_categorias_por_id(id: UUID4, db_session: DB_dependecy):
             atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()

             if not atleta:
                          raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=f'Atleta numero {id} não encontrado!')
                          
             return atleta



@router.patch("/{id}",
            summary="Informar id do atleta",
           status_code=HTTPStatus.OK,
           response_model = AtletaOut
           )
async def editar_atleta(id: UUID4,
                        db_session: DB_dependecy,
                        atleta_up: AtletaUp=Body(...)):
             
             atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()

             if not atleta:
                          raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Atleta não encontrado!')

             atleta_update = atleta_up.model_dump(exclude_unset=True)

             for key, value in atleta_update.items():
                          setattr(atleta, key, value)
                          
             await db_session.commit()
             await db_session.refresh(atleta)
             
             return atleta


@router.delete("/{id}",
            summary="Deletar atleta",
           status_code=HTTPStatus.NO_CONTENT,
           response_model = None
           )
async def listar_categorias_por_id(id: UUID4, db_session: DB_dependecy):
             atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()

             if not atleta:
                          raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=f'Atleta numero {id} não encontrado!')

             await db_session.delete(atleta)
             await db_session.commit()
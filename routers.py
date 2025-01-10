from controller.router_atleta import router as atleta
from controller.router_categoria import router as categoria
from controller.router_ct import router as ct
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])
api_router.include_router(categoria, prefix='/categorias', tags=['categorias'])
api_router.include_router(ct, prefix='/centro_treinamento', tags=['centro_treinamento'])
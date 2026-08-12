from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.modelos.cliente import Cliente
from app.banco_de_dados.cliente_repositorio import ClienteRepositorio
from app.dependencias import obter_cliente_repositorio

router = APIRouter(
    prefix="/clientes"
)

CLIENTE_LIST = [
        Cliente(id_=1, nome = "Jorge", email = "jorge@xpto.com", telefone = "47991222324"),
        Cliente(id_=2, nome = "Renato", email = "renato@xpto.com", telefone = "47991222325"),
        Cliente(id_=3 ,nome = "Tobias", email = "tobias@xpto.com", telefone = "47991222389"),
        Cliente(id_=4 ,nome = "Remo", email = "remo@xpto.com", telefone = "47991222321"),
        ]

@router.get("/", response_model=list[Cliente])
async def listar_clientes(cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)]):
    return await cliente_repositorio.listar_clientes()

@router.get("/{cliente_id}", response_model = Cliente | None)
async def obter_cliente(
    cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)],
    cliente_id: int
):
    cliente = await cliente_repositorio.obter_cliente(cliente_id)

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado!")

    return None
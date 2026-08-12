from fastapi import APIRouter

from app.modelos.cliente import Cliente

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
async def listar_clientes():
    return CLIENTE_LIST

@router.get("/{cliente_id}", response_model = Cliente | None)
async def obter_cliente(cliente_id: int):
    for cliente in CLIENTE_LIST:
        if cliente.id_ == cliente_id:
            return cliente
    
    return None



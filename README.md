# projeto_relat-rios

## Uso rápido com FastAPI ✅

Exemplo de uso dos **Pydantic schemas** gerados em `App/schemas`:

```py
from fastapi import FastAPI
from App.schemas import ClientRead, ClientCreate

app = FastAPI()

# exemplo de endpoint de leitura usando response_model
@app.get('/clients/{client_id}', response_model=ClientRead)
def read_client(client_id: int):
    # retornar instância SQLAlchemy (orm_mode=True permite conversão automática)
    ...

# exemplo de endpoint de criação usando request body
@app.post('/clients', response_model=ClientRead)
def create_client(payload: ClientCreate):
    # validar payload e persistir com SQLAlchemy
    ...
```

> Observação: os schemas possuem `orm_mode = True` para permitir que FastAPI converta objetos ORM diretamente para JSON.

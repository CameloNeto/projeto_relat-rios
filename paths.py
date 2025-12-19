from pathlib import Path

def clients_CRUD_path() -> Path:
    clients_path = Path('./sql/clients/')
    if clients_path.exists():
        return clients_path
    else:
        raise ModuleNotFoundError("O caminho não foi encontrado")

from database.operations.colect_clients import colect_clients
from database.operations.colect_emails import colect_emails
from database.operations.colect_facilities import colect_facilities
import asyncio
from pathlib import Path
import paths
import os


async def syncronize_clients():
    if not paths.database().exists():
        raise FileExistsError("O banco de dados não foi criado")
    await colect_clients()
    processes = []
    for process in [colect_emails(), colect_facilities()]:
        processes.append(process)
    await asyncio.gather(*processes)

if __name__ == "__main__":
    asyncio.run(syncronize_clients())
from synchronize_clients import syncronize_clients
from App.operations.colect_bills import colect_bills
import asyncio

def synchronize_all():
    asyncio.run(syncronize_clients())
    asyncio.run(colect_bills())

if __name__ == "__main__":
    synchronize_all()
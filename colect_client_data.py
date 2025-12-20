import sqlite3
import httpx
import asyncio
from keys import DG_TOKEN
from DataBase import DataBase
import json

async def get_facilities(document:str) -> List[str]:
        """
        Docstring for get_facilities

        :return: Retorna uma lista de strings com os números das instalações
        :rtype: List[tuple]
        """
        
        urlDG = 'https://gestao.dg.energy/api/v1/installations/'

        headersDG = {
            'Authorization':f'Token {DG_TOKEN}'
        }

        facilities = []

        while urlDG:
            request = await httpx.AsyncClient(timeout=120).request("GET", urlDG, headers=headersDG)
            results = request.json().get("results")
            for facility in results:
                if facility.get('owner') == document:
                    facilities.append(facility.get('number'))
            urlDG = request.json().get("next")
        return facilities

async def colect_clients():
    urlDG = 'https://gestao.dg.energy/api/v1/entities/'

    headersDG = {
            'Authorization':f'Token {DG_TOKEN}'
        }

    database = DataBase()

    while urlDG:
        request = await httpx.AsyncClient(timeout=120).request("GET", urlDG, headers=headersDG)
        results = request.json().get("results")
        for client in results:
            if not database.exists("clients", "id", client.get('id')):
                facilities = await get_facilities(client.get('document'))
                database.insert_clients(
                                        [client.get('id'),
                                        client.get('name'),
                                        client.get('document_type'),
                                        client.get('document'),
                                        json.dumps(client.get('emails')),
                                        json.dumps(facilities)]
                                        )
        urlDG = request.json().get("next")

if __name__ == "__main__":
    asyncio.run(colect_clients())
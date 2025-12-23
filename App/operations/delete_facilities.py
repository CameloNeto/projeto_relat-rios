from App.models.make_session import db_session
from App.models.facility import facility
from sqlalchemy import select
from keys import DG_TOKEN
import httpx


async def delete_facilities():
    BATCH_SIZE = 100
    last_id = 0

    url_DG = 'https://gestao.dg.energy/api/v1/installations/'


    with db_session() as session:
        
        while url_DG:
            request = await httpx.AsyncClient(timeout=120).get(url_DG, headers={
                'Authorization':f'Token {DG_TOKEN}'
            })

            dg_results = request.json().get("results")

            dg_count = len(dg_results)
            db_loops = 0
            batch_count = 0
            while True:
                db_results = session.execute(select(facility).where(facility.id > last_id).limit(BATCH_SIZE).order_by(facility.id)).scalars().all()
                for n, db_facility in enumerate(db_results):
                    last_id+=1
                    db_loops+=1
                
                    if str(db_facility.number) == dg_results[n+BATCH_SIZE*batch_count].get("number"):
                        continue
                    else:
                        session.delete(db_facility)
                        session.commit()
                        break

                if dg_count <= db_loops:
                    break
                else:
                    batch_count += 1
            url_DG = request.json().get("next")

if __name__ == "__main__":
    import asyncio
    asyncio.run(delete_facilities())
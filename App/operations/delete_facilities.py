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
            print(request)

            dg_results = request.json().get("results")

            dg_count = len(dg_results)
            print(f"DG facilities fetched: {dg_count}")
            db_count = 0
            init_loop = 0

            
            while db_count < dg_count:
                db_results = session.execute(select(facility).where(facility.id > last_id).limit(BATCH_SIZE).order_by(facility.id)).scalars().all()
                for n, db_facility in enumerate(db_results):
                    print(f"{db_count} |{db_facility.number} {db_facility.id} | {dg_results[db_count+n].get('number')} {db_count+n}")
                    if db_facility.number == dg_results[db_count+n].get("number"):
                        continue
                    else:
                        pass
                        #session.delete(db_facility)
                        #session.commit()
                db_count += len(db_results)
                
            break
            url_DG = request.json().get("next")

if __name__ == "__main__":
    import asyncio
    asyncio.run(delete_facilities())
import httpx
import asyncio
from keys import DG_TOKEN
import json
from sqlalchemy import insert, select, exists
from App.models.make_session import db_session
from App.models.facility import facility
from App.models.bill import bill


async def colect_bills():
    urlDG = 'https://gestao.dg.energy/api/v1/bills/'

    headersDG = {
            'Authorization':f'Token {DG_TOKEN}'
        }

    with db_session() as session:
        while urlDG:
            request = await httpx.AsyncClient(timeout=120).request("GET", urlDG, headers=headersDG)
            results = request.json().get("results")

            for dg_bill in results:
                condition = session.scalar(select(exists(bill).where(bill.id==dg_bill.get("id"))))
                facility_id = session.query(facility).where(facility.number==dg_bill.get("installation_data").get("number")).scalar().id

                if not condition:
                    add_bill = insert(bill).values(
                        id=dg_bill.get("id"),
                        due_date=dg_bill.get("due_date"),
                        payment_status=dg_bill.get("payment_status"),
                        consumption=dg_bill.get("consumption"),
                        total_amount_distributor=dg_bill.get("total_amount_distributor"),
                        value=dg_bill.get("value"),
                        amount_saved=dg_bill.get("amount_saved"),
                        bill_generated=dg_bill.get("bill_generated"),
                        facility_id=facility_id,
                    )
                
                    session.execute(add_bill)
                    session.commit()

            urlDG = request.json().get("next")

if __name__ == "__main__":
    asyncio.run(colect_bills())
from App.models.make_session import db_session
from App.models.facility import facility
from sqlalchemy import select
import httpx

BATCH_SIZE = 100
last_id = 0

with db_session() as session:
    while True: 
        db_facilities = session.execute(
            select(facility)
            .where(facility.id > last_id)
            .order_by(facility.id)
            .limit(BATCH_SIZE)
        ).scalars().all()

        for db_facility in db_facilities:
            
            last_id = db_facility.id
        
        if not db_facilities:
            break
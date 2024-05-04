from database import sync_engine, async_engine, session_factory
from sqlalchemy import text, insert, select, update
from models import workers_teble, WorkersOrm, metadata_obj

def get_123_sync():
    with sync_engine.connect() as conn:
        res = conn.execute(text('SELECT 1,2,3 union SELECT 4,5,6'))
        print(f'{res=}')

async def get_123_async():
    async with async_engine.connect() as conn:
        res = await conn.execute(text('SELECT 1,2,3 union SELECT 4,5,6'))
        print(f'{res.all()=}')

class SynCore:
    @staticmethod
    def create_tebles():
        sync_engine.echo = False
        metadata_obj.drop_all(sync_engine)
        metadata_obj.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with sync_engine.connect() as conn:
            # Это голый запрос на вставку данных
            # stmt = """INSERT INTO workers (username) VALUES ('Bobr'), ('Volk');"""
            # Это уже блатной запрос, можно делать вот так
            stmt = insert(workers_teble).values(
                [
                    {'username': 'Bobr'},
                    {'username': 'Volk'},
                ]
            )
            conn.execute(stmt)
            conn.commit()

    @staticmethod
    def select_workers():
        with sync_engine.connect() as conn:
            query = select(workers_teble)
            result = conn.execute(query)
            workers = result.all()
            print(f"{workers=}")

    @staticmethod
    def update_workers(new_username: str = "Misha", worker_id: int = 2):
        with sync_engine.connect() as conn:
            # stmt = text("UPDATE workers SET username=:username WHERE id=:id")
            # stmt = stmt.bindparams(username=new_username, id=worker_id)
            stmt = (
                update(workers_teble).
                values(username=new_username).
                filter_by(id=worker_id)
            )
            # .where(workers_teble.c.id==worker_id)
            conn.execute(stmt)
            conn.commit()

class AsynCore:
    pass
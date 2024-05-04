from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
import asyncio
from sqlalchemy import create_engine, text, String
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from config import settings
from typing import Annotated
# Синхронная работа
sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    # pool_size=5,
    # max_overflow=10
)

session_factory = sessionmaker(sync_engine)


str_256 = Annotated[str, 256]

class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }

# Явное подключение к базе данных через контекстный менеджер 
# with engine.connect() as conn:
#     res = conn.execute(text('SELECT VERSION()'))
#     print(f'{res=}')
#     conn.commit()

# Не явное подкючение
# with sync_engine.begin() as conn:
#     res = conn.execute(text('SELECT 1,2,3 union SELECT 4,5,6'))
#     print(f'{res.all()=}')




##### Асинхронная работа #######
async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
)

async_sessiona = async_sessionmaker(async_engine)

# async def get_123():
#     async with async_engine.begin() as conn:
#         res = await conn.execute(text('SELECT 1,2,3 union SELECT 4,5,6'))
#         print(f'{res.all()=}')

# asyncio.run(get_123())

from database import sync_engine, session_factory, Base
from models import metadata_obj, WorkersOrm, ResumesOrm, Workload
from sqlalchemy import select, insert, func, cast, Integer, and_


class SyncOrm:
    @staticmethod
    def create_tebles():
        sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)  
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with session_factory() as session:
            worker_bobr = WorkersOrm(username="Bobr")
            worker_volk = WorkersOrm(username="Volk")

            # stmt = insert(WorkersOrm).values(
            #     [
            #         {'username': 'Bobr'},
            #         {'username': 'Volk'},
            #     ]
            # )
            # session.execute(stmt)
            session.add_all([worker_bobr, worker_volk])
            # session.flash() Добавляет результат в бд но продолжает работу ф-ии
            session.commit()


    @staticmethod
    def select_workers():
        with session_factory() as session:
            # Два запроса в отличии от других, в этом случае будет медлен            
            # worker_id = 1
            # worker_jack = session.get(WorkersOrm, worker_id)
            # result = worker_jack.username
            # print(f"{result=}")

            query = select(WorkersOrm)
            result = session.execute(query)
            workers = result.scalars().all()
            print(f"{workers=}")
             

    @staticmethod
    def update_workers(new_username: str = "Misha", worker_id: int = 2):
        with session_factory() as session:
            worker_mishel = session.get(WorkersOrm, worker_id)
            worker_mishel.username = new_username
            session.commit()

    @staticmethod
    def insert_resumes():
        with session_factory() as session:
            resume_jack_1 = ResumesOrm(
                title="Python Junior Developer", compensation=50000, workload=Workload.fulltime, worker_id=1)
            resume_jack_2 = ResumesOrm(
                title="Python Разработчик", compensation=150000, workload=Workload.fulltime, worker_id=1)
            resume_michael_1 = ResumesOrm(
                title="Python Data Engineer", compensation=250000, workload=Workload.parttime, worker_id=2)
            resume_michael_2 = ResumesOrm(
                title="Data Scientist", compensation=300000, workload=Workload.fulltime, worker_id=2)
            session.add_all([resume_jack_1, resume_jack_2, 
                             resume_michael_1, resume_michael_2])
            session.commit()    

    @staticmethod
    def select_resumes_avg_compensation(like_language: str = "Python"):
        with session_factory() as session:
            """
            select workload, avg(compensation)::int as avg_compensation
            from resumes
            where title like '%Python%' and compensation > 40000
            group by workload;
            """
            query = (
                select(
                    ResumesOrm.workload,
                    cast(func.avg(ResumesOrm.compensation), Integer).label("avg_compensation")
                )
                .select_from(ResumesOrm)
                .filter(and_(
                    ResumesOrm.title.contains(like_language),
                    ResumesOrm.compensation > 40000
                ))
                .group_by(ResumesOrm.workload)
                .having(cast(func.avg(ResumesOrm.compensation), Integer) > 70000)
            )
            # print(query.compile(compile_kwargs={"literal_binds": True})) Вывод запроса
            res = session.execute(query)
            result = res.all()
            print(f"{result}")

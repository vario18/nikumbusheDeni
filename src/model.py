from typing import Optional

from sqlmodel import SQLModel, Session, create_engine, Field

DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/nikumbusheDB"

engine = create_engine(DATABASE_URL)


class Cars(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    carOwner: str = Field(default=None)
    phoneNumber: str
    plateLetter: str
    plateNumber: str
    owed: int = Field(default=0)

    @classmethod
    def get_by_id(cls, id: int):
        with Session(engine) as session:
            _car = session.query(Cars).filter(Cars.id == id).first()
            if _car:
                return _car

    @classmethod
    def get_all(cls):
        with Session(engine) as session:
            return session.query(Cars).all()


def create_db_and_tables():
    # SQLModel.metadata.create_all(engine)
    pass

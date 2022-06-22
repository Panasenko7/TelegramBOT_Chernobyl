from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    working_hours = Column(Integer)

    # def __init__(self):
    #     self.working_hours = 0

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, hours={self.working_hours!r})"

    def __str__(self):
        return f" Name= {self.name!r}, worked {self.working_hours!r} hours"


from sqlalchemy import create_engine
engine = create_engine("sqlite:///file.sql", echo=True, future=True)
Base.metadata.create_all(engine)

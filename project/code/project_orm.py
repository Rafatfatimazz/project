import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,Float,ForeignKey,DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base=declarative_base()
# we will create our users table

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    email=Column(String(50),unique=True)
    name=Column(String(50))
    password=Column(String(50))
    group=Column(Integer,default=1)
    created_at=Column(DateTime,default=datetime.utcnow,nullable=False)
    # current date and time in datetime format

    def __repr__(self)->str:
        return f"{self.id}|{self.name}|{self.group}"

if __name__=="__main__":
    engine=create_engine("sqlite:///database.sqlite")
    Base.metadata.create_all(engine)

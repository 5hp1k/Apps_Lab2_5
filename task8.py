from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
from task1 import Jobs

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String)
    name = Column(String)
    age = Column(Integer)
    position = Column(String)
    speciality = Column(String)
    address = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    modified_date = Column(DateTime)

class Jobs(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_leader = Column(Integer, ForeignKey('users.id'))
    job = Column(String)
    work_size = Column(Integer)
    collaborators = Column(String)
    start_date = Column(DateTime, default=datetime.now)
    end_date = Column(DateTime)
    is_finished = Column(Boolean)

    user = relationship("User", foreign_keys=[team_leader])

    def __repr__(self):
        return f"<Job> {self.job}"


engine = create_engine(f'sqlite:///mars_explorer.db')
Session = sessionmaker(bind=engine)
session = Session()

jobs = session.query(Jobs).filter(
    Jobs.work_size < 20,
    Jobs.is_finished == False
).all()

for job in jobs:
    print(job)

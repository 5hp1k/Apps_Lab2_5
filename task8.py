from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from task1 import Jobs


def __repr__(self):
    return f"<Job> {self.job}"


setattr(Jobs, '__repr__', __repr__)

Base = declarative_base()
engine = create_engine('sqlite:///mars_explorer.db')
Session = sessionmaker(bind=engine)
session = Session()

jobs = session.query(Jobs).filter(
    Jobs.work_size < 20,
    Jobs.is_finished == False
).all()

for job in jobs:
    print(job)

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    is_finished = Column(Boolean)
    user = relationship("User", foreign_keys=[team_leader])


class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    chief = Column(Integer, ForeignKey('users.id'))
    members = Column(String)  # Хранение списка ID в виде строки
    email = Column(String, unique=True)

    chief_user = relationship("User", foreign_keys=[chief])


if __name__ == "__main__":
    engine = create_engine('sqlite:///mars_explorer.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    departments = [Department(title='Geological Survey', chief=1,
                              members='2,3', email='geo_surv@mars.org'),
                   Department(title='Engineering', chief=10,
                              members='12,13,14', email='eng@mars.org')]

    for department in departments:
        session.add(department)
        session.commit()

    print('\nDepartment has been successfully added to the database')

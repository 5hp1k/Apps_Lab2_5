from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

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

class Job(Base):
    __tablename__ = 'jobs'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    team_leader = Column(Integer, ForeignKey('users.id'))
    description = Column(String)
    work_size = Column(Integer)
    collaborators = Column(String)  # Список id участников в виде строки
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    is_finished = Column(Boolean)

    # Определение связи с моделью User
    user = relationship('User', foreign_keys=[team_leader])

# Создание базы данных
engine = create_engine('sqlite:///mars_explorer.db')
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Добавление данных в таблицу users
captain_data = {
    'surname': 'Scott',
    'name': 'Ridley',
    'age': 21,
    'position': 'captain',
    'speciality': 'research engineer',
    'address': 'module_1',
    'email': 'scott_chief@mars.org',
    'hashed_password': 'hashed_password_here',
    'modified_date': '2024-04-14T00:00:00'
}

colonists_data = [
    {
        'surname': 'Johnson',
        'name': 'Anna',
        'age': 30,
        'position': 'colonist',
        'speciality': 'biologist',
        'address': 'module_2',
        'email': 'johnson_bio@mars.org',
        'hashed_password': 'hashed_password_here',
        'modified_date': '2024-04-14T00:00:00'
    },
    {
        'surname': 'Williams',
        'name': 'Bob',
        'age': 35,
        'position': 'colonist',
        'speciality': 'geologist',
        'address': 'module_3',
        'email': 'williams_geo@mars.org',
        'hashed_password': 'hashed_password_here',
        'modified_date': '2024-04-14T00:00:00'
    },
    # Добавьте еще 3 колонистов здесь
]

# Добавление капитана в таблицу users
captain = User(**captain_data)
session.add(captain)

# Добавление колонистов в таблицу users
for colonist_data in colonists_data:
    colonist = User(**colonist_data)
    session.add(colonist)

# Сохранение изменений
session.commit()

# Закрытие сессии
session.close()

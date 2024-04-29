from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task1 import User
from task11 import Department
from datetime import datetime


engine = create_engine(f'sqlite:///mars_explorer.db')
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

user1 = User(surname='Doe', name='John', age=30, position='Geologist', speciality='Mineralogy', address='Module_3', email='john.doe@mars.org', 
             hashed_password='hashed_password', modified_date=datetime.now(), work_size=30)
user2 = User(surname='Smith', name='Emma', age=28, position='Geologist', speciality='Geomorphology', address='Module_3', email='emma.smith@mars.org', 
             hashed_password='hashed_password', modified_date=datetime.now(), work_size=20)
print('\nUsers have successfully been added')

session.add(user1)
session.add(user2)
session.commit()

department_0 = Department(id=0, title="Colony development", email="colony_development@mars.org")
department_1 = Department(id=1, title="Geological survey", email="geological_survey@mars.org")

session.add(department_0)
session.add(department_1)
session.commit()

session.close()

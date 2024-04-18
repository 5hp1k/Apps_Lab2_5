from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task1 import User


db_name = input("Enter the name of your database: ")

engine = create_engine(f'sqlite:///{db_name}.db')
Session = sessionmaker(bind=engine)
session = Session()

underage_colonists = session.query(User).filter(User.age < 18).all()

for colonist in underage_colonists:
    print(f"{colonist.id} {colonist.surname} {colonist.name} - {colonist.age} years old")

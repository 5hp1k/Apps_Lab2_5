from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task1 import User


db_name = input("Enter the name of your database: ")

engine = create_engine(f'sqlite:///{db_name}.db')
Session = sessionmaker(bind=engine)
session = Session()

query = session.query(User).filter(User.address == 'module_1', User.age < 21)
query.update({User.address: 'module_3'})

session.commit()

print("The addresses have been successfully changed.")

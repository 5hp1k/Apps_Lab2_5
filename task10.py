from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task1 import User


engine = create_engine('sqlite:///mars_explorer.db')
Session = sessionmaker(bind=engine)
session = Session()

query = session.query(User).filter(User.address == 'module_1', User.age < 21)
query.update({User.address: 'module_3'})

session.commit()

print("The addresses have been successfully changed.")

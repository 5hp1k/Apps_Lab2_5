from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task1 import User


db_name = input("Enter the name of your database: ")

engine = create_engine(f'sqlite:///{db_name}.db')
Session = sessionmaker(bind=engine)
session = Session()

colonists = session.query(User).filter(
    (User.position.like('%chief%')) | (User.position.like('%middle%'))
).all()

for colonist in colonists:
    print(f"{colonist.id} {colonist.surname} {colonist.name} - {colonist.position}")

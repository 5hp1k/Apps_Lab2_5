from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task1 import User


db_name = input("Enter the name of your database: ")

engine = create_engine(f'sqlite:///{db_name}.db')
Session = sessionmaker(bind=engine)
session = Session()

colonists = session.query(User).filter(
    User.address == 'module_1',
    ~User.speciality.like('%engineer%'),
    ~User.position.like('%engineer%')
).all()

for colonist in colonists:
    print(colonist.id)

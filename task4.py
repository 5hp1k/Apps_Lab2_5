from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task1 import User


def user_repr(self):
    return f"<Colonist> {self.id} {self.surname} {self.name}"


db_name = input("Enter the name of your database: ")

User.__repr__ = user_repr

engine = create_engine(f'sqlite:///{db_name}')
Session = sessionmaker(bind=engine)
session = Session()

colonists_in_module_1 = session.query(User).filter_by(address='module_1').all()

for colonist in colonists_in_module_1:
    print(colonist)

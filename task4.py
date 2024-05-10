from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task1 import User


def user_repr(self):
    return f"<Colonist> {self.id} {self.surname} {self.name}"


User.__repr__ = user_repr

engine = create_engine('sqlite:///mars_explorer.db')
Session = sessionmaker(bind=engine)
session = Session()

colonists_in_module_1 = session.query(User).filter_by(address='module_1').all()

for colonist in colonists_in_module_1:
    print(colonist)

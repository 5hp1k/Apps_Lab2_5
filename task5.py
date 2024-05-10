from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task1 import User


engine = create_engine('sqlite:///mars_explorer.db')
Session = sessionmaker(bind=engine)
session = Session()

colonists = session.query(User).filter(
    User.address == 'module_1',
    ~User.speciality.like('%engineer%'),
    ~User.position.like('%engineer%')
).all()

for colonist in colonists:
    print(colonist.id)

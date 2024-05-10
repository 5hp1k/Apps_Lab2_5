from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task1 import User


engine = create_engine('sqlite:///mars_explorer.db')
Session = sessionmaker(bind=engine)
session = Session()

colonists = session.query(User).filter(
    (User.position.like('%chief%')) | (User.position.like('%middle%'))
).all()

for colonist in colonists:
    print(f"{colonist.id} {colonist.surname} {colonist.name} - {colonist.position}")

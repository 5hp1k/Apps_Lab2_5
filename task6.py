from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task1 import User


engine = create_engine('sqlite:///mars_explorer.db')
Session = sessionmaker(bind=engine)
session = Session()

underage_colonists = session.query(User).filter(User.age < 18).all()

for colonist in underage_colonists:
    print(f"{colonist.id} {colonist.surname} {colonist.name} - {colonist.age} years old")

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from task1 import Jobs, User


engine = create_engine('sqlite:///mars_explorer.db')
Session = sessionmaker(bind=engine)
session = Session()

largest_team_size = session.query(
    func.max(func.length(Jobs.collaborators))).scalar()

team_leaders = session.query(User).join(Jobs, User.id == Jobs.team_leader).filter(
    func.length(Jobs.collaborators) == largest_team_size
).all()

if len(team_leaders) == 1:
    print(
        f"Team lead with the largest team: {team_leaders[0].surname} {team_leaders[0].name}")
else:
    print("Teamleads with the largest teams:")
    for leader in team_leaders:
        print(f"{leader.surname} {leader.name}")

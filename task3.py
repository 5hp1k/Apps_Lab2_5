from datetime import datetime
from sqlalchemy.orm import sessionmaker
from task1 import Jobs, engine


Session = sessionmaker(bind=engine)
session = Session()

jobs_data = [
    {
        'team_leader': 1,
        'job': 'deployment of residential modules 1 and 2',
        'work_size': 15,
        'collaborators': '2, 3',
        'start_date': datetime.now(),
        'is_finished': False
    },
    {
        'team_leader': 1,
        'job': 'maintenance of life support systems',
        'work_size': 10,
        'collaborators': '4, 5',
        'start_date': datetime.now(),
        'is_finished': False
    },
    {
        'team_leader': 2,
        'job': 'environmental research',
        'work_size': 18,
        'collaborators': '1, 3',
        'start_date': datetime.now(),
        'is_finished': False
    },
    {
        'team_leader': 3,
        'job': 'mineral exploration',
        'work_size': 22,
        'collaborators': '2, 4',
        'start_date': datetime.now(),
        'is_finished': False
    },
    {
        'team_leader': 4,
        'job': 'chemical analysis of soil samples',
        'work_size': 8,
        'collaborators': '1, 5',
        'start_date': datetime.now(),
        'is_finished': True
    },
    {
        'team_leader': 5,
        'job': 'maintenance of power supply systems',
        'work_size': 12,
        'collaborators': '2, 3',
        'start_date': datetime.now(),
        'is_finished': False
    },
    {
        'team_leader': 6,
        'job': 'meteorological observations',
        'work_size': 16,
        'collaborators': '1, 4',
        'start_date': datetime.now(),
        'is_finished': False
    },
    {
        'team_leader': 7,
        'job': 'construction of new modules',
        'work_size': 25,
        'collaborators': '3, 5',
        'start_date': datetime.now(),
        'is_finished': False
    },
    {
        'team_leader': 12,
        'job': 'digging a quarry',
        'work_size': 30,
        'collaborators': '13, 14',
        'start_date': datetime.now(),
        'is_finished': False
    }
]

for job_data in jobs_data:
    job = Jobs(**job_data)
    session.add(job)

session.commit()

print('\nRecords have been successfully added to the database')

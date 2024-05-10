from datetime import datetime
from sqlalchemy.orm import sessionmaker
from task1 import User, engine


Session = sessionmaker(bind=engine)
session = Session()

captain = User(surname='Scott',
               name='Ridley',
               age=21,
               position='captain',
               speciality='research engineer',
               address='module_1',
               email='scott_chief@mars.org',
               hashed_password='some_hashed_password',
               modified_date=datetime.now())

session.add(captain)

colonists_data = [
    {
        'surname': 'Smith',
        'name': 'John',
        'age': 30,
        'position': 'engineer',
        'speciality': 'mechanical engineer',
        'address': 'module_2',
        'email': 'smith_john@mars.org',
        'hashed_password': 'some_hashed_password',
        'modified_date': datetime.now()
    },
    {
        'surname': 'Johnson',
        'name': 'Emily',
        'age': 25,
        'position': 'biologist',
        'speciality': 'microbiologist',
        'address': 'module_3',
        'email': 'johnson_emily@mars.org',
        'hashed_password': 'some_hashed_password',
        'modified_date': datetime.now()
    },
    {
        'surname': 'Williams',
        'name': 'James',
        'age': 28,
        'position': 'geologist',
        'speciality': 'rock specialist',
        'address': 'module_4',
        'email': 'williams_james@mars.org',
        'hashed_password': 'some_hashed_password',
        'modified_date': datetime.now()
    },
    {
        'surname': 'Brown',
        'name': 'Sarah',
        'age': 29,
        'position': 'chemist',
        'speciality': 'organic chemist',
        'address': 'module_5',
        'email': 'brown_sarah@mars.org',
        'hashed_password': 'some_hashed_password',
        'modified_date': datetime.now()
    },
    {
        'surname': 'Jones',
        'name': 'Michael',
        'age': 27,
        'position': 'physicist',
        'speciality': 'quantum physicist',
        'address': 'module_6',
        'email': 'jones_michael@mars.org',
        'hashed_password': 'some_hashed_password',
        'modified_date': datetime.now()
    },
    {
        'surname': 'Alexander',
        'name': 'Brown',
        'age': 20,
        'position': 'chef',
        'speciality': 'italian chef',
        'address': 'module_1',
        'email': 'alex.brown@mars.org',
        'hashed_password': 'some_hashed_password',
        'modified_date': datetime.now()
    },
    {
        'surname': 'Joshua',
        'name': 'Graham',
        'age': 14,
        'position': 'child',
        'speciality': None,
        'address': 'module_4',
        'email': 'cool.josh@mars.org',
        'hashed_password': 'some_hashed_password',
        'modified_date': datetime.now()
    },
    {
        'surname': 'Jasmine',
        'name': 'Briggs',
        'age': 11,
        'position': 'child',
        'speciality': None,
        'address': 'module_3',
        'email': 'jbriggs@mars.org',
        'hashed_password': 'some_hashed_password',
        'modified_date': datetime.now()
    },
    {
        'surname': 'Taylor',
        'name': 'Rachel',
        'age': 35,
        'position': 'chief engineer',
        'speciality': 'mechanical engineer',
        'address': 'module_1',
        'email': 'taylor_rachel@mars.org',
        'hashed_password': 'some_hashed_password',
        'modified_date': datetime.now()
    },
    {
        'surname': 'Evans',
        'name': 'Oliver',
        'age': 40,
        'position': 'middle biologist',
        'speciality': 'microbiologist',
        'address': 'module_2',
        'email': 'evans_oliver@mars.org',
        'hashed_password': 'some_hashed_password',
        'modified_date': datetime.now()
    },
    {
        'surname': 'Roberts',
        'name': 'Emma',
        'age': 38,
        'position': 'chief geologist',
        'speciality': 'rock specialist',
        'address': 'module_3',
        'email': 'roberts_emma@mars.org',
        'hashed_password': 'some_hashed_password',
        'modified_date': datetime.now()
    },
    {
        'surname': 'King',
        'name': 'Ethan',
        'age': 32,
        'position': 'middle chemist',
        'speciality': 'organic chemist',
        'address': 'module_4',
        'email': 'king_ethan@mars.org',
        'hashed_password': 'some_hashed_password',
        'modified_date': datetime.now()
    },
    {
        'surname': 'Morgan',
        'name': 'Ava',
        'age': 37,
        'position': 'chief physicist',
        'speciality': 'quantum physicist',
        'address': 'module_5',
        'email': 'morgan_ava@mars.org',
        'hashed_password': 'some_hashed_password',
        'modified_date': datetime.now()
    },
    {
        'surname': 'Sophia',
        'name': 'Clark',
        'age': 10,
        'position': 'child',
        'speciality': None,
        'address': 'module_1',
        'email': 'sophia_clark@mars.org',
        'hashed_password': 'some_hashed_password',
        'modified_date': datetime.now()
    },
    {
        'surname': 'Liam',
        'name': 'Dawson',
        'age': 9,
        'position': 'child',
        'speciality': None,
        'address': 'module_1',
        'email': 'liam_dawson@mars.org',
        'hashed_password': 'some_hashed_password',
        'modified_date': datetime.now()
    }
]

for colonist_data in colonists_data:
    colonist = User(**colonist_data)
    session.add(colonist)

session.commit()

print('\nRecords have been successfully added to the database')

from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship
from task1 import Base


department_members_association = Table('department_members', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('department_id', Integer, ForeignKey('departments.id'))
)

class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    chief = Column(Integer, ForeignKey('users.id'))
    email = Column(String)
    
    chief_user = relationship("User", foreign_keys=[chief])
    members = relationship("User", secondary=department_members_association, back_populates="departments")

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String)
    name = Column(String)
    age = Column(Integer)
    position = Column(String)
    speciality = Column(String)
    address = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    modified_date = Column(DateTime)
    
    departments = relationship("Department", secondary=department_members_association, back_populates="members")
 
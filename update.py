from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://psql:1234@localhost:5432/db1')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Student(Base):
    __tablename__ = 'student1'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)
    grade = Column(String(50))

Base.metadata.create_all(engine)

# student = session.query(Student).filter(Student.name == 'test1').first()
# if student:
#     student.name = 'Maha'
#     session.commit()
#     print(f"Student's name updated to {student.name}")
# else:
#     print("Student not found.")


student = session.query(Student).filter(Student.name == 'Maha').first()
if student:
    print(student.name)
else:
    print("Student not found.")
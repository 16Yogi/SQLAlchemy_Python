from sqlalchemy import create_engine, Column, Integer, String,or_,func
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

# students = session.query(Student)
# for student in students:
    # print(Student.name,student.age)

# students = session.query(Student).order_by(Student.name)
# for student in students:
    # print(student.name)


# student = session.query(Student).filter(Student.name=="test1").first()
# print(student.name,student.age)


# students = session.query(Student).filter(or_(Student.name == 'test1', Student.name == 'test2'))
# for student in students:
    # print(student.name,student.age)
# 

# students_count = session.query(Student).filter(or_(Student.name=='test1'))
# print(students_count)


students_count = session.query(func.count(Student.id)).filter(Student.name == 'test1').scalar()
print(f"Number of students named 'test1': {students_count}")
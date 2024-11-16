from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.exc import IntegrityError
from config import *


class Base(DeclarativeBase): pass
class Person(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True)
    user_full_name = Column(String)

class Message(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)

engine = create_engine(
    url=SQL_ALCHEMY_DATABASE,
    connect_args={"check_same_thread": False}
)

LocalSession = sessionmaker(autoflush=True, bind=engine)
db = LocalSession()

def create_tables():
    Base.metadata.create_all(bind=engine)

def add_user(fullname, userid):
    user = Person(user_full_name = fullname, user_id = userid)
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        print(f"User with ID: {userid} is already exists")

def add_message(userid, question, answer):
    message = Message(user_id = userid, question=question, answer=answer)
    db.add(message)
    try:
        db.commit()
    except:
        db.rollback()
        print("Something went wrong")
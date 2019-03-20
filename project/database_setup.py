import sys ,time , datetime
from sqlalchemy import Column , ForeignKey , Integer , String, DateTime
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('user.id'))
    recipient_id = Column(Integer, ForeignKey('user.id'))
    Message = Column(String(250))
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    user = relationship(User)

engine = create_engine('sqlite:///a3traf.db')
Base.metadata.create_all(engine)

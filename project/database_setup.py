import sys ,time , datetime
from sqlalchemy import Column , ForeignKey , Integer , String, DateTime
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import func
Base = declarative_base()

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer)
    recipient_id = Column(Integer)
    Message = Column(String(250), nullable=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())

engine = create_engine('sqlite:///a3traf.db')
Base.metadata.create_all(engine)

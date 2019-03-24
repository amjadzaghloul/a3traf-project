from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Post

engine = create_engine('sqlite:///a3traf.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
post1 = Post(sender_id= 1 , recipient_id= 2, Message='مرحباً أمجد كيف حالك')
session.add(post1)
session.commit()

post2 = Post(sender_id= 2 , recipient_id= 1, Message='مرحباً هنادي كيف حالك')
session.add(post2)
session.commit()


print("done")
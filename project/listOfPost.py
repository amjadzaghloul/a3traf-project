from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Post, User

engine = create_engine('sqlite:///a3traf.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
user1 = User(name="Amjad Zaghloul", email="amjad.zaghloul@gmail.com",
             picture='https://lh5.googleusercontent.com/-HF11rvXelt8/AAAAAAAAAAI/AAAAAAAACh4/UBgEkQ-4hQM/photo.jpg')
session.add(user1)
session.commit()

user2 = User(name="hanade Zaghloul", email="hanade.zaghloul@gmail.com",
             picture='https://i.pinimg.com/originals/91/2d/0b/912d0b0d1ab486523121b28c324533a3.jpg')
session.add(user2)
session.commit()

print("done")
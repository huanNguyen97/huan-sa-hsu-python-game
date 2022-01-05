# Import from orms
from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship

# Import from owner
from database.db_MySQL import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password = Column(String, index=True)
    image_url = Column(String, index=True)
    type_user = Column(String, index=True)
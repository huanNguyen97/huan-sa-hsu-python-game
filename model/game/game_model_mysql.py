# Import from orms
from sqlalchemy import Column, Integer, String, Float
# from sqlalchemy.orm import relationship

# Import from owner
from database.db_MySQL import Base


class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    brand = Column(String, index=True)
    year_released = Column(Integer, index=True)
    price = Column(Float, index=True)
    url = Column(String, index=True)
    id_user = Column(Integer, index=True)
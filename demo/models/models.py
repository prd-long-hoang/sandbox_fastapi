from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from demo.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)


class SellPlaces(Base):
    __tablename__ = "sellplaces"

    id = Column(Integer, primary_key=True, index=True)
    location_name = Column(String, index=True)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

class UserReview(Base):
    __tablename__ = "user_review"
    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    sell_places_id = Column(Integer, ForeignKey("sellplaces.id"))


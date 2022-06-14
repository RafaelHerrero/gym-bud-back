from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserTable(Base):

    __tablename__ = 'users'
    __table_args__ = {'schema': 'public'}

    user_id = Column(String, primary_key=True)
    user_firstname = Column(String)
    user_lastname = Column(String)
    user_login = Column(String)
    user_password = Column(String)
    updated_at = Column(DateTime)
    created_at = Column(DateTime)

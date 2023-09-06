from sqlalchemy import Column, Integer, String
from base import Base

class ClientEntity(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)

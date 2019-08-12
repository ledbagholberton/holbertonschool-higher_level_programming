#!/usr/bin/python3
"""Definition model_city"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()


class City(Base):
    """Definition class City"""
    __tablename__ = "cities"
    id = Column('id', Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, nullable=False,
                      ForeignKey('states.id'))
    state = relationship("State", backpopulates="cities")

#!/usr/bin/python3
"""Definition model_city"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from relationship_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """Definition class City"""
    __tablename__ = "cities"
    id = Column('id', Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'),
                      nullable=False)

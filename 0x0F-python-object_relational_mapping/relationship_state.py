#!/usr/bin/python3
"""Definition Model State"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """Definition Class State"""
    __tablename__ = "states"
    id = Column('id', Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column('name', String(128), nullable=False)
    cities = relationship("City", backref="state")

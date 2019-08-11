#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    __tablename__ = "states"
    id = Column('id', Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column('name', String(128), nullable=False)

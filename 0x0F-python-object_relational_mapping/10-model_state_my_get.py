#!/usr/bin/python3
"""Alchemy Query safe argv[4]"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    name2 = sys.argv[4].split("; ")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    a = 0
    for state in session.query(State).filter(State.name == name2[0])
    .all():
        print("{}".format(state.id))
        a = 1
    if a == 0:
        print("Not found")
    session.close()

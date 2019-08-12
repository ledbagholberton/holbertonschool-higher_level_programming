#!/usr/bin/python3
"""Alchemy Query and Join with cities table"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for my_state, my_city in (session.query(State, City)
                        .filter(State.id == City.state_id)):
        print("{}: ({}) {}".format(my_state.name, my_city.id, my_city.name))
    session.commit()
    session.close()

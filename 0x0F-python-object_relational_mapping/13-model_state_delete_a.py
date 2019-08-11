#!/usr/bin/python3
"""Query and delete all states with a"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    our_state = session.query(State).filter(State.name.like('%a%')).first()
    while (our_state is not None):
        session.delete(our_state)
        our_state = session.query(State).filter(State.name.like('%a%')).first()
    session.commit()
    session.close()

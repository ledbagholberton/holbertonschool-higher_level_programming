#!/usr/bin/python3
"""Alchemy Query for Relationship"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    my_state = State(name = "California")
    my_city = City(name = "San Francisco")
    my_city.state = my_state
    session.add(my_city, my_state)
    session.commit()
    session.close()

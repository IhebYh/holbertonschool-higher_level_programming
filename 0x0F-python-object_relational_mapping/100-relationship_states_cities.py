#!/usr/bin/python3
"""
relationship between states and cities
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    stateToAdd = State(name="California")
    stateToAdd.cities = [City(name="San Francisco")]
    re = session.add(stateToAdd)
    session.commit()
    session.close()

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
    rows = session.query(City).all()
    for city in rows:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.commit()
    session.close()

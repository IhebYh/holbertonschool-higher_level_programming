#!/usr/bin/python3
"""
list all State objects from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    query = session.query(State).filter_by(name=argv[4]).first()
    if query is None:
        print("Not found")
    else:
        print(str(query.id))
    session.close()

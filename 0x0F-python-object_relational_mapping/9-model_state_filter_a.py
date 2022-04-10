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
    session = Session(engine)
    m = '%a%'
    query = session.query(State).filter(State.name.like(m)).order_by(State.id)
    for q in query:
        print("{}: {}".format(q.id, q.name))
    session.close()

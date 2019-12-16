#!/usr/bin/python3
"""
This script lists all states
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.engine import url
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    city = session.query(State, City).filter(State.id == City.state_id).all()

    for i, j in city:
        print("{}: ({}) {}".format(i.name, j.id, j.name))

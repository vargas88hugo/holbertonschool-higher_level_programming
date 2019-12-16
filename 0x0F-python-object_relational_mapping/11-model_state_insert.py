#!/usr/bin/python3
"""
This script lists all states
"""
from sys import argv
from model_state import Base, State
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
    state = State(name='Luisana')
    session.add(state)
    session.commit()

    print(state.id)

    session.close()

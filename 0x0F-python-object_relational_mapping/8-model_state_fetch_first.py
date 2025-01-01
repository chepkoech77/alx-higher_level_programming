#!/usr/bin/python3
"""module to fetch from db"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, db_name):
    """Get states"""
    # connect to the database
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(username, password, db_name)
            )
    Base.metadata.create_all(engine)

    # create session to interact with db
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve all State objects
    states = session.query(State).order_by(State.id).first()

    # Display results
    if states:
        print(f"{states.id}: {states.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()


if __name__ == "__main__":
    username, password, db_name = argv[1:]

    # call the function
    list_states(username, password, db_name)

#!/usr/bin/python3
"""List first state from database
"""


if __name__ == "__main__":
    import sys
    import sqlalchemy
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    my_query = session.query(State).order_by(State.id)[0]
    print("{}:".format(my_query.id), my_query.name)
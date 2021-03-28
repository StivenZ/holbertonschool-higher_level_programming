#!/usr/bin/python3
"""Module on starting session with mysqlalchemy
"""
if __name__ == "__main__":
    """Fetch objects from 'cities' table
    """
    import sqlalchemy
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:\
                            3306/{}'.format(sys.argv[1], sys.argv[2],
                                            sys.argv[3]), pool_pre_ping=True)
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()

    for states, cities in session.query(State, City).\
        filter(State.id == City.state_id).\
            order_by(City.id.asc()):
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))

#!/usr/bin/python3
"""Module on mysql alchemy filter
"""
if __name__ == "__main__":
    """Update data from the database
    """
    import sqlalchemy
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:\
                            3306/{}'.format(sys.argv[1], sys.argv[2],
                                            sys.argv[3]), pool_pre_ping=True)
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()

    my_query = session.query(State).filter_by(id=2)
    my_query[0].name = 'New Mexico'
    session.commit()

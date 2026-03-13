import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope='session')
def test_client():
    engine = create_engine('sqlite:///:memory:', connect_args={"check_same_thread": False})
    connection = engine.connect()
    transaction = connection.begin()
    
    yield connection  # This is where the testing happens
    
    transaction.rollback()
    connection.close()

@pytest.fixture(autouse=True)
def session(test_client):
    """Create a new session for each test."""
    Session = sessionmaker(bind=test_client)
    session = Session()
    yield session
    session.close()
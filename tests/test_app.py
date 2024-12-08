from datetime import datetime
import pytest
from fastapi.testclient import TestClient
from fastapi import status
from fastapi_user_management.app import app  # Assuming your FastAPI app is in main.py
from fastapi_user_management.core.init_db import init_db
from fastapi_user_management.models.base import Base
from fastapi_user_management.models.user import UserModel, UserStatusValues
from fastapi_user_management.schemas.user import UserBase
from fastapi_user_management.core.database import SessionLocal, engine, get_db  # Make sure to import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# Test Database Setup for isolated tests
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionTestLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override for testing
def get_db_override():
    db = SessionTestLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="module")
def client():
    # Create all tables in the test database before tests run
    Base.metadata.create_all(engine)
    with Session(bind=engine) as session:
        init_db(db=session)
    with TestClient(app) as client:
        yield client
    Base.metadata.drop_all(bind=engine)  # Drop all tables after tests are complete

@pytest.fixture(scope="module")
def create_user(client):
    # Create a test user for the profile endpoint
    db = SessionTestLocal()
    test_user = UserModel(
        username="testuser@mail.com",
        password="testpassword",  # This should match the plain password for login in tests
        fullname="Test User",
        phone_number=1234567890,
        status=UserStatusValues.ACTIVE,
        created_at=datetime.now(),
    )
    db.add(test_user)
    db.commit()
    db.refresh(test_user)
    db.close()
    return test_user

@pytest.fixture(scope="module")
def token(client, create_user):
    # Simulate a login to obtain the JWT token for the test user
    login_data = {"username": create_user.username, "password": "testpassword"}
    response = client.post("/auth/token", data=login_data)
    assert response.status_code == 200
    return response.json()["access_token"]

def test_get_user_profile(client, token, create_user):
    """Test for the `/user/profile` endpoint"""
    response = client.get(
        "/user/profile", headers={"Authorization": f"Bearer {token}"}
    )

    # Assert the response is correct
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "username": create_user.username,
        "fullname": create_user.fullname,
        "phone_number": create_user.phone_number,
        "status": create_user.status,
    }

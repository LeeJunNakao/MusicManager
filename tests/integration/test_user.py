import pytest
import os
# from services.user_services import list_users
from adapters.repository import UserRepository
from config import get_session
from adapters.orm.user import User

@pytest.fixture(name="create_valid_data")
def create_valid_data_fixture():
    return {
        "name": "João",
        "email": "joao@email.com",
        "password": "Abc123@",
    }


@pytest.fixture(name="update_valid_data")
def update_valid_data_fixture():
    return {"id": 1, "name": "João"}


def test_first():
    # UserRepository.create(name="pedro", email="pedro@email.com", password="123456")
    # users = UserRepository.list()
    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    # print(users)
    
    

    assert 10 == 1
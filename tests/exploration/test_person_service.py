from unittest.mock import create_autospec

import pytest

from testing_course.exploration.person import Person
from testing_course.exploration.person_repository import PersonRepository
from testing_course.exploration.person_service import PersonService


@pytest.fixture
def repo():
    return create_autospec(PersonRepository, instance=True)


@pytest.fixture
def service(repo) -> PersonService:
    return PersonService(repo)


def test_register_with_valid_name_and_age_creates_person(service, repo) -> None:
    # Arrange
    name = "Alice"
    age = 20

    # Act
    service.register(name, age)

    # Assert
    repo.create_person.assert_called_once()
    created = repo.create_person.call_args.args[0]
    assert created.name == name
    assert created.age == age


def test_register_with_too_young_age_raises_value_error(service) -> None:
    with pytest.raises(ValueError, match="too young"):
        service.register("Bob", 13)


def test_get_average_age_returns_correct_result(service, repo) -> None:
    repo.read_all_persons.return_value = [Person("Alice", 30), Person("Bob", 40)]

    assert service.get_average_age() == 35

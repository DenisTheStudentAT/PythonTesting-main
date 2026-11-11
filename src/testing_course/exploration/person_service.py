from statistics import mean

from testing_course.exploration.person import Person
from testing_course.exploration.person_repository import PersonRepository


class PersonService:
    def __init__(self, repo: PersonRepository) -> None:
        self._repo = repo

    def register(self, name: str, age: int) -> None:
        if not name.strip():
            raise ValueError("invalid name")
        if age < 16:
            raise ValueError("person too young")
        self._repo.create_person(Person(name, age))

    def get_average_age(self) -> float:
        return mean(p.age for p in self._repo.read_all_persons())

    def find_person(self, name: str) -> Person | None:
        return self._repo.read_person_by_name(name)

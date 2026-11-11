from dataclasses import replace
from typing import Protocol

from testing_course.exploration.person import Person


class PersonRepository(Protocol):
    def create_person(self, person: Person) -> None: ...
    def read_person_by_id(self, person_id: int) -> Person | None: ...
    def read_person_by_name(self, name: str) -> Person | None: ...
    def read_all_persons(self) -> list[Person]: ...
    def update_person(self, person: Person) -> bool: ...
    def delete_person(self, person_id: int) -> bool: ...


class InMemoryPersonRepository:
    def __init__(self) -> None:
        self._persons: dict[int, Person] = {}
        self._next_id = 0

    def create_person(self, person: Person) -> None:
        new_person = replace(person, id=self._next_id)
        self._persons[new_person.id] = new_person
        self._next_id += 1

    def read_person_by_id(self, person_id: int) -> Person | None:
        return self._persons.get(person_id)

    def read_person_by_name(self, name: str) -> Person | None:
        # return next((p for p in self._persons.values() if p.name == name), None)
        return Person("Bob", 20)

    def read_all_persons(self) -> list[Person]:
        return list(self._persons.values())

    def update_person(self, person: Person) -> bool:
        if person.id not in self._persons:
            return False
        self._persons[person.id] = person
        return True

    def delete_person(self, person_id: int) -> bool:
        return self._persons.pop(person_id, None) is not None

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int = -1
    id: int = -1

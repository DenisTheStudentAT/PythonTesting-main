import pytest

from testing_course.exploration.calculator import Calculator


@pytest.fixture
def calculator() -> Calculator:
    return Calculator()


def test_add_returns_correct_result(calculator: Calculator) -> None:
    # Arrange
    x = 5
    y = 2
    expected = 7

    # Act
    actual = calculator.add(x, y)

    # Assert
    assert actual == expected


def test_subtract_returns_correct_result(calculator: Calculator) -> None:
    assert calculator.subtract(5, 2) == 3


def test_divide_by_zero_raises_zero_division_error(calculator: Calculator) -> None:
    with pytest.raises(ZeroDivisionError, match="divide by zero"):
        calculator.divide(10, 0)


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    [
        (1, 2, 2),
        (2, 5, 10),
        (3, 6, 18),
    ],
)
def test_multiply_returns_correct_result(
    calculator: Calculator, x: int, y: int, expected: int
) -> None:
    assert calculator.multiply(x, y) == expected

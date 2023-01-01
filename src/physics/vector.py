from typing import Iterable, List, Self, Tuple, Union


class Vector2D(Iterable):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def from_vec(vec: Iterable[int]) -> Self:
        return Vector2D(vec[0], vec[1])
    
    def to_vec(self) -> Tuple[int, int]:
        return (self.x, self.y)

    def longer_than(self, other: Self) -> bool:
        return self.x**2 + self.y**2 < other.x**2 + other.y**2

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __iter__(self):
        return iter([self.x, self.y])

    def __abs__(self) -> Self:
        x = abs(self.x)
        y = abs(self.y)
        return Vector2D(x, y)

    def __add__(self, other: Iterable) -> Self:
        if type(other) in [list, tuple]:
            other = Vector2D.from_vec(other)
        if type(other) == Vector2D:
            x = self.x + other.x
            y = self.y + other.y
            return Vector2D(x, y)
        else:
            raise TypeError

    def __sub__(self, other: Iterable) -> Self:
        if type(other) in [list, tuple]:
            other = Vector2D.from_vec(other)
        if type(other) == Vector2D:
            x = self.x - other.x
            y = self.y - other.y
            return Vector2D(x, y)
        else:
            raise TypeError

    def __eq__(self, other: Self) -> bool:
        if type(other) in [list, tuple]:
            other = Vector2D.from_vec(other)
        if type(other) == Vector2D:
            return self.x == other.x and self.y == other.y
        else:
            raise TypeError

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __lt__(self, other: Self) -> List[bool]:
        return [self.x < other.x, self.y < other.y]

    def __le__(self, other: Self) -> List[bool]:
        return [self.x <= other.x, self.y <= other.y]

    def __gt__(self, other: Self)  -> List[bool]:
        return [self.x > other.x, self.y > other.y]

    def __ge__(self, other: Self)  -> List[bool]:
        return [self.x >= other.x, self.y >= other.y]

    def __mul__(self, other: Union[Self, int, float]) -> Self:
        if type(other) in [int, float]:
            x = self.x * other
            y = self.y * other
            return Vector2D(x, y)
        else:
            raise Exception("Pas encore implémenté")
    
    def __truediv__(self, other: Union[Self, int, float]) -> Self:
        if type(other) in [int, float]:
            x = self.x / other
            y = self.y / other
            return Vector2D(x, y)
        else:
            raise Exception("Pas encore implémenté")

    def orthogonal(self) -> Self:
        return Vector2D(-self.y, self.x)
    
    def is_orthogonal_with(self, v: Self) -> bool:
        return dot(self, v) == 0


def dot(v1: Vector2D, v2: Vector2D) -> int:
    return v1.x*v2.x + v1.y*v2.y


class Base:
    
    def __init__(self, u, v) -> None:
        self.u = u
        self.v = v
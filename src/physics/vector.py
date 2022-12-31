from typing import Iterable, List, Self, Tuple


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

    def __iter__(self):
        return iter([self.x, self.y])

    def __add__(self, other: Iterable) -> Self:
        if type(other) != Self:
            other = Vector2D.from_vec(other)
        x = self.x + other.x
        y = self.y + other.y
        return Vector2D(x, y)

    def __sub__(self, other: Iterable) -> Self:
        if type(other) != Self:
            other = Vector2D.from_vec(other)
        x = self.x - other.x
        y = self.y - other.y
        return Vector2D(x, y)

    # TODO: Faire le reste des opérations proprements
    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: object) -> bool:
        pass

    def __lt__(self, other: Self) -> List[bool]:
        return [self.x < other.x, self.y < other.y]

    def __le__(self, other: Self) -> List[bool]:
        return [self.x <= other.x, self.y <= other.y]

    def __gt__(self, other: Self)  -> List[bool]:
        return [self.x > other.x, self.y > other.y]

    def __ge__(self, other: Self)  -> List[bool]:
        return [self.x >= other.x, self.y >= other.y]

    def __mul__(self, other: Self) -> Self:
        raise Exception("Pas encore implémenté")
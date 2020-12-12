from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List


@dataclass
class NVector:
    values: List[Any]

    def __len__(self):
        return len(self.values)

    def __init__(self, *values):
        self.values = list(values)

    def __mul__(self, other):
        return self.__rmul__(other)

    def __rmul__(self, other):
        if isinstance(other, NVector):
            raise ValueError("Can't multiply two vectors")
        return self.__class__(*[value * other for value in self.values])

    def __add__(self, other):
        if isinstance(other, NVector):
            if len(self.values) != len(other.values):
                raise ValueError("Vector lengths must be the same to add")
            return self.__class__(*[self.values[i] + other.values[i] for i in range(len(self.values))])
        else:
            return self.__class__(*[self.values[i] + other for i in range(len(self.values))])

    def __sub__(self, other):
        return self.__add__(-1 * other)

    def __truediv__(self, other):
        if isinstance(other, NVector):
            raise ValueError("Can't divide two vectors")
        return self.__class__(*[value / other for value in self.values])

    def __floordiv__(self, other):
        if isinstance(other, NVector):
            raise ValueError("Can't divide two vectors")
        return self.__class__(*[value // other for value in self.values])

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value


class Vector2D(NVector):
    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, value):
        self[0] = value

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, value):
        self[1] = value

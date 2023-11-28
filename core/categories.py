from enum import IntEnum, StrEnum


class Number(StrEnum):
    SINGULAR = 'singular'
    PLURAL = 'plural'


class Person(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3


class Tense(StrEnum):
    PAST = 'past'
    PRESENT = 'present'
    FUTURE = 'future'


class Hardness(StrEnum):
    HARD = 'hard'
    SOFT = 'soft'


class Sonority(StrEnum):
    VOICED = 'voiced'
    VOICELESS = 'voiceless'


if __name__ == '__main__':
    print(repr(Number.SINGULAR))

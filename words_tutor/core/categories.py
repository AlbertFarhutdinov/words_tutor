from enum import StrEnum


class GrammaticalNumber(StrEnum):
    SINGULAR = 'singular'
    PLURAL = 'plural'


class Tense(StrEnum):
    PAST = 'past'
    PRESENT = 'present'
    FUTURE = 'future'

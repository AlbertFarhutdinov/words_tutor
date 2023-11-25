from categories import Number, Person, Tense


class Verb:
    
    def __init__(
        self,
        imperative: str,
        tense: str = 'present',
        is_negative: bool = False,
        is_question: bool = False,
    ):
        self.imperative = imperative
        self.tense = tense
        self.is_negative = is_negative
        self.is_question = is_question

    def conjugate(
        self,
        number: Number,
        person: Person,
        tense: Tense,
    ):
        pass

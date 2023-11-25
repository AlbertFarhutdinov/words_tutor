from categories import Number, Person, Tense


class Pronoun:
    
    def __init__(
        self,
        number: Number,
        person: Person,
        tense: Tense,
    ):
        self.number = number
        self.person = person
        self.tense = tense

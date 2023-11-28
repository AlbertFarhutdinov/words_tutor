from enum import StrEnum

from core.categories import Hardness, Number, Sonority, Tense

NASAL = 'nasal'
NON_NASAL = 'non_nasal'

VOWEL = 'vowel'
CONSONANT = 'consonant'

AFFIRMATIVE = 'affirmative'
NEGATIVE = 'negative'
QUESTION = 'question'

INFINITIVE = 'infinitive'


A_UPPER = '\N{CYRILLIC CAPITAL LETTER SCHWA}'
G_UPPER = '\N{CYRILLIC CAPITAL LETTER ZHE WITH DESCENDER}'
N_UPPER = '\N{CYRILLIC CAPITAL LETTER EN WITH DESCENDER}'
O_UPPER = '\N{CYRILLIC CAPITAL LETTER BARRED O}'
U_UPPER = '\N{CYRILLIC CAPITAL LETTER STRAIGHT U}'
H_UPPER = '\N{CYRILLIC CAPITAL LETTER SHHA}'

A_LOWER = '\N{CYRILLIC SMALL LETTER SCHWA}'
G_LOWER = '\N{CYRILLIC SMALL LETTER ZHE WITH DESCENDER}'
N_LOWER = '\N{CYRILLIC SMALL LETTER EN WITH DESCENDER}'
O_LOWER = '\N{CYRILLIC SMALL LETTER BARRED O}'
U_LOWER = '\N{CYRILLIC SMALL LETTER STRAIGHT U}'
H_LOWER = '\N{CYRILLIC SMALL LETTER SHHA}'


CONSONANTS = {
    'б', 'в', 'г', 'д', 'ж', G_LOWER, 
    'з', 'й', 'к', 'л', 'м', 'н', N_LOWER,
    'п', 'р', 'с', 'т', 'ф', 'х', H_LOWER, 
    'ц', 'ч', 'ш', 'щ',
}

VOWELS = {
    'а', A_LOWER, 
    'е', 'ё', 'и', 'о', O_LOWER, 'у',
    U_LOWER, 'ы', 'э', 'ю', 'я',
}

Hardness.HARD_VOWELS = {'а', 'о', 'у', 'ы', 'э'}
Hardness.SOFT_VOWELS = {A_LOWER, 'е', 'ё', 'и', O_LOWER, U_LOWER, 'ю', 'я'}
NASAL_CONSONANTS = {'м', 'н', N_LOWER}
VOICED_CONSONANTS = {
    'б', 'в', 'г', 'д', 'ж', G_LOWER, 
    'з', 'й', 'л', 'м', 'н', N_LOWER,
    'р',
}
VOICELESS_CONSONANTS = {
    'к', 'п', 'с', 'т', 'ф', 'х', H_LOWER, 
    'ч', 'ш', 'щ',
}


PRONOUNS_NOMINATIVE = {
    (1, Number.SINGULAR): 'мин',
    (2, Number.SINGULAR): 'cин',
    (3, Number.SINGULAR): 'ул',
    (1, Number.PLURAL): 'без',
    (2, Number.PLURAL): 'сез',
    (3, Number.PLURAL): 'алар',
}
PRONOUNS_ACCUSATIVE = {
    (1, Number.SINGULAR): 'мине',
    (2, Number.SINGULAR): 'cине',
    (3, Number.SINGULAR): f'а{N_LOWER}ы',
    (1, Number.PLURAL): 'безне',
    (2, Number.PLURAL): 'сезне',
    (3, Number.PLURAL): 'аларны',
}
PRONOUNS_DATIVE = {
    (1, Number.SINGULAR): f'ми{N_LOWER}a',
    (2, Number.SINGULAR): f'cи{N_LOWER}а',
    (3, Number.SINGULAR): f'а{N_LOWER}а',
    (1, Number.PLURAL): f'безг{A_LOWER}',
    (2, Number.PLURAL): f'сезг{A_LOWER}',
    (3, Number.PLURAL): 'аларга',
}


class SoftVowel(StrEnum):
    A = A_LOWER
    E = 'e'
    Y = 'и'


class HardVowel(StrEnum):
    A = 'а'
    E = 'ы'
    Y = 'ый'


class VoicedConsonant(StrEnum):
    G = 'г'
    D = 'д'


class VoicelessConsonant(StrEnum):
    G = 'к'
    D = 'т'


NOUN_ACCUSATIVE_POSTFIXES = {
    Hardness.HARD: 'ны',
    Hardness.SOFT: 'не',
}

VERB_INFINITIVE_POSTFIXES = {
    CONSONANT: {
        Hardness.HARD: 'ырга',
        Hardness.SOFT: f'ерг{A_LOWER}',
    },
    VOWEL: {
        Hardness.HARD: 'арга',
        Hardness.SOFT: f'{A_LOWER}рг{A_LOWER}',
    }
}

VERB_POSSESSIVE_POSTFIXES = {
    Tense.PAST: {
        Hardness.HARD: {
            (1, Number.SINGULAR): 'м',
            (2, Number.SINGULAR): N_LOWER,
            (3, Number.SINGULAR): '',
            (1, Number.PLURAL): 'к',
            (2, Number.PLURAL): 'гыз',
            (3, Number.PLURAL): 'лар',
        },
        Hardness.SOFT: {
            (1, Number.SINGULAR): 'м',
            (2, Number.SINGULAR): N_LOWER,
            (3, Number.SINGULAR): '',
            (1, Number.PLURAL): 'к',
            (2, Number.PLURAL): 'гез',
            (3, Number.PLURAL): f'л{A_LOWER}р',
        },
    },
    Tense.PRESENT: {
        Hardness.HARD: {
            (1, Number.SINGULAR): 'м',
            (2, Number.SINGULAR): f'сы{N_LOWER}',
            (3, Number.SINGULAR): '',
            (1, Number.PLURAL): 'быз',
            (2, Number.PLURAL): 'сыз',
            (3, Number.PLURAL): 'лар',
        },
        Hardness.SOFT: {
            (1, Number.SINGULAR): 'м',
            (2, Number.SINGULAR): f'се{N_LOWER}',
            (3, Number.SINGULAR): '',
            (1, Number.PLURAL): 'без',
            (2, Number.PLURAL): 'сез',
            (3, Number.PLURAL): f'л{A_LOWER}р',
        },
    },
    Tense.FUTURE: {
        Hardness.HARD: {
            (1, Number.SINGULAR): 'мын',
            (2, Number.SINGULAR): f'сы{N_LOWER}',
            (3, Number.SINGULAR): '',
            (1, Number.PLURAL): 'быз',
            (2, Number.PLURAL): 'сыз',
            (3, Number.PLURAL): 'лар',
        },
        Hardness.SOFT: {
            (1, Number.SINGULAR): 'мен',
            (2, Number.SINGULAR): f'се{N_LOWER}',
            (3, Number.SINGULAR): '',
            (1, Number.PLURAL): 'без',
            (2, Number.PLURAL): 'сез',
            (3, Number.PLURAL): f'л{A_LOWER}р',
        },
    }
}
VERB_AFFIRMATIVE_POSTFIXES = {
    Tense.PRESENT: {
        CONSONANT: {
            Hardness.HARD: 'a',
            Hardness.SOFT: A_LOWER,
        },
        VOWEL: {
            Hardness.HARD: 'ый',
            Hardness.SOFT: 'и',
        }
    },
    Tense.FUTURE: {
        CONSONANT: {
            Hardness.HARD: 'ыр',
            Hardness.SOFT: 'ер',
        },
        VOWEL: {
            Hardness.HARD: 'р',
            Hardness.SOFT: 'р',
        }
    },
}

VERB_NEGATIVE_PRESENT_POSTFIXES = {
    Hardness.HARD: 'мый',
    Hardness.SOFT: 'ми',
}
VERB_NEGATIVE_PAST_POSTFIXES = {
    Hardness.HARD: 'ма',
    Hardness.SOFT: f'м{A_LOWER}',
}

VERB_PAST_POSTFIXES = {
    Hardness.HARD: {Sonority.VOICED: 'ды', Sonority.VOICELESS: 'ты'},
    Hardness.SOFT: {Sonority.VOICED: 'де', Sonority.VOICELESS: 'те'},
}

VERB_NEGATIVE_FUTURE_POSTFIXES = {
    Hardness.HARD: {
        (1, Number.SINGULAR): 'мам',
        (2, Number.SINGULAR): f'массы{N_LOWER}',
        (3, Number.SINGULAR): 'мас',
        (1, Number.PLURAL): 'мабыз',
        (2, Number.PLURAL): 'массыз',
        (3, Number.PLURAL): 'маслар',
    },
    Hardness.SOFT: {
        (1, Number.SINGULAR): f'м{A_LOWER}м',
        (2, Number.SINGULAR): f'м{A_LOWER}ссе{N_LOWER}',
        (3, Number.SINGULAR): f'м{A_LOWER}с',
        (1, Number.PLURAL): f'м{A_LOWER}без',
        (2, Number.PLURAL): f'м{A_LOWER}ссез',
        (3, Number.PLURAL): f'м{A_LOWER}сл{A_LOWER}р',
    },
}


class TatarVerb:

    def __init__(self, imperative: str) -> None:
        self.imperative = imperative
        self.is_hardness = self._check_hardness()
        self.last_letter_type = self._get_last_letter_type()
        self.vowel = HardVowel if self.is_hardness else SoftVowel

    def conjugate(self):
        pass

    def _check_hardness(self) -> bool:
        hard_vowels, soft_vowels = 0, 0
        for letter in self.imperative:
            if letter.lower() in Hardness.HARD_VOWELS:
                hard_vowels += 1
            if letter.lower() in Hardness.SOFT_VOWELS:
                soft_vowels += 1
        return hard_vowels >= soft_vowels

    def _get_last_letter_type(self) -> str:
        if self.imperative[-1] in VOICED_CONSONANTS:
            return Sonority.VOICED
        if self.imperative[-1] in VOICELESS_CONSONANTS:
            return Sonority.VOICELESS
        return VOWEL

    def _get_question_present(self):
        return f'м{self.vowel.E}'

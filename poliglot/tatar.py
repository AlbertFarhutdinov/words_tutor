HARD = 'hard'
SOFT = 'soft'

VOICED = 'voiced'
VOICELESS = 'voiceless'

NASAL = 'nasal'
NON_NASAL = 'non_nasal'

SINGULAR = 'singular'
PLURAL = 'plural'

PRESENT = 'present'
PAST = 'past'
FUTURE = 'future'

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

HARD_VOWELS = {'а', 'о', 'у', 'ы', 'э'}
SOFT_VOWELS = {A_LOWER, 'е', 'ё', 'и', O_LOWER, U_LOWER, 'ю', 'я'}
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
    (1, SINGULAR): 'мин',
    (2, SINGULAR): 'cин',
    (3, SINGULAR): 'ул',
    (1, PLURAL): 'без',
    (2, PLURAL): 'сез',
    (3, PLURAL): 'алар',
}
PRONOUNS_ACCUSATIVE = {
    (1, SINGULAR): 'мине',
    (2, SINGULAR): 'cине',
    (3, SINGULAR): f'а{N_LOWER}ы',
    (1, PLURAL): 'безне',
    (2, PLURAL): 'сезне',
    (3, PLURAL): 'аларны',
}
PRONOUNS_DATIVE = {
    (1, SINGULAR): f'ми{N_LOWER}a',
    (2, SINGULAR): f'cи{N_LOWER}а',
    (3, SINGULAR): f'а{N_LOWER}а',
    (1, PLURAL): f'безг{A_LOWER}',
    (2, PLURAL): f'сезг{A_LOWER}',
    (3, PLURAL): 'аларга',
}



vowel_alternations = [
    {HARD: 'а', SOFT: A_LOWER},
    {HARD: 'ы', SOFT: 'e'},
    {HARD: 'ый', SOFT: 'и'},
]
consonant_alternations = [
    {VOICED: 'г', VOICELESS: 'к'},
    {VOICED: 'д', VOICELESS: 'т'},
]


VERB_INFINITIVE_POSTFIXES = {
    CONSONANT: {
        HARD: 'ырга',
        SOFT: f'ерг{A_LOWER}',
    },
    VOWEL: {
        HARD: 'арга',
        SOFT: f'{A_LOWER}рг{A_LOWER}',
    }
}


VERB_POSSESIVE_PRESENT_POSTFIXES = {
    HARD: {
        (1, SINGULAR): 'м',
        (2, SINGULAR): f'сы{N_LOWER}',
        (3, SINGULAR): '',
        (1, PLURAL): 'быз',
        (2, PLURAL): 'сыз',
        (3, PLURAL): 'лар',
    },
    SOFT: {
        (1, SINGULAR): 'м',
        (2, SINGULAR): f'се{N_LOWER}',
        (3, SINGULAR): '',
        (1, PLURAL): 'без',
        (2, PLURAL): 'сез',
        (3, PLURAL): f'л{A_LOWER}р',
    },
}

VERB_AFFIRMATIVE_PRESENT_POSTFIXES = {
    CONSONANT: {
        HARD: 'a',
        SOFT: A_LOWER,
    },
    VOWEL: {
        HARD: 'ый',
        SOFT: 'и',
    }
}


VERB_NEGATIVE_PRESENT_POSTFIXES = {
    HARD: 'мый',
    SOFT: 'ми',
}


VERB_QUESTION_POSTFIXES = {
    HARD: 'мы',
    SOFT: 'ме',
}


VERB_PAST_POSTFIXES = {
    HARD: {VOICED: 'ды', VOICELESS: 'ты'},
    SOFT: {VOICED: 'де', VOICELESS: 'те'},
}


VERB_POSSESIVE_PAST_POSTFIXES = {
    HARD: {
        (1, SINGULAR): 'м',
        (2, SINGULAR): N_LOWER,
        (3, SINGULAR): '',
        (1, PLURAL): 'к',
        (2, PLURAL): 'гыз',
        (3, PLURAL): 'лар',
    },
    SOFT: {
        (1, SINGULAR): 'м',
        (2, SINGULAR): N_LOWER,
        (3, SINGULAR): '',
        (1, PLURAL): 'к',
        (2, PLURAL): 'гез',
        (3, PLURAL): f'л{A_LOWER}р',
    },
}


VERB_NEGATIVE_PAST_POSTFIXES = {
    HARD: 'ма',
    SOFT: f'м{A_LOWER}',
}



NOUN_ACCUSATIVE_POSTFIXES = {
    HARD: 'ны',
    SOFT: 'не',
}

VERB_AFFIRMATIVE_FUTURE_POSTFIXES = {
    CONSONANT: {
        HARD: 'ыр',
        SOFT: 'ер',
    },
    VOWEL: {
        HARD: 'р',
        SOFT: 'р',
    }
}


VERB_POSSESIVE_FUTURE_POSTFIXES = {
    HARD: {
        (1, SINGULAR): 'мын',
        (2, SINGULAR): f'сы{N_LOWER}',
        (3, SINGULAR): '',
        (1, PLURAL): 'быз',
        (2, PLURAL): 'сыз',
        (3, PLURAL): 'лар',
    },
    SOFT: {
        (1, SINGULAR): 'мен',
        (2, SINGULAR): f'се{N_LOWER}',
        (3, SINGULAR): '',
        (1, PLURAL): 'без',
        (2, PLURAL): 'сез',
        (3, PLURAL): f'л{A_LOWER}р',
    },
}


VERB_NEGATIVE_FUTURE_POSTFIXES = {
    HARD: {
        (1, SINGULAR): 'мам',
        (2, SINGULAR): f'массы{N_LOWER}',
        (3, SINGULAR): 'мас',
        (1, PLURAL): 'мабыз',
        (2, PLURAL): 'массыз',
        (3, PLURAL): 'маслар',
    },
    SOFT: {
        (1, SINGULAR): f'м{A_LOWER}м',
        (2, SINGULAR): f'м{A_LOWER}ссе{N_LOWER}',
        (3, SINGULAR): f'м{A_LOWER}с',
        (1, PLURAL): f'м{A_LOWER}без',
        (2, PLURAL): f'м{A_LOWER}ссез',
        (3, PLURAL): f'м{A_LOWER}сл{A_LOWER}р',
    },
}


class TatarVerb:

    def __init__(self, imperative: str) -> None:
        self.imperative = imperative
        self.is_hard = self.check_hardness()
        self.is_hard = self.check_hardness()

    def check_hardness(self) -> bool:
        hard_vowels, soft_vowels = 0, 0
        for letter in self.imperative:
            if letter.lower() in HARD_VOWELS:
                hard_vowels += 1
            if letter.lower() in SOFT_VOWELS:
                soft_vowels += 1
        return hard_vowels >= soft_vowels

    def get_last_letter_type(self) -> bool:
        if self.imperative[-1] in VOICED_CONSONANTS:
            return VOICED
        if self.imperative[-1] in VOICELESS_CONSONANTS:
            return VOICELESS
        return VOWEL

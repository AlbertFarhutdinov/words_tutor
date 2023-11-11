"""
This module contains constants that are used in this project.

COMING_BACK_TIME
    The time in days that must pass since the last repetition
    of the learned word to return it to the list of unlearned words.
WORD
    Vocabulary key for english words.
TRANSCRIPTION
    Vocabulary key for transcriptions of english words.
TRANSLATION
    Vocabulary key for russian translations of english words.
SUCCESS_NUMBER
    Vocabulary key for numbers of successful repetitions of english words.
LEARNING_DATE
    Vocabulary key for dates from which english words is considered as learned.

"""


DEFAULT_STRING = ''
COMING_BACK_TIME = 90
WORD = 'word'
TRANSCRIPTION = 'transcription'
TRANSLATION = 'translation'
SUCCESS_NUMBER = 'success_number'
LEARNING_DATE = 'learning_date'

EN = 'english'
RU = 'russian'
PL = 'polish'
FR = 'french'

LANGUAGES = [EN, RU, PL, FR]

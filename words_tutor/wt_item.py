import constants as con
from pydantic import BaseModel


class WTItem(BaseModel):
    """
    Class containing english word, its transcription, translation,
    number of successful repetitions and learning date.

    Attributes
    ----------
    vocabulary : list, optional
        List of dicts containing words, its transcriptions, translations,
        numbers of successful repetitions and learning dates.
    index : int, optional
        Index of required dict in `vocabulary`.
    word : str
        English word to be learned.
    transcription : str
        Transcription of the word to be learned.
    translation : str
        Translation of the word to be learned.
    success_number : int
        Number of successful repetitions of the word.
    learning_date : str
        Date from which the word is considered as learned.

    """
    vocabulary: list[dict[str, str | int]] = [{}]
    index: int = 0
    word: str = '?'
    transcription: str = '?'
    translation: str = '?'
    success_number: int = 0
    learning_date: str = ''

    def __post_init__(self) -> None:
        wt_item = self.vocabulary[self.index]
        self.word = wt_item.get(con.WORD, '')
        self.transcription = wt_item.get(con.TRANSCRIPTION, '')
        self.translation = wt_item.get(con.TRANSLATION, '')
        self.success_number = wt_item.get(con.SUCCESS_NUMBER, 0)
        self.learning_date = wt_item.get(con.LEARNING_DATE)

    def __str__(self) -> str:
        """Return the nicely printable string representation of instance."""
        return f'{self.word} [{self.transcription}] - {self.translation}'

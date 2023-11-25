from pydantic import BaseModel

import constants as con


class Word(BaseModel):
    id_: int
    language: str = con.EN
    word: str = con.DEFAULT_STRING
    transcription: str = con.DEFAULT_STRING
    translations: dict[str, int] = {}
    part_of_speech: str = con.DEFAULT_STRING

    def __str__(self) -> str:
        """Return the nicely printable string representation of instance."""
        if self.word == con.DEFAULT_STRING:
            return '? [?]'
        return f'{self.word} [{self.transcription}]'

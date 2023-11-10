from __future__ import annotations

from pydantic import BaseModel

import constants as con


class Word(BaseModel):
    language: str = con.EN
    word: str = '?'
    transcription: str = '?'
    translations: dict[str, Word] = '?'

    def __str__(self) -> str:
        """Return the nicely printable string representation of instance."""
        return f'{self.word} [{self.transcription}]'

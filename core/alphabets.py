from pydantic import BaseModel

from string import ascii_lowercase


class English(BaseModel):
    alphabet: str = ascii_lowercase
    consonants: str = 'bcdfghjklmnpqrstvwxz'
    vowels: str = 'aeiouy'


if __name__ == '__main__':
    print(English().alphabet)

from pathlib import Path

import pandas as pd


class MCW1000:

    def __init__(self, language: str) -> None:
        self.language = language
        self.vocabulary = pd.DataFrame()
        self.filename = Path(__file__).parents[1].joinpath(
            'vocabularies',
            'most_common_words1000',
            f'{self.language}.csv'
        )

    def download(self):
        pass
        # TODO implement parser for
        #  https://1000mostcommonwords.com/1000-most-common-{language}-words/

    def read(self) -> None:
        self.vocabulary = pd.read_csv(self.filename)

    def sort(self) -> None:
        self.vocabulary = self.vocabulary.sort_values(
            by='english',
        ).reset_index(drop=True)[['english', self.language]]

    def lowercase(self) -> None:
        self.vocabulary[self.language] = (
            self.vocabulary[self.language].str.lower()
        )

    def save(self) -> None:
        self.vocabulary.to_csv(self.filename, index=False)


if __name__ == '__main__':
    for lng in ('azerbaijani', 'russian', 'polish', 'french', 'tatar'):
        mcw = MCW1000(language=lng)
        mcw.read()
        mcw.sort()
        mcw.lowercase()
        mcw.save()

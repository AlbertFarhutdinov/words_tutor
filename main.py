from random import randint
import sys
import time
from typing import Dict, List, Optional, Tuple, Union

import pandas as pd


# TODO: add "try-except" statements for sys.args
# TODO: add mode 'rus -> eng'
# TODO: add date for "learned" word and its comeback after the specified time
# TODO: add processing of words in parenthesis, other forms etc.
# TODO: add documentation and type hints.


def get_args() -> Tuple[str, int]:
    filename, max_success_number = None, None
    if len(sys.argv) == 3:
        if sys.argv[1].isdigit():
            filename, max_success_number = sys.argv[2], int(sys.argv[1])
        elif sys.argv[2].isdigit():
            filename, max_success_number = sys.argv[1], int(sys.argv[2])
    return filename, max_success_number


def process_answer(answer: str):
    return answer.strip().lower().replace('ё', 'е')


class WTItem:

    def __init__(
            self,
            vocabulary: Optional[List[Dict[str, Union[str, int]]]] = None,
            index: Optional[int] = None,
    ) -> None:
        if vocabulary is None and index is None:
            vocabulary = [{}]
            index = 0
        self.word = vocabulary[index].get('word')
        self.pronunciation = vocabulary[index].get('pronunciation')
        self.transcription = vocabulary[index].get('transcription')
        self.success_number = vocabulary[index].get('successes')

    def __repr__(self):
        pass

    def __str__(self):
        pass


class WordsTutor:

    def __init__(
            self,
            filename: str,
            max_success_number: int,
    ):
        self.filename = filename
        self.max_success_number = max_success_number
        self.vocabulary_frame = pd.read_csv(filename, sep=';')
        self.vocabulary = self.vocabulary_frame.to_dict(orient='records')

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def get_random_item(self, index: int):
        if self.vocabulary[index]:
            if self.vocabulary[index]['successes'] < self.max_success_number:
                return WTItem(
                    vocabulary=self.vocabulary,
                    index=index,
                )
            return WTItem()
        return WTItem()

    def run(self) -> None:
        size = len(self.vocabulary)
        old_index = 0
        old_item = self.get_random_item(index=old_index)
        is_last_wrong = False
        print('Start.')
        while True:
            try:
                index = randint(0, len(self.vocabulary) - 1)
                item = self.get_random_item(index=index)
                if item.word:
                    right_answers = item.transcription.split(',')
                    for i, right_answer in enumerate(right_answers):
                        right_answers[i] = process_answer(right_answer)

                    print(f"\nWord: {item.word}.")
                    time.sleep(0.5)
                    answer = process_answer(input('Input translation: '))
                    if answer == '-1':
                        break

                    if answer == '+' and is_last_wrong:
                        old_item.success_number += 2
                        print(
                            f"Word: {old_item.word}. "
                            f"Successes: {old_item.success_number}"
                        )
                        self.vocabulary_frame.loc[
                            old_index,
                            'successes'
                        ] = old_item.success_number
                        if old_item.success_number >= self.max_success_number:
                            print(
                                f'Word `{old_item.word}` will be skipped.'
                            )
                            old_item = None

                        print(f"\nWord: {item.word}.")
                        time.sleep(0.5)
                        answer = process_answer(input('Input translation: '))
                        if answer == '-1':
                            break

                    if answer in right_answers:
                        print(f'Right! Pronunciation: {item.pronunciation}')
                        is_last_wrong = False
                        item.success_number += 1
                        self.vocabulary_frame.loc[
                            index,
                            'successes',
                        ] = item.success_number
                        if item.success_number >= self.max_success_number:
                            print(f'Word `{item.word}` will be skipped.')
                            # item = WTItem()
                            continue
                    else:
                        is_last_wrong = True
                        print(
                            f'Wrong! Right answer: {right_answers}. '
                            f'Pronunciation: {item.pronunciation}.'
                        )
                        item.success_number -= 1
                        if answer == '':
                            item.success_number -= 1
                        self.vocabulary_frame.loc[
                            index,
                            'successes',
                        ] = item.success_number
                    print(f"Successes: {item.success_number}")
                    old_index = index
                    old_item = self.get_random_item(index=old_index)
            except Exception:
                break

        points = (
                self.vocabulary_frame['successes'] >= self.max_success_number
        ).sum()
        print(f'Learned words: {points}/{size}')
        while True:
            try:
                self.vocabulary_frame.to_csv(
                    self.filename,
                    sep=';',
                    index=False,
                )
            except PermissionError:
                input(f'Close the file {self.filename} and press Enter.')
            else:
                self.vocabulary_frame.to_csv(
                    self.filename,
                    sep=';',
                    index=False,
                )
                break
    
    
if __name__ == '__main__':
    FILENAME, MAX_SUCCESS_NUMBER = get_args()
    WordsTutor(filename=FILENAME, max_success_number=MAX_SUCCESS_NUMBER).run()

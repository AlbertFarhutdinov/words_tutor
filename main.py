from datetime import date
from random import randint
import os
import sys
import time
from typing import Dict, List, Optional, Union

import pandas as pd

import constants as con


# TODO: add mode 'rus -> eng'
# TODO: add processing of words in parenthesis, other forms etc.
# TODO: add documentation and type hints.


# sys.tracebacklimit = 0


def get_answer():
    return input('Input translation: ')


def process_answer(answer: str):
    return answer.strip().lower().replace('ё', 'е')


class WTItem:

    def __init__(
            self,
            vocabulary: Optional[List[Dict[str, Union[str, int]]]] = None,
            index: Optional[int] = None,
    ) -> None:
        self.vocabulary = vocabulary
        self.index = index
        if vocabulary is None and index is None:
            vocabulary = [{}]
            index = 0
        self.word = vocabulary[index].get(con.WORD)
        self.transcription = vocabulary[index].get(con.TRANSCRIPTION)
        self.translation = vocabulary[index].get(con.TRANSLATION)
        self.success_number = vocabulary[index].get(con.SUCCESS_NUMBER)
        self.learning_date = vocabulary[index].get(con.LEARNING_DATE)

    def __repr__(self):
        return ''.join([
            f'{self.__class__.__name__}('
            f'vocabulary={self.vocabulary!r}',
            ', '
            f'index={self.index!r}',
            ')'
        ])

    def __str__(self):
        return f'{self.word} [{self.transcription}] - {self.translation}'


class WordsTutor:

    def __init__(
            self,
            filename: str = '',
            max_success_number: Optional[int] = None,
    ):
        self.filename = filename
        self.vocabulary_frame = (
            pd.read_csv(filename, sep=';')
            if filename
            else pd.DataFrame()
        )
        self.vocabulary = self.vocabulary_frame.to_dict(orient='records')
        self.max_success_number = max_success_number

    @property
    def vocabulary_size(self):
        return len(self.vocabulary)

    def __repr__(self):
        return ''.join([
            f'{self.__class__.__name__}('
            f'filename={self.filename!r}',
            ', '
            f'max_success_number={self.max_success_number!r}',
            ')'
        ])

    def get_random_item(self, index: int):
        if self.vocabulary[index]:
            item = WTItem(
                vocabulary=self.vocabulary,
                index=index,
            )
            if str(item.learning_date) not in ('', 'None', 'nan'):
                learning_date = item.learning_date.split('-')
                learning_date = date(
                    year=int(learning_date[0]),
                    month=int(learning_date[1]),
                    day=int(learning_date[2]),
                )
                if (date.today() - learning_date).days > con.COMING_BACK_TIME:
                    print(
                        f'Word {item.word} is not repeated '
                        f'since {item.learning_date}. '
                        "It's time to repeat it."
                    )
                    item.learning_date = ''
                    item.success_number = 0
                    self.update_item_in_vocabulary(item=item)
                    self.update_item_in_frame(item=item)
            if item.success_number < self.max_success_number:
                return item
            return WTItem()
        return WTItem()

    def print_result(self) -> None:
        points = (
                self.vocabulary_frame[con.SUCCESS_NUMBER]
                >= self.max_success_number
        ).sum()
        print(f'Learned words: {points}/{self.vocabulary_size}')

    def save_vocabulary(self) -> None:
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

    def update_item_in_vocabulary(
            self,
            item: WTItem,
    ) -> None:
        self.vocabulary[item.index][con.LEARNING_DATE] = item.learning_date
        self.vocabulary[item.index][con.SUCCESS_NUMBER] = item.success_number

    def update_item_in_frame(
            self,
            item: WTItem,
    ) -> None:
        self.vocabulary_frame.loc[
            item.index,
            con.LEARNING_DATE
        ] = item.learning_date
        self.vocabulary_frame.loc[
            item.index,
            con.SUCCESS_NUMBER
        ] = item.success_number

    def help(self):
        pass

    def run(self) -> None:
        old_item = self.get_random_item(index=0)
        is_last_wrong = False
        print('Start.')
        while True:
            try:
                index = randint(0, self.vocabulary_size - 1)
                item = self.get_random_item(index=index)
                if item.word:
                    right_answers = item.translation.split(',')
                    for i, right_answer in enumerate(right_answers):
                        right_answers[i] = process_answer(right_answer)

                    print(f"\nWord: {item.word}.")
                    time.sleep(0.5)
                    answer = process_answer(get_answer())
                    if answer == '-1':
                        break

                    if answer == '+' and is_last_wrong:
                        old_item.success_number += 2
                        print(
                            f"Word: {old_item.word}. "
                            f"Successes: {old_item.success_number}"
                        )
                        self.update_item_in_frame(item=old_item)
                        if old_item.success_number >= self.max_success_number:
                            print(
                                f'Word `{old_item.word}` will be skipped.'
                            )
                            old_item = None

                        print(f"\nWord: {item.word}.")
                        time.sleep(0.5)
                        answer = process_answer(get_answer())
                        if answer == '-1':
                            break

                    if answer in right_answers:
                        print(f'Right! Pronunciation: {item.transcription}')
                        is_last_wrong = False
                        item.success_number += 1
                        self.update_item_in_frame(item=item)
                        if item.success_number >= self.max_success_number:
                            print(f'Word `{item.word}` will be skipped.')
                            continue
                    else:
                        is_last_wrong = True
                        print(
                            f'Wrong! Right answer: {right_answers}. '
                            f'Pronunciation: {item.transcription}.'
                        )
                        item.success_number -= 1
                        if answer == '':
                            item.success_number -= 1
                        self.update_item_in_frame(item=item)
                    print(f"Successes: {item.success_number}")
                    old_item = self.get_random_item(index=index)
            except (IndexError, KeyError, TypeError, ValueError,) as error:
                print(error)
                print(error.args)
                break

        self.print_result()
        self.save_vocabulary()


def main():
    try:
        command = sys.argv[1]
    except IndexError:
        print('Name of command is absent.')
        sys.exit(1)
    if command not in ('help', 'run'):
        print('Unacceptable name of command.')
        sys.exit(1)

    if command == 'help':
        WordsTutor().help()
    else:
        try:
            filename = sys.argv[2]
        except IndexError:
            print('Filename is absent.')
            sys.exit(1)
        filename = os.path.join(os.getcwd(), filename)
        if not os.path.isfile(filename):
            print(f'File with name `{filename}` is not found.')
            sys.exit(1)

        try:
            max_success_number = sys.argv[3]
        except IndexError:
            print('Maximum value of successes for one word is absent.')
            sys.exit(1)
        if not (max_success_number.isdigit() and int(max_success_number) > 0):
            print('Maximum value of successes must be positive number.')
            sys.exit(1)
        max_success_number = int(max_success_number)

        WordsTutor(
            filename=filename,
            max_success_number=max_success_number,
        ).run()


if __name__ == '__main__':
    main()

import logging
from datetime import date
from random import randint
from time import sleep

import constants as con
import pandas as pd
from answer_processor import AnswerProcessor
from wt_item import WTItem


class WordsTutor:
    """
    Class for learning English words by Russian speakers.

    Attributes
    ----------
    filename : str, optional, default: ''
        Name of the file with words, translations and other information.
        If it is not specified, empty DataFrame is created.
    max_success_number : int, optional
        The number of successful repetitions for word
        after which it is considered as learned.
    vocabulary_frame: DataFrame
        A table containing words, its transcriptions, translations,
        numbers of successful repetition and learning dates.
    vocabulary: dict
        List of dicts containing words, its transcriptions, translations,
        numbers of successful repetition and learning dates.

    Methods
    -------
    get_item(index: int) -> WTItem:
        Return `WTItem` instance for item in `vocabulary` attribute
        with specified index.
    help()
        Get help on using `WordsTutor` instances.
    print_result()
        Print result of training.
    run()
        Run training.
    save_vocabulary()
        Save updated vocabulary to the file.

    """

    def __init__(
        self,
        filename: str = '',
        max_success_number: int | None = None,
    ) -> None:
        """
        Initialization of `WordsTutor` instance.

        Parameters
        ----------
        filename : str, optional, default: ''
            Name of the file with words, translations and other information.
            If it is not specified, empty DataFrame is created.
        max_success_number : int, optional
            The number of successful repetitions for word
            after which it is considered as learned.

        """
        self.filename = filename
        self.max_success_number = max_success_number
        if filename:
            self.vocabulary_frame = pd.read_csv(filename, sep=';')
        else:
            self.vocabulary_frame = pd.DataFrame()

        self.vocabulary = self.vocabulary_frame.to_dict(orient='records')

    @property
    def vocabulary_size(self) -> int:
        """Return size of `self.vocabulary`."""
        return len(self.vocabulary)

    def __repr__(self) -> str:
        """Return the 'official' string representation of instance."""
        return ''.join([
            f'{self.__class__.__name__}('
            f'filename={self.filename!r}',
            ', '
            f'max_success_number={self.max_success_number!r}',
            ')',
        ])

    def get_item(self, index: int) -> WTItem:
        """
        Return `WTItem` instance
        for item in `self.vocabulary` with specified index.

        """
        if self.vocabulary[index]:
            wt_item = WTItem(
                vocabulary=self.vocabulary,
                index=index,
            )
            if str(wt_item.learning_date) not in ('', 'None', 'nan'):
                learning_date = wt_item.learning_date.split('-')
                learning_date = date(
                    year=int(learning_date[0]),
                    month=int(learning_date[1]),
                    day=int(learning_date[2]),
                )
                if (date.today() - learning_date).days > con.COMING_BACK_TIME:
                    msg = (
                        f'Word {wt_item.word} is not repeated '
                        f'since {wt_item.learning_date}. '
                        "It's time to repeat it."
                    )
                    logging.info(msg)
                    wt_item.learning_date = ''
                    wt_item.success_number = 0
                    self.__update_item_in_vocabulary(item=wt_item)
                    self.__update_item_in_frame(item=wt_item)
            if wt_item.success_number < self.max_success_number:
                return wt_item
            return WTItem()
        return WTItem()

    def print_result(self) -> None:
        """Print result of training."""
        points = (
                self.vocabulary_frame[con.SUCCESS_NUMBER]
                >= self.max_success_number
        ).sum()
        logging.info(f'Learned words: {points}/{self.vocabulary_size}')

    def save_vocabulary(self) -> None:
        """Save updated vocabulary to the file."""
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

    def run(self) -> None:
        """Run training."""
        old_item = self.get_item(index=0)
        is_last_wrong = False
        logging.info('Start.')
        while True:
            try:
                index = randint(0, self.vocabulary_size - 1)
                item = self.get_item(index=index)
                if item.word:
                    right_answers = item.translation.split(',')
                    for i, right_answer in enumerate(right_answers):
                        right_answers[i] = AnswerProcessor(
                            answer=right_answer,
                        ).get_processed()

                    msg = f'\nWord: {item.word}.'
                    logging.info(msg)
                    sleep(0.5)
                    answer = AnswerProcessor().get_processed()
                    if answer == '-1':
                        break

                    if answer == '+' and is_last_wrong:
                        old_item.success_number += 2
                        msg = (
                            f'Word: {old_item.word}. '
                            f'Successes: {old_item.success_number}'
                        )
                        logging.info(msg)
                        self.__update_item_in_frame(item=old_item)
                        if old_item.success_number >= self.max_success_number:
                            msg = f'Word `{old_item.word}` will be skipped.'
                            logging.info(msg)
                            old_item = None

                        msg = f'\nWord: {item.word}.'
                        logging.info(msg)
                        sleep(0.5)
                        answer = AnswerProcessor().get_processed()
                        if answer == '-1':
                            break

                    if answer in right_answers:
                        msg = f'Right! Pronunciation: {item.transcription}'
                        logging.info(msg)
                        is_last_wrong = False
                        item.success_number += 1
                        self.__update_item_in_frame(item=item)
                        if item.success_number >= self.max_success_number:
                            msg = f'Word `{item.word}` will be skipped.'
                            logging.info(msg)
                            continue
                    else:
                        is_last_wrong = True
                        msg = (
                            f'Wrong! Right answer: {right_answers}. '
                            f'Pronunciation: {item.transcription}.'
                        )
                        logging.info(msg)
                        item.success_number -= 1
                        if answer == '':
                            item.success_number -= 1
                        self.__update_item_in_frame(item=item)
                    msg = f'Successes: {item.success_number}'
                    logging.info(msg)
                    old_item = self.get_item(index=index)
            except (IndexError, KeyError, TypeError, ValueError) as error:
                msg = f'{error} ({error.args})'
                logging.error(msg)
                break

        self.print_result()
        self.save_vocabulary()

    def __update_item_in_vocabulary(
        self,
        item: WTItem,
    ) -> None:
        """
        Update learning date and number of successful repetitions
        for the word in `self.vocabulary`
        corresponding to the specified `WTItem` instance.

        """
        self.vocabulary[item.index][con.LEARNING_DATE] = item.learning_date
        self.vocabulary[item.index][con.SUCCESS_NUMBER] = item.success_number

    def __update_item_in_frame(
        self,
        item: WTItem,
    ) -> None:
        """
        Update learning date and number of successful repetitions
        for the word in `self.vocabulary_frame`
        corresponding to the specified `WTItem` instance.

        """
        self.vocabulary_frame.loc[
            item.index,
            con.LEARNING_DATE,
        ] = item.learning_date
        self.vocabulary_frame.loc[
            item.index,
            con.SUCCESS_NUMBER,
        ] = item.success_number

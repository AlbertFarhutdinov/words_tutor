"""The script to run a console application for learning words."""

import logging
import os
import sys

from words_tutor.core import WordsTutor

# TODO: add mode 'rus -> eng'
# TODO: add processing of words in parenthesis, other forms etc.


sys.tracebacklimit = 0


def main() -> None:
    """Create `WordsTutor` instance and run the training."""
    try:
        command = sys.argv[1]
    except IndexError:
        logging.error('Name of command is absent.')
        sys.exit(1)
    if command not in {'help', 'run'}:
        logging.error('Unacceptable name of command.')
        sys.exit(1)

    if command == 'help':
        WordsTutor().help()
    else:
        try:
            filename = sys.argv[2]
        except IndexError:
            logging.error('Filename is absent.')
            sys.exit(1)
        filename = os.path.join(os.getcwd(), filename)
        if not os.path.isfile(filename):
            msg = 'File with name `{0} is not found.'.format(filename)
            logging.error(msg)
            sys.exit(1)

        try:
            max_success_number = sys.argv[3]
        except IndexError:
            logging.error('Maximum value of successes for one word is absent.')
            sys.exit(1)
        if not (max_success_number.isdigit() and int(max_success_number) > 0):
            logging.error(
                'Maximum value of successes must be positive number.',
            )
            sys.exit(1)
        max_success_number = int(max_success_number)

        WordsTutor(
            filename=filename,
            max_success_number=max_success_number,
        ).run()


if __name__ == '__main__':
    main()

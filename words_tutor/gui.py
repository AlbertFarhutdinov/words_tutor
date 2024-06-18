import csv
import random
import sys

import PyQt6.QtWidgets as QtW
from PyQt6.QtCore import Qt


class WordTrainer(QtW.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('English-Russian Word Trainer')
        self.setGeometry(100, 100, 500, 250)

        self.words = self.load_words('words.csv')
        self.current_word = None
        self.translation_direction = 'en_to_ru'

        self.score = 0
        self.total_attempts = 0

        self.direction_button = QtW.QPushButton(
            'Switch to Russian to English',
            self,
        )
        self._connect(
            signal=self.direction_button.clicked,
            action=self.switch_direction,
        )

        self.label = QtW.QLabel('Translate the word:', self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.word_label = QtW.QLabel('', self)
        self.word_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word_label.setStyleSheet('font-size: 20px;')

        self.input = QtW.QLineEdit(self)
        self.input.setPlaceholderText('Enter translation here')

        self.check_button = QtW.QPushButton('Check', self)
        self._connect(
            signal=self.check_button.clicked,
            action=self.check_translation,
        )

        self.next_button = QtW.QPushButton('Next', self)
        self._connect(
            signal=self.next_button.clicked,
            action=self.next_word,
        )

        self.score_label = QtW.QLabel('Score: 0/0', self)
        self.score_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QtW.QVBoxLayout()
        layout.addWidget(self.direction_button)
        layout.addWidget(self.label)
        layout.addWidget(self.word_label)
        layout.addWidget(self.input)
        layout.addWidget(self.check_button)
        layout.addWidget(self.next_button)
        layout.addWidget(self.score_label)

        container = QtW.QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.next_word()

    @staticmethod
    def _connect(signal, action):
        getattr(signal, 'connect')(action)

    @staticmethod
    def load_words(filename):
        words = []
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                english, russian = row
                words.append((english.strip(), russian.strip()))
        return words

    def switch_direction(self):
        if self.translation_direction == 'en_to_ru':
            self.translation_direction = 'ru_to_en'
            self.direction_button.setText('Switch to English to Russian')
        else:
            self.translation_direction = 'en_to_ru'
            self.direction_button.setText('Switch to Russian to English')
        self.next_word()

    def next_word(self):
        self.current_word = random.choice(self.words)
        if self.translation_direction == 'en_to_ru':
            self.word_label.setText(self.current_word[0])
        else:
            self.word_label.setText(self.current_word[1])
        self.input.clear()

    def check_translation(self):
        user_translation = self.input.text().strip().lower()
        if self.translation_direction == 'en_to_ru':
            correct_translation = self.current_word[1].strip().lower()
        else:
            correct_translation = self.current_word[0].strip().lower()

        self.total_attempts += 1

        if user_translation == correct_translation:
            self.score += 1
            QtW.QMessageBox.information(
                self,
                'Correct!',
                'Your translation is correct!',
            )
        else:
            QtW.QMessageBox.warning(
                self,
                'Incorrect',
                f'Your translation is incorrect. '
                f'The correct translation is "{correct_translation}".',
            )

        self.update_score()
        self.next_word()

    def update_score(self):
        self.score_label.setText(f'Score: {self.score}/{self.total_attempts}')


if __name__ == '__main__':
    app = QtW.QApplication(sys.argv)
    window = WordTrainer()
    window.show()
    sys.exit(app.exec())

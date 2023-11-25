class AnswerProcessor:

    def __init__(self, answer: str | None = None) -> None:
        self.answer = answer
        if not self.answer:
            self.answer = self.request()

    @staticmethod
    def request() -> str:
        """Return translation inputted by user for the specified word."""
        return input('Input translation: ')

    def get_processed(self) -> str:
        """Return processed answer inputted by user."""
        return self.answer.strip().lower().replace('ё', 'е')

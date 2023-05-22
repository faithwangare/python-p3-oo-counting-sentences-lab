import re

class MyString:
    def __init__(self, value=None):
        self._value = None
        if value is not None:
            self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
      if not self.value:
        return 0
      sentences = [sentence for sentence in re.split(r'[.!?]', self.value) if sentence]
      return len(sentences)

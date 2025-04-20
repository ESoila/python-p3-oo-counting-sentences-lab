#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')
  
    def is_question(self):
        return self.value.endswith('?')
  
    def is_exclamation(self):
        return self.value.endswith('!')  
  
    def count_sentences(self):
        sentences = re.split(r'[.!?]\s*', self.value.strip())
        sentences = [s for s in sentences if s]
        return len(sentences)
import os
import re

class InvertedIndex:

    def __init__(self):
        self.index = {}

    def tokenize(self, text):
        return re.findall(r'\w+', text.lower())

    def build_index(self, folder_path):

        for filename in os.listdir(folder_path):

            path = os.path.join(folder_path, filename)

            with open(path, 'r', encoding='utf-8') as file:

                text = file.read()

                words = self.tokenize(text)

                for word in words:

                    if word not in self.index:
                        self.index[word] = {}

                    if filename not in self.index[word]:
                        self.index[word][filename] = 0

                    self.index[word][filename] += 1

        return self.index
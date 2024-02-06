class GrammarStats:
    def __init__(self):
        self.ending_punctuation = ['.', '!', '?']
        self.tried = 0
        self.valid = 0
        pass

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if len(text) < 1:
            raise Exception("Must provide a text for validity check")
        elif text[0].isupper() and text[-1] in self.ending_punctuation:
            self.tried += 1
            self.valid += 1
            return True
        else:
            self.tried += 1
            return False

    def percentage_good(self):
        return int((self.valid / self.tried) * 100)
class GrammarStats:
    def __init__(self):
        self.ending_punctuation = ['.!?']
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
            return True
        else:
            return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass

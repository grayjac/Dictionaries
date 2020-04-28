import string
from sentiment import string_filter

test = 'This string is a string!'
fucker = test.translate(test.maketrans('', '', string.punctuation))

def open_txt(sentence='sentiment.txt'):
    with open(sentence) as fh:
        # Skip initial comments that starts with #
        while True:
            line = fh.readline()
            # break while statement if it is not a comment line
            # i.e. does not startwith #
            if not line.startswith('#') or line.strip():
                break

        # Second while loop to process the rest of the file
        while line:
            print(line)



#!/usr/bin/env python3


# ME499-S20 Python Lab 3
# Programmer: Jacob Gray
# Last Edit: 4/27/2020


import string
import sys


def load_score_dict(txt_file='sentiment.txt'):
    """
    This function takes a text file and returns a dictionary.
    :param txt_file: Text file to load.
    :return: Dictionary.
    """

    dictionary = {}

    with open(txt_file, 'r') as txt:
        for line in txt:
            if line.startswith("#") or not line.strip():
                continue

            (key, value) = line.split()
            dictionary[key] = float(value)

    return dictionary


def string_filter(sentence):
    """
    This function takes a string and converts all letters to lowercase and removes all punctuation defined by
    string.punctuation.
    :param sentence: String.
    :return: Returns a new filtered string.
    """

    filtered_sentence = sentence.translate(sentence.maketrans('', '', string.punctuation))

    return filtered_sentence.lower()


def get_words(sentence):
    """
    This function takes a sentence as a string and returns an iterable of unique words in the string.
    :param sentence: String.
    :return: List of unique words
    """

    filtered_sentence = string_filter(sentence)
    sentence_list = (list(filtered_sentence.split()))
    unique = []

    for i in range(len(sentence_list)):
        if sentence_list[i] not in unique:
            unique.append(sentence_list[i])

    return unique


def score_sentence(sentence, score_dictionary):
    """
    This function takes in a sentence in the form of a string and outputs and sums a score corresponding to
    the score dictionary for each unique word in the sentence. If the word isn't in the dictionary, the score is zero.
    :param sentence: String.
    :param score_dictionary: Where scores are stored for each unique word.
    :return: Sum of scores.
    """

    num_list = []
    sentence_list = get_words(sentence)

    for i in range(len(sentence_list)):
        if not sentence_list[i] in score_dictionary:
            num_list.append(0)
        else:
            num_list.append(score_dictionary[sentence_list[i]])

    return sum(num_list)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Please enter a name when calling this file')
        print(r"Example: PycharmProjects\Dictionaries\sentiment.py some_file.txt")
        sys.exit(0)

    file_name = str(sys.argv[1])

    with open(file_name, 'r') as txt:
        sentence = txt.read()

    if score_sentence(sentence, load_score_dict()) > 0:
        print('Positive')

    elif score_sentence(sentence, load_score_dict()) == 0:
        print('Neutral')

    else:
        print('Negative')

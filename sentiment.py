#!/usr/bin/env python3


# ME499-S20 Python Homework 1 Data Analysis
# Programmer: Jacob Gray
# Last Edit: 4/26/2020
from typing import TextIO


def load_score_dict(txt_file='sentiment.txt'):
    """
    This function takes a text file and returns a dictionary.
    :param txt_file: Text file to load.
    :return: Dictionary.
    """

    dictionary = {}

    with open(txt_file, 'r') as gross_txt:
        clean_txt = gross_txt.readlines()[3:]
        for line in clean_txt:
            (key, value) = line.split()
            dictionary[key] = float(value)

    return dictionary

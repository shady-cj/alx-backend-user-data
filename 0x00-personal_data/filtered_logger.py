#!/usr/bin/env python3
"""
This module contains a function named filter_datum
that returns the log message obfuscated:
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    The function uses a regex to replace occurrences
    of certain field values and
    returns the log message obfuscated.
    """
    new_message = message
    for field in fields:
        new_message = re.sub(r'({})=(.*?){}'.format(field, separator),
                             r"\1={}{}".format(redaction, separator),
                             new_message)
    return new_message

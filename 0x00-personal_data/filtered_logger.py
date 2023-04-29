#!/usr/bin/env python3
"""
This module contains a function named filter_datum
that returns the log message obfuscated:
"""
import re
import typing
import logging
import os
import mysql.connector


def filter_datum(fields: typing.List[str], redaction: str,
                 message: str, separator: str) -> str:
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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typing.List[str]):
        """
        Initializes the formatter with the required fields
        and calling the super() constructor to configure the
        FORMAT fields.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the record message based on the REDACTION, and FIELDs
        set in the constructor and returns the formatted log Record
        """
        formattedMessage = filter_datum(self.fields, self.REDACTION,
                                        record.getMessage(), self.SEPARATOR)
        record.msg = formattedMessage
        return super().format(record)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """
    Returns a logger
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)
    logger.propagate = False
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connects to a remote database and returns the connection pool.
    """
    DB_USERNAME = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    DB_HOST = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    DB_PASSWORD = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    DB_NAME = os.getenv('PERSONAL_DATA_DB_NAME', '')
    conn = mysql.connector.connect(user=DB_USERNAME, password=DB_PASSWORD,
                                   host=DB_HOST,
                                   database=DB_NAME)
    return conn


def main():
    """
    The function will obtain a database connection
    using get_db and retrieve all rows in
    the users table and display each row
    under a filtered format like this:
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()
    for row in cursor:
        message = "name={}; email={}; phone={}; ssn={}; \
password={}; ip={}; last_login={}; user_agent={};".format(
                                                    row[1],
                                                    row[2],
                                                    row[3],
                                                    row[4],
                                                    row[5],
                                                    row[6],
                                                    row[7],
                                                    row[8]
                                                    )
        logger.info(message)
    cursor.close()
    db.close()

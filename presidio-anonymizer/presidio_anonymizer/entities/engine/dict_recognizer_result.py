from dataclasses import dataclass
from typing import Iterator, List, Union

from presidio_anonymizer.entities import RecognizerResult


@dataclass
class DictRecognizerResult:
    """
    Data class for holding the output of the Presidio Analyzer on dictionaries.

    :param key: key in dictionary
    :param value: value to run analysis on (either string or list of strings)
    :param recognizer_results: Analyzer output for one value.
    Could be either:
     - A list of recognizer results if the input is one string
     - A list of lists of recognizer results, if the input is a list of strings.
     - An iterator of a DictRecognizerResult, if the input is a dictionary.
     In this case the recognizer_results would be the iterator
     of the DictRecognizerResult next level in the dictionary.
    """

    key: str
    value: Union[str, List[str], dict]
    recognizer_results: Union[
        List[RecognizerResult],
        List[List[RecognizerResult]],
        Iterator["DictRecognizerResult"],
    ]

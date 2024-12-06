from enum import Enum as PyEnum


class WordType(PyEnum):
    NOUN = "noun"
    ADJECRIVE = "adjective"


class WordNumber(PyEnum):
    SINGULAR = "singular"
    PLURAL = "plural"


class WordGender(PyEnum):
    MASCULINE = "masculine"
    FEMININE = "feminine"
    NEUTER = "neuter"

from .case import Case
from .enums import WordGender, WordNumber, WordType
from .language import Language
from .words import WordForm, WordPattern

# This allows you to do: from app.models import Language, Case, etc.
__all__ = [
    "Case",
    "Language",
    "WordForm",
    "WordPattern",
    "WordGender",
    "WordNumber",
    "WordType",
]

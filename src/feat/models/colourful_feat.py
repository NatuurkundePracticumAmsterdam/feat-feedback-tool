from enum import Enum


class CheckboxSheet(Enum):
    STYLE_DEFAULT = None
    STYLE_POSITIVE = "color: rgb(34, 139, 34)"
    STYLE_SUGGESTION = "color: rgb(255, 172, 28)"
    STYLE_NEGATIVE = "color: rgb(210, 43, 43)"

    @classmethod
    def from_symbol(cls, symbol: str):
        if symbol == "+":
            return cls.STYLE_POSITIVE
        elif symbol == "~":
            return cls.STYLE_SUGGESTION
        elif symbol == "-":
            return cls.STYLE_NEGATIVE
        else:
            return cls.STYLE_DEFAULT


def extract_feedback_stylesheet(feedback_text: str) -> tuple[str | None, str]:
    """Extracts stylesheet for the checkbox of the feedback point corresponding to the positivity
    of the point and removes the encoding symbol from the text (if present).

    Args:
        feedback_text (str): feedback text with symbol encoding positivity of feedback point

    Returns:
        tuple[str|None,str]: stylesheet for textbox with correct colour (None if not present),
                             updated feedback_text with encoding symbol removed (if present)
    """
    symbol = feedback_text[0]
    stylesheet = CheckboxSheet.from_symbol(symbol).value

    if stylesheet is not None:
        extracted_feedback = feedback_text[1:]
    else:
        extracted_feedback = feedback_text

    return stylesheet, extracted_feedback

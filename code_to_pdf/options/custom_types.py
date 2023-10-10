"""Custom types to be used in options for validation."""

from typing import Annotated, Literal

from pydantic import AfterValidator, StringConstraints
from pygments.styles import STYLE_MAP


def is_pygments_style(value: str) -> str:
    """Return whether `string` is a valid pygments style."""

    assert (
        value in STYLE_MAP
    ), "Not a valid style (see https://pygments.org/styles/)"
    return value


PygmentsStyle = Annotated[str, AfterValidator(is_pygments_style)]
FontSize = Literal["10pt", "11pt", "12pt"]
Margin = Annotated[str, StringConstraints(pattern=r"^\d+(\.\d+)?in$")]

PaperSize = Literal[
    "a0paper",
    "a1paper",
    "a2paper",
    "a3paper",
    "a4paper",
    "a5paper",
    "a6paper",
    "b0paper",
    "b1paper",
    "b2paper",
    "b3paper",
    "b4paper",
    "b5paper",
    "b6paper",
    "c0paper",
    "c1paper",
    "c2paper",
    "c3paper",
    "c4paper",
    "c5paper",
    "c6paper",
    "b0j",
    "b1j",
    "b2j",
    "b3j",
    "b4j",
    "b5j",
    "b6j",
    "ansiapaper",
    "ansibpaper",
    "ansicpaper",
    "ansidpaper",
    "ansiepaper",
    "letterpaper",
    "executivepaper",
    "legalpaper",
]

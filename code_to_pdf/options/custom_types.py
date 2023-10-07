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

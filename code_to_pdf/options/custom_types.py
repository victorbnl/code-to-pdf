"""Custom types to be used in options for validation."""

from typing import Annotated, Literal

from pydantic import AfterValidator, StringConstraints
from pygments.styles import get_all_styles


def is_pygments_style(value: str) -> str:
    """Return whether `string` is a valid pygments style."""

    assert (
        value in get_all_styles()
    ), "Not a valid style (see https://pygments.org/styles/)"
    return value


Size = Annotated[str, StringConstraints(pattern=r"^\d+(\.\d+)?(in|cm)$")]

PygmentsStyle = Annotated[str, AfterValidator(is_pygments_style)]
FontSize = Literal["10pt", "11pt", "12pt"]
Paper = Annotated[
    str,
    StringConstraints(
        pattern=r"^((([a-c][0-6]|ansi[a-e]|letter|executive|legal)paper)|^(b[0-6]j))$"
    )
]

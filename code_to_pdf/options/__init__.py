"""Option data classes."""

from pydantic import BaseModel

from code_to_pdf.options.custom_types import FontSize, Margin, PygmentsStyle

short_aliases = {"style": "s"}


class Options(BaseModel):
    """
    Options for document generation.

    Attributes:
        style: pygments style (see https://pygments.org/styles/)
        font_size: document font size
        linenos: whether or not to display line numbers
        linenostep: if `linenos` is enabled, print every n-th line number
        top_margin: document top margin
        bottom_margin: document bottom margin
        left_margin: document left margin
        right_margin: document right margin
    """

    style: PygmentsStyle = "default"

    font_size: FontSize = "10pt"

    linenos: bool = False
    linenostep: int = 0

    top_margin: Margin = "0.4in"
    bottom_margin: Margin = "0.4in"
    left_margin: Margin = "0.5in"
    right_margin: Margin = "0.5in"

"""Option data classes."""

from pydantic import BaseModel

from code_to_pdf.options.custom_types import FontSize, Margin, PygmentsStyle

short_aliases = {"style": "s"}


class Options(BaseModel):
    """
    Options for document generation.

    Attributes:
        style: Pygments style (see https://pygments.org/styles/).
        font_size: Document font size.
        linenos: Whether or not to display line numbers.
        linenostep: If `linenos` is enabled, print every n-th line number.
        page_numbers: Whether or not to print page numbers.
        top_margin: Document top margin.
        bottom_margin: Document bottom margin.
        left_margin: Document left margin.
        right_margin: Document right margin.
    """

    style: PygmentsStyle = "default"

    font_size: FontSize = "10pt"

    linenos: bool = False
    linenostep: int = 0

    page_numbers: bool = False

    top_margin: Margin = "0.4in"
    bottom_margin: Margin = "0.4in"
    left_margin: Margin = "0.5in"
    right_margin: Margin = "0.5in"

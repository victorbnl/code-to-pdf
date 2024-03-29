"""Option data classes."""

from pydantic import BaseModel

from code_to_pdf.options.custom_types import (
    FontSize, Size, Paper, PygmentsStyle
)

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
        paper: Paper format of resulting document (`paper_width` and
               `paper_height`, when provided, both take precedence over
               `paper`).
        paper_width: Paper width of resulting document.
        paper_height: Paper height of resulting document.
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

    paper: Paper | None = None
    paper_width: Size | None = None
    paper_height: Size | None = None

    top_margin: Size = "0.4in"
    bottom_margin: Size = "0.4in"
    left_margin: Size = "0.5in"
    right_margin: Size = "0.5in"

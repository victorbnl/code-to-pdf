"""Option data classes."""

from pydantic import BaseModel

from code_to_pdf.custom_types import PygmentsStyle, FontSize, Margin


short_aliases = {
    'style': 's'
}


class StyleOptions(BaseModel):
    """
    Options related to document style.

    Attributes:
        style: pygments style (see https://pygments.org/styles/)
        font_size: document font size
        linenos: whether or not to display line numbers
        top_margin: document top margin
        bottom_margin: document bottom margin
        left_margin: document left margin
        right_margin: document right margin
    """

    style: PygmentsStyle = 'default'
    font_size: FontSize = '10pt'
    linenos: bool = False
    top_margin: Margin = '0.4in'
    bottom_margin: Margin = '0.4in'
    left_margin: Margin = '0.5in'
    right_margin: Margin = '0.5in'

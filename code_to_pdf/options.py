"""Option data classes."""

from dataclasses import dataclass


short_aliases = {
    'style': 's'
}


@dataclass
class StyleOptions:
    """
    Options related to document style.

    Attributes:
        style: pygments style (see https://pygments.org/styles/)
        font_size: document font size
        top_margin: document top margin
        bottom_margin: document bottom margin
        left_margin: document left margin
        right_margin: document right margin
    """

    style: str = 'default'
    font_size: str = '10pt'
    top_margin: str = '0.4in'
    bottom_margin: str = '0.4in'
    left_margin: str = '0.5in'
    right_margin: str = '0.5in'

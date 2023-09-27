"""
Builds LaTeX from source code.
"""

from pygments import highlight
from pygments.lexers import guess_lexer, guess_lexer_for_filename
from pygments.formatters import LatexFormatter
from pygments.styles import get_style_by_name


class LatexBuilder:
    """
    Builds LaTeX from source code.
    """

    def __init__(self, style: str = 'default'):

        self.style = style

    def __build_preamble(self):

        top_margin = 0.3
        bottom_margin = 0.3
        right_margin = 0.5
        left_margin = 0.5

        style = get_style_by_name(self.style)
        background = style.background_color[1:]

        preamble = f"""
            \\usepackage[
                top={top_margin}in,
                bottom={bottom_margin}in,
                right={right_margin}in,
                left={left_margin}in
            ]{{geometry}}

            \\usepackage[dvipsnames]{{xcolor}}
            \\definecolor{{background}}{{HTML}}{{{background}}}
            \\pagecolor{{background}}

            \\pagenumbering{{gobble}}
        """

        return preamble

    def build(self, source_code: str, filename: str | None = None):
        """
        Returns LaTeX code built from `source_code`.
        """

        if filename is None:
            lexer = guess_lexer(source_code)
        else:
            lexer = guess_lexer_for_filename(filename, source_code)

        preamble = self.__build_preamble()

        formatter = LatexFormatter(
            full=True, style=self.style, preamble=preamble
        )
        latex_code = highlight(source_code, lexer, formatter)

        return latex_code

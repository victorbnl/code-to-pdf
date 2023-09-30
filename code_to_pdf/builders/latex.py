"""
Builds LaTeX from source code.
"""

from os import path

from pygments import highlight
from pygments.lexers import guess_lexer, guess_lexer_for_filename
from pygments.formatters import LatexFormatter
from pygments.styles import get_style_by_name


class LatexBuilder:
    """
    Builds LaTeX from source code.
    """

    def __init__(self, *, style: str = 'default', font_size: str = '10pt'):

        self.style = style
        self.font_size = font_size
        self.formatter = LatexFormatter(style=style)

    def __build_template(self):

        with open(
            path.join(path.dirname(__file__), 'templates', 'latex.tex'),
            'r',
            encoding='utf-8'
        ) as template_file:
            template = template_file.read()

        style = get_style_by_name(self.style)
        background = style.background_color[1:]

        style_defs = self.formatter.get_style_defs()

        template_data = {
            "FONT_SIZE": self.font_size,
            "TOP_MARGIN": "0.4in",
            "BOTTOM_MARGIN": "0.4in",
            "RIGHT_MARGIN": "0.5in",
            "LEFT_MARGIN": "0.5in",
            "BACKGROUND_COLOR": background,
            "STYLE_DEFS": style_defs,
        }

        for key, value in template_data.items():
            template = template.replace(key, value)

        return template

    def __build_latex_code(self, source_code: str, filename: str | None = None):

        if filename is None:
            lexer = guess_lexer(source_code)
        else:
            lexer = guess_lexer_for_filename(filename, source_code)

        latex_code = highlight(source_code, lexer, self.formatter)

        return latex_code

    def build(self, source_code: str, filename: str | None = None):
        """
        Returns LaTeX document code built from `source_code`.
        """

        template = self.__build_template()
        latex_code = self.__build_latex_code(source_code, filename)

        document = template.replace("CONTENT", latex_code)

        return document

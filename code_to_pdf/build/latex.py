"""Convert source code to LaTeX."""

from os import path

from pygments import highlight
from pygments.lexers import guess_lexer, guess_lexer_for_filename
from pygments.formatters import LatexFormatter
from pygments.styles import get_style_by_name

from code_to_pdf.options import Options
from code_to_pdf.utils import is_dark_colour


class LatexBuilder:
    """Builder for converting source code to LaTeX."""

    def __init__(self, options: Options) -> None:
        self.options = options
        self.formatter = LatexFormatter(
            style=options.style,
            linenos=options.linenos,
            linenostep=5,
        )

    def __build_template(self) -> str:
        with open(
            path.join(path.dirname(__file__), 'templates', 'latex.tex'),
            'r',
            encoding='utf-8'
        ) as template_file:
            template = template_file.read()

        style = get_style_by_name(self.options.style)
        background_color = style.background_color

        if is_dark_colour(background_color):
            foreground_color = f"#{6*'b'}"
        else:
            foreground_color = f"#{6*'5'}"

        style_defs = self.formatter.get_style_defs()

        template_data = {
            "FONT_SIZE": self.options.font_size,
            "TOP_MARGIN": self.options.top_margin,
            "BOTTOM_MARGIN": self.options.bottom_margin,
            "RIGHT_MARGIN": self.options.right_margin,
            "LEFT_MARGIN": self.options.left_margin,
            "BACKGROUND_COLOR": background_color[1:],
            "FOREGROUND_COLOR": foreground_color[1:],
            "STYLE_DEFS": style_defs,
        }

        for key, value in template_data.items():
            template = template.replace(key, value)

        return template

    def __build_latex_code(
        self, source_code: str, filename: str | None = None
    ) -> str:
        if filename is None:
            lexer = guess_lexer(source_code)
        else:
            lexer = guess_lexer_for_filename(filename, source_code)

        latex_code = highlight(source_code, lexer, self.formatter)

        return latex_code

    def build(self, source_code: str, filename: str | None = None) -> str:
        """Return LaTeX from source code."""

        template = self.__build_template()
        latex_code = self.__build_latex_code(source_code, filename)

        document = template.replace("CONTENT", latex_code)

        return document

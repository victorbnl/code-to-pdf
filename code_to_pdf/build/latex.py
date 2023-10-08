"""Convert source code to LaTeX."""

from jinja2 import Environment, PackageLoader, select_autoescape
from pygments import highlight
from pygments.formatters import LatexFormatter  # pylint: disable=no-name-in-module
from pygments.lexer import Lexer, LexerMeta
from pygments.lexers import guess_lexer, guess_lexer_for_filename
from pygments.styles import get_style_by_name

from code_to_pdf.options import Options
from code_to_pdf.utils import is_dark_color


class LatexBuilder:
    """Builder for converting source code to LaTeX."""

    def __init__(self, options: Options) -> None:
        self.options = options

        if self.options.page_numbers:
            bottom_margin = float(self.options.bottom_margin[:-2])
            self.options.bottom_margin = f"{bottom_margin + 0.5}in"

        if self.options.linenos:
            left_margin = float(self.options.left_margin[:-2])
            self.options.left_margin = f"{left_margin + 0.3}in"

        self.formatter = LatexFormatter(
            style=options.style,
            linenos=options.linenos,
            linenostep=options.linenostep,
        )

    def __build_latex_code(self, source_code: str, filename: str | None = None) -> str:
        lexer: Lexer | LexerMeta
        if filename is None:
            lexer = guess_lexer(source_code)
        else:
            lexer = guess_lexer_for_filename(filename, source_code)

        latex_code = highlight(source_code, lexer, self.formatter)

        return latex_code

    def __build_template(self, latex_code: str) -> str:
        style_defs = self.formatter.get_style_defs()

        style = get_style_by_name(self.options.style)
        background_color = style.background_color

        if is_dark_color(background_color):
            foreground_color = f"#{6*'b'}"
        else:
            foreground_color = f"#{6*'5'}"

        colors = {
            "background": background_color[1:],
            "foreground": foreground_color[1:],
        }

        env = Environment(
            loader=PackageLoader("code_to_pdf.build"),
            autoescape=select_autoescape(),
            block_start_string="<%",
            block_end_string="%>",
            variable_start_string="<=",
            variable_end_string="=>",
        )
        template = env.get_template("latex.tex.jinja")
        result = template.render(
            options=self.options,
            colors=colors,
            style_defs=style_defs,
            content=latex_code,
        )

        return result

    def build(self, source_code: str, filename: str | None) -> str:
        """Return LaTeX from source code."""

        latex_code = self.__build_latex_code(source_code, filename)
        template = self.__build_template(latex_code)

        return template

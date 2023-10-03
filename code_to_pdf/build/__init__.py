"""Build a document with source code."""

from code_to_pdf.build.latex import LatexBuilder
from code_to_pdf.build.pdf import PdfBuilder


def build(
    source_code: str,
    filename: str | None = None,
    *,
    style: str = 'default',
    font_size: str = '10pt',
    top_margin: str = '0.4in',
    bottom_margin: str = '0.4in',
    left_margin: str = '0.5in',
    right_margin: str = '0.5in',
) -> bytes:
    """Return PDF file content from source code."""

    latex_builder = LatexBuilder(
        style=style,
        font_size=font_size,
        top_margin=top_margin,
        bottom_margin=bottom_margin,
        left_margin=left_margin,
        right_margin=right_margin,
    )
    latex_code = latex_builder.build(source_code, filename)

    pdf_builder = PdfBuilder()
    pdf_content = pdf_builder.build(latex_code)

    return pdf_content

from code_to_pdf.converters.latex import source_to_latex
from code_to_pdf.converters.pdf import latex_to_pdf


def build(
    source_code: str, filename: str | None = None, style: str = 'default'
) -> bytes:
    """
    Returns the bytes of a PDF file which contains `source_code`.
    """

    latex_code = source_to_latex(source_code, filename, style)
    pdf_content = latex_to_pdf(latex_code)

    return pdf_content

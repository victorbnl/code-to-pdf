"""
LaTeX to PDF converter.
"""


from os import path
import tempfile
import subprocess


def latex_to_pdf(latex_code: str) -> bytes:
    """
    Returns the content of the PDF file generated from `latex_code`.
    """

    with tempfile.TemporaryDirectory() as tmpdir:

        with open(
            path.join(tmpdir, 'output.tex'), 'w', encoding='utf-8'
        ) as tex_file:
            tex_file.write(latex_code)

        subprocess.run(
            ['pdflatex', 'output.tex'],
            cwd=tmpdir,
            check=True,
            stdout=subprocess.DEVNULL
        )

        with open(path.join(tmpdir, 'output.pdf'), 'rb') as pdf_file:
            pdf_content = pdf_file.read()

    return pdf_content

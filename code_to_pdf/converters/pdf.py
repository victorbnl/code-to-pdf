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

        try:
            subprocess.run(
                ['pdflatex', '-halt-on-error', 'output.tex'],
                cwd=tmpdir,
                check=True,
                capture_output=True
            )
        except subprocess.CalledProcessError as error:
            print(error.stdout.decode('utf-8'))
            raise error

        with open(path.join(tmpdir, 'output.pdf'), 'rb') as pdf_file:
            pdf_content = pdf_file.read()

    return pdf_content

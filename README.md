# Code to PDF

Writes source code into a PDF document.

<p align="center">
    <img src=".readme/screenshot.png">
</p>

## Motivation

As a matter of fact, I created this project because my school teacher preferred to get our homework as PDF files rather than source files. So I figured I’d automate it to save myself from copying the code in LibreOffice Writer for each homework.

## Requirements

- `pdflatex`

## Installation

```
pip install git+https://github.com/victorbnl/code-to-pdf
```

## Usage

```
code-to-pdf -s one-dark source.py document.pdf
```

**Note:** See [pygments’ documentation](https://pygments.org/styles/) for a list of available styles.

#!/bin/bash

mkdir outputs

for style in 'github-dark' 'one-dark' 'igor'
do
    python -m code_to_pdf \
        --paper-width 13cm \
        --paper-height 16cm \
        --style "$style" \
        source_code.py "outputs/$style.pdf"
done

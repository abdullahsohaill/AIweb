# Nanonets OCR Small
**URL:** https://huggingface.co/nanonets/Nanonets-OCR-s
**Page Title:** nanonets/Nanonets-OCR-s · Hugging Face
--------------------

Nanonets-OCR-s by Nanonets is a powerful, state-of-the-art image-to-markdown OCR model that goes far beyond traditional text extraction. It transforms documents into structured markdown with intelligent content recognition and semantic tagging, making it ideal for downstream processing by Large Language Models (LLMs).
Nanonets-OCR-s is packed with features designed to handle complex documents with ease:
- LaTeX Equation Recognition: Automatically converts mathematical equations and formulas into properly formatted LaTeX syntax. It distinguishes between inline ( $...$ ) and display ( $$...$$ ) equations.
- Intelligent Image Description: Describes images within documents using structured <img> tags, making them digestible for LLM processing. It can describe various image types, including logos, charts, graphs and so on, detailing their content, style, and context.
- Signature Detection & Isolation: Identifies and isolates signatures from other text, outputting them within a <signature> tag. This is crucial for processing legal and business documents.
- Watermark Extraction: Detects and extracts watermark text from documents, placing it within a <watermark> tag.
- Smart Checkbox Handling: Converts form checkboxes and radio buttons into standardized Unicode symbols ( ☐ , ☑ , ☒ ) for consistent and reliable processing.
- Complex Table Extraction: Accurately extracts complex tables from documents and converts them into both markdown and HTML table formats.
📢 Read the full announcement | 🤗 Hugging Face Space Demo

## Usage

### Using transformers

### Using vLLM

- Start the vLLM server.
- Predict with the model

### Using docext

Checkout GitHub for more details.
[LINK: GitHub](https://github.com/NanoNets/docext/tree/dev/markdown)

## BibTex

## Model tree for nanonets/Nanonets-OCR-s

Base model

## Spaces using nanonets/Nanonets-OCR-s 37


--------------------
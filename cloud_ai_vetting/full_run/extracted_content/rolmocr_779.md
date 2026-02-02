# RolmOCR
**URL:** https://huggingface.co/reducto/RolmOCR
**Page Title:** reducto/RolmOCR · Hugging Face
--------------------


## RolmOCR by Reducto AI

Earlier this year, the Allen Institute for AI released olmOCR, an open-source tool that performs document OCR using the Qwen2-VL-7B vision language model (VLM). We were excited to see a high-quality, openly available approach to parsing PDFs and other complex documents — and curious to explore what else might be possible using newer foundation models and some lightweight optimizations.
The result is RolmOCR , a drop-in alternative to olmOCR that’s faster, uses less memory, and still performs well on a variety of document types. We're releasing it under Apache 2.0 for anyone to try out, explore, or build on.
This model is a fine-tuned version of Qwen/Qwen2.5-VL-7B-Instruct on the full allenai/olmOCR-mix-0225 dataset.

## Key changes

We made three notable changes:
- New Base Model : We swapped in a more recent version of the existing model (Qwen2.5-VL-7B) as the foundation.
New Base Model : We swapped in a more recent version of the existing model (Qwen2.5-VL-7B) as the foundation.
- No Metadata inputs : Unlike the original, we don’t use metadata extracted from PDFs. This significantly reduces prompt length, which in turn lowers both processing time and VRAM usage — without hurting accuracy in most cases.
No Metadata inputs : Unlike the original, we don’t use metadata extracted from PDFs. This significantly reduces prompt length, which in turn lowers both processing time and VRAM usage — without hurting accuracy in most cases.
- Rotation of training data: About 15% of the training data was rotated to enhance robustness to off-angle documents. We otherwise use the same training set.
Rotation of training data: About 15% of the training data was rotated to enhance robustness to off-angle documents. We otherwise use the same training set.

## Usage

Host your model with vLLM:
Call the model via openai compatible server:

## Limitations

- RolmOCR, like other VLM-based OCR solutions, still suffer from hallucination or dropping contents.
- Unlike the Reducto Parsing API , RolmOCR cannot output layout bounding boxes.
- We have not evaluated the performance of any quantized versions.

## BibTex and citation info

## Model tree for reducto/RolmOCR

Base model

## Dataset used to train reducto/RolmOCR

## Spaces using reducto/RolmOCR 17


--------------------
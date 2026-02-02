# Deepseek's OCR system compresses image-based text so AI can handle much longer documents
**URL:** https://the-decoder.com/deepseeks-ocr-system-compresses-image-based-text-so-ai-can-handle-much-longer-documents
**Page Title:** Deepseek's OCR system compresses image-based text so AI can handle much longer documents
--------------------


## Deepseek's OCR system compresses image-based text so AI can handle much longer documents

## Key Points

- Chinese AI company Deepseek has developed a system that processes text documents as images, reducing storage needs for text recognition by a factor of ten while retaining 97 percent of the information.
- The Deepseek-OCR architecture combines Meta's SAM model and OpenAI's CLIP model with a compressor, allowing the system to use significantly fewer compute units per document and achieve comparable or better results in benchmarks with only a fraction of the tokens.
- Deepseek-OCR can process up to 33 million pages per day on modern hardware, supports around 100 languages, and is particularly well suited, according to the developers, for generating large training datasets for AI models and for efficient storage of chatbot contexts.

## Topics

- Processes 33 million pages per day
Chinese AI company Deepseek has built an OCR system that compresses image-based text documents for language models, aiming to let AI handle much longer contexts without running into memory limits.
The main idea is that processing text as an image can use less compute than working with the digital text itself. According to Deepseek's technical paper , their OCR can compress text by up to a factor of ten while keeping 97 percent of the original information.
[LINK: technical paper](http://github.com/deepseek-ai/DeepSeek-OCR)
Deepseek OCR's deep parsing mode can convert financial charts into structured data, automatically generating Markdown tables and graphs. | Image: DeepseekThe system has two core parts: DeepEncoder, which handles image processing, and a text generator built on Deepseek3B-MoE with 570 million active parameters. DeepEncoder itself uses 380 million parameters to analyze each image and produce a compressed version.
DeepEncoder joins Meta's 80-million-parameter SAM (Segment Anything Model) for image segmentation with OpenAI's 300-million-parameter CLIP, which links images and text. A 16x compressor sits between them, drastically cutting the number of image tokens. A 1,024 by 1,024 pixel image starts with 4,096 tokens. SAM processes them, and the compressor reduces this to just 256 tokens, which are then passed to the compute-intensive CLIP model.
Deepseek OCR can work with a range of image resolutions. At lower resolutions, it needs only 64 "vision tokens" per image; at higher resolutions, up to 400. By comparison, conventional OCR systems often require thousands of tokens for the same task.
In OmniDocBench tests, Deepseek OCR outperformed GOT-OCR 2.0 using just 100 vision tokens compared to 256. With fewer than 800 tokens, it also beat MinerU 2.0, which requires more than 6,000 tokens per page.
Token requirements depend on the document. Simple presentations use 64 tokens. Books and reports need about 100. Complex newspapers require Deepseek's "Gundam mode" with up to 800 tokens.
The system supports a wide range of document types, from plain text to diagrams, chemical formulas, and geometric figures. It works in about 100 languages, can keep the original formatting, output plain text, and still provide general image descriptions.
For training, the researchers used 30 million PDF pages in roughly 100 languages, including 25 million in Chinese and English, along with 10 million synthetic diagrams, 5 million chemical formulas, and 1 million geometric figures.

## Processes 33 million pages per day

In real-world use, Deepseek OCR can process over 200,000 pages per day on a single Nvidia A100 GPU. With 20 servers, each running eight A100s, throughput jumps to 33 million pages daily.
This kind of throughput could help build training datasets for other AI models. Modern language models need massive amounts of text, and Deepseek OCR can extract it from documents. Both the code and model weights are publicly available .
[LINK: code](https://github.com/deepseek-ai/DeepSeek-OCR)
[LINK: publicly available](https://github.com/deepseek-ai/DeepSeek-OCR)

### AI News Without the Hype – Curated by Humans

As a THE DECODER subscriber , you get ad-free reading, our weekly AI newsletter , the exclusive "AI Radar" Frontier Report 6× per year , access to comments, and our complete archive.
[LINK: Github](https://github.com/deepseek-ai/DeepSeek-OCR)

--------------------
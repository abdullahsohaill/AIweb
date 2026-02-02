# StarVector
**URL:** https://starvector.github.io
**Page Title:** StarVector
--------------------


## StarVector: G enerating S calable V ector G raphics C ode F rom I mages A nd T ext

CVPR 2025
[LINK: Juan A Rodriguez 1,2,4](https://joanrod.github.io)
[LINK: Abhay Puri 1](https://abhaypuri.github.io/portfolio/)
[LINK: Shubham Agarwal 1,2](https://shubhamagarwal92.github.io/)
[LINK: Star on GitHub](https://github.com/joanrod/star-vector)
[LINK: Code](https://github.com/joanrod/star-vector)
StarVector represents a breakthrough in Scalable Vector Graphics (SVG) generation, seamlessly integrating visual and textual inputs into a unified foundation SVG model. By reframing vectorization as a code generation task rather than a traditional image processing problem, StarVector transcends previous limitations. This paradigm shift enables the model to leverage the full richness of SVG syntax—including circles, polygons, text elements, and complex paths—without simplification. Our approach allows training on internet-scale data to capture the diverse spectrum of vector representations. At its core, the model employs a vision-language architecture (VLM), enabling unprecedented capabilities in generating complex SVG elements. Complemented by SVG-Stack—our extensive dataset—and SVG-Bench—our comprehensive evaluation framework—StarVector establishes a new paradigm for high-quality vector graphics generation.

### Key Capabilities

StarVector's multimodal architecture processes both visual and textual information with remarkable precision, enabling sophisticated image vectorization and text-guided SVG creation that captures fine details and structural relationships. The image encoder and language decoder work together to understand the semantics of an image in pixel space, recognizing primitive shapes, hierarchies, and layers to produce compact and semantically meaningful SVG primitive outputs.
Where traditional algorithms falter, StarVector excels—effortlessly recognizing and generating intricate SVG elements including text, complex paths, and various primitives directly from images. The model intelligently identifies geometric shapes, connectivity patterns, and structural elements to produce professional-quality diagrams and icons.
Built upon SVG-Stack—our meticulously curated dataset of over 2 million SVG samples—and evaluated through SVG-Bench, StarVector benefits from diverse, high-quality training examples that ensure consistent performance across various graphic styles and complexities.
StarVector significantly outperforms existing methods in both text-to-SVG and image-to-SVG generation tasks, demonstrating a substantial leap forward in vectorization quality while remaining fully accessible to the research community as an open-source resource.

## Model Architecture

StarVector employs a vision-language architecture to generate high-quality SVG code
The architecture shown above enables StarVector to process both images and text prompts through a unified framework. This approach allows the model to leverage the strengths of both modalities, resulting in more accurate and contextually appropriate SVG generation. The LLM Adapter is a critical component that bridges the gap between visual and textual representations, ensuring that the model can effectively translate visual information into structured SVG code.

## Quick Start - Image2SVG Generation

Get started with StarVector in just a few lines of code
The code above demonstrates how to load a pre-trained StarVector model using the Transformers library, process an input image, and generate SVG code. The model handles all the complexity of understanding the visual elements and translating them into structured vector graphics code.
Note: To use image rasterization features, you need to install the starvector library. Visit the StarVector repository for installation instructions and to ensure all dependencies are properly installed.
[LINK: StarVector repository](https://github.com/joanrod/star-vector/tree/main?tab=readme-ov-file#installation)

## Models

StarVector models achieve state-of-the-art performance on SVG generation tasks
We provide Hugging Face 🤗 model checkpoints for image2SVG vectorization, for 💫 StarVector-8B and 💫 StarVector-1B. These are the results on SVG-Bench, using the DinoScore metric.
Note: StarVector models will not work for natural images or illustrations, as they have not been trained on those images. They excel in vectorizing icons, logotypes, technical diagrams, graphs, and charts.
As shown in the table above, StarVector-8B achieves the highest performance across all benchmark datasets, demonstrating its effectiveness in generating high-quality SVG code from images. The model's ability to understand and reproduce complex vector graphics makes it particularly valuable for applications requiring precise vectorization of icons, logos, and technical diagrams.

## Datasets - SVG-Bench

A comprehensive benchmark for evaluating SVG generation models
SVG-Bench is a benchmark for evaluating SVG generation models. It contains 10 datasets, and 3 tasks: Image-to-SVG, Text-to-SVG, and Diagram-to-SVG. The benchmark provides a standardized way to assess the performance of different approaches to SVG generation, enabling fair comparisons and driving progress in the field.
See our Huggingface 🤗 Dataset Collection
We offer a summary of statistics about the datasets used in our training and evaluation experiments. These datasets are included in SVG-Bench. The subscript _sim_ stands for the simplified version of the dataset, as required by some baselines.

### Datasets Examples

The diversity and scale of these datasets enable StarVector to learn a wide range of SVG generation capabilities, from simple icons to complex diagrams. By training on this comprehensive collection, the model develops a robust understanding of vector graphics principles and can generalize to new, unseen examples.

## Qualitative Results

Visual comparison of StarVector against baseline methods
The following examples demonstrate StarVector's superior performance in generating high-quality SVG code from various input images. These comparisons highlight the model's ability to capture fine details and structural elements that other methods often miss.
Key observations: StarVector consistently produces cleaner, more accurate SVG representations compared to traditional vectorization methods. The model's ability to understand semantic content enables it to make intelligent decisions about which details to preserve and how to structure the resulting SVG code.
These qualitative results demonstrate that StarVector not only achieves higher numerical scores on benchmark metrics but also produces visually superior results that better capture the intent and structure of the original images. This is particularly evident in complex cases like technical diagrams and detailed icons, where traditional methods often struggle to maintain coherence and accuracy.

## Conclusion

StarVector represents a significant advancement in the field of vector graphics generation. By combining the power of vision-language models with a comprehensive training dataset, we've created a system that can accurately translate images into high-quality SVG code. The model's performance on SVG-Bench demonstrates its effectiveness across a wide range of vector graphics tasks.
We believe that StarVector will enable new applications in design, illustration, and technical documentation, making vector graphics more accessible and easier to create. We invite the research community to build upon our work and explore new directions in this exciting field.
For more details, please refer to our paper and explore our code repository .
[LINK: code repository](https://github.com/joanrod/star-vector)
If you find this work useful, please cite:

--------------------
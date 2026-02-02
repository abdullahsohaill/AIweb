# NV-QwenOmni-Embed
**URL:** https://huggingface.co/nvidia/omni-embed-nemotron-3b
**Page Title:** nvidia/omni-embed-nemotron-3b · Hugging Face
--------------------


## Omni-Embed-Nemotron-3B

## Description

NV-QwenOmni-Embed-3B-v1 is a versatile multimodal embedding model capable of encoding content across multiple modalities, including text, image, audio, and video, either individually or in combination, and supports retrieval using queries that can also be multimodal. It is designed to serve as a foundational component in multi-modal Retrieval-Augmented Generation (RAG) systems.
The foundational Qwen Omni model ( Qwen/Qwen2.5-Omni-3B ) is based on the Thinker-Talker architecture. We only leverage the Thinker component to encode and understand diverse modalities. In this implementation, we do not include the Talker component, as the model focuses on multimodal understanding rather than response generation.
This model is for research and development only.
For more technical details, please refer to our technical report: Omni-Embed-Nemotron: A Unified Multimodal Retrieval Model for Text, Image, Audio, and Video

### License/Terms of Use

Governing Terms for nvidia/omni-embed-nemotron-3b model: NVIDIA OneWay Noncommercial License.
ADDITIONAL INFORMATION: Qwen RESEARCH LICENSE AGREEMENT
This project will download and install additional third-party open source software projects. Review the license terms of these open source projects before use.

### Team

- Mengyao Xu
- Gabriel Moreira
- Radek Osmulski
- Ronay Ak
- Yauhen Babakhin
- Bo Liu
- Even Oldridge
- Benedikt Schifferer
Correspondence to Mengyao Xu ( mengyaox@nvidia.com ) and Benedikt Schifferer ( bschifferer@nvidia.com )

### Citation

### Deployment Geography

Global

### Use Case

NV-Omni-Embed is intended for researchers and developers building retrieval-based applications that require understanding and retrieve information across multiple modalities. It is particularly useful in multimodal RAG systems, where queries and documents may include combinations of text, images, audio, and videos. Potential applications include multimedia search engines, cross-modal retrieval systems, and conversational AI with rich input understanding.

### Release Date

Huggingface 10/1/2025 via [ https://huggingface.co/nvidia/omni-embed-nemotron-3b]

## Model Architecture

- Architecture Type: Transformer
- Network Architecture: Qwen/Qwen2.5-Omni-3B
NV-QwenOmni-Embed-3B-v1 is a transformer-based multimodal embedding model built on top of the Thinker component from Qwen/Qwen2.5-Omni-3B . Unlike the original Thinker-Talker architecture, this model does not include the Talker module, as it is designed specifically for multimodal understanding and retrieval rather than response generation. Number of model parameters is 4.7B.
The model incorporates a vision encoder, an audio encoder, and a large language model (LLM) from the Qwen architecture to process diverse modalities. Unlike the Omni model, which interleaves audio and video tokens with TMRoPE, our retrieval encoder keeps the two streams separate. Audio and video are encoded independently, preserving their full temporal structure without interleaving. Our experiments show this design improves retrieval performance.
NV-QwenOmni-Embed-3B-v1 is trained using a bi-encoder architecture where queries and candidate inputs are embedded independently. A contrastive learning objective is employed to align relevant query-content pairs while pushing apart unrelated ones in the shared embedding space.

## Input

Other Properties : The model's maximum context length is 32768 tokens.

## Output

- Output Type: Floats
- Output Format: List of float arrays
- Output Parameters: A tensor of floats equivalent to [batchsize x 2048]
- Other Properties Related to Output: Model outputs embedding vectors of dimension 2048 for each input.
Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

### Usage

The model requires transformers version 4.51.3

## Software Integration:

Runtime Engine(s): TensorRT, Triton
Supported Hardware Microarchitecture Compatibility: A100 40GB, A100 80GB, H100 80GB
Supported Operating System(s): Linux
The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.

## Model Version(s)

- Nvidia Omni Embed Nemotron 3B
- Short name: omni-embed-nemotron-3b-v1

## Training and Evaluation Datasets

## Training Dataset

Data Modality :
Image
Text
Image Training Data Size : 1 Million to 1 Billion Images
Text Training Data Size : Less than a Billion Tokens
The model was trained on publicly available datasets, including HotpotQA , MIRACL , Natural Questions (NQ) , Stack Exchange , SQuAD , Tiger Math/Stack , DocMatix-IR , Vidore-ColPali-Training , and Wiki-SS-NQ .
- Data Collection Method by dataset: Hybrid: Automated, Human, Synthetic
- Labeling Method by dataset: Hybrid: Automated, Human, Synthetic
- Properties: 1M samples from public datasets.

## Evaluation Dataset

We evaluate our model on multiple benchmarks covering different modalities. For text retrieval, we select some text retrieval datasets from MTEB . For image retrieval, evaluation is conducted on the public ViDoRe V1 dataset. Since no established video retrieval benchmarks exist, we construct two custom evaluation sets based on the LPM dataset and FineVideo. To provide fair comparison with the state-of-the-art text-only baselines, we use the speech-to-text transcripts released with FineVideo and the transcripts from LPM as the input corpus for standard text retrieval models.
- Data Collection Method by dataset: Hybrid: Automated, Human, Synthetic
- Labeling Method by dataset: Hybrid: Automated, Human, Synthetic
- Properties: More details on ViDoRe V1 can be found on their leaderboard: Visual Document Retrieval Benchmark .

### Model performance comparison on Video retrieval datasets (LPM and FineVideo) using NDCG@10 and NDCG@5 metrics:

Multimodal retrieval performance across input modalities on LPM and FineVideo using NDCG@10. Baselines support text only; multimodal settings apply to Omni.

### LPM performance (NDCG@10) modalities breakdown

### FineVideo performance (NDCG@10) modalities breakdown

### Evaluation of embedding models across text retrieval benchmarks. Results are reported using nDCG@10.

### Evaluation of baseline models and our models on ViDoRe V1 (as of September 30th). Results are presented using nDCG@5 metrics.

## Inference:

Acceleration Engine: Not Applicable Test Hardware: A100 40GB, A100 80GB, H100 80GB

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.
Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns here .

## Bias

## Explainability

## Privacy

## Safety And Security

## Model tree for nvidia/omni-embed-nemotron-3b

## Collection including nvidia/omni-embed-nemotron-3b

## Papers for nvidia/omni-embed-nemotron-3b


--------------------
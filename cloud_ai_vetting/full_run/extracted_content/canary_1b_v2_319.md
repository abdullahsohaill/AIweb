# canary-1b-v2
**URL:** https://huggingface.co/nvidia/canary-1b-v2
**Page Title:** nvidia/canary-1b-v2 · Hugging Face
--------------------


## 🐤 Canary 1B v2: Multitask Speech Transcription and Translation Model

Canary-1b-v2 is a powerful 1-billion parameter model built for high-quality speech transcription and translation across 25 European languages.
It excels at both automatic speech recognition (ASR) and speech translation (AST), supporting:
- Speech Transcription (ASR) for 25 languages
- Speech Translation (AST) from English → 24 languages
- Speech Translation (AST) from 24 languages → English
Supported Languages: Bulgarian ( bg ), Croatian ( hr ), Czech ( cs ), Danish ( da ), Dutch ( nl ), English ( en ), Estonian ( et ), Finnish ( fi ), French ( fr ), German ( de ), Greek ( el ), Hungarian ( hu ), Italian ( it ), Latvian ( lv ), Lithuanian ( lt ), Maltese ( mt ), Polish ( pl ), Portuguese ( pt ), Romanian ( ro ), Slovak ( sk ), Slovenian ( sl ), Spanish ( es ), Swedish ( sv ), Russian ( ru ), Ukrainian ( uk )
🗣️ Experience Canary-1b-v2 in action at Hugging Face Demo
Canary-1b-v2 model is ready for commercial/non-commercial use.

## License/Terms of Use:

GOVERNING TERMS: Use of this model is governed by the CC-BY-4.0 license.

## Discover more from NVIDIA:

For documentation, deployment guides, enterprise-ready APIs, and the latest open models—including Nemotron and other cutting-edge speech, translation, and generative AI—visit the NVIDIA Developer Portal at developer.nvidia.com .
Join the community to access tools, support, and resources to accelerate your development with NVIDIA’s NeMo, Riva, NIM, and foundation models.
[LINK: developer.nvidia.com](https://developer.nvidia.com)

### Explore more from NVIDIA:

What is Nemotron ? NVIDIA Developer Nemotron NVIDIA Riva Speech NeMo Documentation
[LINK: Nemotron](https://developer.nvidia.com/nemotron)
[LINK: NVIDIA Riva Speech](https://developer.nvidia.com/riva?sortBy=developer_learning_library%2Fsort%2Ffeatured_in.riva%3Adesc%2Ctitle%3Aasc#demos)
[LINK: NeMo Documentation](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/models.html)

## Key Features

Canary-1b-v2 is a scaled and enhanced version of the Canary model family, offering:
- Support for 25 European languages , expanding from the 4 languages in canary-1b / canary-1b-flash to 21 additional languages
- State-of-the-art performance among models of similar size
- Comparable quality to models 3× larger , while being up to 10× faster
- Automatic punctuation and capitalization
- Accurate word-level and segment-level timestamps
- Segment-level timestamps also available for translated outputs
- Released under a permissive CC BY 4.0 license
Canary-1b-v2 model is the first model from NeMo team that leveraged full Nvidia's Granary dataset [1] [2], showcasing its multitask and multilingual capabilities.
For full details on the model architecture, training methodology, datasets, and evaluation results, check out the Canary-1b-v2 Technical Report .
For a deeper glimpse into the Canary family of models, explore this comprehensive NeMo tutorial on multitask speech models .
[LINK: NeMo tutorial on multitask speech models](https://github.com/NVIDIA/NeMo/blob/main/tutorials/asr/Canary_Multitask_Speech_Model.ipynb)

### Automatic Speech Recognition (ASR)

Figure 1: ASR WER comparison across different models. This does not include Punctuation and Capitalisation errors.

### Speech Translation (AST)

Figure 2: AST X → En COMET scores comparison across different models
Figure 3: AST En → X COMET scores comparison across different models

### Evaluation Notes

Note 1: The above evaluations are conducted in two settings: (1) All supported languages (24 languages, excluding Latvian since seamless-m4t-v2-large and seamless-m4t-medium do not support it), and (2) Common languages (6 languages supported by all compared models: en, fr, de, it, pt, es).
Note 2: Performance differences may be partly attributed to Portuguese variant differences - our training data uses European Portuguese while most benchmarks use Brazilian Portuguese.

## Deployment Geography

Global

## Use case

This model serves developers, researchers, academics, and industries building applications that require speech-to-text capabilities, including but not limited to: conversational AI, voice assistants, transcription services, subtitle generation, and voice analytics platforms.

## Release Date

Huggingface 08/14/2025

## Model Architecture

Canary-1b-v2 is an encoder-decoder architecture featuring a FastConformer Encoder [3] and a Transformer Decoder [4]. The model extracts audio features through the encoder and uses task-specific tokens—such as <source language> and <target language> —to guide the Transformer Decoder in generating text output.
It uses a unified SentencePiece Tokenizer [5] with a vocabulary of 16,384 tokens , optimized across all 25 supported languages. The architecture includes 32 encoder layers and 8 decoder layers , totaling 978 million parameters .
For implementation details, see the NeMo repository .
[LINK: NeMo repository](https://github.com/NVIDIA/NeMo)

## Input

- Input Type(s): 16kHz Audio
- Input Format(s): .wav and .flac audio formats
- Input Parameters: 1D (audio signal)
- Other Properties Related to Input: Monochannel audio

## Output

- Output Type(s): Text
- Output Format: String
- Output Parameters: 1D (text)
- Other Properties Related to Output: Punctuation and Capitalization included.
Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## How to Use This Model

To train, fine-tune or play with the model you will need to install NVIDIA NeMo [6]. We recommend you install it after you've installed latest PyTorch version.
[LINK: NVIDIA NeMo](https://github.com/NVIDIA/NeMo)
The model is available for use in the NeMo toolkit [6], and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.
First, let's get a sample:
Then simply do:
Be sure to specify necessary target_lang for proper translation:
Note: Use main branch of NeMo to get timestamps until it is released in NeMo 2.5.
[LINK: main branch of NeMo](https://github.com/NVIDIA/NeMo/)
To transcribe with timestamps:
To translate with timestamps:
For translation task, please, refer to segment-level timestamps for getting intuitive and accurate alignment.
Note: If timestamps are not required for your work, you can reduce memory usage by restoring only the .nemo file without the auxiliary CTC model. To do this, extract the .nemo file, remove any timestamps_asr_model files, then repackage it into a new .nemo file.

## Software Integration

Runtime Engine(s):
- NeMo main branch (until it is released in NeMo 2.5)
Supported Hardware Microarchitecture Compatibility:
- NVIDIA Ampere
- NVIDIA Blackwell
- NVIDIA Hopper
[Preferred/Supported] Operating System(s):
- Linux
Hardware Specific Requirements: At least 6GB RAM for model to load.
Current version: Canary-1b-v2 . Previous versions can be accessed here.

## Training and Evaluation Datasets

### Training

The model was trained using the NeMo toolkit [4], following a 3-stage training procedure:
- Initialized from a 4-language ASR model
- Stage 1: Trained for 150,000 steps on X→En and English ASR tasks using 64 A100 GPUs
- Stage 2: Trained for 115,000 additional steps on the full dataset (ASR, X→En, En→X)
- Stage 3: Fine-tuned for 10,000 steps on a language-balanced high-quality subset of Granary and NeMo ASR Set 3.0
For all the stages of training, both languages and corpora are weighted using temperature sampling (τ = 0.5).
Training script: speech_to_text_aed.py
[LINK: speech_to_text_aed.py](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/speech_multitask/speech_to_text_aed.py)
Tokenizer script: process_asr_text_tokenizer.py
[LINK: process_asr_text_tokenizer.py](https://github.com/NVIDIA/NeMo/blob/main/scripts/tokenizers/process_asr_text_tokenizer.py)

### Training Dataset

Canary-1b-v2 was trained on a massive multilingual speech recognition and translation dataset combining Nvidia's newly published Granary and in-house dataset NeMo ASR Set 3.0.
Granary Dataset [5] [6] with improved pseudo-labels and efficiently filtered versions of the following corpora:
- YTC [7]
- MOSEL [8]
- YODAS [9]
Granary is now available on Hugging Face .
To read more about the pseudo-labeling technique and pipeline , please refer to the Granary Paper .
[LINK: pipeline](https://github.com/NVIDIA/NeMo-speech-data-processor/tree/main/dataset_configs/multilingual/granary)
NeMo ASR Set 3.0 including human-labeled transcriptions from the following corpora:
- Multilingual LibriSpeech (MLS)
- Mozilla Common Voice (v7.0)
- AMI (70 hrs)
- Fleurs
- LibriSpeech (960 hours)
- Fisher Corpus
- National Speech Corpus Part 1
- VCTK
- Europarl-ASR
Total training hours: 1.7M
- ASR: 660,000 hrs
- X→En: 360,000 hrs
- En→X: 690,000 hrs
- Non-speech: 36,000 hrs
All transcripts include punctuation and capitalization.
Data Collection Method by dataset
- Hybrid: Automated, Human
Labeling Method by dataset
- Hybrid: Synthetic, Human

### Evaluation Dataset

- Fleurs [10], MLS [11], CoVoST [12]
- Hugging Face Open ASR Leaderboard [13]
- Earnings-22 [14], This American Life [15] (long-form)
- MUSAN [16]
Data Collection Method by dataset
- Human
Labeling Method by dataset
- Human

## Benchmark Results

This section reports the evaluation results of the Canary-1b-v2 model across multiple tasks, including Automatic Speech Recognition (ASR), Speech Translation (AST), robustness to noise, and long-form transcription.

### Automatic Speech Recognition (ASR)

Note: Presented WERs do not include Punctuation and Capitalization errors.
More details on evaluation can be found at HuggingFace ASR Leaderboard

### Speech Translation (AST)

### Noise Robustness

Performance across different Signal-to-Noise Ratios (SNR) using MUSAN music and noise samples [16] on the LibriSpeech Clean test set . Metric : Word Error Rate ( WER )

### Hallucination Robustness

Number of characters per minute on MUSAN [16] 48 hrs eval set:

### Long-form Inference

Canary-1b-v2 achieves strong performance on long-form transcription by using dynamic chunking with 1-second overlap between chunks, allowing for efficient parallel processing. This dynamic chunking feature is automatically enabled when calling .transcribe() on a single audio file, or when using batch_size=1 with multiple audio files that are longer than 40 seconds.
Note: Presented WERs do not include Punctuation and Capitalization errors.

## Inference

Engine :
- NVIDIA NeMo
Test Hardware :
- NVIDIA A10
- NVIDIA A100
- NVIDIA A30
- NVIDIA A5000
- NVIDIA H100
- NVIDIA L4
- NVIDIA L40

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.
For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards here .
[LINK: here](https://developer.nvidia.com/blog/enhancing-ai-transparency-and-ethical-considerations-with-model-card/)
Please report security vulnerabilities or NVIDIA AI Concerns here .

## Bias:

## Explainability:

## Privacy:

## Safety:

## References

[1] Granary: Speech Recognition and Translation Dataset in 25 European Languages
[2] NVIDIA Granary Dataset Card
[3] Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition
[4] Attention is All You Need
[5] Google Sentencepiece Tokenizer
[LINK: Google Sentencepiece Tokenizer](https://github.com/google/sentencepiece)
[6] NVIDIA NeMo Toolkit
[LINK: NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)
[7] Youtube-Commons
[8] MOSEL: 950,000 Hours of Speech Data for Open-Source Speech Foundation Model Training on EU Languages
[9] YODAS: Youtube-Oriented Dataset for Audio and Speech
[10] FLEURS: Few-shot Learning Evaluation of Universal Representations of Speech
[11] MLS: A Large-Scale Multilingual Dataset for Speech Research
[12] CoVoST 2 and Massively Multilingual Speech-to-Text Translation
[13] HuggingFace Open ASR Leaderboard
[14] Earnings-22 Benchmark
[LINK: Earnings-22 Benchmark](https://github.com/revdotcom/speech-datasets/tree/main/earnings22)
[15] Speech Recognition and Multi-Speaker Diarization of Long Conversations
[16] MUSAN: A Music, Speech, and Noise Corpus

## Model tree for nvidia/canary-1b-v2

## Dataset used to train nvidia/canary-1b-v2

## Spaces using nvidia/canary-1b-v2 10

## Collections including nvidia/canary-1b-v2

## Papers for nvidia/canary-1b-v2

## Evaluation results

- Test WER (Bg) on FLEURS test set self-reported 9.250
- Test WER (Cs) on FLEURS test set self-reported 7.860
- Test WER (Da) on FLEURS test set self-reported 11.250
- Test WER (De) on FLEURS test set self-reported 4.400
- Test WER (El) on FLEURS test set self-reported 9.210
- Test WER (En) on FLEURS test set self-reported 4.500
- Test WER (Es) on FLEURS test set self-reported 2.900
- Test WER (Et) on FLEURS test set self-reported 12.550
- Test WER (Fi) on FLEURS test set self-reported 8.590
- Test WER (Fr) on FLEURS test set self-reported 5.020
- Test WER (Hr) on FLEURS test set self-reported 8.290
- Test WER (Hu) on FLEURS test set self-reported 12.900
- Test WER (It) on FLEURS test set self-reported 3.070
- Test WER (Lt) on FLEURS test set self-reported 12.360
- Test WER (Lv) on FLEURS test set self-reported 9.660
- Test WER (Mt) on FLEURS test set self-reported 18.310
- Test WER (Nl) on FLEURS test set self-reported 6.120
- Test WER (Pl) on FLEURS test set self-reported 6.640
- Test WER (Pt) on FLEURS test set self-reported 4.390
- Test WER (Ro) on FLEURS test set self-reported 6.610

--------------------
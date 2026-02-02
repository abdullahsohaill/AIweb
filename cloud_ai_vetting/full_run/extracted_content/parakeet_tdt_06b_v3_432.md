# parakeet-tdt-0.6b-v3
**URL:** https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3
**Page Title:** nvidia/parakeet-tdt-0.6b-v3 · Hugging Face
--------------------


## 🦜 parakeet-tdt-0.6b-v3: Multilingual Speech-to-Text Model

| |

## Description:

parakeet-tdt-0.6b-v3 is a 600-million-parameter multilingual automatic speech recognition (ASR) model designed for high-throughput speech-to-text transcription. It extends the parakeet-tdt-0.6b-v2 model by expanding language support from English to 25 European languages. The model automatically detects the language of the audio and transcribes it without requiring additional prompting. It is part of a series of models that leverage the Granary [1, 2] multilingual corpus as their primary training dataset.
🗣️ Try Demo here: https://huggingface.co/spaces/nvidia/parakeet-tdt-0.6b-v3
Supported Languages: Bulgarian ( bg ), Croatian ( hr ), Czech ( cs ), Danish ( da ), Dutch ( nl ), English ( en ), Estonian ( et ), Finnish ( fi ), French ( fr ), German ( de ), Greek ( el ), Hungarian ( hu ), Italian ( it ), Latvian ( lv ), Lithuanian ( lt ), Maltese ( mt ), Polish ( pl ), Portuguese ( pt ), Romanian ( ro ), Slovak ( sk ), Slovenian ( sl ), Spanish ( es ), Swedish ( sv ), Russian ( ru ), Ukrainian ( uk )
This model is ready for commercial/non-commercial use.

## Key Features:

parakeet-tdt-0.6b-v3 's key features are built on the foundation of its predecessor, parakeet-tdt-0.6b-v2 , and include:
- Automatic punctuation and capitalization
- Accurate word-level and segment-level timestamps
- Long audio transcription, supporting audio up to 24 minutes long with full attention (on A100 80GB) or up to 3 hours with local attention.
- Released under a permissive CC BY 4.0 license
For full details on the model architecture, training methodology, datasets, and evaluation results, check out the Technical Report .

## License/Terms of Use:

GOVERNING TERMS: Use of this model is governed by the CC-BY-4.0 license.

### Discover more from NVIDIA:

For documentation, deployment guides, enterprise-ready APIs, and the latest open models—including Nemotron and other cutting-edge speech, translation, and generative AI—visit the NVIDIA Developer Portal at developer.nvidia.com.
Join the community to access tools, support, and resources to accelerate your development with NVIDIA’s NeMo, Riva, NIM, and foundation models.
What is Nemotron ? NVIDIA Developer Nemotron NVIDIA Riva Speech NeMo Documentation
[LINK: Nemotron](https://developer.nvidia.com/nemotron)
[LINK: NVIDIA Riva Speech](https://developer.nvidia.com/riva?sortBy=developer_learning_library%2Fsort%2Ffeatured_in.riva%3Adesc%2Ctitle%3Aasc#demos)
[LINK: NeMo Documentation](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/models.html)

## Automatic Speech Recognition (ASR) Performance

Figure 1: ASR WER comparison across different models. This does not include Punctuation and Capitalisation errors.

### Evaluation Notes

Note 1: The above evaluations are conducted  for 24 supported languages, excluding Latvian since seamless-m4t-v2-large and seamless-m4t-medium do not support it.
Note 2: Performance differences may be partly attributed to Portuguese variant differences - our training data uses European Portuguese while most benchmarks use Brazilian Portuguese.

### Deployment Geography:

Global

### Use Case:

This model serves developers, researchers, academics, and industries building applications that require speech-to-text capabilities, including but not limited to: conversational AI, voice assistants, transcription services, subtitle generation, and voice analytics platforms.

### Release Date:

Huggingface 08/14/2025

### Model Architecture:

Architecture Type :
FastConformer-TDT
Network Architecture :
- This model was developed based on FastConformer encoder architecture[3] and TDT decoder[4]
[LINK: FastConformer encoder](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#fast-conformer)
- This model has 600 million model parameters.

### Input:

Input Type(s): 16kHz Audio Input Format(s): .wav and .flac audio formats Input Parameters: 1D (audio signal) Other Properties Related to Input: Monochannel audio

### Output:

Output Type(s): Text Output Format: String Output Parameters: 1D (text) Other Properties Related to Output: Punctuations and Capitalizations included.
Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.
For more information, refer to the NeMo documentation .
[LINK: NeMo documentation](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#fast-conformer)

## How to Use this Model:

To train, fine-tune or play with the model you will need to install NVIDIA NeMo . We recommend you install it after you've installed latest PyTorch version.
[LINK: NVIDIA NeMo](https://github.com/NVIDIA/NeMo)
The model is available for use in the NeMo toolkit [5], and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.
First, let's get a sample
Then simply do:
To transcribe with timestamps:
To use parakeet models in streaming mode use this script as shown below:
[LINK: script](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/asr_chunked_inference/rnnt/speech_to_text_streaming_infer_rnnt.py)
NVIDIA NIM for v2 parakeet model is available at https://build.nvidia.com/nvidia/parakeet-tdt-0_6b-v2 .

## Software Integration:

Runtime Engine(s):
- NeMo 2.4
Supported Hardware Microarchitecture Compatibility:
- NVIDIA Ampere
- NVIDIA Blackwell
- NVIDIA Hopper
- NVIDIA Volta
[Preferred/Supported] Operating System(s):
- Linux
Hardware Specific Requirements:
Atleast 2GB RAM for model to load. The bigger the RAM, the larger audio input it supports.
Current version: parakeet-tdt-0.6b-v3 . Previous versions can be accessed here.

## Training and Evaluation Datasets:

### Training

This model was trained using the NeMo toolkit [5], following the strategies below:
- Initialized from a CTC multilingual checkpoint pretrained on the Granary dataset [1] [2].
- Trained for 150,000 steps on 128 A100 GPUs.
- Dataset corpora and languages were balanced using a temperature sampling value of 0.5.
- Stage 2 fine-tuning was performed for 5,000 steps on 4 A100 GPUs using approximately 7,500 hours of high-quality, human-transcribed data of NeMo ASR Set 3.0.
Training was conducted using this example script and TDT configuration .
[LINK: example script](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/asr_transducer/speech_to_text_rnnt_bpe.py)
[LINK: TDT configuration](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/conf/fastconformer/hybrid_transducer_ctc/fastconformer_hybrid_tdt_ctc_bpe.yaml)
During the training, a unified SentencePiece Tokenizer [6] with a vocabulary of 8,192 tokens was used. The unified tokenizer was constructed from the training set transcripts using this script and was optimized across all 25 supported languages.
[LINK: script](https://github.com/NVIDIA/NeMo/blob/main/scripts/tokenizers/process_asr_text_tokenizer.py)

### Training Dataset

The model was trained on the combination of Granary dataset's ASR subset and in-house dataset NeMo ASR Set 3.0:
- 10,000 hours from human-transcribed NeMo ASR Set 3.0, including: LibriSpeech (960 hours) Fisher Corpus National Speech Corpus Part 1 VCTK Europarl-ASR Multilingual LibriSpeech Mozilla Common Voice (v7.0) AMI
10,000 hours from human-transcribed NeMo ASR Set 3.0, including:
- LibriSpeech (960 hours)
- Fisher Corpus
- National Speech Corpus Part 1
- VCTK
- Europarl-ASR
- Multilingual LibriSpeech
- Mozilla Common Voice (v7.0)
- AMI
- 660,000 hours of pseudo-labeled data from Granary [1] [2], including: YTC [7] MOSEL [8] YODAS [9]
660,000 hours of pseudo-labeled data from Granary [1] [2], including:
- YTC [7]
- MOSEL [8]
- YODAS [9]
All transcriptions preserve punctuation and capitalization. The Granary dataset will be made publicly available after presentation at Interspeech 2025.
Data Collection Method by dataset
- Hybrid: Automated, Human
Labeling Method by dataset
- Hybrid: Synthetic, Human
Properties:
- Noise robust data from various sources
- Single channel, 16kHz sampled data
For multilingual ASR performance evaluation:
- Fleurs [10]
- MLS [11]
- CoVoST [12]
For English ASR performance evaluation:
- Hugging Face Open ASR Leaderboard [13] datasets
Data Collection Method by dataset
- Human
Labeling Method by dataset
- Human
Properties:
- All are commonly used for benchmarking English ASR systems.
- Audio data is typically processed into a 16kHz mono channel format for ASR evaluation, consistent with benchmarks like the Open ASR Leaderboard .

## Performance

The tables below summarizes the WER (%) using a Transducer decoder with greedy decoding (without an external language model):
Note: WERs are calculated after removing Punctuation and Capitalization from reference and predicted text.
Additional evaluation details are available on the Hugging Face ASR Leaderboard .[13]

### Noise Robustness

Performance across different Signal-to-Noise Ratios (SNR) using MUSAN music and noise samples [14]:

## References

[1] Granary: Speech Recognition and Translation Dataset in 25 European Languages
[2] NVIDIA Granary Dataset Card
[3] Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition
[4] Efficient Sequence Transduction by Jointly Predicting Tokens and Durations
[5] NVIDIA NeMo Toolkit
[LINK: NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)
[6] Google Sentencepiece Tokenizer
[LINK: Google Sentencepiece Tokenizer](https://github.com/google/sentencepiece)
[7] Youtube-Commons
[8] MOSEL: 950,000 Hours of Speech Data for Open-Source Speech Foundation Model Training on EU Languages
[9] YODAS: Youtube-Oriented Dataset for Audio and Speech
[10] FLEURS: Few-shot Learning Evaluation of Universal Representations of Speech
[11] MLS: A Large-Scale Multilingual Dataset for Speech Research
[12] CoVoST 2 and Massively Multilingual Speech-to-Text Translation
[13] HuggingFace ASR Leaderboard
[14] MUSAN: A Music, Speech, and Noise Corpus

## Inference:

Engine :
- NVIDIA NeMo
Test Hardware :
- NVIDIA A10
- NVIDIA A100
- NVIDIA A30
- NVIDIA H100
- NVIDIA L4
- NVIDIA L40
- NVIDIA Turing T4
- NVIDIA Volta V100

## Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.
For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards here .
[LINK: here](https://developer.nvidia.com/blog/enhancing-ai-transparency-and-ethical-considerations-with-model-card/)
Please report security vulnerabilities or NVIDIA AI Concerns here .

## Bias:

## Explainability:

## Privacy:

## Safety:

## Model tree for nvidia/parakeet-tdt-0.6b-v3

## Dataset used to train nvidia/parakeet-tdt-0.6b-v3

## Spaces using nvidia/parakeet-tdt-0.6b-v3 24

## Collections including nvidia/parakeet-tdt-0.6b-v3

## Papers for nvidia/parakeet-tdt-0.6b-v3

## Evaluation results

- Test WER on AMI (Meetings test) test set self-reported 11.310
- Test WER on Earnings-22 test set self-reported 11.420
- Test WER on GigaSpeech test set self-reported 9.590
- Test WER on LibriSpeech (clean) test set self-reported 1.930
- Test WER on LibriSpeech (other) test set self-reported 3.590
- Test WER on SPGI Speech test set self-reported 3.970
- Test WER on tedlium-v3 test set self-reported 2.750
- Test WER on Vox Populi test set self-reported 6.140
- Test WER (Bg) on FLEURS test set self-reported 12.640
- Test WER (Cs) on FLEURS test set self-reported 11.010
- Test WER (Da) on FLEURS test set self-reported 18.410
- Test WER (De) on FLEURS test set self-reported 5.040
- Test WER (El) on FLEURS test set self-reported 20.700
- Test WER (En) on FLEURS test set self-reported 4.850
- Test WER (Es) on FLEURS test set self-reported 3.450
- Test WER (Et) on FLEURS test set self-reported 17.730
- Test WER (Fi) on FLEURS test set self-reported 13.210
- Test WER (Fr) on FLEURS test set self-reported 5.150
- Test WER (Hr) on FLEURS test set self-reported 12.460
- Test WER (Hu) on FLEURS test set self-reported 15.720

--------------------
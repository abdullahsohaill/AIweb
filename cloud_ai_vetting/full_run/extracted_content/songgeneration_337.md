# SongGeneration
**URL:** https://huggingface.co/tencent/SongGeneration
**Page Title:** tencent/SongGeneration · Hugging Face
--------------------


## SongGeneration

Demo | Paper | Code | Space Demo
[LINK: Demo](https://levo-demo.github.io/)
[LINK: Code](https://github.com/tencent-ailab/songgeneration)
This repository is the official weight repository for LeVo: High-Quality Song Generation with Multi-Preference Alignment. In this repository, we provide the SongGeneration model, inference scripts, and the checkpoint that has been trained on the Million Song Dataset.

## Model Versions

## Overview

We develop the SongGeneration model. It is an LM-based framework consisting of LeLM and a music codec . LeLM is capable of parallelly modeling two types of tokens: mixed tokens, which represent the combined audio of vocals and accompaniment to achieve vocal-instrument harmony, and dual-track tokens, which separately encode vocals and accompaniment for high-quality song generation. The music codec reconstructs the dual-track tokens into highfidelity music audio. SongGeneration significantly improves over the open-source music generation models and performs competitively with current state-of-the-art industry systems. For more details, please refer to our paper .

## License

The code and weights in this repository is released in the LICENSE file.

## Spaces using tencent/SongGeneration 7

## Paper for tencent/SongGeneration


--------------------
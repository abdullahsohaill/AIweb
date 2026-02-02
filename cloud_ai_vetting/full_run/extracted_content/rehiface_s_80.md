# ReHiFace-S
**URL:** https://huggingface.co/GuijiAI/ReHiFace-S
**Page Title:** GuijiAI/ReHiFace-S · Hugging Face
--------------------

[LINK: https://huggingface.co/docs/hub/model-cards#model-card-metadata](https://huggingface.co/docs/hub/model-cards#model-card-metadata)

## ReHiFace-S 🤖🤖🤖

## 🚀 Introduction

ReHiFace-S, short for “Real Time High-Fidelity Faceswap”, is a real-time high-fidelity faceswap algorithm created by Silicon-based Intelligence. By open-sourcing the capabilities of digital human generation, developers can easily generate large-scale digital humans who they want, enabling real-time faceswap capability.

## 💪 Project features

- Real-time on NVIDIA GTX 1080Ti
- Zero-shot inference
- High Fidelity faceswap
- Support ONNX and live camera mode
- Support super resulution and color transfer
- Better Xseg model for face segment

## 🔥 Examples

We show some faceswap examples.

## 🔧 Getting Started

### Clone the code and prepare the environment

- Python >= 3.9 (Recommend to use Anaconda or Miniconda )
[LINK: Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- PyTorch >= 1.13
- CUDA 11.7
- Linux Ubuntu20.04

## 😊 Pretrained models

Download all pretrained weights from Google Drive or Baidu Yun . We have packed all weights in one directory 😊. Download and place them in ./pretrain_models folder ensuring the directory structure is as follows:

## 💻 How to Test

Or, you can change the input by specifying the --src_img_path and --video_path arguments:

### Live Cam faceswap

You should at least run by NVIDIA GTX 1080Ti.
Notice: The time taken to render to a video and warm up the models are not included.
Not support Super Resolution.
Notice: Support change source face during live with 'data/image_feature_dict.pkl' !

## 🤗 Gradio interface

We also provide a Gradio interface for a better experience, just run by:

## ✨ Acknowledgments

- Thanks to Hififace for base faceswap framework.
[LINK: Hififace](https://github.com/johannwyh/HifiFace)
- Thanks to CurricularFace for pretrained face feature model.
[LINK: CurricularFace](https://github.com/HuangYG123/CurricularFace)
- Thanks to Xseg for base face segment framework.
[LINK: Xseg](https://github.com/iperov/DeepFaceLab/tree/master)
- Thanks to GFPGAN for face super resolution.
[LINK: GFPGAN](https://github.com/TencentARC/GFPGAN)
- Thanks to LivePortrait and duix.ai for README template.
[LINK: LivePortrait](https://github.com/KwaiVGI/LivePortrait)
[LINK: duix.ai](https://github.com/GuijiAI/duix.ai)

## 🌟 Citation

If you find ReHiFace-S useful for your research, welcome to 🌟 this repo.
[LINK: How to track](https://huggingface.co/docs/hub/models-download-stats)
[LINK: NEW](https://huggingface.co/docs/inference-providers)

--------------------
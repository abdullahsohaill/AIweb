# bartowski/cognitivecomputations\_Dolphin3.0-Mistral-24B-GGUF
**URL:** https://huggingface.co/bartowski/cognitivecomputations_Dolphin3.0-Mistral-24B-GGUF
**Page Title:** bartowski/cognitivecomputations_Dolphin3.0-Mistral-24B-GGUF · Hugging Face
--------------------


## Llamacpp imatrix Quantizations of Dolphin3.0-Mistral-24B by cognitivecomputations

Using llama.cpp release b4585 for quantization.
[LINK: llama.cpp](https://github.com/ggerganov/llama.cpp/)
[LINK: b4585](https://github.com/ggerganov/llama.cpp/releases/tag/b4585)
Original model: https://huggingface.co/cognitivecomputations/Dolphin3.0-Mistral-24B
All quants made using imatrix option with dataset from here
[LINK: here](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8)
Run them in LM Studio
Run them directly with llama.cpp , or any other llama.cpp based project
[LINK: llama.cpp](https://github.com/ggerganov/llama.cpp)

## Prompt format

## Download a file (not the whole branch) from below:

## Embed/output weights

Some of these quants (Q3_K_XL, Q4_K_L etc) are the standard quantization method with the embeddings and output weights quantized to Q8_0 instead of what they would normally default to.

## Downloading using huggingface-cli

First, make sure you have hugginface-cli installed:
Then, you can target the specific file you want:
If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:
You can either specify a new local-dir (cognitivecomputations_Dolphin3.0-Mistral-24B-Q8_0) or download them all in place (./)

## ARM/AVX information

Previously, you would download Q4_0_4_4/4_8/8_8, and these would have their weights interleaved in memory in order to improve performance on ARM and AVX machines by loading up more data in one pass.
Now, however, there is something called "online repacking" for weights. details in this PR . If you use Q4_0 and your hardware would benefit from repacking weights, it will do it automatically on the fly.
[LINK: this PR](https://github.com/ggerganov/llama.cpp/pull/9921)
As of llama.cpp build b4282 you will not be able to run the Q4_0_X_X files and will instead need to use Q4_0.
[LINK: b4282](https://github.com/ggerganov/llama.cpp/releases/tag/b4282)
Additionally, if you want to get slightly better quality for , you can use IQ4_NL thanks to this PR which will also repack the weights for ARM, though only the 4_4 for now. The loading time may be slower but it will result in an overall speed incrase.
[LINK: this PR](https://github.com/ggerganov/llama.cpp/pull/10541)
I'm keeping this section to show the potential theoretical uplift in performance from using the Q4_0 with online repacking.
Q4_0_8_8 offers a nice bump to prompt processing and a small bump to text generation

## Which file should I choose?

A great write up with charts showing various performances is provided by Artefact2 here
[LINK: here](https://gist.github.com/Artefact2/b5f810600771265fc1e39442288e8ec9)
The first thing to figure out is how big a model you can run. To do this, you'll need to figure out how much RAM and/or VRAM you have.
If you want your model running as FAST as possible, you'll want to fit the whole thing on your GPU's VRAM. Aim for a quant with a file size 1-2GB smaller than your GPU's total VRAM.
If you want the absolute maximum quality, add both your system RAM and your GPU's VRAM together, then similarly grab a quant with a file size 1-2GB Smaller than that total.
Next, you'll need to decide if you want to use an 'I-quant' or a 'K-quant'.
If you don't want to think too much, grab one of the K-quants. These are in format 'QX_K_X', like Q5_K_M.
If you want to get more into the weeds, you can check out this extremely useful feature chart:
llama.cpp feature matrix
[LINK: llama.cpp feature matrix](https://github.com/ggerganov/llama.cpp/wiki/Feature-matrix)
But basically, if you're aiming for below Q4, and you're running cuBLAS (Nvidia) or rocBLAS (AMD), you should look towards the I-quants. These are in format IQX_X, like IQ3_M. These are newer and offer better performance for their size.
These I-quants can also be used on CPU and Apple Metal, but will be slower than their K-quant equivalent, so speed vs performance is a tradeoff you'll have to decide.
The I-quants are not compatible with Vulcan, which is also AMD, so if you have an AMD card double check if you're using the rocBLAS build or the Vulcan build. At the time of writing this, LM Studio has a preview with ROCm support, and other inference engines have specific builds for ROCm.

## Credits

Thank you kalomaze and Dampf for assistance in creating the imatrix calibration dataset.
Thank you ZeroWw for the inspiration to experiment with embed/output.
Thank you to LM Studio for sponsoring my work.
Want to support my work? Visit my ko-fi page here: https://ko-fi.com/bartowski
2-bit
3-bit
4-bit
5-bit
6-bit
8-bit
32-bit

## Model tree for bartowski/cognitivecomputations_Dolphin3.0-Mistral-24B-GGUF

Base model

## Datasets used to train bartowski/cognitivecomputations_Dolphin3.0-Mistral-24B-GGUF

## Space using bartowski/cognitivecomputations_Dolphin3.0-Mistral-24B-GGUF 1


--------------------
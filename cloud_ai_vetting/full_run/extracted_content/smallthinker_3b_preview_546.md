# SmallThinker-3B-preview
**URL:** https://huggingface.co/PowerInfer/SmallThinker-3B-Preview
**Page Title:** Tiiny/SmallThinker-3B-Preview · Hugging Face
--------------------


## SmallThinker-3B-preview

We introduce SmallThinker-3B-preview , a new model fine-tuned from the Qwen2.5-3b-Instruct model.
Now you can directly deploy SmallThinker On your phones with PowerServe .
[LINK: PowerServe](https://github.com/powerserve-project/PowerServe)

## Benchmark Performance

Limitation: Due to SmallThinker's current limitations in instruction following, for math_comp we adopt a more lenient evaluation method where only correct answers are required, without constraining responses to follow the specified AAAAA format.
Colab Link: Colab

## Intended Use Cases

SmallThinker is designed for the following use cases:
- Edge Deployment: Its small size makes it ideal for deployment on resource-constrained devices.
- Draft Model for QwQ-32B-Preview: SmallThinker can serve as a fast and efficient draft model for the larger QwQ-32B-Preview model. From my test, in llama.cpp we can get 70% speedup (from 40 tokens/s to 70 tokens/s).

## Training Details

The model was trained using 8 H100 GPUs with a global batch size of 16. The specific configuration is as follows:
The SFT (Supervised Fine-Tuning) process was conducted in two phases:
- First Phase: Used only the PowerInfer/QWQ-LONGCOT-500K dataset Trained for 1.5 epochs
- Used only the PowerInfer/QWQ-LONGCOT-500K dataset
- Trained for 1.5 epochs
- Second Phase: Combined training with PowerInfer/QWQ-LONGCOT-500K and PowerInfer/LONGCOT-Refine datasets Continued training for 2 additional epochs
- Combined training with PowerInfer/QWQ-LONGCOT-500K and PowerInfer/LONGCOT-Refine datasets
- Continued training for 2 additional epochs

## Limitations & Disclaimer

Please be aware of the following limitations:
- Language Limitation: The model has only been trained on English-language datasets, hence its capabilities in other languages are still lacking.
- Limited Knowledge: Due to limited SFT data and the model's relatively small scale, its reasoning capabilities are constrained by its knowledge base.
- Unpredictable Outputs: The model may produce unexpected outputs due to its size and probabilistic generation paradigm. Users should exercise caution and validate the model's responses.
- Repetition Issue: The model tends to repeat itself when answering high-difficulty questions. Please increase the repetition_penalty to mitigate this issue.

## Model tree for Tiiny/SmallThinker-3B-Preview

Base model

## Datasets used to train Tiiny/SmallThinker-3B-Preview

## Spaces using Tiiny/SmallThinker-3B-Preview 19


--------------------
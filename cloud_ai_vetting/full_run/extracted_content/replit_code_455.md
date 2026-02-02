# replit-code
**URL:** https://huggingface.co/replit/replit-code-v1-3b
**Page Title:** replit/replit-code-v1-3b · Hugging Face
--------------------


## replit-code-v1-3b

Developed by: Replit, Inc.
🧑‍💻 Test it on our Demo Space! 🧑‍💻
⚙️ Fine-tuning and Instruct-tuning guides ⚙️
[LINK: ⚙️ Fine-tuning and Instruct-tuning guides ⚙️](https://github.com/replit/replitLM)

## Model Description

replit-code-v1-3b is a 2.7B Causal Language Model focused on Code Completion . The model has been trained on a subset of the Stack Dedup v1.2 dataset .
The training mixture includes 20 different languages , listed here in descending order of number of tokens: Markdown , Java , JavaScript , Python , TypeScript , PHP , SQL , JSX , reStructuredText , Rust , C , CSS , Go , C++ , HTML , Vue , Ruby , Jupyter Notebook , R , Shell In total, the training dataset contains 175B tokens, which were repeated over 3 epochs -- in total, replit-code-v1-3b has been trained on 525B tokens (~195 tokens per parameter).
The model has been trained on the MosaicML platform with 256 x A100-40GB GPUs, leveraging their latest LLM examples repo . replit-code-v1-3b is powered by state-of-the-art LLM techniques, such as: Flash Attention for fast training and inference, AliBi positional embeddings to support variable context length at inference time, LionW optimizer , 
etc.
[LINK: LLM examples repo](https://github.com/mosaicml/examples/tree/release/v0.0.4/examples/llm)

## Intended Use

Replit intends this model be used by anyone as a foundational model for application-specific fine-tuning without strict limitations on commercial use.

## Limitations

The pre-training dataset may have contained offensive or inappropriate content even after applying data cleansing filters, and such content may be reflected in model generated text. We recommend that users exercise reasonable caution when using in production systems. Do not use for any applications that may cause harm or distress to individuals or groups.

## License

The model checkpoint and vocabulary file are licensed under the Creative Commons license (CC BY-SA-4.0). Under the license, you must give credit to Replit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests that Replit endorses you or your use.
The source code files ( *.py ) are licensed under the Apache 2.0 license.

## Contact

For questions and comments about the model, please post in the community section.

## How to Use

First of all, you need to install the latest versions of the following dependencies:
You can then load the model as follows:
To use the optimized Triton implementation of FlashAttention on GPUs with BF16 precision, first install the following dependencies:
Then, move the model to bfloat16 and use it as follows:
Note that trust_remote_code=True is passed to the from_pretrained method because ReplitLM is not a class in the Transformers library.
[LINK: Transformers](https://huggingface.co/docs/transformers/index)

### Tokenizer

We have trained a custom SentencePiece Unigram tokenizer optimized with a vocabulary specifically for code of 32768 tokens.
Note that using this requires the sentencepiece library to be installed.
The tokenizer can be used as follows:
Note that:
- trust_remote_code=True is passed to the from_pretrained method because ReplitLM is not a class in the Transformers library.
[LINK: Transformers](https://huggingface.co/docs/transformers/index)
- clean_up_tokenization_spaces=False is meant to avoid removing spaces in the output, because that would affect the syntactical correctness of the generated code.

### Generation

You can generate code using the transformers library as follows:
Experiment with different decoding methods and parameters to get the best results for your use case.

### Loading with 8-bit and 4-bit quantization

You can also load the model in 8-bit with the load_in_8bit=True kwarg that uses bitsandbytes under the hood.
First you need to  install the following additional dependanices:
Then you can load the model in 8bit as follows:
The additional kwargs that make this possible are device_map='auto' and load_in_8bit=True .
For loading in 4-bit, at the time of writing, support for load_in_4bit has not been merged into the latest releases for transformers and accelerate . However you can use it if you install the dependancies the main branches of the published repos:
Then load in 4-bit with:
- Hugging Face's Quantization Doc
[LINK: Hugging Face's Quantization Doc](https://huggingface.co/docs/transformers/main/main_classes/quantization)
- Original Blogpost introducing 8-bit
- New Blogpost introducing 4-bit

### Post Processing

Note that as with all code generation models, post-processing of the generated code is important. In particular, the following post-processing steps are recommended:
- stop generation when the EOS token is encountered
- remove trailing whitespaces
- set max_tokens to a reasonable value based on your completion use case
- truncate generation to stop words such as return , def , "```", " \n\n\n " to avoid generating incomplete code when max_tokens is larger than the length of the expected generated code.

## Model tree for replit/replit-code-v1-3b

## Dataset used to train replit/replit-code-v1-3b

## Spaces using replit/replit-code-v1-3b 28

## Papers for replit/replit-code-v1-3b

## Evaluation results

- pass@1 on HumanEval self-reported 0.219

--------------------
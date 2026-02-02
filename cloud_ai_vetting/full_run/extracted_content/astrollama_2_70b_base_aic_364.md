# Astrollama-2-70b-base_aic
**URL:** https://huggingface.co/AstroMLab/astrollama-2-70b-base_aic
**Page Title:** AstroMLab/astrollama-2-70b-base_aic · Hugging Face
--------------------


## AstroLLaMA-2-70B-Base_AIC

AstroLLaMA-2-70B-Base_AIC is a specialized base language model for astronomy, developed by fine-tuning Meta's LLaMA-2-70b architecture on astronomical literature. This model was developed by the AstroMLab team and is, to our best knowledge, the first specialized 70B parameter-level LLM in astronomy. It is designed for next token prediction tasks and is not an instruct/chat model.

## Model Details

- Base Architecture : LLaMA-2-70b
- Training Data : Abstract, Introduction, and Conclusion (AIC) sections from arXiv's astro-ph category papers (from arXiv's inception up to July 2023)
- Data Processing : The training data was derived from LaTeX source files using regex-based extraction methods to identify and extract the relevant sections (Abstract, Introduction, and Conclusion).
- Fine-tuning Method : Continual Pre-Training (CPT) using the LMFlow framework
- Training Details : Learning rate: 2 × 10⁻⁵ Total batch size: 160 Maximum token length: 2048 Warmup ratio: 0.03 Cosine decay schedule for learning rate reduction Training duration: 1 epoch (approximately 2,000 A100 GPU hours)
- Learning rate: 2 × 10⁻⁵
- Total batch size: 160
- Maximum token length: 2048
- Warmup ratio: 0.03
- Cosine decay schedule for learning rate reduction
- Training duration: 1 epoch (approximately 2,000 A100 GPU hours)
- Primary Use : Next token prediction for astronomy-related text generation and analysis
- Reference : Pan et al. 2024

## Generating text from a prompt

## Model Performance and Significance

AstroLLaMA-2-70B-Base_AIC demonstrates notable improvements over its baseline LLaMA-2-70B model, marking a crucial step in specialized astronomical LLMs. Here's a performance comparison chart based upon the astronomical benchmarking Q&A as described in Ting et al. 2024 :
It demonstrates that training specialized LLMs can be effective, especially at larger model scales.

## Ethical Considerations

While this model is designed for scientific use, users should be mindful of potential misuse, such as generating misleading scientific content. Always verify model outputs against peer-reviewed sources for critical applications.

## Citation

If you use this model in your research, please cite:

## Model tree for AstroMLab/astrollama-2-70b-base_aic

Base model

## Papers for AstroMLab/astrollama-2-70b-base_aic


--------------------
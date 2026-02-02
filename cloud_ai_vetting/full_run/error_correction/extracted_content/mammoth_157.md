# MAmmoTH
**URL:** https://tiger-ai-lab.github.io/MAmmoTH
**Page Title:** MAmmoTH
--------------------


## 🦣 MAmmoTH: Building Math Generalist Models through Hybrid Instruction Tuning

[LINK: Xiang Yue](https://xiangyue9607.github.io/)
[LINK: Yao Fu](https://franxyao.github.io/)
[LINK: Yu Su](https://ysu1989.github.io/)
[LINK: Wenhu Chen](https://wenhuchen.github.io/)
[LINK: Code](https://github.com/TIGER-AI-Lab/MAmmoTH)

## Abstract

We introduce 🦣MAmmoTH, a series of open-source large language models (LLMs) specifically tailored for general math problem-solving. The MAmmoTH models are trained on MathInstruct, our meticulously curated instruction tuning dataset. MathInstruct is compiled
                                from 13 math datasets with intermediate rationales, six of which have rationales newly curated by us. It boasts the hybrid of chain-of- thought (CoT) and program-of-thought (PoT) rationales, and also ensures exten- sive
                                coverage of diverse fields in math. The hybrid of CoT and PoT can not only unleash the potential of tool use but also allow different thought processes for dif- ferent math problems. As a result, the MAmmoTH series substantially
                                outperform existing open-source models on nine mathematical reasoning datasets across all scales with an average accuracy gain ranging from 12% to 29%. Remarkably, our MAmmoTH-7B model reaches 35% on MATH (a competition-level
                                dataset), which exceeds the best open-source 7B model (WizardMath) by 25%, and the MAmmoTH-34B model achieves 46% accuracy on MATH, even surpassing GPT- 4’s CoT result. Our work underscores the importance of diverse problem
                                coverage and the use of hybrid rationales in developing superior math generalist models.

## Figure 1: The hybrid instruction tuning of 🦣MAmmoTH, a series of models trained to solve a diverse set of mathematical problems using CoTs and PoTs.

## Our Dataset: MathInstruct

## Overall Results

## Figure 2: Overall results of 🦣MAmmoTH on the in-domain and out-of-domain datasets.

Overall, we can see that MAmmoTH and MAmmoTH-Coder are able to outperform the SoTA model at different scales. In general, the performance gain for OOD datasets is more significant than IND datasets. These results show us the potential of our models as
                                a mathematical generalist. On several datasets, MAmmoTH-Coder-34B and MAmmoTH-70B are even surpassing closed-source LLMs (see more break down results below).

## Where does the gain come from?

## Figure 3: Investigation of the influence of CoT \& PoT hybrid training on the 7B Llama-2 model. Key insights include: 1) The SoTA model, utilizing dataset-specific CoT fine-tuning on GSM and MATH, displays strong performance within its domains but struggles
                                in OOD scenarios; 2) Diverse data sources in MathInstruct enable better math generalist model; 3) Fine-tuning on the PoT subsets generally outperforms fine-tuning on the CoT subsets; 4) Hybrid training yields the best-performing
                                model.

In order to better understand what factors contribute to the great gain of 🦣MAmmoTH over existing baselines, we set up a group of control experiments in the Figure 3. We study the following setups:
- 🦣 MAmmoTH (MathInstruct - CoT): This experiment aims to understand how much our curated CoT data could improve the generalization over the SoTA model WizardMath trained specifically on GSM + MATH. As can be seen,
                                        while sacrificing accuracy on GSM + MATH by 3%, our CoT subset fine-tuning improves the overall nine-dataset accuracy from 27% to 32%.
- 🦣 MAmmoTH (MathInstruct - PoT): This experiment aims to understand the advantage of our PoT subset. As can be observed, our PoT subset fine-tuning can significantly improve the overall accuracy from 27% to 37.5%.
                                        This ablation reflects the importance of unlocking the program generation capabilities of our model.
- 🦣 MAmmoTH (MathInstruct - Hybrid): We further combine CoT and PoT as the hybrid training data to achieve the best overall performance of 45.4%. This combined gain comes from two aspects: The CoT subset can help maintain the generic language-based reasoning skills to handle scenarios where PoT cannot handle well, e.g., the multi-choice questions in AQuA, SAT, and MMLU. The PoT subset can teach the model how to utilize Python APIs to solve complex math problems with high precision, e.g., the MATH problems requiring complex computation.
- The CoT subset can help maintain the generic language-based reasoning skills to handle scenarios where PoT cannot handle well, e.g., the multi-choice questions in AQuA, SAT, and MMLU.
- The PoT subset can teach the model how to utilize Python APIs to solve complex math problems with high precision, e.g., the MATH problems requiring complex computation.

## Comprehensive Results: Break Down

## Reference


--------------------
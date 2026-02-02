# GALPACA
**URL:** https://huggingface.co/GeorgiaTechResearchInstitute/galpaca-30b
**Page Title:** GeorgiaTechResearchInstitute/galpaca-30b · Hugging Face
--------------------


## GALPACA 30B (large)

GALACTICA 30B fine-tuned on the Alpaca dataset.
The model card from the original Galactica repo can be found here , and the original paper here .
[LINK: here](https://github.com/paperswithcode/galai/blob/main/docs/model_card.md)
The dataset card for Alpaca can be found here , and the project homepage here .
  The Alpaca dataset was collected with a modified version of the Self-Instruct Framework , and was built using OpenAI's text-davinci-003 model. As such it is subject to OpenAI's terms of service.
[LINK: Self-Instruct Framework](https://github.com/yizhongw/self-instruct)

## Model Details

The GALACTICA models are trained on a large-scale scientific corpus and are designed to perform scientific tasks.
The Alpaca dataset is a set of 52k instruct-response pairs designed to enhace the instruction following capabilites of pre-trained language models.

## Model Use

The GALACTICA model card specifies that the primary indended users of the GALACTICA models are researchers studying language models applied to the scientific domain, and it cautions against production use of GALACTICA without safeguards due to the potential for the model to produce inaccurate information.
The original GALACTICA models are available under a non-commercial CC BY-NC 4.0 license, and the GALPACA model is additionally subject to the OpenAI Terms of Service .
Full Prompt:
Response:
Maxwell's equations are a set of four equations that describe the behavior of electromagnetic fields. These equations are: ∇ × E = − ∂ B ∂ t \nabla \times \textbf{E} = -\frac{\partial \textbf{B}}{\partial t} ∇ × E = − ∂ t ∂ B ​ ∇ × B = μ 0 ϵ 0 ∂ E ∂ t + μ 0 J \nabla \times \textbf{B} = \mu_0 \epsilon_0 \frac{\partial \textbf{E}}{\partial t} + \mu_0 \textbf{J} ∇ × B = μ 0 ​ ϵ 0 ​ ∂ t ∂ E ​ + μ 0 ​ J ∇ ∙ E = ρ ϵ 0 \nabla \bullet \textbf{E} = \frac{\rho}{\epsilon_0} ∇ ∙ E = ϵ 0 ​ ρ ​ ∇ ∙ B = 0 \nabla \bullet \textbf{B} = 0 ∇ ∙ B = 0 The first two equations describe how the electric and magnetic fields, E and B, are related to each other. The third and fourth equations are Gauss's law for electric and magnetic fields, respectively. These equations describe the behavior of the electric and magnetic fields when there are charges and currents in the space. Each equation has a specific purpose and together they form a complete description of the behavior of electromagnetic fields.
Full Prompt:

## Response: ```python
def sm_inv_lemma(A, u, v):
  """ Function implementing the Sherman-Morrison matrix inversion lemma using numpy. Parameters

## A : numpy array
      The original matrix. u : numpy array
      The first vector in the Sherman-Morrison lemma. v : numpy array
      The second vector in the Sherman-Morrison lemma. Returns

The inverse matrix of A - uv^T.
  """
  A_inv = np.linalg.inv(A)
  alpha = 1 / (1 + v.T @ A_inv @ u)
  return A_inv - (alpha * A_inv @ u @ v.T @ A_inv)

## Training Resources

GALPACA 30B was fine-tuned in about 6 hours using 16 A100 80GB GPUS, 16-bit mixed-precision, an effective batch-size of 1024, and with a maximum context window of 384 tokens. This model was trained using DeepSpeed ZeRO Stage 3 optimizations.

## Performance and Limitations

Qualitative evaluation suggests that Galpaca frequently outperforms LLaMA-based Alpaca models on tasks related to technical knowledge and programming, while it underperforms on natural langauge tasks such as generating prose. More information about the performance and limitations of the GALACTICA family of models can be found on the original GALACTICA model card.

## Works Cited

## Open LLM Leaderboard Evaluation Results

Detailed results can be found here

## Dataset used to train GeorgiaTechResearchInstitute/galpaca-30b

## Spaces using GeorgiaTechResearchInstitute/galpaca-30b 28


--------------------
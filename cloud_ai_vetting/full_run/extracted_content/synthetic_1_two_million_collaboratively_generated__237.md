# SYNTHETIC-1: Two Million Collaboratively Generated Reasoning Traces from Deepseek-R1
**URL:** https://huggingface.co/datasets/PrimeIntellect/SYNTHETIC-1-SFT-Data
**Page Title:** PrimeIntellect/SYNTHETIC-1-SFT-Data · Datasets at Hugging Face
--------------------


## SYNTHETIC-1: Two Million Crowdsourced Reasoning Traces from Deepseek-R1

SYNTHETIC-1 is a reasoning dataset obtained from Deepseek-R1, generated with crowdsourced compute and annotated with diverse verifiers such as LLM judges or symbolic mathematics verifiers. This is the SFT version of the dataset - the raw data and preference dataset can be found in our 🤗 SYNTHETIC-1 Collection .
The dataset consists of the following tasks and verifiers that were implemented in our library genesys :
[LINK: genesys](https://github.com/PrimeIntellect-ai/genesys)

### Mathematics Problems (777k samples):

- Tasks: Competition-Level Math Problems from NuminaMath , with LLM-based post-processing to turn multiple-choice questions into free form questions and to filter out questions without automatically verifiable responses (e.g. questions asking for proofs)
- Verifier: Symbolic verification based on the math-verify library
[LINK: math-verify](https://github.com/huggingface/Math-Verify)
- Task Dataset: PrimeIntellect/verifiable-math-problems

### Algorithmic Coding Problems (144k samples):

- Tasks: Algorithmic Challenges from coding competitions and platforms such as Leetcode, curated from Apps , Codecontests , Codeforces and TACO datasets. LLM-based post-processing was applied to additionally translate Python problems into Javascript, Rust and C++ problems
- Verifier: Containerized execution of unit tests
- Task Dataset: PrimeIntellect/verifiable-coding-problems

### Real-World Software Engineering Problems (70k samples):

- Tasks: Derived from real-world GitHub commits in the CommitPack dataset. Each problem pairs a pre-commit code file with an LLM-generated modification instruction, crafted using context from the original commit message and the post-commit file state.
- Verifier: An LLM judge compares LLM-generated code against the actual post-commit file state.
- Task Dataset: PrimeIntellect/real-world-swe-problems

### Open-Ended STEM Question Answering (313k samples):

- Tasks: Questions curated from a broad range of technical and scientific topics using the StackExchange dataset . LLM-based filtering retains only those questions with objectively correct responses, excluding opinion-based queries, and only keeps questions that require genuine reasoning rather than simple recall or memorization of information.w
- Verifier: An LLM judge scores responses by comparing them to the most upvoted answer.
- Task Dataset: PrimeIntellect/stackexchange-question-answering

### Synthetic Code Understanding Tasks (61k samples):

- Tasks: Fully synthetic task where the goal is to predict the output of code that performs string transformations given the code and some string input. We generate arbitrary string-processing functions via LLM prompting and recursively increase their complexity using a scheme akin to evol-instruct . Inputs include both random strings and snippets from news articles, with ground truth outputs obtained by executing the generated code.
- Verifier: LLM-predicted output strings are directly compared with real output strings and are judged as correct when an exact match occurs.
- Task Dataset: PrimeIntellect/synthetic-code-understanding

## Citation

Feel free to cite SYNTHETIC-1 if you have found it useful for your work

## Models trained or fine-tuned on PrimeIntellect/SYNTHETIC-1-SFT-Data

## Collection including PrimeIntellect/SYNTHETIC-1-SFT-Data

## Paper for PrimeIntellect/SYNTHETIC-1-SFT-Data


--------------------
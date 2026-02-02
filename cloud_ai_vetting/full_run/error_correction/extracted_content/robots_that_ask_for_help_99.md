# Robots That Ask For Help
**URL:** https://robot-help.github.io
**Page Title:** Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners
--------------------


## Robots That Ask For Help : Uncertainty Alignment for Large Language Model Planners

- Allen Z. Ren
[LINK: Allen Z. Ren](//allenzren.github.io)
- Anushri Dixit
- Alexandra Bodrova
- Sumeet Singh
- Stephen Tu
[LINK: Stephen Tu](//stephentu.github.io/)
- Noah Brown
- Peng Xu
- Leila Takayama
- Fei Xia
[LINK: Fei Xia](//fxia22.github.io/)
- Jake Varley
- Zhenjia Xu
- Dorsa Sadigh
- Andy Zeng
[LINK: Andy Zeng](//andyzeng.github.io/)
- Anirudha Majumdar
[LINK: Code](https://github.com/google-research/google-research/tree/master/language_model_uncertainty)

### Abstract

Large language models (LLMs) exhibit a wide range of promising capabilities --- from step-by-step planning to commonsense reasoning --- that may provide utility for robots, but remain prone to confidently hallucinated predictions. In this work, we present KnowNo, which is a framework for measuring and aligning the uncertainty of LLM-based planners such that they know when they don't know and ask for help when needed. KnowNo builds on the theory of conformal prediction to provide statistical guarantees on task completion while minimizing human help in complex multi-step planning settings. Experiments across a variety of simulated and real robot setups that involve tasks with different modes of ambiguity (e.g., from spatial to numeric uncertainties, from human preferences to Winograd schemas) show that KnowNo performs favorably over modern baselines (which may involve ensembles or extensive prompt tuning) in terms of improving efficiency and autonomy, while providing formal assurances. KnowNo can be used with LLMs out of the box without model-finetuning, and suggests a promising lightweight approach to modeling uncertainty that can complement and scale with the growing capabilities of foundation models.

### Goal

In the setting of the robot with access to a LLM-based planner and human help, we aim to achieve both: (1) calibrated confidence: the robot should seek sufficient help to ensure a statistically guaranteed level of task success specified by the user, and (2) minimal help: the robot should minimize the overall amount of help it seeks by narrowing down possible ambiguities in a task. We collectively refer to these sufficiency and minimality conditions as uncertainty alignment .

### Approach

KnowNo builds upon conformal prediction (CP) to formally quantify the LLM uncertainty and achieve uncertainty alignment. KnowNo first constructs a calibration dataset that covers diverse scenarios that the robot encounters. For each scenario, KnowNo prompts LLM to generate plausible options and then ask it to choose one --- similar to a Multiple Choice Question Answering (MCQA) setup. KnowNo obtains the likelihood of the LLM predicting the five choices: A, B, C, D, E. Then calibration is done using the likelihood of the true options of the calibration data, and the result is a likelihood threshold. At test time given a new scenario, the prediction set includes options with likelihood above the threshold. CP provides statistical guarantee that the true option is included in the prediction set with probability of a user-specified level. In addition, CP affords the benefit of producing smallest average prediction set size with theoretical guarantees.

### Experiment Videos

Choose a user instruction:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
User instruction: Sort the items that human likes in the blue plate, and ones human dislikes in the green plate. Items involved in each trial:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Choose a user instruction:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:
Prediction set, human help, executed action:

### Citation

### Acknowledgements

This work was partially supported by the NSF CAREER Award [\#2044149] and the Office of Naval Research [N00014-23-1-2148]. We thank Chad Boodoo for helping set up the UR5 hardware experiments, and Jensen Gao, Nathaniel Simon, and David Snyder for the helpful feedback on the paper. The website template is from Code as Policies .
[LINK: Code as Policies](https://code-as-policies.github.io/)

--------------------
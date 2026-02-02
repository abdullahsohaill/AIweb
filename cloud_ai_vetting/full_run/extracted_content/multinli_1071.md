# MultiNLI
**URL:** https://cims.nyu.edu/~sbowman/multinli
**Page Title:** MultiNLI
--------------------


## MultiNLI

### The Multi-Genre NLI Corpus

Adina Williams Nikita Nangia Sam Bowman NYU
[LINK: Nikita Nangia](https://woollysocks.github.io/)
The Multi-Genre Natural Language Inference (MultiNLI) corpus is a crowd-sourced collection of 433k sentence pairs annotated with textual entailment information. The corpus is modeled on the SNLI corpus, but differs in that covers a range of genres of spoken and written text, and supports a distinctive cross-genre generalization evaluation. The corpus served as the basis for the shared task of the RepEval 2017 Workshop at EMNLP in Copenhagen.
[LINK: RepEval 2017 Workshop](https://repeval2017.github.io/shared/)
MultiNLI is distributed in a single ZIP file containing the corpus as both JSON lines (jsonl) and tab-separated text (txt).
Download: MultiNLI 1.0 (227MB, ZIP)
MultiNLI 0.9 differs from MultiNLI 1.0 only in the pairID and promptID fields in the training and development sets (and the attached paper), so results achieved on version 0.9 are still valid on 1.0. Version 0.9 can be downloaded here .
MultiNLI is modeled after SNLI. The two corpora are distributed in the same formats, and for many applications, it may be productive to treat them as a single, larger corpus. You can find out more about SNLI here and download it from an NYU mirror here .
A description of the data can be found here (PDF) or in the corpus package zip. If you use the corpus in an academic paper, please cite us:
The data description paper presents the following baselines:
Note that the ESIM relies on attention between sentences and would be ineligible for inclusion in the RepEval competition. All three models are trained on a mix of MultiNLI and SNLI and use GloVe word vectors. Code (TensorFlow/Python) is available here , alongside a script to reproduce the categories used in the error analysis in the paper.
[LINK: here](https://github.com/NYU-MLL/multiNLI)
Additional analysis-oriented datasets are available as part of GLUE and here .
[LINK: here](https://abhilasharavichander.github.io/NLI_StressTest/)
To evaluate your system on the full test set, use the following Kaggle in Class competitions. You do not need to submit code to evaluate your model, and you may evaluate under a psuedonym, but you are expected to post a brief description of your model in the competition discussion board.
- MultiNLI Matched
- MultiNLI Mismatched
These competitions will be open indefinitely. Evaluations on a subset of the test set had previously been conducted with different leaderboards through the RepEval 2017 Workshop .
[LINK: RepEval 2017 Workshop](https://repeval2017.github.io/shared/)
Researchers interested in multi-task learning and general-purpose representation learning can also access the test set through a separate leaderboard on the GLUE platform .
The best result (state of the art) that we've seen written up in a paper is 82.1/81.4 from Radford et al. 2018 .
The XNLI corpus provides additional development and test sets for MultiNLI in fifteen languages.
Evaluations on the hard subset of the test set used in Gururangan et al. '18 are available separately ( matched / mismatched ).
See details in the data description paper .
This work was made possible by a Google Faculty Research Award. We also thank George Dahl, the organizers
of the RepEval 2016 and RepEval 2017 workshops,
Andrew Drozdov, Angeliki Lazaridou, and
our other NYU colleagues for help and advice.

--------------------
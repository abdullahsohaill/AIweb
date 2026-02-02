# AlpacaEval
**URL:** https://tatsu-lab.github.io/alpaca_eval
**Page Title:** AlpacaEval Leaderboard
--------------------


## AlpacaEval Leaderboard

## An Automatic Evaluator for Instruction-following Language Models

[LINK: Github](https://github.com/tatsu-lab/alpaca_eval)

## About AlpacaEval

AlpacaEval an LLM-based automatic evaluation that is fast, cheap, and reliable.
            It is based on the AlpacaFarm evaluation set,
            which tests the ability of models to follow general user instructions.
            These responses are then compared to reference responses (Davinci003 for AlpacaEval, GPT-4 Preview for AlpacaEval 2.0) by
            the provided GPT-4 based auto-annotators,
            which results in the win rates presented above.
            AlpacaEval displays a high agreement rate with ground truth human annotations,
            and leaderboard rankings on AlpacaEval are very correlated with leaderboard rankings
            based on human annotators.
            Please see our documentation for more details on our analysis.
[LINK: AlpacaEval](https://github.com/tatsu-lab/alpaca_eval)
[LINK: documentation](https://github.com/tatsu-lab/alpaca_eval#analysis)

## Adding new models

We welcome new model contributions to the leaderboard from the community!
            To do so, please follow the steps in the contributions
                section .
            Specifically, you'll need to run the model on the evaluation set,
            auto-annotate the outputs, and submit a PR with the model config and leaderboard results.
            We've also set up a Discord for community support and discussion.
[LINK: contributions
                section](https://github.com/tatsu-lab/alpaca_eval#contributing)

## Adding new evaluators or eval sets

We also welcome contributions for new evaluators or new eval sets!
            For making new evaluators, we release our ground-truth human annotations and comparison
            metrics .
            We also release a rough guide to follow for making new eval sets.
            We specifically encourage contributions for harder instructions distributions and for safety testing of
            LLMs.
[LINK: human annotations](https://github.com/tatsu-lab/alpaca_eval#data-release)
[LINK: comparison
            metrics](https://github.com/tatsu-lab/alpaca_eval#analyzing-an-evaluator)
[LINK: rough guide](https://github.com/tatsu-lab/alpaca_eval#analyzing-an-eval-set)

## AlpacaEval limitations

While AlpacaEval provides a useful comparison of model capabilities in following instructions,
            it is not a comprehensive or gold-standard evaluation of model abilities.
            For one, as detailed in the AlpacaFarm paper ,
            the auto annotator winrates are correlated with length.
            Though human annotations also display this bias,
            it is unclear if more verbose answers add utility in downstream tasks.
            Additionally, the AlpacaFarm eval set, though diverse, consists mainly of simple instructions.
            We encourage the community to contribute new, more complex eval sets, such as for tool use.
            Finally, AlpacaEval does not evaluate the safety of any of the models.

--------------------
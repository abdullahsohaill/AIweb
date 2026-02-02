# Berkeley Function-Calling Leaderboard
**URL:** https://gorilla.cs.berkeley.edu/leaderboard.html
**Page Title:** Berkeley Function Calling Leaderboard (BFCL) V4
--------------------

[LINK: Try it Out!](#api-explorer)

## Berkeley Function-Calling Leaderboard

## BFCL: From Tool Use to Agentic Evaluation of Large Language Models

The Berkeley Function Calling Leaderboard (BFCL) V4
                evaluates the
                LLM's ability to call functions (aka tools) accurately. This
                leaderboard consists of real-world data and will be updated periodically. For more information on the
                evaluation dataset and methodology, please refer to our blogs: BFCL-v1 introducing AST as an
                evaluation metric, BFCL-v2 introducing enterprise and OSS-contributed functions, BFCL-v3 introducing multi-turn interactions, and BFCL-v4 introducing holistic agentic evaluation. Checkout code and
                    data .
[LINK: code and
                    data](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard)
[LINK: [Change
                                        Log]](https://github.com/ShishirPatil/gorilla/blob/main/berkeley-function-call-leaderboard/CHANGELOG.md)
[LINK: Grok-4-1-fast-reasoning (FC)](https://docs.x.ai/docs/models)
[LINK: Grok-4-0709 (Prompt)](https://docs.x.ai/docs/models)
[LINK: Grok-4-0709 (FC)](https://docs.x.ai/docs/models)
[LINK: Grok-4-1-fast-non-reasoning (FC)](https://docs.x.ai/docs/models)
[LINK: DeepSeek-V3.2-Exp (Prompt + Thinking)](https://api-docs.deepseek.com/news/news250528)
[LINK: DeepSeek-V3.2-Exp (FC)](https://api-docs.deepseek.com/news/news250528)
[LINK: mistral-large-2411 (FC)](https://docs.mistral.ai/guides/model-selection/)
[LINK: Mistral-Medium-2505](https://docs.mistral.ai/guides/model-selection/)
[LINK: Mistral-Medium-2505 (FC)](https://docs.mistral.ai/guides/model-selection/)
[LINK: Mistral-small-2506 (FC)](https://docs.mistral.ai/guides/model-selection/)
[LINK: Mistral-Small-2506 (Prompt)](https://docs.mistral.ai/guides/model-selection/)
[LINK: mistral-large-2411 (Prompt)](https://docs.mistral.ai/guides/model-selection/)
[LINK: Gemma-3-12b-it (Prompt)](https://blog.google/technology/developers/gemma-3/)
[LINK: Gemma-3-27b-it (Prompt)](https://blog.google/technology/developers/gemma-3/)
[LINK: Gemma-3-4b-it (Prompt)](https://blog.google/technology/developers/gemma-3/)
[LINK: Gemma-3-1b-it (Prompt)](https://blog.google/technology/developers/gemma-3/)
FC = native support for function/tool calling. Prompt = walk-around for function calling, using model's normal text generation capability.
Cost is calculated as an estimate of the cost for the entire benchmark, in USD. Latency is measured in seconds.
Overall Accuracy is the unweighted average of all the sub-categories.
                For details on score composition, please refer to our blog .
Format sensitivity test cases are only supported for prompt (non-FC) models.
Click on column header to sort. If you would like to add
                your model or contribute test-cases, please contact us via discord .
Models are evaluated using commit f7cf735 .
                All the model response we obtained is available here .
                To reproduce the results, please either checkout our codebase at this
                    checkpoint ,
                or install the PyPI package pip install bfcl-eval==2025.12.17 .
[LINK: here](https://github.com/HuanzhiMao/BFCL-Result)
[LINK: this
                    checkpoint](https://github.com/ShishirPatil/gorilla/commit/f7cf7359b7ac615a0b294831c5ba2bc95ee4a000)

## Wagon Wheel

The following chart shows the comparison of the models based on a few
                metrics. You can select and deselect which models to compare. More
                information on each metric can be found in the blog .

## Function Calling Demo

In this demo for function calling, you can enter a prompt and a
                function and see the output. There will be two outputs (and two output
                boxes accordingly): one in the actual code format (the top one) and
                the other in the OpenAI compatible format (the bottom one). Note that
                the OpenAI compatible format output is only available if the actual
                code output has valid syntax and can be parsed. We also provide you a
                few examples to try out and get a sense of the input format and the
                output.

## Contact Us

## Citation


--------------------
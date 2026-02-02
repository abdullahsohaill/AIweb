# **CommonsenseVQA**
**URL:** https://huggingface.co/datasets/tau/commonsense_qa
**Page Title:** tau/commonsense_qa · Datasets at Hugging Face
--------------------


## Dataset Card for "commonsense_qa"

### Dataset Summary

CommonsenseQA is a new multiple-choice question answering dataset that requires different types of commonsense knowledge
to predict the correct answers . It contains 12,102 questions with one correct answer and four distractor answers.
The dataset is provided in two major training/validation/testing set splits: "Random split" which is the main evaluation
split, and "Question token split", see paper for details.

### Supported Tasks and Leaderboards

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

The dataset is in English ( en ).

## Dataset Structure

### Data Instances

- Size of downloaded dataset files: 4.68 MB
- Size of the generated dataset: 2.18 MB
- Total amount of disk used: 6.86 MB
An example of 'train' looks as follows:

### Data Fields

The data fields are the same among all splits.
- id ( str ): Unique ID.
- question : a string feature.
- question_concept ( str ): ConceptNet concept associated to the question.
- choices : a dictionary feature containing: label : a string feature. text : a string feature.
- label : a string feature.
- text : a string feature.
- answerKey : a string feature.

### Data Splits

## Dataset Creation

### Curation Rationale

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Source Data

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Annotations

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Personal and Sensitive Information

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Considerations for Using the Data

### Social Impact of Dataset

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Discussion of Biases

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Other Known Limitations

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Additional Information

### Dataset Curators

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Licensing Information

The dataset is licensed under the MIT License.
See: https://github.com/jonathanherzig/commonsenseqa/issues/5
[LINK: https://github.com/jonathanherzig/commonsenseqa/issues/5](https://github.com/jonathanherzig/commonsenseqa/issues/5)

### Citation Information

### Contributions

Thanks to @thomwolf , @lewtun , @albertvillanova , @patrickvonplaten for adding this dataset.
[LINK: @thomwolf](https://github.com/thomwolf)
[LINK: @lewtun](https://github.com/lewtun)
[LINK: @albertvillanova](https://github.com/albertvillanova)
[LINK: @patrickvonplaten](https://github.com/patrickvonplaten)
[LINK: Repository: github.com](https://github.com/jonathanherzig/commonsenseqa)

## Models trained or fine-tuned on tau/commonsense_qa

## Spaces using tau/commonsense_qa 2

## Paper for tau/commonsense_qa


--------------------
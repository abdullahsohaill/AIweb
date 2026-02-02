# LoRA
Methods
**URL:** https://huggingface.co/docs/peft/main/en/task_guides/lora_based_methods
**Page Title:** LoRA methods
--------------------

PEFT documentation
LoRA methods

## PEFT

[LINK: 20,521](https://github.com/huggingface/peft)
[LINK: installation from source](/docs/peft/install#source)
[LINK: v0.18.0](/docs/peft/v0.18.0/task_guides/lora_based_methods)
and get access to the augmented documentation experience
to get started

## LoRA methods

A popular way to efficiently train large models is to insert (typically in the attention blocks) smaller trainable matrices that are a low-rank decomposition of the delta weight matrix to be learnt during finetuning. The pretrained model’s original weight matrix is frozen and only the smaller matrices are updated during training. This reduces the number of trainable parameters, reducing memory usage and training time which can be very expensive for large models.
There are several different ways to express the weight matrix as a low-rank decomposition, but Low-Rank Adaptation (LoRA) is the most common method. The PEFT library supports several other LoRA variants, such as Low-Rank Hadamard Product (LoHa) , Low-Rank Kronecker Product (LoKr) , and Adaptive Low-Rank Adaptation (AdaLoRA) . You can learn more about how these methods work conceptually in the Adapters guide. If you’re interested in applying these methods to other tasks and use cases like semantic segmentation, token classification, take a look at our notebook collection !
Additionally, PEFT supports the X-LoRA Mixture of LoRA Experts method.
This guide will show you how to quickly train an image classification model - with a low-rank decomposition method - to identify the class of food shown in an image.
Some familiarity with the general process of training an image classification model would be really helpful and allow you to focus on the low-rank decomposition methods. If you’re new, we recommend taking a look at the Image classification guide first from the Transformers documentation. When you’re ready, come back and see how easy it is to drop PEFT in to your training!
[LINK: Image classification](https://huggingface.co/docs/transformers/tasks/image_classification)
Before you begin, make sure you have all the necessary libraries installed.

## Dataset

In this guide, you’ll use the Food-101 dataset which contains images of 101 food classes (take a look at the dataset viewer to get a better idea of what the dataset looks like).
Load the dataset with the load_dataset function.
[LINK: load_dataset](https://huggingface.co/docs/datasets/main/en/package_reference/loading_methods#datasets.load_dataset)
Each food class is labeled with an integer, so to make it easier to understand what these integers represent, you’ll create a label2id and id2label dictionary to map the integer to its class label.
Load an image processor to properly resize and normalize the pixel values of the training and evaluation images.
You can also use the image processor to prepare some transformation functions for data augmentation and pixel scaling.
Define the training and validation datasets, and use the set_transform function to apply the transformations on-the-fly.
[LINK: set_transform](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset.set_transform)
Finally, you’ll need a data collator to create a batch of training and evaluation data and convert the labels to torch.tensor objects.

## Model

Now let’s load a pretrained model to use as the base model. This guide uses the google/vit-base-patch16-224-in21k model, but you can use any image classification model you want. Pass the label2id and id2label dictionaries to the model so it knows how to map the integer labels to their class labels, and you can optionally pass the ignore_mismatched_sizes=True parameter if you’re finetuning a checkpoint that has already been finetuned.

### PEFT configuration and model

Every PEFT method requires a configuration that holds all the parameters specifying how the PEFT method should be applied. Once the configuration is setup, pass it to the get_peft_model() function along with the base model to create a trainable PeftModel .
[LINK: get_peft_model()](/docs/peft/main/en/package_reference/peft_model#peft.get_peft_model)
[LINK: PeftModel](/docs/peft/main/en/package_reference/peft_model#peft.PeftModel)
Call the print_trainable_parameters() method to compare the number of parameters of PeftModel versus the number of parameters in the base model!
[LINK: print_trainable_parameters()](/docs/peft/main/en/package_reference/peft_model#peft.PeftModel.print_trainable_parameters)
[LINK: PeftModel](/docs/peft/main/en/package_reference/peft_model#peft.PeftModel)
LoRA decomposes the weight update matrix into two smaller matrices. The size of these low-rank matrices is determined by its rank or r . A higher rank means the model has more parameters to train, but it also means the model has more learning capacity. You’ll also want to specify the target_modules which determine where the smaller matrices are inserted. For this guide, you’ll target the query and value matrices of the attention blocks. Other important parameters to set are lora_alpha (scaling factor), bias (whether none , all or only the LoRA bias parameters should be trained), and modules_to_save (the modules apart from the LoRA layers to be trained and saved). All of these parameters - and more - are found in the LoraConfig .
[LINK: LoraConfig](/docs/peft/main/en/package_reference/lora#peft.LoraConfig)

### Training

For training, let’s use the Trainer class from Transformers. The Trainer contains a PyTorch training loop, and when you’re ready, call train to start training. To customize the training run, configure the training hyperparameters in the TrainingArguments class. With LoRA-like methods, you can afford to use a higher batch size and learning rate.
[LINK: Trainer](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.Trainer)
[LINK: train](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.Trainer.train)
[LINK: TrainingArguments](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments)
AdaLoRA has an update_and_allocate() method that should be called at each training step to update the parameter budget and mask, otherwise the adaptation step is not performed. This requires writing a custom training loop or subclassing the Trainer to incorporate this method. As an example, take a look at this custom training loop .
[LINK: update_and_allocate()](/docs/peft/main/en/package_reference/adalora#peft.AdaLoraModel.update_and_allocate)
[LINK: Trainer](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.Trainer)
[LINK: custom training loop](https://github.com/huggingface/peft/blob/912ad41e96e03652cabf47522cd876076f7a0c4f/examples/conditional_generation/peft_adalora_seq2seq.py#L120)
Begin training with train .
[LINK: train](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.Trainer.train)

## Share your model

Once training is complete, you can upload your model to the Hub with the push_to_hub method. You’ll need to login to your Hugging Face account first and enter your token when prompted.
[LINK: push_to_hub](https://huggingface.co/docs/transformers/main/en/main_classes/model#transformers.PreTrainedModel.push_to_hub)
Call push_to_hub to save your model to your repositoy.
[LINK: push_to_hub](https://huggingface.co/docs/transformers/main/en/main_classes/model#transformers.PreTrainedModel.push_to_hub)

## Inference

Let’s load the model from the Hub and test it out on a food image.
Convert the image to RGB and return the underlying PyTorch tensors.
Now run the model and return the predicted class!
[LINK: Update on GitHub](https://github.com/huggingface/peft/blob/main/docs/source/task_guides/lora_based_methods.md)
[LINK: ← Prompt-based methods](/docs/peft/main/en/task_guides/prompt_based_methods)
[LINK: IA3 →](/docs/peft/main/en/task_guides/ia3)

--------------------
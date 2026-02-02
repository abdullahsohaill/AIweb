# Transformers.js
**URL:** https://huggingface.co/docs/transformers.js
**Page Title:** Transformers.js
--------------------

Transformers.js documentation
Transformers.js

## Transformers.js

[LINK: 15,257](https://github.com/huggingface/transformers.js)
[LINK: v3.0.0](/docs/transformers.js/v3.0.0/index)
and get access to the augmented documentation experience
to get started

## Transformers.js

### State-of-the-art Machine Learning for the Web

State-of-the-art Machine Learning for the Web
Run 🤗 Transformers directly in your browser, with no need for a server!
Transformers.js is designed to be functionally equivalent to Hugging Face’s transformers python library, meaning you can run the same pretrained models using a very similar API. These models support common tasks in different modalities, such as:
[LINK: transformers](https://github.com/huggingface/transformers)
- 📝 Natural Language Processing : text classification, named entity recognition, question answering, language modeling, summarization, translation, multiple choice, and text generation.
- 🖼️ Computer Vision : image classification, object detection, segmentation, and depth estimation.
- 🗣️ Audio : automatic speech recognition, audio classification, and text-to-speech.
- 🐙 Multimodal : embeddings, zero-shot audio classification, zero-shot image classification, and zero-shot object detection.
Transformers.js uses ONNX Runtime to run models in the browser. The best part about it, is that you can easily convert your pretrained PyTorch, TensorFlow, or JAX models to ONNX using 🤗 Optimum .
[LINK: 🤗 Optimum](https://github.com/huggingface/optimum#onnx--onnx-runtime)
For more information, check out the full documentation .
[LINK: documentation](https://huggingface.co/docs/transformers.js)

## Quick tour

It’s super simple to translate from existing code! Just like the python library, we support the pipeline API. Pipelines group together a pretrained model with preprocessing of inputs and postprocessing of outputs, making it the easiest way to run models with the library.
You can also use a different model by specifying the model id or path as the second argument to the pipeline function. For example:
By default, when running in the browser, the model will be run on your CPU (via WASM). If you would like
to run the model on your GPU (via WebGPU), you can do this by setting device: 'webgpu' , for example:
For more information, check out the WebGPU guide .
The WebGPU API is still experimental in many browsers, so if you run into any issues,
please file a bug report .
[LINK: bug report](https://github.com/huggingface/transformers.js/issues/new?title=%5BWebGPU%5D%20Error%20running%20MODEL_ID_GOES_HERE&assignees=&labels=bug,webgpu&projects=&template=1_bug-report.yml)
In resource-constrained environments, such as web browsers, it is advisable to use a quantized version of
the model to lower bandwidth and optimize performance. This can be achieved by adjusting the dtype option,
which allows you to select the appropriate data type for your model. While the available options may vary
depending on the specific model, typical choices include "fp32" (default for WebGPU), "fp16" , "q8" (default for WASM), and "q4" . For more information, check out the quantization guide .

## Contents

The documentation is organized into 4 sections:
- GET STARTED provides a quick tour of the library and installation instructions to get up and running.
- TUTORIALS are a great place to start if you’re a beginner! We also include sample applications for you to play around with!
- DEVELOPER GUIDES show you how to use the library to achieve a specific goal.
- API REFERENCE describes all classes and functions, as well as their available parameters and types.

## Examples

Want to jump straight in? Get started with one of our sample applications/templates, which can be found here .
[LINK: here](https://github.com/huggingface/transformers.js-examples)
[LINK: code](https://github.com/xenova/whisper-web)
[LINK: code](https://github.com/xenova/doodle-dash)
[LINK: code](https://github.com/huggingface/transformers.js/tree/main/examples/code-completion/)
[LINK: code](https://github.com/huggingface/transformers.js/tree/main/examples/semantic-image-search-client/)
[LINK: code](https://github.com/huggingface/transformers.js/tree/main/examples/semantic-image-search/)
[LINK: code](https://github.com/huggingface/transformers.js/tree/main/examples/vanilla-js/)
[LINK: code](https://github.com/huggingface/transformers.js/tree/main/examples/react-translator/)
[LINK: code](https://github.com/huggingface/transformers.js/tree/main/examples/text-to-speech-client/)
[LINK: code](https://github.com/huggingface/transformers.js/tree/main/examples/extension/)
[LINK: code](https://github.com/huggingface/transformers.js/tree/main/examples/electron/)
[LINK: code](https://github.com/huggingface/transformers.js/tree/main/examples/next-client/)
[LINK: code](https://github.com/huggingface/transformers.js/tree/main/examples/next-server/)
[LINK: code](https://github.com/huggingface/transformers.js/tree/main/examples/node/)
[LINK: code](https://github.com/huggingface/transformers.js/tree/main/examples/demo-site/)
[LINK: demo](https://huggingface.github.io/transformers.js/)
Check out the Transformers.js template on Hugging Face to get started in one click!

## Supported tasks/models

Here is the list of all tasks and architectures currently supported by Transformers.js.
If you don’t see your task/model listed here or it is not yet supported, feel free
to open up a feature request here .
[LINK: here](https://github.com/huggingface/transformers.js/issues/new/choose)
To find compatible models on the Hub, select the “transformers.js” library tag in the filter menu (or visit this link ).
You can refine your search by selecting the task you’re interested in (e.g., text-classification ).

### Tasks

[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.FillMaskPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.QuestionAnsweringPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.FeatureExtractionPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.SummarizationPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.TextClassificationPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.TextGenerationPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.Text2TextGenerationPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.TokenClassificationPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.TranslationPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.ZeroShotClassificationPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.FeatureExtractionPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.BackgroundRemovalPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.DepthEstimationPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.ImageClassificationPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.ImageSegmentationPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.ImageToImagePipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.ObjectDetectionPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.ImageFeatureExtractionPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.AudioClassificationPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.AutomaticSpeechRecognitionPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.TextToAudioPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.DocumentQuestionAnsweringPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.ImageToTextPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.ZeroShotAudioClassificationPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.ZeroShotImageClassificationPipeline)
[LINK: (docs)](https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.ZeroShotObjectDetectionPipeline)

### Models

- ALBERT (from Google Research and the Toyota Technological Institute at Chicago) released with the paper ALBERT: A Lite BERT for Self-supervised Learning of Language Representations , by Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, Radu Soricut.
[LINK: ALBERT](https://huggingface.co/docs/transformers/model_doc/albert)
- Arcee (from Arcee AI) released with the blog post Announcing Arcee Foundation Models by Fernando Fernandes, Varun Singh, Charles Goddard, Lucas Atkins, Mark McQuade, Maziyar Panahi, Conner Stewart, Colin Kealty, Raghav Ravishankar, Lucas Krauss, Anneketh Vij, Pranav Veldurthi, Abhishek Thakur, Julien Simon, Scott Zembsch, Benjamin Langer, Aleksiej Cecocho, Maitri Patel.
[LINK: Arcee](https://huggingface.co/docs/transformers/model_doc/arcee)
- Audio Spectrogram Transformer (from MIT) released with the paper AST: Audio Spectrogram Transformer by Yuan Gong, Yu-An Chung, James Glass.
[LINK: Audio Spectrogram Transformer](https://huggingface.co/docs/transformers/model_doc/audio-spectrogram-transformer)
- BART (from Facebook) released with the paper BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension by Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Ves Stoyanov and Luke Zettlemoyer.
[LINK: BART](https://huggingface.co/docs/transformers/model_doc/bart)
- BEiT (from Microsoft) released with the paper BEiT: BERT Pre-Training of Image Transformers by Hangbo Bao, Li Dong, Furu Wei.
[LINK: BEiT](https://huggingface.co/docs/transformers/model_doc/beit)
- BERT (from Google) released with the paper BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding by Jacob Devlin, Ming-Wei Chang, Kenton Lee and Kristina Toutanova.
[LINK: BERT](https://huggingface.co/docs/transformers/model_doc/bert)
- Blenderbot (from Facebook) released with the paper Recipes for building an open-domain chatbot by Stephen Roller, Emily Dinan, Naman Goyal, Da Ju, Mary Williamson, Yinhan Liu, Jing Xu, Myle Ott, Kurt Shuster, Eric M. Smith, Y-Lan Boureau, Jason Weston.
[LINK: Blenderbot](https://huggingface.co/docs/transformers/model_doc/blenderbot)
- BlenderbotSmall (from Facebook) released with the paper Recipes for building an open-domain chatbot by Stephen Roller, Emily Dinan, Naman Goyal, Da Ju, Mary Williamson, Yinhan Liu, Jing Xu, Myle Ott, Kurt Shuster, Eric M. Smith, Y-Lan Boureau, Jason Weston.
[LINK: BlenderbotSmall](https://huggingface.co/docs/transformers/model_doc/blenderbot-small)
- BLOOM (from BigScience workshop) released by the BigScience Workshop .
[LINK: BLOOM](https://huggingface.co/docs/transformers/model_doc/bloom)
- CamemBERT (from Inria/Facebook/Sorbonne) released with the paper CamemBERT: a Tasty French Language Model by Louis Martin , Benjamin Muller , Pedro Javier Ortiz Suárez*, Yoann Dupont, Laurent Romary, Éric Villemonte de la Clergerie, Djamé Seddah and Benoît Sagot.
[LINK: CamemBERT](https://huggingface.co/docs/transformers/model_doc/camembert)
- Chinese-CLIP (from OFA-Sys) released with the paper Chinese CLIP: Contrastive Vision-Language Pretraining in Chinese by An Yang, Junshu Pan, Junyang Lin, Rui Men, Yichang Zhang, Jingren Zhou, Chang Zhou.
[LINK: Chinese-CLIP](https://huggingface.co/docs/transformers/model_doc/chinese_clip)
- CLAP (from LAION-AI) released with the paper Large-scale Contrastive Language-Audio Pretraining with Feature Fusion and Keyword-to-Caption Augmentation by Yusong Wu, Ke Chen, Tianyu Zhang, Yuchen Hui, Taylor Berg-Kirkpatrick, Shlomo Dubnov.
[LINK: CLAP](https://huggingface.co/docs/transformers/model_doc/clap)
- CLIP (from OpenAI) released with the paper Learning Transferable Visual Models From Natural Language Supervision by Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, Ilya Sutskever.
[LINK: CLIP](https://huggingface.co/docs/transformers/model_doc/clip)
- CLIPSeg (from University of Göttingen) released with the paper Image Segmentation Using Text and Image Prompts by Timo Lüddecke and Alexander Ecker.
[LINK: CLIPSeg](https://huggingface.co/docs/transformers/model_doc/clipseg)
- CodeGen (from Salesforce) released with the paper A Conversational Paradigm for Program Synthesis by Erik Nijkamp, Bo Pang, Hiroaki Hayashi, Lifu Tu, Huan Wang, Yingbo Zhou, Silvio Savarese, Caiming Xiong.
[LINK: CodeGen](https://huggingface.co/docs/transformers/model_doc/codegen)
- CodeLlama (from MetaAI) released with the paper Code Llama: Open Foundation Models for Code by Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Ellen Tan, Yossi Adi, Jingyu Liu, Tal Remez, Jérémy Rapin, Artyom Kozhevnikov, Ivan Evtimov, Joanna Bitton, Manish Bhatt, Cristian Canton Ferrer, Aaron Grattafiori, Wenhan Xiong, Alexandre Défossez, Jade Copet, Faisal Azhar, Hugo Touvron, Louis Martin, Nicolas Usunier, Thomas Scialom, Gabriel Synnaeve.
[LINK: CodeLlama](https://huggingface.co/docs/transformers/model_doc/llama_code)
- Cohere (from Cohere) released with the paper Command-R: Retrieval Augmented Generation at Production Scale by Cohere.
[LINK: Cohere](https://huggingface.co/docs/transformers/main/model_doc/cohere)
- ConvBERT (from YituTech) released with the paper ConvBERT: Improving BERT with Span-based Dynamic Convolution by Zihang Jiang, Weihao Yu, Daquan Zhou, Yunpeng Chen, Jiashi Feng, Shuicheng Yan.
[LINK: ConvBERT](https://huggingface.co/docs/transformers/model_doc/convbert)
- ConvNeXT (from Facebook AI) released with the paper A ConvNet for the 2020s by Zhuang Liu, Hanzi Mao, Chao-Yuan Wu, Christoph Feichtenhofer, Trevor Darrell, Saining Xie.
[LINK: ConvNeXT](https://huggingface.co/docs/transformers/model_doc/convnext)
- ConvNeXTV2 (from Facebook AI) released with the paper ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders by Sanghyun Woo, Shoubhik Debnath, Ronghang Hu, Xinlei Chen, Zhuang Liu, In So Kweon, Saining Xie.
[LINK: ConvNeXTV2](https://huggingface.co/docs/transformers/model_doc/convnextv2)
- D-FINE (from University of Science and Technology of China) released with the paper D-FINE: Redefine Regression Task in DETRs as Fine-grained Distribution Refinement by Yansong Peng, Hebei Li, Peixi Wu, Yueyi Zhang, Xiaoyan Sun, Feng Wu.
[LINK: D-FINE](https://huggingface.co/docs/transformers/model_doc/d_fine)
- DAC (from Descript) released with the paper Descript Audio Codec: High-Fidelity Audio Compression with Improved RVQGAN by Rithesh Kumar, Prem Seetharaman, Alejandro Luebs, Ishaan Kumar, Kundan Kumar.
[LINK: DAC](https://huggingface.co/docs/transformers/model_doc/dac)
- DeBERTa (from Microsoft) released with the paper DeBERTa: Decoding-enhanced BERT with Disentangled Attention by Pengcheng He, Xiaodong Liu, Jianfeng Gao, Weizhu Chen.
[LINK: DeBERTa](https://huggingface.co/docs/transformers/model_doc/deberta)
- DeBERTa-v2 (from Microsoft) released with the paper DeBERTa: Decoding-enhanced BERT with Disentangled Attention by Pengcheng He, Xiaodong Liu, Jianfeng Gao, Weizhu Chen.
[LINK: DeBERTa-v2](https://huggingface.co/docs/transformers/model_doc/deberta-v2)
- Decision Transformer (from Berkeley/Facebook/Google) released with the paper Decision Transformer: Reinforcement Learning via Sequence Modeling by Lili Chen, Kevin Lu, Aravind Rajeswaran, Kimin Lee, Aditya Grover, Michael Laskin, Pieter Abbeel, Aravind Srinivas, Igor Mordatch.
[LINK: Decision Transformer](https://huggingface.co/docs/transformers/model_doc/decision_transformer)
- DeiT (from Facebook) released with the paper Training data-efficient image transformers & distillation through attention by Hugo Touvron, Matthieu Cord, Matthijs Douze, Francisco Massa, Alexandre Sablayrolles, Hervé Jégou.
[LINK: DeiT](https://huggingface.co/docs/transformers/model_doc/deit)
- Depth Anything (from University of Hong Kong and TikTok) released with the paper Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data by Lihe Yang, Bingyi Kang, Zilong Huang, Xiaogang Xu, Jiashi Feng, Hengshuang Zhao.
[LINK: Depth Anything](https://huggingface.co/docs/transformers/main/model_doc/depth_anything)
- Depth Pro (from Apple) released with the paper Depth Pro: Sharp Monocular Metric Depth in Less Than a Second by Aleksei Bochkovskii, Amaël Delaunoy, Hugo Germain, Marcel Santos, Yichao Zhou, Stephan R. Richter, Vladlen Koltun.
- DETR (from Facebook) released with the paper End-to-End Object Detection with Transformers by Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas Usunier, Alexander Kirillov, Sergey Zagoruyko.
[LINK: DETR](https://huggingface.co/docs/transformers/model_doc/detr)
- DINOv2 (from Meta AI) released with the paper DINOv2: Learning Robust Visual Features without Supervision by Maxime Oquab, Timothée Darcet, Théo Moutakanni, Huy Vo, Marc Szafraniec, Vasil Khalidov, Pierre Fernandez, Daniel Haziza, Francisco Massa, Alaaeldin El-Nouby, Mahmoud Assran, Nicolas Ballas, Wojciech Galuba, Russell Howes, Po-Yao Huang, Shang-Wen Li, Ishan Misra, Michael Rabbat, Vasu Sharma, Gabriel Synnaeve, Hu Xu, Hervé Jegou, Julien Mairal, Patrick Labatut, Armand Joulin, Piotr Bojanowski.
[LINK: DINOv2](https://huggingface.co/docs/transformers/model_doc/dinov2)
- DINOv2 with Registers (from Meta AI) released with the paper DINOv2 with Registers by Timothée Darcet, Maxime Oquab, Julien Mairal, Piotr Bojanowski.
[LINK: DINOv2 with Registers](https://huggingface.co/docs/transformers/model_doc/dinov2_with_registers)
- DINOv3 (from Meta AI) released with the paper DINOv3 by Oriane Siméoni, Huy V. Vo, Maximilian Seitzer, Federico Baldassarre, Maxime Oquab, Cijo Jose, Vasil Khalidov, Marc Szafraniec, Seungeun Yi, Michaël Ramamonjisoa, Francisco Massa, Daniel Haziza, Luca Wehrstedt, Jianyuan Wang, Timothée Darcet, Théo Moutakanni, Leonel Sentana, Claire Roberts, Andrea Vedaldi, Jamie Tolan, John Brandt, Camille Couprie, Julien Mairal, Hervé Jégou, Patrick Labatut, Piotr Bojanowski.
[LINK: DINOv3](https://huggingface.co/docs/transformers/model_doc/dinov3)
- DistilBERT (from HuggingFace), released together with the paper DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter by Victor Sanh, Lysandre Debut and Thomas Wolf. The same method has been applied to compress GPT2 into DistilGPT2 , RoBERTa into DistilRoBERTa , Multilingual BERT into DistilmBERT and a German version of DistilBERT.
[LINK: DistilBERT](https://huggingface.co/docs/transformers/model_doc/distilbert)
[LINK: DistilGPT2](https://github.com/huggingface/transformers/tree/main/examples/research_projects/distillation)
[LINK: DistilRoBERTa](https://github.com/huggingface/transformers/tree/main/examples/research_projects/distillation)
[LINK: DistilmBERT](https://github.com/huggingface/transformers/tree/main/examples/research_projects/distillation)
- DiT (from Microsoft Research) released with the paper DiT: Self-supervised Pre-training for Document Image Transformer by Junlong Li, Yiheng Xu, Tengchao Lv, Lei Cui, Cha Zhang, Furu Wei.
[LINK: DiT](https://huggingface.co/docs/transformers/model_doc/dit)
- Donut (from NAVER), released together with the paper OCR-free Document Understanding Transformer by Geewook Kim, Teakgyu Hong, Moonbin Yim, Jeongyeon Nam, Jinyoung Park, Jinyeong Yim, Wonseok Hwang, Sangdoo Yun, Dongyoon Han, Seunghyun Park.
[LINK: Donut](https://huggingface.co/docs/transformers/model_doc/donut)
- DPT (from Intel Labs) released with the paper Vision Transformers for Dense Prediction by René Ranftl, Alexey Bochkovskiy, Vladlen Koltun.
[LINK: DPT](https://huggingface.co/docs/transformers/master/model_doc/dpt)
- EdgeTAM (from Facebook) released with the paper EdgeTAM: On-Device Track Anything Model by Chong Zhou, Chenchen Zhu, Yunyang Xiong, Saksham Suri, Fanyi Xiao, Lemeng Wu, Raghuraman Krishnamoorthi, Bo Dai, Chen Change Loy, Vikas Chandra, Bilge Soran.
[LINK: EdgeTAM](https://huggingface.co/docs/transformers/model_doc/edgetam)
- EfficientNet (from Google Brain) released with the paper EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks by Mingxing Tan, Quoc V. Le.
[LINK: EfficientNet](https://huggingface.co/docs/transformers/model_doc/efficientnet)
- ELECTRA (from Google Research/Stanford University) released with the paper ELECTRA: Pre-training text encoders as discriminators rather than generators by Kevin Clark, Minh-Thang Luong, Quoc V. Le, Christopher D. Manning.
[LINK: ELECTRA](https://huggingface.co/docs/transformers/model_doc/electra)
- ERNIE-4.5 (from Baidu ERNIE Team) released with the blog post Announcing the Open Source Release of the ERNIE 4.5 Model Family by the Baidu ERNIE Team.
- ESM (from Meta AI) are transformer protein language models. ESM-1b was released with the paper Biological structure and function emerge from scaling unsupervised learning to 250 million protein sequences by Alexander Rives, Joshua Meier, Tom Sercu, Siddharth Goyal, Zeming Lin, Jason Liu, Demi Guo, Myle Ott, C. Lawrence Zitnick, Jerry Ma, and Rob Fergus. ESM-1v was released with the paper Language models enable zero-shot prediction of the effects of mutations on protein function by Joshua Meier, Roshan Rao, Robert Verkuil, Jason Liu, Tom Sercu and Alexander Rives. ESM-2 and ESMFold were released with the paper Language models of protein sequences at the scale of evolution enable accurate structure prediction by Zeming Lin, Halil Akin, Roshan Rao, Brian Hie, Zhongkai Zhu, Wenting Lu, Allan dos Santos Costa, Maryam Fazel-Zarandi, Tom Sercu, Sal Candido, Alexander Rives.
[LINK: ESM](https://huggingface.co/docs/transformers/model_doc/esm)
- EXAONE (from LG AI Research) released with the papers EXAONE 3.0 7.8B Instruction Tuned Language Model and EXAONE 3.5: Series of Large Language Models for Real-world Use Cases by the LG AI Research team.
- Falcon (from Technology Innovation Institute) by Almazrouei, Ebtesam and Alobeidli, Hamza and Alshamsi, Abdulaziz and Cappelli, Alessandro and Cojocaru, Ruxandra and Debbah, Merouane and Goffinet, Etienne and Heslow, Daniel and Launay, Julien and Malartic, Quentin and Noune, Badreddine and Pannier, Baptiste and Penedo, Guilherme.
[LINK: Falcon](https://huggingface.co/docs/transformers/model_doc/falcon)
- FastViT (from Apple) released with the paper FastViT: A Fast Hybrid Vision Transformer using Structural Reparameterization by Pavan Kumar Anasosalu Vasu, James Gabriel, Jeff Zhu, Oncel Tuzel and Anurag Ranjan.
- FLAN-T5 (from Google AI) released in the repository google-research/t5x by Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, Albert Webson, Shixiang Shane Gu, Zhuyun Dai, Mirac Suzgun, Xinyun Chen, Aakanksha Chowdhery, Sharan Narang, Gaurav Mishra, Adams Yu, Vincent Zhao, Yanping Huang, Andrew Dai, Hongkun Yu, Slav Petrov, Ed H. Chi, Jeff Dean, Jacob Devlin, Adam Roberts, Denny Zhou, Quoc V. Le, and Jason Wei
[LINK: FLAN-T5](https://huggingface.co/docs/transformers/model_doc/flan-t5)
[LINK: google-research/t5x](https://github.com/google-research/t5x/blob/main/docs/models.md#flan-t5-checkpoints)
- Florence2 (from Microsoft) released with the paper Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks by Bin Xiao, Haiping Wu, Weijian Xu, Xiyang Dai, Houdong Hu, Yumao Lu, Michael Zeng, Ce Liu, Lu Yuan.
- Gemma (from Google) released with the paper Gemma: Open Models Based on Gemini Technology and Research by the Gemma Google team.
[LINK: Gemma](https://huggingface.co/docs/transformers/main/model_doc/gemma)
[LINK: Gemma: Open Models Based on Gemini Technology and Research](https://blog.google/technology/developers/gemma-open-models/)
- Gemma2 (from Google) released with the paper Gemma2: Open Models Based on Gemini Technology and Research by the Gemma Google team.
[LINK: Gemma2](https://huggingface.co/docs/transformers/main/model_doc/gemma2)
[LINK: Gemma2: Open Models Based on Gemini Technology and Research](https://blog.google/technology/developers/google-gemma-2/)
- Gemma3 (from Google) released with the paper Introducing Gemma 3: The most capable model you can run on a single GPU or TPU by the Gemma Google team.
[LINK: Gemma3](https://huggingface.co/docs/transformers/main/model_doc/gemma3)
[LINK: Introducing Gemma 3: The most capable model you can run on a single GPU or TPU](https://blog.google/technology/developers/gemma-3/)
- Gemma3n (from Google) released with the paper Announcing Gemma 3n preview: powerful, efficient, mobile-first AI by the Gemma Google team.
[LINK: Gemma3n](https://huggingface.co/docs/transformers/main/model_doc/gemma3n)
[LINK: Announcing Gemma 3n preview: powerful, efficient, mobile-first AI](https://developers.googleblog.com/en/introducing-gemma-3n/)
- GLM (from the GLM Team, THUDM & ZhipuAI) released with the paper ChatGLM: A Family of Large Language Models from GLM-130B to GLM-4 All Tools by Team GLM: Aohan Zeng, Bin Xu, Bowen Wang, Chenhui Zhang, Da Yin, Dan Zhang, Diego Rojas, Guanyu Feng, Hanlin Zhao, Hanyu Lai, Hao Yu, Hongning Wang, Jiadai Sun, Jiajie Zhang, Jiale Cheng, Jiayi Gui, Jie Tang, Jing Zhang, Jingyu Sun, Juanzi Li, Lei Zhao, Lindong Wu, Lucen Zhong, Mingdao Liu, Minlie Huang, Peng Zhang, Qinkai Zheng, Rui Lu, Shuaiqi Duan, Shudan Zhang, Shulin Cao, Shuxun Yang, Weng Lam Tam, Wenyi Zhao, Xiao Liu, Xiao Xia, Xiaohan Zhang, Xiaotao Gu, Xin Lv, Xinghan Liu, Xinyi Liu, Xinyue Yang, Xixuan Song, Xunkai Zhang, Yifan An, Yifan Xu, Yilin Niu, Yuantao Yang, Yueyan Li, Yushi Bai, Yuxiao Dong, Zehan Qi, Zhaoyu Wang, Zhen Yang, Zhengxiao Du, Zhenyu Hou, Zihan Wang.
[LINK: GLM](https://huggingface.co/docs/transformers/main/model_doc/glm)
- GLPN (from KAIST) released with the paper Global-Local Path Networks for Monocular Depth Estimation with Vertical CutDepth by Doyeon Kim, Woonghyun Ga, Pyungwhan Ahn, Donggyu Joo, Sehwan Chun, Junmo Kim.
[LINK: GLPN](https://huggingface.co/docs/transformers/model_doc/glpn)
- GPT Neo (from EleutherAI) released in the repository EleutherAI/gpt-neo by Sid Black, Stella Biderman, Leo Gao, Phil Wang and Connor Leahy.
[LINK: GPT Neo](https://huggingface.co/docs/transformers/model_doc/gpt_neo)
[LINK: EleutherAI/gpt-neo](https://github.com/EleutherAI/gpt-neo)
- GPT NeoX (from EleutherAI) released with the paper GPT-NeoX-20B: An Open-Source Autoregressive Language Model by Sid Black, Stella Biderman, Eric Hallahan, Quentin Anthony, Leo Gao, Laurence Golding, Horace He, Connor Leahy, Kyle McDonell, Jason Phang, Michael Pieler, USVSN Sai Prashanth, Shivanshu Purohit, Laria Reynolds, Jonathan Tow, Ben Wang, Samuel Weinbach
[LINK: GPT NeoX](https://huggingface.co/docs/transformers/model_doc/gpt_neox)
- GPT-2 (from OpenAI) released with the paper Language Models are Unsupervised Multitask Learners by Alec Radford , Jeffrey Wu , Rewon Child, David Luan, Dario Amodei and Ilya Sutskever .
[LINK: GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2)
- GPT-J (from EleutherAI) released in the repository kingoflolz/mesh-transformer-jax by Ben Wang and Aran Komatsuzaki.
[LINK: GPT-J](https://huggingface.co/docs/transformers/model_doc/gptj)
[LINK: kingoflolz/mesh-transformer-jax](https://github.com/kingoflolz/mesh-transformer-jax/)
- GPTBigCode (from BigCode) released with the paper SantaCoder: don’t reach for the stars! by Loubna Ben Allal, Raymond Li, Denis Kocetkov, Chenghao Mou, Christopher Akiki, Carlos Munoz Ferrandis, Niklas Muennighoff, Mayank Mishra, Alex Gu, Manan Dey, Logesh Kumar Umapathi, Carolyn Jane Anderson, Yangtian Zi, Joel Lamy Poirier, Hailey Schoelkopf, Sergey Troshin, Dmitry Abulkhanov, Manuel Romero, Michael Lappert, Francesco De Toni, Bernardo García del Río, Qian Liu, Shamik Bose, Urvashi Bhattacharyya, Terry Yue Zhuo, Ian Yu, Paulo Villegas, Marco Zocca, Sourab Mangrulkar, David Lansky, Huu Nguyen, Danish Contractor, Luis Villa, Jia Li, Dzmitry Bahdanau, Yacine Jernite, Sean Hughes, Daniel Fried, Arjun Guha, Harm de Vries, Leandro von Werra.
[LINK: GPTBigCode](https://huggingface.co/docs/transformers/model_doc/gpt_bigcode)
- Granite (from IBM) released with the paper Power Scheduler: A Batch Size and Token Number Agnostic Learning Rate Scheduler by Yikang Shen, Matthew Stallone, Mayank Mishra, Gaoyuan Zhang, Shawn Tan, Aditya Prasad, Adriana Meza Soria, David D. Cox, Rameswar Panda.
[LINK: Granite](https://huggingface.co/docs/transformers/main/model_doc/granite)
- GraniteMoeHybrid (from IBM) released with the blog post IBM Granite 4.0: hyper-efficient, high performance hybrid models for enterprise by the IBM Granite team.
[LINK: GraniteMoeHybrid](https://huggingface.co/docs/transformers/main/model_doc/granitemoehybrid)
- Grounding DINO (from IDEA-Research) released with the paper Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection by Shilong Liu, Zhaoyang Zeng, Tianhe Ren, Feng Li, Hao Zhang, Jie Yang, Qing Jiang, Chunyuan Li, Jianwei Yang, Hang Su, Jun Zhu, Lei Zhang.
[LINK: Grounding DINO](https://huggingface.co/docs/transformers/model_doc/grounding-dino)
- GroupViT (from UCSD, NVIDIA) released with the paper GroupViT: Semantic Segmentation Emerges from Text Supervision by Jiarui Xu, Shalini De Mello, Sifei Liu, Wonmin Byeon, Thomas Breuel, Jan Kautz, Xiaolong Wang.
[LINK: GroupViT](https://huggingface.co/docs/transformers/model_doc/groupvit)
- Helium (from the Kyutai Team) released with the blog post Announcing Helium-1 Preview by the Kyutai Team.
[LINK: Helium](https://huggingface.co/docs/transformers/main/model_doc/helium)
- HerBERT (from Allegro.pl, AGH University of Science and Technology) released with the paper KLEJ: Comprehensive Benchmark for Polish Language Understanding by Piotr Rybak, Robert Mroczkowski, Janusz Tracz, Ireneusz Gawlik.
[LINK: HerBERT](https://huggingface.co/docs/transformers/model_doc/herbert)
- Hiera (from Meta) released with the paper Hiera: A Hierarchical Vision Transformer without the Bells-and-Whistles by Chaitanya Ryali, Yuan-Ting Hu, Daniel Bolya, Chen Wei, Haoqi Fan, Po-Yao Huang, Vaibhav Aggarwal, Arkabandhu Chowdhury, Omid Poursaeed, Judy Hoffman, Jitendra Malik, Yanghao Li, Christoph Feichtenhofer.
[LINK: Hiera](https://huggingface.co/docs/transformers/model_doc/hiera)
- Hubert (from Facebook) released with the paper HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units by Wei-Ning Hsu, Benjamin Bolte, Yao-Hung Hubert Tsai, Kushal Lakhotia, Ruslan Salakhutdinov, Abdelrahman Mohamed.
[LINK: Hubert](https://huggingface.co/docs/transformers/model_doc/hubert)
- I-JEPA (from Meta) released with the paper Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture by Mahmoud Assran, Quentin Duval, Ishan Misra, Piotr Bojanowski, Pascal Vincent, Michael Rabbat, Yann LeCun, Nicolas Ballas.
[LINK: I-JEPA](https://huggingface.co/docs/transformers/model_doc/ijepa)
- Idefics3 (from Hugging Face) released with the paper Building and better understanding vision-language models: insights and future directions by Hugo Laurençon, Andrés Marafioti, Victor Sanh, Léo Tronchon.
[LINK: Idefics3](https://huggingface.co/docs/transformers/model_doc/idefics3)
- JAIS (from Core42) released with the paper Jais and Jais-chat: Arabic-Centric Foundation and Instruction-Tuned Open Generative Large Language Models by Neha Sengupta, Sunil Kumar Sahu, Bokang Jia, Satheesh Katipomu, Haonan Li, Fajri Koto, William Marshall, Gurpreet Gosal, Cynthia Liu, Zhiming Chen, Osama Mohammed Afzal, Samta Kamboj, Onkar Pandit, Rahul Pal, Lalit Pradhan, Zain Muhammad Mujahid, Massa Baali, Xudong Han, Sondos Mahmoud Bsharat, Alham Fikri Aji, Zhiqiang Shen, Zhengzhong Liu, Natalia Vassilieva, Joel Hestness, Andy Hock, Andrew Feldman, Jonathan Lee, Andrew Jackson, Hector Xuguang Ren, Preslav Nakov, Timothy Baldwin, Eric Xing.
- Janus (from DeepSeek) released with the paper Janus: Decoupling Visual Encoding for Unified Multimodal Understanding and Generation Chengyue Wu, Xiaokang Chen, Zhiyu Wu, Yiyang Ma, Xingchao Liu, Zizheng Pan, Wen Liu, Zhenda Xie, Xingkai Yu, Chong Ruan, Ping Luo.
- JinaCLIP (from Jina AI) released with the paper Jina CLIP: Your CLIP Model Is Also Your Text Retriever by Andreas Koukounas, Georgios Mastrapas, Michael Günther, Bo Wang, Scott Martens, Isabelle Mohr, Saba Sturua, Mohammad Kalim Akram, Joan Fontanals Martínez, Saahil Ognawala, Susana Guzman, Maximilian Werk, Nan Wang, Han Xiao.
- LiteWhisper (from University of Washington, Kotoba Technologies) released with the paper LiteASR: Efficient Automatic Speech Recognition with Low-Rank Approximation by Keisuke Kamahori, Jungo Kasai, Noriyuki Kojima, Baris Kasikci.
- LongT5 (from Google AI) released with the paper LongT5: Efficient Text-To-Text Transformer for Long Sequences by Mandy Guo, Joshua Ainslie, David Uthus, Santiago Ontanon, Jianmo Ni, Yun-Hsuan Sung, Yinfei Yang.
[LINK: LongT5](https://huggingface.co/docs/transformers/model_doc/longt5)
- LFM2 (from Liquid AI) released with the blog post Introducing LFM2: The Fastest On-Device Foundation Models on the Market by the Liquid AI Team.
[LINK: LFM2](https://huggingface.co/docs/transformers/model_doc/lfm2)
- LLaMA (from The FAIR team of Meta AI) released with the paper LLaMA: Open and Efficient Foundation Language Models by Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, Guillaume Lample.
[LINK: LLaMA](https://huggingface.co/docs/transformers/model_doc/llama)
- Llama2 (from The FAIR team of Meta AI) released with the paper Llama2: Open Foundation and Fine-Tuned Chat Models by Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal, Anthony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushka rMishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiaoqing EllenTan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert Stojnic, Sergey Edunov, Thomas Scialom.
[LINK: Llama2](https://huggingface.co/docs/transformers/model_doc/llama2)
- Llama3 (from The FAIR team of Meta AI) released with the paper The Llama 3 Herd of Models by the Llama Team at Meta.
[LINK: Llama3](https://huggingface.co/docs/transformers/model_doc/llama3)
- Llama4 (from The FAIR team of Meta AI) released with the blog post The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation by the Llama Team at Meta.
[LINK: Llama4](https://huggingface.co/docs/transformers/model_doc/llama4)
- LLaVa (from Microsoft Research & University of Wisconsin-Madison) released with the paper Visual Instruction Tuning by Haotian Liu, Chunyuan Li, Yuheng Li and Yong Jae Lee.
[LINK: LLaVa](https://huggingface.co/docs/transformers/model_doc/llava)
- LLaVA-OneVision (from ByteDance & NTU & CUHK & HKUST) released with the paper LLaVA-OneVision: Easy Visual Task Transfer by Bo Li, Yuanhan Zhang, Dong Guo, Renrui Zhang, Feng Li, Hao Zhang, Kaichen Zhang, Yanwei Li, Ziwei Liu, Chunyuan Li
[LINK: LLaVA-OneVision](https://huggingface.co/docs/transformers/model_doc/llava_onevision)
- M2M100 (from Facebook) released with the paper Beyond English-Centric Multilingual Machine Translation by Angela Fan, Shruti Bhosale, Holger Schwenk, Zhiyi Ma, Ahmed El-Kishky, Siddharth Goyal, Mandeep Baines, Onur Celebi, Guillaume Wenzek, Vishrav Chaudhary, Naman Goyal, Tom Birch, Vitaliy Liptchinsky, Sergey Edunov, Edouard Grave, Michael Auli, Armand Joulin.
[LINK: M2M100](https://huggingface.co/docs/transformers/model_doc/m2m_100)
- MarianMT Machine translation models trained using OPUS data by Jörg Tiedemann. The Marian Framework is being developed by the Microsoft Translator Team.
[LINK: MarianMT](https://huggingface.co/docs/transformers/model_doc/marian)
[LINK: Marian Framework](https://marian-nmt.github.io/)
- MaskFormer (from Meta and UIUC) released with the paper Per-Pixel Classification is Not All You Need for Semantic Segmentation by Bowen Cheng, Alexander G. Schwing, Alexander Kirillov.
[LINK: MaskFormer](https://huggingface.co/docs/transformers/model_doc/maskformer)
- mBART (from Facebook) released with the paper Multilingual Denoising Pre-training for Neural Machine Translation by Yinhan Liu, Jiatao Gu, Naman Goyal, Xian Li, Sergey Edunov, Marjan Ghazvininejad, Mike Lewis, Luke Zettlemoyer.
[LINK: mBART](https://huggingface.co/docs/transformers/model_doc/mbart)
- mBART-50 (from Facebook) released with the paper Multilingual Translation with Extensible Multilingual Pretraining and Finetuning by Yuqing Tang, Chau Tran, Xian Li, Peng-Jen Chen, Naman Goyal, Vishrav Chaudhary, Jiatao Gu, Angela Fan.
[LINK: mBART-50](https://huggingface.co/docs/transformers/model_doc/mbart)
- Metric3D released with the paper Metric3D: Towards Zero-shot Metric 3D Prediction from A Single Image by Wei Yin, Chi Zhang, Hao Chen, Zhipeng Cai, Gang Yu, Kaixuan Wang, Xiaozhi Chen, Chunhua Shen.
- Metric3Dv2 released with the paper Metric3Dv2: A Versatile Monocular Geometric Foundation Model for Zero-shot Metric Depth and Surface Normal Estimation by Mu Hu, Wei Yin, Chi Zhang, Zhipeng Cai, Xiaoxiao Long, Kaixuan Wang, Hao Chen, Gang Yu, Chunhua Shen, Shaojie Shen.
- MusicGen (from Meta) released with the paper Simple and Controllable Music Generation by Jade Copet, Felix Kreuk, Itai Gat, Tal Remez, David Kant, Gabriel Synnaeve, Yossi Adi and Alexandre Défossez.
[LINK: MusicGen](https://huggingface.co/docs/transformers/model_doc/musicgen)
- MGP-STR (from Alibaba Research) released with the paper Multi-Granularity Prediction for Scene Text Recognition by Peng Wang, Cheng Da, and Cong Yao.
[LINK: MGP-STR](https://huggingface.co/docs/transformers/model_doc/mgp-str)
- Mimi (from Kyutai) released with the paper Moshi: a speech-text foundation model for real-time dialogue by Alexandre Défossez, Laurent Mazaré, Manu Orsini, Amélie Royer, Patrick Pérez, Hervé Jégou, Edouard Grave and Neil Zeghidour.
[LINK: Mimi](https://huggingface.co/docs/transformers/model_doc/mimi)
- Ministral (from Mistral AI) by The Mistral AI team.
[LINK: Ministral](https://huggingface.co/docs/transformers/model_doc/ministral)
- Ministral3 (from Mistral AI) by The Mistral AI team.
[LINK: Ministral3](https://huggingface.co/docs/transformers/model_doc/ministral3)
- Mistral (from Mistral AI) by The Mistral AI team: Albert Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lélio Renard Lavaud, Lucile Saulnier, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothée Lacroix, William El Sayed.
[LINK: Mistral](https://huggingface.co/docs/transformers/model_doc/mistral)
- Mistral3 (from Mistral AI) by The Mistral AI team.
[LINK: Mistral3](https://huggingface.co/docs/transformers/model_doc/mistral3)
- MMS (from Facebook) released with the paper Scaling Speech Technology to 1,000+ Languages by Vineel Pratap, Andros Tjandra, Bowen Shi, Paden Tomasello, Arun Babu, Sayani Kundu, Ali Elkahky, Zhaoheng Ni, Apoorv Vyas, Maryam Fazel-Zarandi, Alexei Baevski, Yossi Adi, Xiaohui Zhang, Wei-Ning Hsu, Alexis Conneau, Michael Auli.
[LINK: MMS](https://huggingface.co/docs/transformers/model_doc/mms)
- MobileBERT (from CMU/Google Brain) released with the paper MobileBERT: a Compact Task-Agnostic BERT for Resource-Limited Devices by Zhiqing Sun, Hongkun Yu, Xiaodan Song, Renjie Liu, Yiming Yang, and Denny Zhou.
[LINK: MobileBERT](https://huggingface.co/docs/transformers/model_doc/mobilebert)
- MobileCLIP (from Apple) released with the paper MobileCLIP: Fast Image-Text Models through Multi-Modal Reinforced Training by Pavan Kumar Anasosalu Vasu, Hadi Pouransari, Fartash Faghri, Raviteja Vemulapalli, Oncel Tuzel.
- MobileLLM (from Meta) released with the paper MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Use Cases by Zechun Liu, Changsheng Zhao, Forrest Iandola, Chen Lai, Yuandong Tian, Igor Fedorov, Yunyang Xiong, Ernie Chang, Yangyang Shi, Raghuraman Krishnamoorthi, Liangzhen Lai, Vikas Chandra.
- MobileNetV1 (from Google Inc.) released with the paper MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications by Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang, Tobias Weyand, Marco Andreetto, Hartwig Adam.
[LINK: MobileNetV1](https://huggingface.co/docs/transformers/model_doc/mobilenet_v1)
- MobileNetV2 (from Google Inc.) released with the paper MobileNetV2: Inverted Residuals and Linear Bottlenecks by Mark Sandler, Andrew Howard, Menglong Zhu, Andrey Zhmoginov, Liang-Chieh Chen.
[LINK: MobileNetV2](https://huggingface.co/docs/transformers/model_doc/mobilenet_v2)
- MobileNetV3 (from Google Inc.) released with the paper Searching for MobileNetV3 by Andrew Howard, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang, Yukun Zhu, Ruoming Pang, Vijay Vasudevan, Quoc V. Le, Hartwig Adam.
- MobileNetV4 (from Google Inc.) released with the paper MobileNetV4 - Universal Models for the Mobile Ecosystem by Danfeng Qin, Chas Leichner, Manolis Delakis, Marco Fornoni, Shixin Luo, Fan Yang, Weijun Wang, Colby Banbury, Chengxi Ye, Berkin Akin, Vaibhav Aggarwal, Tenghui Zhu, Daniele Moro, Andrew Howard.
- MobileViT (from Apple) released with the paper MobileViT: Light-weight, General-purpose, and Mobile-friendly Vision Transformer by Sachin Mehta and Mohammad Rastegari.
[LINK: MobileViT](https://huggingface.co/docs/transformers/model_doc/mobilevit)
- MobileViTV2 (from Apple) released with the paper Separable Self-attention for Mobile Vision Transformers by Sachin Mehta and Mohammad Rastegari.
[LINK: MobileViTV2](https://huggingface.co/docs/transformers/model_doc/mobilevitv2)
- ModernBERT (from Answer.AI and LightOn) released with the paper Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference by Benjamin Warner, Antoine Chaffin, Benjamin Clavié, Orion Weller, Oskar Hallström, Said Taghadouini, Alexis Gallagher, Raja Biswas, Faisal Ladhak, Tom Aarsen, Nathan Cooper, Griffin Adams, Jeremy Howard, Iacopo Poli.
[LINK: ModernBERT](https://huggingface.co/docs/transformers/model_doc/modernbert)
- ModernBERT Decoder (from Johns Hopkins University and LightOn) released with the paper Seq vs Seq: An Open Suite of Paired Encoders and Decoders by Orion Weller, Kathryn Ricci, Marc Marone, Antoine Chaffin, Dawn Lawrie, Benjamin Van Durme.
[LINK: ModernBERT Decoder](https://huggingface.co/docs/transformers/model_doc/modernbert-decoder)
- Moondream1 released in the repository moondream by vikhyat.
[LINK: moondream](https://github.com/vikhyat/moondream)
- Moonshine (from Useful Sensors) released with the paper Moonshine: Speech Recognition for Live Transcription and Voice Commands by Nat Jeffries, Evan King, Manjunath Kudlur, Guy Nicholson, James Wang, Pete Warden.
[LINK: Moonshine](https://huggingface.co/docs/transformers/model_doc/moonshine)
- MPNet (from Microsoft Research) released with the paper MPNet: Masked and Permuted Pre-training for Language Understanding by Kaitao Song, Xu Tan, Tao Qin, Jianfeng Lu, Tie-Yan Liu.
[LINK: MPNet](https://huggingface.co/docs/transformers/model_doc/mpnet)
- MPT (from MosaicML) released with the repository llm-foundry by the MosaicML NLP Team.
[LINK: MPT](https://huggingface.co/docs/transformers/model_doc/mpt)
[LINK: llm-foundry](https://github.com/mosaicml/llm-foundry/)
- MT5 (from Google AI) released with the paper mT5: A massively multilingual pre-trained text-to-text transformer by Linting Xue, Noah Constant, Adam Roberts, Mihir Kale, Rami Al-Rfou, Aditya Siddhant, Aditya Barua, Colin Raffel.
[LINK: MT5](https://huggingface.co/docs/transformers/model_doc/mt5)
- NanoChat released with the repository nanochat: The best ChatGPT that $100 can buy by Andrej Karpathy.
[LINK: NanoChat](https://huggingface.co/docs/transformers/model_doc/nanochat)
[LINK: nanochat: The best ChatGPT that $100 can buy](https://github.com/karpathy/nanochat)
- NeoBERT (from Chandar Research Lab) released with the paper NeoBERT: A Next-Generation BERT by Lola Le Breton, Quentin Fournier, Mariam El Mezouar, John X. Morris, Sarath Chandar.
- NLLB (from Meta) released with the paper No Language Left Behind: Scaling Human-Centered Machine Translation by the NLLB team.
[LINK: NLLB](https://huggingface.co/docs/transformers/model_doc/nllb)
- Nougat (from Meta AI) released with the paper Nougat: Neural Optical Understanding for Academic Documents by Lukas Blecher, Guillem Cucurull, Thomas Scialom, Robert Stojnic.
[LINK: Nougat](https://huggingface.co/docs/transformers/model_doc/nougat)
- OLMo (from Ai2) released with the paper OLMo: Accelerating the Science of Language Models by Dirk Groeneveld, Iz Beltagy, Pete Walsh, Akshita Bhagia, Rodney Kinney, Oyvind Tafjord, Ananya Harsh Jha, Hamish Ivison, Ian Magnusson, Yizhong Wang, Shane Arora, David Atkinson, Russell Authur, Khyathi Raghavi Chandu, Arman Cohan, Jennifer Dumas, Yanai Elazar, Yuling Gu, Jack Hessel, Tushar Khot, William Merrill, Jacob Morrison, Niklas Muennighoff, Aakanksha Naik, Crystal Nam, Matthew E. Peters, Valentina Pyatkin, Abhilasha Ravichander, Dustin Schwenk, Saurabh Shah, Will Smith, Emma Strubell, Nishant Subramani, Mitchell Wortsman, Pradeep Dasigi, Nathan Lambert, Kyle Richardson, Luke Zettlemoyer, Jesse Dodge, Kyle Lo, Luca Soldaini, Noah A. Smith, Hannaneh Hajishirzi.
[LINK: OLMo](https://huggingface.co/docs/transformers/master/model_doc/olmo)
- OLMo2 (from Ai2) released with the blog OLMo 2: The best fully open language model to date by the Ai2 OLMo team.
[LINK: OLMo2](https://huggingface.co/docs/transformers/master/model_doc/olmo2)
- OpenELM (from Apple) released with the paper OpenELM: An Efficient Language Model Family with Open-source Training and Inference Framework by Sachin Mehta, Mohammad Hossein Sekhavat, Qingqing Cao, Maxwell Horton, Yanzi Jin, Chenfan Sun, Iman Mirzadeh, Mahyar Najibi, Dmitry Belenko, Peter Zatloukal, Mohammad Rastegari.
- OPT (from Meta AI) released with the paper OPT: Open Pre-trained Transformer Language Models by Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen et al.
[LINK: OPT](https://huggingface.co/docs/transformers/master/model_doc/opt)
- OWL-ViT (from Google AI) released with the paper Simple Open-Vocabulary Object Detection with Vision Transformers by Matthias Minderer, Alexey Gritsenko, Austin Stone, Maxim Neumann, Dirk Weissenborn, Alexey Dosovitskiy, Aravindh Mahendran, Anurag Arnab, Mostafa Dehghani, Zhuoran Shen, Xiao Wang, Xiaohua Zhai, Thomas Kipf, and Neil Houlsby.
[LINK: OWL-ViT](https://huggingface.co/docs/transformers/model_doc/owlvit)
- OWLv2 (from Google AI) released with the paper Scaling Open-Vocabulary Object Detection by Matthias Minderer, Alexey Gritsenko, Neil Houlsby.
[LINK: OWLv2](https://huggingface.co/docs/transformers/model_doc/owlv2)
- PaliGemma (from Google) released with the papers PaliGemma: A versatile 3B VLM for transfer and PaliGemma 2: A Family of Versatile VLMs for Transfer by the PaliGemma Google team.
[LINK: PaliGemma](https://huggingface.co/docs/transformers/main/model_doc/paligemma)
- Parakeet (from NVIDIA) released with the blog post Introducing the Parakeet ASR family by the NVIDIA NeMo team.
[LINK: Parakeet](https://huggingface.co/docs/transformers/main/model_doc/parakeet)
[LINK: Introducing the Parakeet ASR family](https://developer.nvidia.com/blog/pushing-the-boundaries-of-speech-recognition-with-nemo-parakeet-asr-models/)
- PatchTSMixer (from IBM) released with the paper TSMixer: Lightweight MLP-Mixer Model for Multivariate Time Series Forecasting by Vijay Ekambaram, Arindam Jati, Nam Nguyen, Phanwadee Sinthong, Jayant Kalagnanam.
[LINK: PatchTSMixer](https://huggingface.co/docs/transformers/main/model_doc/patchtsmixer)
- PatchTST (from Princeton University, IBM) released with the paper A Time Series is Worth 64 Words: Long-term Forecasting with Transformers by Yuqi Nie, Nam H. Nguyen, Phanwadee Sinthong, Jayant Kalagnanam.
[LINK: PatchTST](https://huggingface.co/docs/transformers/main/model_doc/patchtst)
- Phi (from Microsoft) released with the papers - Textbooks Are All You Need by Suriya Gunasekar, Yi Zhang, Jyoti Aneja, Caio César Teodoro Mendes, Allie Del Giorno, Sivakanth Gopi, Mojan Javaheripi, Piero Kauffmann, Gustavo de Rosa, Olli Saarikivi, Adil Salim, Shital Shah, Harkirat Singh Behl, Xin Wang, Sébastien Bubeck, Ronen Eldan, Adam Tauman Kalai, Yin Tat Lee and Yuanzhi Li, Textbooks Are All You Need II: phi-1.5 technical report by Yuanzhi Li, Sébastien Bubeck, Ronen Eldan, Allie Del Giorno, Suriya Gunasekar and Yin Tat Lee.
[LINK: Phi](https://huggingface.co/docs/transformers/main/model_doc/phi)
- Phi3 (from Microsoft) released with the paper Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone by Marah Abdin, Sam Ade Jacobs, Ammar Ahmad Awan, Jyoti Aneja, Ahmed Awadallah, Hany Awadalla, Nguyen Bach, Amit Bahree, Arash Bakhtiari, Harkirat Behl, Alon Benhaim, Misha Bilenko, Johan Bjorck, Sébastien Bubeck, Martin Cai, Caio César Teodoro Mendes, Weizhu Chen, Vishrav Chaudhary, Parul Chopra, Allie Del Giorno, Gustavo de Rosa, Matthew Dixon, Ronen Eldan, Dan Iter, Amit Garg, Abhishek Goswami, Suriya Gunasekar, Emman Haider, Junheng Hao, Russell J. Hewett, Jamie Huynh, Mojan Javaheripi, Xin Jin, Piero Kauffmann, Nikos Karampatziakis, Dongwoo Kim, Mahoud Khademi, Lev Kurilenko, James R. Lee, Yin Tat Lee, Yuanzhi Li, Chen Liang, Weishung Liu, Eric Lin, Zeqi Lin, Piyush Madan, Arindam Mitra, Hardik Modi, Anh Nguyen, Brandon Norick, Barun Patra, Daniel Perez-Becker, Thomas Portet, Reid Pryzant, Heyang Qin, Marko Radmilac, Corby Rosset, Sambudha Roy, Olatunji Ruwase, Olli Saarikivi, Amin Saied, Adil Salim, Michael Santacroce, Shital Shah, Ning Shang, Hiteshi Sharma, Xia Song, Masahiro Tanaka, Xin Wang, Rachel Ward, Guanhua Wang, Philipp Witte, Michael Wyatt, Can Xu, Jiahang Xu, Sonali Yadav, Fan Yang, Ziyi Yang, Donghan Yu, Chengruidong Zhang, Cyril Zhang, Jianwen Zhang, Li Lyna Zhang, Yi Zhang, Yue Zhang, Yunan Zhang, Xiren Zhou.
[LINK: Phi3](https://huggingface.co/docs/transformers/main/model_doc/phi3)
- Phi3V (from Microsoft) released with the paper Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone by Marah Abdin, Jyoti Aneja, Hany Awadalla, Ahmed Awadallah, Ammar Ahmad Awan, Nguyen Bach, Amit Bahree, Arash Bakhtiari, Jianmin Bao, Harkirat Behl, Alon Benhaim, Misha Bilenko, Johan Bjorck, Sébastien Bubeck, Martin Cai, Qin Cai, Vishrav Chaudhary, Dong Chen, Dongdong Chen, Weizhu Chen, Yen-Chun Chen, Yi-Ling Chen, Hao Cheng, Parul Chopra, Xiyang Dai, Matthew Dixon, Ronen Eldan, Victor Fragoso, Jianfeng Gao, Mei Gao, Min Gao, Amit Garg, Allie Del Giorno, Abhishek Goswami, Suriya Gunasekar, Emman Haider, Junheng Hao, Russell J. Hewett, Wenxiang Hu, Jamie Huynh, Dan Iter, Sam Ade Jacobs, Mojan Javaheripi, Xin Jin, Nikos Karampatziakis, Piero Kauffmann, Mahoud Khademi, Dongwoo Kim, Young Jin Kim, Lev Kurilenko, James R. Lee, Yin Tat Lee, Yuanzhi Li, Yunsheng Li, Chen Liang, Lars Liden, Xihui Lin, Zeqi Lin, Ce Liu, Liyuan Liu, Mengchen Liu, Weishung Liu, Xiaodong Liu, Chong Luo, Piyush Madan, Ali Mahmoudzadeh, David Majercak, Matt Mazzola, Caio César Teodoro Mendes, Arindam Mitra, Hardik Modi, Anh Nguyen, Brandon Norick, Barun Patra, Daniel Perez-Becker, Thomas Portet, Reid Pryzant, Heyang Qin, Marko Radmilac, Liliang Ren, Gustavo de Rosa, Corby Rosset, Sambudha Roy, Olatunji Ruwase, Olli Saarikivi, Amin Saied, Adil Salim, Michael Santacroce, Shital Shah, Ning Shang, Hiteshi Sharma, Yelong Shen, Swadheen Shukla, Xia Song, Masahiro Tanaka, Andrea Tupini, Praneetha Vaddamanu, Chunyu Wang, Guanhua Wang, Lijuan Wang , Shuohang Wang, Xin Wang, Yu Wang, Rachel Ward, Wen Wen, Philipp Witte, Haiping Wu, Xiaoxia Wu, Michael Wyatt, Bin Xiao, Can Xu, Jiahang Xu, Weijian Xu, Jilong Xue, Sonali Yadav, Fan Yang, Jianwei Yang, Yifan Yang, Ziyi Yang, Donghan Yu, Lu Yuan, Chenruidong Zhang, Cyril Zhang, Jianwen Zhang, Li Lyna Zhang, Yi Zhang, Yue Zhang, Yunan Zhang, Xiren Zhou.
- PVT (from Nanjing University, The University of Hong Kong etc.) released with the paper Pyramid Vision Transformer: A Versatile Backbone for Dense Prediction without Convolutions by Wenhai Wang, Enze Xie, Xiang Li, Deng-Ping Fan, Kaitao Song, Ding Liang, Tong Lu, Ping Luo, Ling Shao.
[LINK: PVT](https://huggingface.co/docs/transformers/main/model_doc/pvt)
- PyAnnote released in the repository pyannote/pyannote-audio by Hervé Bredin.
[LINK: pyannote/pyannote-audio](https://github.com/pyannote/pyannote-audio)
- Qwen2 (from the Qwen team, Alibaba Group) released with the paper Qwen Technical Report by Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu, Keming Lu, Jianxin Ma, Rui Men, Xingzhang Ren, Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng Wang, Shijie Wang, Wei Wang, Shengguang Wu, Benfeng Xu, Jin Xu, An Yang, Hao Yang, Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu, Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xingxuan Zhang, Yichang Zhang, Zhenru Zhang, Chang Zhou, Jingren Zhou, Xiaohuan Zhou and Tianhang Zhu.
[LINK: Qwen2](https://huggingface.co/docs/transformers/model_doc/qwen2)
- Qwen2-VL (from the Qwen team, Alibaba Group) released with the paper Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond by Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou, Jingren Zhou.
[LINK: Qwen2-VL](https://huggingface.co/docs/transformers/model_doc/qwen2_vl)
- Qwen3 (from the Qwen team, Alibaba Group) released with the blog post Qwen3: Think Deeper, Act Faster by the Qwen team.
[LINK: Qwen3](https://huggingface.co/docs/transformers/en/model_doc/qwen3)
[LINK: Qwen3: Think Deeper, Act Faster](https://qwenlm.github.io/blog/qwen3/)
- ResNet (from Microsoft Research) released with the paper Deep Residual Learning for Image Recognition by Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun.
[LINK: ResNet](https://huggingface.co/docs/transformers/model_doc/resnet)
- RF-DETR (from Roboflow) released with the blog post RF-DETR: A SOTA Real-Time Object Detection Model by Peter Robicheaux, James Gallagher, Joseph Nelson, Isaac Robinson.
[LINK: RF-DETR](https://huggingface.co/docs/transformers/model_doc/rf_detr)
- RoBERTa (from Facebook), released together with the paper RoBERTa: A Robustly Optimized BERT Pretraining Approach by Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, Veselin Stoyanov.
[LINK: RoBERTa](https://huggingface.co/docs/transformers/model_doc/roberta)
- RoFormer (from ZhuiyiTechnology), released together with the paper RoFormer: Enhanced Transformer with Rotary Position Embedding by Jianlin Su and Yu Lu and Shengfeng Pan and Bo Wen and Yunfeng Liu.
[LINK: RoFormer](https://huggingface.co/docs/transformers/model_doc/roformer)
- RT-DETR (from Baidu), released together with the paper DETRs Beat YOLOs on Real-time Object Detection by Yian Zhao, Wenyu Lv, Shangliang Xu, Jinman Wei, Guanzhong Wang, Qingqing Dang, Yi Liu, Jie Chen.
[LINK: RT-DETR](https://huggingface.co/docs/transformers/model_doc/rt_detr)
- RT-DETRv2 (from Baidu), released together with the paper RT-DETRv2: Improved Baseline with Bag-of-Freebies for Real-Time Detection Transformer by Wenyu Lv, Yian Zhao, Qinyao Chang, Kui Huang, Guanzhong Wang, Yi Liu.
[LINK: RT-DETRv2](https://huggingface.co/docs/transformers/model_doc/rt_detr_v2)
- Sapiens (from Meta AI) released with the paper Sapiens: Foundation for Human Vision Models by Rawal Khirodkar, Timur Bagautdinov, Julieta Martinez, Su Zhaoen, Austin James, Peter Selednik, Stuart Anderson, Shunsuke Saito.
- SegFormer (from NVIDIA) released with the paper SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers by Enze Xie, Wenhai Wang, Zhiding Yu, Anima Anandkumar, Jose M. Alvarez, Ping Luo.
[LINK: SegFormer](https://huggingface.co/docs/transformers/model_doc/segformer)
- Segment Anything (from Meta AI) released with the paper Segment Anything by Alexander Kirillov, Eric Mintun, Nikhila Ravi, Hanzi Mao, Chloe Rolland, Laura Gustafson, Tete Xiao, Spencer Whitehead, Alex Berg, Wan-Yen Lo, Piotr Dollar, Ross Girshick.
[LINK: Segment Anything](https://huggingface.co/docs/transformers/model_doc/sam)
- Segment Anything 2 (from Meta AI) released with the paper SAM 2: Segment Anything in Images and Videos by Nikhila Ravi, Valentin Gabeur, Yuan-Ting Hu, Ronghang Hu, Chaitanya Ryali, Tengyu Ma, Haitham Khedr, Roman Rädle, Chloe Rolland, Laura Gustafson, Eric Mintun, Junting Pan, Kalyan Vasudev Alwala, Nicolas Carion, Chao-Yuan Wu, Ross Girshick, Piotr Dollár, Christoph Feichtenhofer.
[LINK: Segment Anything 2](https://huggingface.co/docs/transformers/model_doc/sam2)
- Segment Anything 3 (from Meta Superintelligence Labs) released with the paper SAM 3: Segment Anything with Concepts by SAM 3D Team, Xingyu Chen, Fu-Jen Chu, Pierre Gleize, Kevin J Liang, Alexander Sax, Hao Tang, Weiyao Wang, Michelle Guo, Thibaut Hardin, Xiang Li, Aohan Lin, Jiawei Liu, Ziqi Ma, Anushka Sagar, Bowen Song, Xiaodong Wang, Jianing Yang, Bowen Zhang, Piotr Dollar, Georgia Gkioxari, Matt Feiszli, Jitendra Malik, Nicolas Carion, Laura Gustafson, Yuan-Ting Hu, Shoubhik Debnath, Ronghang Hu, Didac Suris Coll-Vinent, Chaitanya Ryali, Kalyan Vasudev Alwala, Haitham Khedr, Andrew Huang, Jie Lei, Tengyu Ma, Baishan Guo, Arpit Kalla, Markus Marks, Joseph Greer, Meng Wang, Peize Sun, Roman Rädle, Triantafyllos Afouras, Effrosyni Mavroudi, Katherine Xu, Tsung-Han Wu, Yu Zhou, Liliane Momeni, Rishi Hazra, Shuangrui Ding, Sagar Vaze, Francois Porcher, Feng Li, Siyuan Li, Aishwarya Kamath, Ho Kei Cheng, Piotr Dollar, Nikhila Ravi, Kate Saenko, Pengchuan Zhang, Christoph Feichtenhofer.
[LINK: Segment Anything 3](https://huggingface.co/docs/transformers/model_doc/sam3)
- SigLIP (from Google AI) released with the paper Sigmoid Loss for Language Image Pre-Training by Xiaohua Zhai, Basil Mustafa, Alexander Kolesnikov, Lucas Beyer.
[LINK: SigLIP](https://huggingface.co/docs/transformers/main/model_doc/siglip)
- ** SmolLM3 (from Hugging Face) released with the blog post SmolLM3: smol, multilingual, long-context reasoner by the Hugging Face TB Research team.
[LINK: SmolLM3](https://huggingface.co/docs/transformers/main/model_doc/smollm3)
- ** SmolVLM (from Hugging Face) released with the blog posts SmolVLM - small yet mighty Vision Language Model and SmolVLM Grows Smaller – Introducing the 250M & 500M Models! by the Hugging Face TB Research team.
[LINK: SmolVLM](https://huggingface.co/docs/transformers/main/model_doc/smolvlm)
- SNAC (from Papla Media, ETH Zurich) released with the paper SNAC: Multi-Scale Neural Audio Codec by Hubert Siuzdak, Florian Grötschla, Luca A. Lanzendörfer.
- SpeechT5 (from Microsoft Research) released with the paper SpeechT5: Unified-Modal Encoder-Decoder Pre-Training for Spoken Language Processing by Junyi Ao, Rui Wang, Long Zhou, Chengyi Wang, Shuo Ren, Yu Wu, Shujie Liu, Tom Ko, Qing Li, Yu Zhang, Zhihua Wei, Yao Qian, Jinyu Li, Furu Wei.
[LINK: SpeechT5](https://huggingface.co/docs/transformers/model_doc/speecht5)
- SqueezeBERT (from Berkeley) released with the paper SqueezeBERT: What can computer vision teach NLP about efficient neural networks? by Forrest N. Iandola, Albert E. Shaw, Ravi Krishna, and Kurt W. Keutzer.
[LINK: SqueezeBERT](https://huggingface.co/docs/transformers/model_doc/squeezebert)
- StableLm (from Stability AI) released with the paper StableLM 3B 4E1T (Technical Report) by Jonathan Tow, Marco Bellagente, Dakota Mahan, Carlos Riquelme Ruiz, Duy Phung, Maksym Zhuravinskyi, Nathan Cooper, Nikhil Pinnaparaju, Reshinth Adithyan, and James Baicoianu.
[LINK: StableLm](https://huggingface.co/docs/transformers/model_doc/stablelm)
- Starcoder2 (from BigCode team) released with the paper StarCoder 2 and The Stack v2: The Next Generation by Anton Lozhkov, Raymond Li, Loubna Ben Allal, Federico Cassano, Joel Lamy-Poirier, Nouamane Tazi, Ao Tang, Dmytro Pykhtar, Jiawei Liu, Yuxiang Wei, Tianyang Liu, Max Tian, Denis Kocetkov, Arthur Zucker, Younes Belkada, Zijian Wang, Qian Liu, Dmitry Abulkhanov, Indraneil Paul, Zhuang Li, Wen-Ding Li, Megan Risdal, Jia Li, Jian Zhu, Terry Yue Zhuo, Evgenii Zheltonozhskii, Nii Osae Osae Dade, Wenhao Yu, Lucas Krauß, Naman Jain, Yixuan Su, Xuanli He, Manan Dey, Edoardo Abati, Yekun Chai, Niklas Muennighoff, Xiangru Tang, Muhtasham Oblokulov, Christopher Akiki, Marc Marone, Chenghao Mou, Mayank Mishra, Alex Gu, Binyuan Hui, Tri Dao, Armel Zebaze, Olivier Dehaene, Nicolas Patry, Canwen Xu, Julian McAuley, Han Hu, Torsten Scholak, Sebastien Paquet, Jennifer Robinson, Carolyn Jane Anderson, Nicolas Chapados, Mostofa Patwary, Nima Tajbakhsh, Yacine Jernite, Carlos Muñoz Ferrandis, Lingming Zhang, Sean Hughes, Thomas Wolf, Arjun Guha, Leandro von Werra, and Harm de Vries.
[LINK: Starcoder2](https://huggingface.co/docs/transformers/main/model_doc/starcoder2)
- StyleTTS 2 (from Columbia University) released with the paper StyleTTS 2: Towards Human-Level Text-to-Speech through Style Diffusion and Adversarial Training with Large Speech Language Models by Yinghao Aaron Li, Cong Han, Vinay S. Raghavan, Gavin Mischler, Nima Mesgarani.
- Supertonic (from Supertone) released with the paper SupertonicTTS: Towards Highly Efficient and Streamlined Text-to-Speech System by Hyeongju Kim, Jinhyeok Yang, Yechan Yu, Seunghun Ji, Jacob Morton, Frederik Bous, Joon Byun, Juheon Lee.
- Swin Transformer (from Microsoft) released with the paper Swin Transformer: Hierarchical Vision Transformer using Shifted Windows by Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng Zhang, Stephen Lin, Baining Guo.
[LINK: Swin Transformer](https://huggingface.co/docs/transformers/model_doc/swin)
- Swin2SR (from University of Würzburg) released with the paper Swin2SR: SwinV2 Transformer for Compressed Image Super-Resolution and Restoration by Marcos V. Conde, Ui-Jin Choi, Maxime Burchi, Radu Timofte.
[LINK: Swin2SR](https://huggingface.co/docs/transformers/model_doc/swin2sr)
- T5 (from Google AI) released with the paper Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer by Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu.
- T5v1.1 (from Google AI) released in the repository google-research/text-to-text-transfer-transformer by Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu.
[LINK: T5v1.1](https://huggingface.co/docs/transformers/model_doc/t5v1.1)
[LINK: google-research/text-to-text-transfer-transformer](https://github.com/google-research/text-to-text-transfer-transformer/blob/main/released_checkpoints.md#t511)
- Table Transformer (from Microsoft Research) released with the paper PubTables-1M: Towards Comprehensive Table Extraction From Unstructured Documents by Brandon Smock, Rohith Pesala, Robin Abraham.
[LINK: Table Transformer](https://huggingface.co/docs/transformers/model_doc/table-transformer)
- TrOCR (from Microsoft), released together with the paper TrOCR: Transformer-based Optical Character Recognition with Pre-trained Models by Minghao Li, Tengchao Lv, Lei Cui, Yijuan Lu, Dinei Florencio, Cha Zhang, Zhoujun Li, Furu Wei.
[LINK: TrOCR](https://huggingface.co/docs/transformers/model_doc/trocr)
- Ultravox (from Fixie.ai) released with the repository fixie-ai/ultravox by the Fixie.ai team.
[LINK: fixie-ai/ultravox](https://github.com/fixie-ai/ultravox)
- UniSpeech (from Microsoft Research) released with the paper UniSpeech: Unified Speech Representation Learning with Labeled and Unlabeled Data by Chengyi Wang, Yu Wu, Yao Qian, Kenichi Kumatani, Shujie Liu, Furu Wei, Michael Zeng, Xuedong Huang.
[LINK: UniSpeech](https://huggingface.co/docs/transformers/model_doc/unispeech)
- UniSpeechSat (from Microsoft Research) released with the paper UNISPEECH-SAT: UNIVERSAL SPEECH REPRESENTATION LEARNING WITH SPEAKER AWARE PRE-TRAINING by Sanyuan Chen, Yu Wu, Chengyi Wang, Zhengyang Chen, Zhuo Chen, Shujie Liu, Jian Wu, Yao Qian, Furu Wei, Jinyu Li, Xiangzhan Yu.
[LINK: UniSpeechSat](https://huggingface.co/docs/transformers/model_doc/unispeech-sat)
- VaultGemma (from Google) released with the technical report VaultGemma: A Differentially Private Gemma Model by the VaultGemma Google team.
[LINK: VaultGemma](https://huggingface.co/docs/transformers/main/model_doc/vaultgemma)
- Vision Transformer (ViT) (from Google AI) released with the paper An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale by Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby.
[LINK: Vision Transformer (ViT)](https://huggingface.co/docs/transformers/model_doc/vit)
- ViTMAE (from Meta AI) released with the paper Masked Autoencoders Are Scalable Vision Learners by Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, Ross Girshick.
[LINK: ViTMAE](https://huggingface.co/docs/transformers/model_doc/vit_mae)
- ViTMatte (from HUST-VL) released with the paper ViTMatte: Boosting Image Matting with Pretrained Plain Vision Transformers by Jingfeng Yao, Xinggang Wang, Shusheng Yang, Baoyuan Wang.
[LINK: ViTMatte](https://huggingface.co/docs/transformers/model_doc/vitmatte)
- ViTMSN (from Meta AI) released with the paper Masked Siamese Networks for Label-Efficient Learning by Mahmoud Assran, Mathilde Caron, Ishan Misra, Piotr Bojanowski, Florian Bordes, Pascal Vincent, Armand Joulin, Michael Rabbat, Nicolas Ballas.
[LINK: ViTMSN](https://huggingface.co/docs/transformers/model_doc/vit_msn)
- ViTPose (from The University of Sydney) released with the paper ViTPose: Simple Vision Transformer Baselines for Human Pose Estimation by Yufei Xu, Jing Zhang, Qiming Zhang, Dacheng Tao.
[LINK: ViTPose](https://huggingface.co/docs/transformers/model_doc/vitpose)
- VITS (from Kakao Enterprise) released with the paper Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech by Jaehyeon Kim, Jungil Kong, Juhee Son.
[LINK: VITS](https://huggingface.co/docs/transformers/model_doc/vits)
- Voxtral (from Mistral AI) released with the paper Voxtral by Alexander H. Liu, Andy Ehrenberg, Andy Lo, Clément Denoix, Corentin Barreau, Guillaume Lample, Jean-Malo Delignon, Khyathi Raghavi Chandu, Patrick von Platen, Pavankumar Reddy Muddireddy, Sanchit Gandhi, Soham Ghosh, Srijan Mishra, Thomas Foubert, Abhinav Rastogi, Adam Yang, Albert Q. Jiang, Alexandre Sablayrolles, Amélie Héliou, Amélie Martin, Anmol Agarwal, Antoine Roux, Arthur Darcet, Arthur Mensch, Baptiste Bout, Baptiste Rozière, Baudouin De Monicault, Chris Bamford, Christian Wallenwein, Christophe Renaudin, Clémence Lanfranchi, Darius Dabert, Devendra Singh Chaplot, Devon Mizelle, Diego de las Casas, Elliot Chane-Sane, Emilien Fugier, Emma Bou Hanna, Gabrielle Berrada, Gauthier Delerce, Gauthier Guinet, Georgii Novikov, Guillaume Martin, Himanshu Jaju, Jan Ludziejewski, Jason Rute, Jean-Hadrien Chabran, Jessica Chudnovsky, Joachim Studnia, Joep Barmentlo, Jonas Amar, Josselin Somerville Roberts, Julien Denize, Karan Saxena, Karmesh Yadav, Kartik Khandelwal, Kush Jain, Lélio Renard Lavaud, Léonard Blier, Lingxiao Zhao, Louis Martin, Lucile Saulnier, Luyu Gao, Marie Pellat, Mathilde Guillaumin, Mathis Felardos, Matthieu Dinot, Maxime Darrin, Maximilian Augustin, Mickaël Seznec, Neha Gupta, Nikhil Raghuraman, Olivier Duchenne, Patricia Wang, Patryk Saffer, Paul Jacob, Paul Wambergue, Paula Kurylowicz, Philomène Chagniot, Pierre Stock, Pravesh Agrawal, Rémi Delacourt, Romain Sauvestre, Roman Soletskyi, Sagar Vaze, Sandeep Subramanian, Saurabh Garg, Shashwat Dalal, Siddharth Gandhi, Sumukh Aithal, Szymon Antoniak, Teven Le Scao, Thibault Schueller, Thibaut Lavril, Thomas Robert, Thomas Wang, Timothée Lacroix, Tom Bewley, Valeriia Nemychnikova, Victor Paltz , Virgile Richard, Wen-Ding Li, William Marshall, Xuanyu Zhang, Yihan Wan, Yunhao Tang.
[LINK: Voxtral](https://huggingface.co/docs/transformers/model_doc/voxtral)
- Wav2Vec2 (from Facebook AI) released with the paper wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations by Alexei Baevski, Henry Zhou, Abdelrahman Mohamed, Michael Auli.
[LINK: Wav2Vec2](https://huggingface.co/docs/transformers/model_doc/wav2vec2)
- Wav2Vec2-BERT (from Meta AI) released with the paper Seamless: Multilingual Expressive and Streaming Speech Translation by the Seamless Communication team.
[LINK: Wav2Vec2-BERT](https://huggingface.co/docs/transformers/main/model_doc/wav2vec2-bert)
- WavLM (from Microsoft Research) released with the paper WavLM: Large-Scale Self-Supervised Pre-Training for Full Stack Speech Processing by Sanyuan Chen, Chengyi Wang, Zhengyang Chen, Yu Wu, Shujie Liu, Zhuo Chen, Jinyu Li, Naoyuki Kanda, Takuya Yoshioka, Xiong Xiao, Jian Wu, Long Zhou, Shuo Ren, Yanmin Qian, Yao Qian, Jian Wu, Michael Zeng, Furu Wei.
[LINK: WavLM](https://huggingface.co/docs/transformers/model_doc/wavlm)
- Whisper (from OpenAI) released with the paper Robust Speech Recognition via Large-Scale Weak Supervision by Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, Ilya Sutskever.
[LINK: Whisper](https://huggingface.co/docs/transformers/model_doc/whisper)
- XLM (from Facebook) released together with the paper Cross-lingual Language Model Pretraining by Guillaume Lample and Alexis Conneau.
[LINK: XLM](https://huggingface.co/docs/transformers/model_doc/xlm)
- XLM-RoBERTa (from Facebook AI), released together with the paper Unsupervised Cross-lingual Representation Learning at Scale by Alexis Conneau , Kartikay Khandelwal , Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer and Veselin Stoyanov.
[LINK: XLM-RoBERTa](https://huggingface.co/docs/transformers/model_doc/xlm-roberta)
- YOLOS (from Huazhong University of Science & Technology) released with the paper You Only Look at One Sequence: Rethinking Transformer in Vision through Object Detection by Yuxin Fang, Bencheng Liao, Xinggang Wang, Jiemin Fang, Jiyang Qi, Rui Wu, Jianwei Niu, Wenyu Liu.
[LINK: YOLOS](https://huggingface.co/docs/transformers/model_doc/yolos)
[LINK: Update on GitHub](https://github.com/huggingface/transformers.js/blob/main/docs/source/index.md)
[LINK: Installation →](/docs/transformers.js/installation)

--------------------
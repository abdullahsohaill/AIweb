# DeepSpeed
**URL:** https://www.deepspeed.ai
**Page Title:** Latest News - DeepSpeed
--------------------

- [2025/12] DeepSpeed Core API updates: PyTorch-style backward and low-precision master states
[2025/12] DeepSpeed Core API updates: PyTorch-style backward and low-precision master states
[LINK: DeepSpeed Core API updates: PyTorch-style backward and low-precision master states](https://github.com/deepspeedai/DeepSpeed/blob/master/blogs/core_api_update/README.md)
- [2025/10] SuperOffload: Unleashing the Power of Large-Scale LLM Training on Superchips
[2025/10] SuperOffload: Unleashing the Power of Large-Scale LLM Training on Superchips
- [2025/10] Study of ZenFlow and ZeRO offload performance with DeepSpeed CPU core binding
[2025/10] Study of ZenFlow and ZeRO offload performance with DeepSpeed CPU core binding
[LINK: Study of ZenFlow and ZeRO offload performance with DeepSpeed CPU core binding](https://github.com/deepspeedai/DeepSpeed/blob/master/blogs/zenflow-corebinding/README.md)
- [2025/08] ZenFlow: Stall-Free Offloading Engine for LLM Training
[2025/08] ZenFlow: Stall-Free Offloading Engine for LLM Training
- [2025/06] Arctic Long Sequence Training (ALST) with DeepSpeed: Scalable And Efficient Training For Multi-Million Token Sequences
[2025/06] Arctic Long Sequence Training (ALST) with DeepSpeed: Scalable And Efficient Training For Multi-Million Token Sequences
- [2025/04] DeepCompile: Unlocking Compiler Optimization for Distributed Training
[LINK: DeepCompile: Unlocking Compiler Optimization for Distributed Training](https://github.com/deepspeedai/DeepSpeed/blob/master/blogs/deepcompile/README.md)
- [2025/03] DeepSpeed AutoTP: Automatic Tensor Parallel Training of Hugging Face models
[LINK: DeepSpeed AutoTP: Automatic Tensor Parallel Training of Hugging Face models](https://github.com/deepspeedai/DeepSpeed/blob/master/blogs/huggingface-tp/README.md)
- [2024/12] Ulysses-Offload: Democratizing Long Context LLM Training
[LINK: Ulysses-Offload: Democratizing Long Context LLM Training](https://github.com/deepspeedai/DeepSpeed/blob/master/blogs/ulysses-offload/README.md)

## Extreme Speed and Scale for DL Training Permalink

DeepSpeed enabled the world’s most powerful language models (at the time of this writing) such as MT-530B and BLOOM . DeepSpeed offers a confluence of system innovations , that has made large scale DL training effective, and efficient, greatly improved ease of use, and redefined the DL training landscape in terms of scale that is possible. These innovations include ZeRO, 3D-Parallelism, DeepSpeed-MoE, ZeRO-Infinity, etc.

## DeepSpeed Adoption Permalink

DeepSpeed has been used to train many different large-scale models. Below is a list of several examples that we are aware of (if you’d like to include your model please submit a PR):
- Megatron-Turing NLG (530B)
- Jurassic-1 (178B)
- BLOOM (176B)
- GLM (130B)
[LINK: GLM (130B)](https://github.com/THUDM/GLM-130B)
- YaLM (100B)
[LINK: YaLM (100B)](https://github.com/yandex/YaLM-100B)
- GPT-NeoX (20B)
[LINK: GPT-NeoX (20B)](https://github.com/EleutherAI/gpt-neox)
- AlexaTM (20B)
- Turing NLG (17B
- METRO-LM (5.4B)
DeepSpeed has been integrated with several different popular open-source DL frameworks such as:
[LINK: Transformers with DeepSpeed](https://huggingface.co/docs/transformers/deepspeed)
[LINK: Accelerate with DeepSpeed](https://huggingface.co/docs/accelerate/usage_guides/deepspeed)
[LINK: Lightning with DeepSpeed](https://pytorch-lightning.readthedocs.io/en/stable/api/pytorch_lightning.strategies.DeepSpeedStrategy.html)
[LINK: MosaicML with DeepSpeed](https://docs.mosaicml.com/en/latest/trainer/using_the_trainer.html?highlight=deepspeed#deepspeed-integration)
DeepSpeed is an integral part of Microsoft’s AI at Scale initiative to enable next-generation AI capabilities at scale.

## Contributing Permalink

DeepSpeed welcomes your contributions! Please see our contributing guide for more details on formatting, testing,
etc.

## Contributor License Agreement Permalink

This project welcomes contributions and suggestions. Most contributions require you to
agree to a Developer Certificate of Origin (DCO)[https://wiki.linuxfoundation.org/dco]
stating that they agree to the terms published at https://developercertificate.org for
that particular contribution.
DCOs are per-commit, so each commit needs to be signed off.  These can be signed in
the commit by adding the -s flag.  DCO enforcement can also be signed off in the PR
itself by clicking on the DCO enforcement check.

## Code of Conduct Permalink

This project has adopted the Microsoft Open Source Code of
Conduct . For more information see the Code of Conduct FAQ or contact opencode@microsoft.com with any additional questions or
comments.

## Publications Permalink

- Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase, Yuxiong He. (2019) ZeRO: memory optimizations toward training trillion parameter models. arXiv:1910.02054 and In Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis (SC ‘20) .
- Jeff Rasley, Samyam Rajbhandari, Olatunji Ruwase, and Yuxiong He. (2020) DeepSpeed: System Optimizations Enable Training Deep Learning Models with Over 100 Billion Parameters. In Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (KDD ‘20, Tutorial) .
- Minjia Zhang, Yuxiong He. (2020) Accelerating Training of Transformer-Based Language Models with Progressive Layer Dropping. arXiv:2010.13369 and NeurIPS 2020 .
- Jie Ren, Samyam Rajbhandari, Reza Yazdani Aminabadi, Olatunji Ruwase, Shuangyan Yang, Minjia Zhang, Dong Li, Yuxiong He. (2021) ZeRO-Offload: Democratizing Billion-Scale Model Training. arXiv:2101.06840 and USENIX ATC 2021 . [paper] [slides] [blog]
- Hanlin Tang, Shaoduo Gan, Ammar Ahmad Awan, Samyam Rajbhandari, Conglong Li, Xiangru Lian, Ji Liu, Ce Zhang, Yuxiong He. (2021) 1-bit Adam: Communication Efficient Large-Scale Training with Adam’s Convergence Speed. arXiv:2102.02888 and ICML 2021 .
- Samyam Rajbhandari, Olatunji Ruwase, Jeff Rasley, Shaden Smith, Yuxiong He. (2021) ZeRO-Infinity: Breaking the GPU Memory Wall for Extreme Scale Deep Learning. arXiv:2104.07857 and SC 2021 . [paper] [slides] [blog]
[LINK: [slides]](https://github.com/deepspeedai/DeepSpeed/blob/master/docs/assets/files/SC21-ZeRO-Infinity.pdf)
- Conglong Li, Ammar Ahmad Awan, Hanlin Tang, Samyam Rajbhandari, Yuxiong He. (2021) 1-bit LAMB: Communication Efficient Large-Scale Large-Batch Training with LAMB’s Convergence Speed. arXiv:2104.06069 and HiPC 2022 .
- Conglong Li, Minjia Zhang, Yuxiong He. (2021) The Stability-Efficiency Dilemma: Investigating Sequence Length Warmup for Training GPT Models. arXiv:2108.06084 and NeurIPS 2022 .
- Yucheng Lu, Conglong Li, Minjia Zhang, Christopher De Sa, Yuxiong He. (2022) Maximizing Communication Efficiency for Large-scale Training via 0/1 Adam. arXiv:2202.06009 .
- Samyam Rajbhandari, Conglong Li, Zhewei Yao, Minjia Zhang, Reza Yazdani Aminabadi, Ammar Ahmad Awan, Jeff Rasley, Yuxiong He. (2022) DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale arXiv:2201.05596 and ICML 2022 . [pdf] [slides] [blog]
[LINK: [slides]](https://github.com/deepspeedai/DeepSpeed/blob/master/docs/assets/files/ICML-5mins.pdf)
- Shaden Smith, Mostofa Patwary, Brandon Norick, Patrick LeGresley, Samyam Rajbhandari, Jared Casper, Zhun Liu, Shrimai Prabhumoye, George Zerveas, Vijay Korthikanti, Elton Zhang, Rewon Child, Reza Yazdani Aminabadi, Julie Bernauer, Xia Song, Mohammad Shoeybi, Yuxiong He, Michael Houston, Saurabh Tiwary, Bryan Catanzaro. (2022) Using DeepSpeed and Megatron to Train Megatron-Turing NLG 530B, A Large-Scale Generative Language Model arXiv:2201.11990 .
- Xiaoxia Wu, Zhewei Yao, Minjia Zhang, Conglong Li, Yuxiong He. (2022) Extreme Compression for Pre-trained Transformers Made Simple and Efficient. arXiv:2206.01859 and NeurIPS 2022 .
- Zhewei Yao, Reza Yazdani Aminabadi, Minjia Zhang, Xiaoxia Wu, Conglong Li, Yuxiong He. (2022) ZeroQuant: Efficient and Affordable Post-Training Quantization for Large-Scale Transformers. arXiv:2206.01861 and NeurIPS 2022 [slides] [blog]
[LINK: [slides]](https://github.com/deepspeedai/DeepSpeed/blob/master/docs/assets/files/zeroquant_series.pdf)
- Reza Yazdani Aminabadi, Samyam Rajbhandari, Minjia Zhang, Ammar Ahmad Awan, Cheng Li, Du Li, Elton Zheng, Jeff Rasley, Shaden Smith, Olatunji Ruwase, Yuxiong He. (2022) DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale. arXiv:2207.00032 and SC 2022 . [paper] [slides] [blog]
[LINK: [slides]](https://github.com/deepspeedai/DeepSpeed/blob/master/docs/assets/files/sc22-ds-inference.pdf)
- Zhewei Yao, Xiaoxia Wu, Conglong Li, Connor Holmes, Minjia Zhang, Cheng Li, Yuxiong He. (2022) Random-LTD: Random and Layerwise Token Dropping Brings Efficient Training for Large-scale Transformers. arXiv:2211.11586 .
- Conglong Li, Zhewei Yao, Xiaoxia Wu, Minjia Zhang, Yuxiong He. (2022) DeepSpeed Data Efficiency: Improving Deep Learning Model Quality and Training Efficiency via Efficient Data Sampling and Routing. arXiv:2212.03597 ENLSP2023 Workshop at NeurIPS2023
[LINK: ENLSP2023 Workshop at NeurIPS2023](https://neurips2023-enlsp.github.io/)
- Xiaoxia Wu, Cheng Li, Reza Yazdani Aminabadi, Zhewei Yao, Yuxiong He. (2023) Understanding INT4 Quantization for Transformer Models: Latency Speedup, Composability, and Failure Cases. arXiv:2301.12017 and ICML2023 .
- Syed Zawad, Cheng Li, Zhewei Yao, Elton Zheng, Yuxiong He, Feng Yan. (2023) DySR: Adaptive Super-Resolution via Algorithm and System Co-design. ICLR:2023 .
- Sheng Shen, Zhewei Yao, Chunyuan Li, Trevor Darrell, Kurt Keutzer, Yuxiong He. (2023) Scaling Vision-Language Models with Sparse Mixture of Experts. arXiv:2303.07226 and Finding at EMNLP2023 .
- Quentin Anthony, Ammar Ahmad Awan, Jeff Rasley, Yuxiong He, Aamir Shafi, Mustafa Abduljabbar, Hari Subramoni, Dhabaleswar Panda. (2023) MCR-DL: Mix-and-Match Communication Runtime for Deep Learning arXiv:2303.08374 and will appear at IPDPS 2023.
- Siddharth Singh, Olatunji Ruwase, Ammar Ahmad Awan, Samyam Rajbhandari, Yuxiong He, Abhinav Bhatele. (2023) A Hybrid Tensor-Expert-Data Parallelism Approach to Optimize Mixture-of-Experts Training arXiv:2303.06318 and will appear at ICS 2023.
- Guanhua Wang, Heyang Qin, Sam Ade Jacobs, Xiaoxia Wu, Connor Holmes, Zhewei Yao, Samyam Rajbhandari, Olatunji Ruwase, Feng Yan, Lei Yang, Yuxiong He. (2023) ZeRO++: Extremely Efficient Collective Communication for Giant Model Training arXiv:2306.10209 and ML for Sys Workshop at NeurIPS2023 [blog]
- Zhewei Yao, Xiaoxia Wu, Cheng Li, Stephen Youn, Yuxiong He. (2023) ZeroQuant-V2: Exploring Post-training Quantization in LLMs from Comprehensive Study to Low Rank Compensation arXiv:2303.08302 and ENLSP2023 Workshop at NeurIPS2023 [slides]
[LINK: ENLSP2023 Workshop at NeurIPS2023](https://neurips2023-enlsp.github.io/)
[LINK: [slides]](https://github.com/deepspeedai/DeepSpeed/blob/master/docs/assets/files/zeroquant_series.pdf)
- Pareesa Ameneh Golnari, Zhewei Yao, Yuxiong He. (2023) Selective Guidance: Are All the Denoising Steps of Guided Diffusion Important? arXiv:2305.09847
- Zhewei Yao, Reza Yazdani Aminabadi, Olatunji Ruwase, Samyam Rajbhandari, Xiaoxia Wu, Ammar Ahmad Awan, Jeff Rasley, Minjia Zhang, Conglong Li, Connor Holmes, Zhongzhu Zhou, Michael Wyatt, Molly Smith, Lev Kurilenko, Heyang Qin, Masahiro Tanaka, Shuai Che, Shuaiwen Leon Song, Yuxiong He. (2023) DeepSpeed-Chat: Easy, Fast and Affordable RLHF Training of ChatGPT-like Models at All Scales arXiv:2308.01320 .
- Xiaoxia Wu, Zhewei Yao, Yuxiong He. (2023) ZeroQuant-FP: A Leap Forward in LLMs Post-Training W4A8 Quantization Using Floating-Point Formats arXiv:2307.09782 and ENLSP2023 Workshop at NeurIPS2023 [slides]
[LINK: ENLSP2023 Workshop at NeurIPS2023](https://neurips2023-enlsp.github.io/)
[LINK: [slides]](https://github.com/deepspeedai/DeepSpeed/blob/master/docs/assets/files/zeroquant_series.pdf)
- Zhewei Yao, Xiaoxia Wu, Conglong Li, Minjia Zhang, Heyang Qin, Olatunji Ruwase, Ammar Ahmad Awan, Samyam Rajbhandari, Yuxiong He. (2023) DeepSpeed-VisualChat: Multi-Round Multi-Image Interleave Chat via Multi-Modal Causal Attention arXiv:2309.14327
- Shuaiwen Leon Song, Bonnie Kruft, Minjia Zhang, Conglong Li, Shiyang Chen, Chengming Zhang, Masahiro Tanaka, Xiaoxia Wu, Jeff Rasley, Ammar Ahmad Awan, Connor Holmes, Martin Cai, Adam Ghanem, Zhongzhu Zhou, Yuxiong He, et al. (2023) DeepSpeed4Science Initiative: Enabling Large-Scale Scientific Discovery through Sophisticated AI System Technologies arXiv:2310.04610 [blog]
- Zhewei Yao, Reza Yazdani Aminabadi, Stephen Youn, Xiaoxia Wu, Elton Zheng, Yuxiong He. (2023) ZeroQuant-HERO: Hardware-Enhanced Robust Optimized Post-Training Quantization Framework for W8A8 Transformers arXiv:2310.17723
- Sam Ade Jacobs, Masahiro Tanaka, Chengming Zhang, Minjia Zhang, Reza Yazdani Aminadabi, Shuaiwen Leon Song, Samyam Rajbhandari, Yuxiong He. (2024) System Optimizations for Enabling Training of Extreme Long Sequence Transformer Models
- Xinyu Lian, Sam Ade Jacobs, Lev Kurilenko, Masahiro Tanaka, Stas Bekman, Olatunji Ruwase, Minjia Zhang. (2024) Universal Checkpointing: Efficient and Flexible Checkpointing for Large Scale Distributed Training arXiv:2406.18820
Xinyu Lian, Sam Ade Jacobs, Lev Kurilenko, Masahiro Tanaka, Stas Bekman, Olatunji Ruwase, Minjia Zhang. (2024) Universal Checkpointing: Efficient and Flexible Checkpointing for Large Scale Distributed Training arXiv:2406.18820
- Sam Ade Jacobs, Masahiro Tanaka, Chengming Zhang, Minjia Zhang, Reza Yazdani Aminadabi, Shuaiwen Leon Song, Samyam Rajbhandari, Yuxiong He. (2024) System Optimizations for Enabling Training of Extreme Long Sequence Transformer Models
- Xinyu Lian, Sam Ade Jacobs, Lev Kurilenko, Masahiro Tanaka, Stas Bekman, Olatunji Ruwase, Minjia Zhang. (2024) Universal Checkpointing: Efficient and Flexible Checkpointing for Large Scale Distributed Training arXiv:2406.18820
- Stas Bekman, Samyam Rajbhandari, Michael Wyatt, Jeff Rasley, Tunji Ruwase, Zhewei Yao, Aurick Qiao, Yuxiong He. (2025) Arctic Long Sequence Training: Scalable And Efficient Training For Multi-Million Token Sequences arXiv:2506.13996
- Tingfeng Lan, Yusen Wu, Bin Ma, Zhaoyuan Su, Rui Yang, Tekin Bicer, Masahiro Tanaka, Olatunji Ruwase, Dong Li, Yue Cheng. (2025) ZenFlow: Enabling Stall-Free Offloading Training via Asynchronous Updates arXiv:2505.12242
- Xinyu Lian, Masahiro Tanaka, Olatunji Ruwase, Minjia Zhang. (2026) SuperOffload: Unleashing the Power of Large-Scale LLM Training on Superchips arxiv , ASPLOS 2026

## Videos Permalink

- DeepSpeed KDD 2020 Tutorial Overview ZeRO + large model training 17B T-NLG demo Fastest BERT training + RScan tuning DeepSpeed hands on deep dive: part 1 , part 2 , part 3 FAQ
- Overview
- ZeRO + large model training
- 17B T-NLG demo
- Fastest BERT training + RScan tuning
- DeepSpeed hands on deep dive: part 1 , part 2 , part 3
- FAQ
- Microsoft Research Webinar Registration is free and all videos are available on-demand. ZeRO & Fastest BERT: Increasing the scale and speed of deep learning training in DeepSpeed .
- Registration is free and all videos are available on-demand.
- ZeRO & Fastest BERT: Increasing the scale and speed of deep learning training in DeepSpeed .
- DeepSpeed on AzureML
- Large Model Training and Inference with DeepSpeed // Samyam Rajbhandari // LLMs in Prod Conference [slides]
[LINK: [slides]](docs/assets/files/presentation-mlops.pdf)
- Community Tutorials DeepSpeed: All the tricks to scale to gigantic models (Mark Saroufim) Turing-NLG, DeepSpeed and the ZeRO optimizer (Yannic Kilcher) Ultimate Guide To Scaling ML Models (The AI Epiphany)
- DeepSpeed: All the tricks to scale to gigantic models (Mark Saroufim)
- Turing-NLG, DeepSpeed and the ZeRO optimizer (Yannic Kilcher)
- Ultimate Guide To Scaling ML Models (The AI Epiphany)

--------------------
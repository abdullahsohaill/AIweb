# **Efficient Streaming Language Models with Attention Sinks**
**URL:** https://iclr.cc/virtual/2024/poster/18794
**Page Title:** ICLR Poster Efficient Streaming Language Models with Attention Sinks
--------------------

### (Raw Extraction Fallback)

Skip to yearly menu bar
Skip to main content
Main Navigation
ICLR 
My Stuff
 Login
Select Year: (2024) 
Getting Started
Schedule
Main Conference 
Workshops
Community 
Sponsors
Organizers
Help 

POSTER
Efficient Streaming Language Models with Attention Sinks
Guangxuan Xiao · Yuandong Tian · Beidi Chen · Song Han · Mike Lewis
2024 Poster
Project Page
[
Slides
] 
[
Poster
] 
[
OpenReview
] 
Abstract
Deploying Large Language Models (LLMs) in streaming applications such as multi-round dialogue, where long interactions are expected, is urgently needed but poses two major challenges.Firstly, during the decoding stage, caching previous tokens' Key and Value states (KV) consumes extensive memory.Secondly, popular LLMs cannot generalize to longer texts than the training sequence length.Window attention, where only the most recent KVs are cached, is a natural approach --- but we show that it fails when the text length surpasses the cache size.We observe an interesting phenomenon, namely attention sink, that keeping the KV of initial tokens will largely recover the performance of window attention. In this paper, we first demonstrate that the emergence of attention sink is due to the strong attention scores towards initial tokens as a ``sink'' even if they are not semantically important.Based on the above analysis, we introduce StreamingLLM, an efficient framework that enables LLMs trained with a finite length attention window to generalize to infinite sequence length without any fine-tuning.We show that StreamingLLM can enable Llama-2, MPT, Falcon, and Pythia to perform stable and efficient language modeling with up to 4 million tokens and more.In addition, we discover that adding a placeholder token as a dedicated attention sink during pre-training can further improve streaming deployment. In streaming settings, StreamingLLM outperforms the sliding window recomputation baseline by up to 22.2
×
 speedup.Code and datasets are provided at https://github.com/mit-han-lab/streaming-llm.
Video
Chat is not available.
ICLR uses cookies for essential functions only. We do not sell your personal information. Our Privacy Policy » 	Accept

The ICLR Logo above may be used on presentations. Right-click and choose download. It is a vector graphic and may be used at any scale.

USEFUL LINKS
About ICLR
Sponsor / Exhibitor Information
Press
CONTACT

 2710 E Corridor Dr, Appleton WI 54913

 Email

 Phone: +1-920-268-4789

ICLR Proceedings at OpenReview

--------------------
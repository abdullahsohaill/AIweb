# [demo]
**URL:** https://osu-nlp-group.github.io/Mind2Web
**Page Title:** Mind2Web
--------------------


## Mind2Web: Towards a Generalist Agent for the Web

[LINK: Xiang Deng](https://xiang-deng.github.io/)
[LINK: Yu Gu](https://entslscheia.github.io/)
[LINK: Shijie Chen](https://chensj98.github.io/)
[LINK: Boshi Wang](https://boshi-wang.github.io/)
[LINK: Yu Su](https://ysu1989.github.io/)
[LINK: Code](https://github.com/OSU-NLP-Group/Mind2Web)
- Reflect diverse and practical use cases on the web.
- Provide challenging yet realistic environments with real-world websites.
- Test generalization ability across tasks and environments.
(a) Find one-way flights from New York to Toronto.
(b) Book a roundtrip on July 1 from Mumbai to London and vice versa on July 5 for two adults and a
                12-year-old in premium
                economy and if a flight is not available, search through the calendar for available flights.
(c) Search receipt with the eTicket 12345678 for the trip reserved by Jason Two
(d) Find a flight from Chicago to London on 20 April and return on 23 April.
(e) Search for the interactions between ibuprofen and aspirin.
(f) As a Verizon user, finance a blue iPhone 13 with 256gb along with monthly apple care.
(g) Find Elon Musk's profile and start following, start notifications and like the latest tweet.
(h) Browse comedy films streaming on Netflix that was released from 1992 to 2007.
(i) Open page to schedule an appointment for car knowledge test.

## Abstract

We introduce Mind2Web , the first dataset for developing and evaluating generalist
agents for the web that can follow language instructions to complete complex tasks
on any website. Existing datasets for web agents either use simulated websites or
only cover a limited set of websites and tasks, thus not suitable for generalist web
agents. With over 2,000 open-ended tasks collected from 137 websites spanning
31 domains and crowdsourced action sequences for the tasks, Mind2Web provides
three necessary ingredients for building generalist web agents: 1. diverse
domains, websites, and tasks, 2. use of real-world websites instead of simulated
and simplified ones, and 3. a broad spectrum of user interaction patterns. Based
on Mind2Web , we conduct an initial exploration of using large language models
(LLMs) for building generalist web agents. While the raw HTML of real-world websites
are often too large to be fed to LLMs, we show that first filtering it with a small
LM significantly improves the effectiveness and efficiency of LLMs. Our solution
demonstrates a decent level of performance, even on websites or entire domains the
model has never seen before, but there is still a substantial room to improve towards
truly generalizable agents.
Updates
- 2025-3-25: Online-Mind2Web released!
[LINK: Online-Mind2Web](https://github.com/OSU-NLP-Group/Online-Mind2Web)
- 2024-3-18: Multimodal-Mind2Web dataset released.
We have paired each HTML document with the corresponding webpage screenshot image and saved
the trouble of downloading Mind2Web Raw Dump .
[LINK: Mind2Web Raw Dump](https://github.com/OSU-NLP-Group/Mind2Web?tab=readme-ov-file#raw-dump-with-full-traces-and-snapshots)
- 2023-8-6: We have updated the GitHub Repo with fine-tuning
code/models for MindAct.
[LINK: GitHub Repo](https://github.com/OSU-NLP-Group/Mind2Web)
- 2023-7-3: We have released the raw dump with the trace file, network traffic, screenshots and other
files. Please check out the data and the GitHub
Repo for more details.
[LINK: GitHub
Repo](https://github.com/OSU-NLP-Group/Mind2Web)
- 2023-6-13: We have released the training/test data and codebase for the paper. Please check out our GitHub Repo .
[LINK: GitHub Repo](https://github.com/OSU-NLP-Group/Mind2Web)

## Introduction

- Cross Task Generalization : Generalization across tasks in the same environment, such as
              (a) to (c).
- Cross Website Generalization : Generalization across websites under the same domain, such as
              (a) to (d).
- Cross Domain Generalization : Generalization across tasks and environments, such as (e) through
              (i).
- Task Description that describes the task in natural language sentences.
- Action Sequence that describes the sequence of actions to be performed to complete the
              task.
- Each action is a pair of (Operation, Target Element) , where the Target Element is an element in the web page that the user choose to interact with, and the Operation is the action to be performed on the element.
- We support four common operations: Click , Hover , Type and Select
- Webpage Snapshots that serve as the environment. We provide snapshots of differnt formats: MHTML that contains the raw HTML code of the webpage. DOM Snapshot that contains snapshot with DOM, layout, and style information Image that contains the screenshot of the webpage. HAR that contains all network traffic for replay. Trace that
                  contains the complete interaction trace for the annotation.
- MHTML that contains the raw HTML code of the webpage.
[LINK: MHTML](https://chromedevtools.github.io/devtools-protocol/tot/Page/#method-captureSnapshot)
- DOM Snapshot that contains snapshot with DOM, layout, and style information
[LINK: DOM Snapshot](https://chromedevtools.github.io/devtools-protocol/tot/DOMSnapshot/)
- Image that contains the screenshot of the webpage.
- HAR that contains all network traffic for replay.
[LINK: HAR](https://playwright.dev/docs/network#record-and-replay-requests)
- Trace that
                  contains the complete interaction trace for the annotation.
[LINK: Trace](https://playwright.dev/docs/trace-viewer)
- Phase 1, Task Proposal : We first ask the worker to propose tasks that can be performed on a
                  given website.
                  We mannually review the proposed tasks and select the ones that are feasible and interesting for
                  annotation in Phase 2.
- Phase 2, Task Demonstration : We ask the worker to demonstrate how to perform the task on the
                  website. We develop
                  an annotation tool with Playwright which records
                  the interaction trace and takes snapshots of the webpage at each step.
- Phase 3, Task Verification : The authors verified all the tasks to make sure that all actions
                  are clean and the task description correctly relfects the annotated actions.

## Data Statistics & Comparison

Below we show some statics of Mind2Web , and how it compares against other existing datasets.
[LINK: WebShop](https://webshop-pnlp.github.io/)
[LINK: WebSRC](https://x-lance.github.io/WebSRC/)
[LINK: META-GUI](https://x-lance.github.io/META-GUI-Leaderboard/)
[LINK: MoTIF](https://github.com/aburns4/MoTIF)
[LINK: SGD](https://github.com/google-research-datasets/dstc8-schema-guided-dialogue)
[LINK: MultiWOZ](https://github.com/budzianowski/multiwoz)

## Data Overview

Below we show an overview of the domains, websites and tasks covered by our dataset.
You can interact with the visualization to explore the data.
- Figure (a) shows the distribution of domains and websites in our dataset, you can click to zoom in.
- Figure (b) shows the distribution of task tags 1 for the selected domain and website. You can
click to select a tag, or click outside to deselect.
- Figure (c) shows sample tasks included in our dataset. The tasks are organized by Intents , Objects and Conditions 1 contained in the task. Select in Figure (a) and (b) to filter the tasks.
(a) Domain & Websites
(b) Tags 1
(c) Tasks organized by Intents, Objects and Conditions 1, 2
- We use ChatGPT & GPT-4 to extract intents, objects and conditions from the tasks, and assign tags. See
the Prompt for more details.
- We only show the 10 most common items at each level here.

## Data Explorer

Below we show the data explorer, which allows you to explore the training data in more detail.
You can click Random Task to load a random task.
Or select a Domain , Website , and type to search for a task.
- Recording
- Raw Trace

## Related Work

Our work is inspired by many existing works, including:
- MiniWoB , MiniWoB++ , RUSS and WebShop that focus on task automation in web environments. Tianlin Shi, Andrej Karpathy, Linxi Fan, Jonathan Hernandez, and Percy Liang. World of Bits:
  An Open-Domain
  Platform for Web-Based Agents. ICML 2017. Evan Zheran Liu*, Kelvin Guu*, Panupong Pasupat*, Tianlin Shi, Percy Liang. Reinforcement Learning
  on Web
  Interfaces using Workflow-Guided Exploration. ICLR 2018. Nancy Xu, Sam Masling, Michael Du, Giovanni Campagna, Larry Heck, James Landay, and Monica S. Lam.
  Grounding
  open-domain instructions to automate web support tasks. arXiv preprint arXiv:2103.16057 (2021). Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan. WebShop: Towards Scalable Real-World Web
  Interaction with Grounded Language Agents. NeurIPS 2022.
- Tianlin Shi, Andrej Karpathy, Linxi Fan, Jonathan Hernandez, and Percy Liang. World of Bits:
  An Open-Domain
  Platform for Web-Based Agents. ICML 2017.
- Evan Zheran Liu*, Kelvin Guu*, Panupong Pasupat*, Tianlin Shi, Percy Liang. Reinforcement Learning
  on Web
  Interfaces using Workflow-Guided Exploration. ICLR 2018.
- Nancy Xu, Sam Masling, Michael Du, Giovanni Campagna, Larry Heck, James Landay, and Monica S. Lam.
  Grounding
  open-domain instructions to automate web support tasks. arXiv preprint arXiv:2103.16057 (2021).
- Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan. WebShop: Towards Scalable Real-World Web
  Interaction with Grounded Language Agents. NeurIPS 2022.
- SWDE and WebSRC that focuses on web extraction and QA. Qiang Hao, Rui Cai, Yanwei Pang, and Lei Zhang. From One Tree to a Forest: a Uniﬁed Solution for
  Structured Web Data
  Extraction. SIGIR 2011. Xingyu Chen, Zihan Zhao, Lu Chen, JiaBao Ji, Danyang Zhang, Ao Luo, Yuxuan Xiong, and Kai Yu. 2021.
  WebSRC: A Dataset
  for Web-Based Structural Reading Comprehension. EMNLP 2021.
- Qiang Hao, Rui Cai, Yanwei Pang, and Lei Zhang. From One Tree to a Forest: a Uniﬁed Solution for
  Structured Web Data
  Extraction. SIGIR 2011.
- Xingyu Chen, Zihan Zhao, Lu Chen, JiaBao Ji, Danyang Zhang, Ao Luo, Yuxuan Xiong, and Kai Yu. 2021.
  WebSRC: A Dataset
  for Web-Based Structural Reading Comprehension. EMNLP 2021.
- PixelHelp , META-GUI and MoTIF that focuses on task automation with mobile APPS. Yang Li, Jiacong He, Xin Zhou, Yuan Zhang, and Jason Baldridge. Mapping Natural Language Instructions to
  Mobile UI Action Sequences. ACL 2020. Liangtai Sun, Xingyu Chen, Lu Chen, Tianle Dai, Zichen Zhu, and Kai Yu. META-GUI: Towards Multi-modal
  Conversational Agents on Mobile GUI. EMNLP 2022. Andrea Burns, Deniz Arsan, Sanjna Agrawal, Ranjitha Kumar, Kate Saenko, and Bryan A. Plummer. A
  Dataset for
  Interactive Vision-Language Navigation with Unknown Command Feasibility. ECCV 2022.
- Yang Li, Jiacong He, Xin Zhou, Yuan Zhang, and Jason Baldridge. Mapping Natural Language Instructions to
  Mobile UI Action Sequences. ACL 2020.
- Liangtai Sun, Xingyu Chen, Lu Chen, Tianle Dai, Zichen Zhu, and Kai Yu. META-GUI: Towards Multi-modal
  Conversational Agents on Mobile GUI. EMNLP 2022.
- Andrea Burns, Deniz Arsan, Sanjna Agrawal, Ranjitha Kumar, Kate Saenko, and Bryan A. Plummer. A
  Dataset for
  Interactive Vision-Language Navigation with Unknown Command Feasibility. ECCV 2022.
Concurrent to our project, there are also many efforts on developing web-based agents, in particular with
large language models.
We hope Mind2Web can serve as a standard benchmark and facilitate the development of such systems.
- ChatGPT and plugins. https://openai.com/blog/chatgpt-plugins .
- ACT-1 from ADEPT. https://www.adept.ai/blog/act-1 .
- LangChain. https://python.langchain.com/en/latest/index.html .
- NatBOT. https://github.com/nat/natbot .
[LINK: https://github.com/nat/natbot](https://github.com/nat/natbot)
- Multion. https://www.multion.ai/ .
- Auto-GPT. https://github.com/Significant-Gravitas/Auto-GPT
[LINK: https://github.com/Significant-Gravitas/Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT)

## Disclaimer

## Citation

## Corresponding Authors

[LINK: Xiang Deng](https://xiang-deng.github.io/)
[LINK: Yu Su](https://ysu1989.github.io/)

--------------------
# 2022/04/04] [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](), Michael Ahn, e al. [[demo]
**URL:** https://say-can.github.io
**Page Title:** SayCan: Grounding Language in Robotic Affordances
--------------------


## Do As I Can, Not As I Say : Grounding Language in Robotic Affordances

- Michael Ahn*
- Anthony Brohan*
- Noah Brown*
- Yevgen Chebotar*
- Omar Cortes*
- Byron David*
- Chelsea Finn*
- Chuyuan Fu*
- Keerthana Gopalakrishnan*
- Karol Hausman*
- Alex Herzog*
- Daniel Ho*
- Jasmine Hsu*
- Julian Ibarz*
- Brian Ichter*
- Alex Irpan*
- Eric Jang*
- Rosario Jauregui Ruano*
- Kyle Jeffrey*
- Sally Jesmonth*
- Nikhil Joshi*
- Ryan Julian*
- Dmitry Kalashnikov*
- Yuheng Kuang*
- Kuang-Huei Lee*
- Sergey Levine*
- Yao Lu*
- Linda Luu*
- Carolina Parada*
- Peter Pastor*
- Jornell Quiambao*
- Kanishka Rao*
- Jarek Rettinghouse*
- Diego Reyes*
- Pierre Sermanet*
- Nicolas Sievers*
- Clayton Tan*
- Alexander Toshev*
- Vincent Vanhoucke*
- Fei Xia*
- Ted Xiao*
- Peng Xu*
- Sichun Xu*
- Mengyuan Yan*
- Andy Zeng*
- Paper
- Video
- Blogpost
- Code
[LINK: Code](https://github.com/google-research/google-research/tree/master/saycan)
- Demo

### What's New

- [8/16/2022] We integrated SayCan with Pathways Language Model (PaLM) , and updated the results. We also added new capabilities including drawer manipulation, chain of thought prompting and multilingual instructions. You can see all the new results in the updated paper .
- [8/16/2022] Our updated results show that SayCan combined with the improved language model (PaLM), which we refer to as PaLM-SayCan, improves the robotics performance of the entire system compared to a previous LLM (FLAN). PaLM-SayCan chooses the correct sequence of skills 84% of the time and executes them successfully 74% of the time, reducing errors by a half compared to FLAN.  This is particularly exciting because it represents the first time we can see how an improvement in language models translates to a similar improvement in robotics.
- [8/16/2022] We open-sourced a version of SayCan on a simulated tabletop environment.
- [4/4/2022] Initial release of SayCan.

### Abstract

Large language models can encode a wealth of semantic knowledge about the world. Such knowledge could in principle be extremely useful to robots aiming to act upon high-level, temporally extended instructions expressed in natural language.
However, a significant weakness of language models is that they lack contextual grounding, which makes it difficult to leverage them for decision making within a given real-world context. 
For example, asking a language model to describe how to clean a spill might result in a reasonable narrative, but it may not be applicable to a particular agent, such as a robot, that needs to perform this task in a particular environment. 
We propose to provide this grounding by means of pretrained behaviors, which are used to condition the model to propose natural language actions that are both feasible and contextually appropriate. 
The robot can act as the language model’s “hands and eyes,” while the language model supplies high-level semantic knowledge about the task. 
We show how low-level tasks can be combined with large language models so  that  the  language  model  provides  high-level  knowledge about the procedures for performing complex and temporally extended instructions,  while  value  functions  associated  with  these  tasks  provide  the  grounding necessary to connect this knowledge to a particular physical environment. 
We evaluate our method on a number of real-world robotic tasks, where we show that this approach is capable of completing long-horizon,  abstract,  natural language instructions on a mobile manipulator.

### Video

### Approach

Imagine a robot operating in a kitchen that is capable of executing skills such as "pick up the coffee cup" or "go to the sink".
To get the robot to use these skills to perform a complex task (e.g. "I spilled my drink, can you help?"), the user could manually break it up into steps consisting of these atomic commands. 
			However,this would be exceedingly tedious. A language model can split the high-level instruction ("I spilled my drink, can you help?") into sub-tasks, but it cannot do that effectively unless it has the context of what the robot is capable of given the abilities, current state of the robot and its environment. When querying existing large language models, we see that a language model queried with "I spilled my drink, can you help?" may respond with "You could try using a vaccuum cleaner" or "I'm sorry, I didn't mean to spill it".

### Results

We benchmarked the proposed algorithm Saycan in two scenes, an office kitchen and a mock office kitchen with 101 tasks specified by natural 
			langauge instructions. Below we show some highlights of the results.
We visualize the decision making process of SayCan. The blue bar indicates (normalized) LLM probability and the red bar 
			indicates (normalized) probability of 
			successful execution of selected skills. The combined score is in green bar, 
			and the algorithm choose the skill with highest combined score. This visualization
			highlights the interpretability of SayCan.
Given the task "I spilled my coke, can you bring me something to clean it up?", SayCan successfully planned and executed the following 
			steps 1. Find a sponge 2. Pick up the sponge
			3. Bring it to you 4. Done. As shown below:
However, if we slightly tweak the task to "I spilled my coke, can you bring me a replacement", SayCan planned the following steps instead
			1. Find a coke can 2. Pick up the coke can
			3. Bring it to you 4. Done. This highlights that SayCan is able to leverage the large capacity of LLMs, 
			where their semantic knowledge about the world can be useful both for interpreting instructions
			and understanding how to execute them.
In the next example, SayCan leverages the ability of the affordances to "override" the language model; though the language model believes picking up the sponge is the right skill, the affordances are aware this isn't possible and instead "find a sponge" is chosen. This highlights the necessity of affordance grounding.
The proposed approach achieves an overall plan success rate of 84% and execution success rate of 74% of 101 tasks, which is 14% and 13% higher than our initial release . For more details, please refer to 
			our paper.  We show that a robot’s performance can be improved simply by enhancing the underlying language model.
The proposed method can scale to long horizon tasks involving multiple steps, for example, for the task "I spilled my coke on the table,
			how would you throw it away and bring me something to help clean", the robot successfully planned and execute 8 steps. The execution 
			and planning process are shown in the video below.
For the task "I just worked out, can you bring me a drink and a snack to recover?, the execution 
			and planning process are shown in the video below.
In the next example, we show SayCan is able to plan and execute a very long-horizon task involving 16 steps.

### New Capabilities

PaLM-SayCan enables new capabilities. First, we show that it is very easy to incorporate new skills into the system, and use drawer manipulation as an example. Second, we show by leveraging chain of thought reasoning, we are able to solve tasks that requires reasoning. Finally we show the system can work with multilingual queries, without explicitly being designed to.
SayCan can be integrated with recent work improving LLM reasoning, such as Chain of Thought . With chain-of-thought prompting, PaLM-SayCan is able to handle tasks that require reasoning.
While not explicitly designed to work with multilingual queries, PaLM-SayCan is able to handle them. The LLM was trained on a multilingual corpus and thus SayCan can handle multilingual queries other than English. There is almost no performance drop on planning success rate when changing the queries from English to Chinese, French and Spanish.
As presented herein, PaLM-SayCan only receives environmental feedback through value functions at the current decision step, meaning if a skill fails or the environment changes, the necessary feedback may not be available. Owing to the extendibility and the natural language interface, follow up work builds upon PaLM-SayCan to enable closed-loop planning by leveraging environment feedback (from e.g., success detectors, scene descriptors, or even human feedback) through an inner monologue .
[LINK: inner monologue](https://innermonologue.github.io/)

### Citation

### Dataset

[LINK: [v0]](https://github.com/say-can/say-can.github.io/tree/main/data)

### Open Source

[LINK: [tabletop saycan]](https://github.com/google-research/google-research/tree/master/saycan)

### Acknowledgements

The authors would like to thank Fred Alcober, Yunfei Bai, Matt Bennice, Maarten Bosma, Justin Boyd, Bill Byrne, Kendra Byrne, Noah Constant, Pete Florence, Laura Graesser, Rico Jonschkowski, Daniel Kappler, Hugo Larochelle, Benjamin Lee, Adrian Li, Maysam Moussalem, Suraj Nair, Jane Park, Evan Rapoport, Krista Reymann, Jeff Seto, Dhruv Shah, Ian Storz, Razvan Surdulescu, Tom Small, Jason Wei, and Vincent Zhao for their help and support in various aspects of the project. The website template was borrowed from Jon Barron .

--------------------
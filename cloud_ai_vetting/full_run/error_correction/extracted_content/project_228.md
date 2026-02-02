# [Project
**URL:** https://zhaowei-wang-nlp.github.io/divscene-project-page
**Page Title:** DivScene: Benchmarking LVLMs for Object Navigation with Diverse Scenes and Objects
--------------------


## DivScene: Benchmarking LVLMs for Object Navigation with Diverse Scenes and Objects

[LINK: Zhaowei Wang](https://zhaowei-wang-nlp.github.io/)
[LINK: Hongming Zhang](https://panda0881.github.io/Hongming_Homepage/)
[LINK: Tianqiang Fang](https://tqfang.github.io/)
[LINK: Yang Yue](https://yueyang1996.github.io/)
[LINK: Kaixin Ma](https://mayer123.github.io/)
[LINK: Xiaoman Pan](https://panx27.github.io/homepage/)
[LINK: Code](https://github.com/zhaowei-wang-nlp/DivScene)

## Abstract

Object navigation in unknown environments is crucial for deploying embodied agents in real-world applications.
            While we have witnessed huge progress due to large-scale scene datasets, faster simulators, and stronger models, 
            previous studies mainly focus on limited scene types and target objects. In this paper, we study a new task of 
            navigating to diverse target objects in a large number of scene types. To benchmark the problem, we present a 
            large-scale scene dataset, DivScene, which contains 4,614 scenes across 81 different types. With the 
            dataset, we build an end-to-end embodied agent, NatVLM, by fine-tuning a Large Vision Language Model (LVLM) 
            through imitation learning. The LVLM is trained to take previous observations from the environment and generate 
            the next actions. We also introduce CoT explanation traces of the action prediction for better performance when 
            tuning LVLMs. Our extensive experiments find that we can build a performant LVLM-based agent through imitation 
            learning on the shortest paths constructed by a BFS planner without any human supervision. Our agent achieves a 
            success rate that surpasses GPT-4o by over 20%. Meanwhile, we carry out various analyses showing the generalization 
            ability of our agent. Our code and data are available at https://github.com/zhaowei-wang-nlp/DivScene.

## DivScene and DivTraj Datasets

In this paper, we study a new task of building navigational agents capable of generalizing to a wide range of unseen objects in diverse scenes. 
            We introduce a new dataset, DivScene, that features the most comprehensive range of scene types to the best of our knowledge. 
            Specifically, we collect 81 scene types based on MIT Scenes Dataset, which are further categorized into five big groups.
            Then, we use LLMs to automatically compose diverse house descriptions by adding attributes to scene types, such as ``a bakery with tile patterned walls.'' 
            We input these descriptions into the language-guided framework, Holodeck, to build houses automatically with the strong ability of GPT-4. 
            Finally, we compile 4,614 houses across 81 distinct scene types on the AI2THOR platform.
            Since we take advantage of the object assets Objaverse, our houses contain over 22K different kinds of objects, 
            making them ideal for testing navigation to diverse objects.

## NatVLM Agent

We propose an end-to-end object navigation agent called NatVLM ( Na vigational Chain-of- T hought VLM ), based on the large vision language model Idefics2 (8B). 
              The model is tuned to generate the next action given the current observation, such as the the egocentric view and the agent's status. 
              Here, we train the LVLM with imitation learning using shortest paths from a heuristic planner. 
              To improve the accuracy, we also manually collect complex CoT explanation traces of each prediction to help the LVLM understand the underlying rationale behind object navigation. 
              By tuning the LVLM, we eliminate the domain gap between navigation tasks and the pre-training corpus. 
              Meanwhile, our navigation is performed in an end-to-end manner with perception, circumventing the captioning model.

## Navigation Results

## Target: walk-in wardrobe

## Target: water bottle

## Target: booth seating

## House and Object Diversity

## Top 10 most common room types
            (outer) under each room category (inner)

## Top 15 most common scene types
            (inner) and their top 5 target object types
            (outer)

## BibTeX


--------------------
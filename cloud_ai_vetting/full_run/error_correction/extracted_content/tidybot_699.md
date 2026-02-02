# TidyBot
**URL:** https://tidybot.cs.princeton.edu
**Page Title:** TidyBot: Personalized Robot Assistance with Large Language Models
--------------------


## TidyBot Personalized Robot Assistance with Large Language Models

For a robot to personalize physical assistance effectively, it must learn user preferences that can be generally reapplied to future scenarios. In this work, we investigate personalization of household cleanup with robots that can tidy up rooms by picking up objects and putting them away. A key challenge is determining the proper place to put each object, as people's preferences can vary greatly depending on personal taste or cultural background. For instance, one person may prefer storing shirts in the drawer, while another may prefer them on the shelf. We aim to build systems that can learn such preferences from just a handful of examples via prior interactions with a particular person. We show that robots can combine language-based planning and perception with the few-shot summarization capabilities of large language models (LLMs) to infer generalized user preferences that are broadly applicable to future interactions. This approach enables fast adaptation and achieves 91.2% accuracy on unseen objects in our benchmark dataset. We also demonstrate our approach on a real-world mobile manipulator called TidyBot, which successfully puts away 85.0% of objects in real-world test scenarios.

### Paper

Autonomous Robots (AuRo) - Special Issue: Large Language Models in Robotics , 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) , 2023 Latest version (October 11, 2023): arXiv:2305.05658 [cs.RO] or here .

### Team

[LINK: Jimmy Wu 1](http://jimmyyhwu.github.io)
[LINK: Rika Antonova 2](https://contactrika.github.io)
[LINK: Andy Zeng 4](https://andyzeng.github.io)
[LINK: Shuran Song 5](https://shurans.github.io)

### Code

[LINK: GitHub](https://github.com/jimmyyhwu/tidybot)
- Benchmark dataset
[LINK: Benchmark dataset](https://github.com/jimmyyhwu/tidybot/blob/main/benchmark/scenarios.yml)
- LLM evaluation
[LINK: LLM evaluation](https://github.com/jimmyyhwu/tidybot/blob/main/benchmark/method_summarization.ipynb)
- Real robot implementation
[LINK: Real robot implementation](https://github.com/jimmyyhwu/tidybot)

### BibTeX

### Annotated Video

### Poster

### Stanford Introductory Video (with audio)

### Technical Summary Video (with audio)

### Real-World Results

Here we show example scenarios from our real-world evaluation. Underneath each video are the rules for the scenario depicted. The rules are automatically inferred by a large language model (LLM) through summarization of user preference examples, and are used by the robot to complete the task. All videos in this section play at 4x speed.
- light-colored clothing → seagrass laundry basket
- dark-colored clothing → white laundry basket
- light-colored clothing → pick and place
- dark-colored clothing → pick and place
- tool → right shelf
- wooden block → middle shelf
- fruit → left shelf
- tool → pick and place
- wooden block → pick and place
- fruit → pick and place
- plastic utensils → coffee table
- plastic bags → black storage box
- paper napkins and paper towels → trash can
- cans → recycling bin
- plastic utensils → pick and place
- plastic bags → pick and place
- paper napkins and paper towels → pick and place
- cans → pick and toss
- clothing → sofa
- snack → plastic storage box
- can → recycling bin
- wooden block → drawer
- fruit → black storage box
- clothing → pick and place
- wooden block → pick and place
- snack → pick and toss
- can → pick and toss
- fruit → pick and toss

### Acknowledgments

We would like to thank William Chong, Kevin Lin, and Jingyun Yang for fruitful technical discussions, and Bob Holmberg for mentorship and support in building up the mobile platforms. This work was supported in part by the Princeton School of Engineering, Toyota Research Institute, and the National Science Foundation under CCF-2030859, DGE-1656466, and IIS-2132519.

### Contact

If you have any questions, please feel free to contact Jimmy Wu .
[LINK: Jimmy Wu](http://jimmyyhwu.github.io)
Note: This is an academic research project and has no connection to any commercial product.
Last update: October 11, 2023

--------------------
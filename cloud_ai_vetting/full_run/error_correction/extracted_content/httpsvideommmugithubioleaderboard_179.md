# https://videommmu.github.io/#Leaderboard
**URL:** https://videommmu.github.io
**Page Title:** Video-MMMU
--------------------


## Video-MMMU

[LINK: Kairui Hu](https://kairuihu.github.io/)
[LINK: Penghao Wu](https://penghao-wu.github.io/)
[LINK: Fanyi Pu](https://github.com/pufanyi)
[LINK: Xiang Yue](https://xiangyue9607.github.io/)
[LINK: Yuanhan Zhang](https://zhangyuanhan-ai.github.io/)
[LINK: Ziwei Liu](https://liuziwei7.github.io/)
1 S-Lab, Nanyang Technological University 2 Carnegie Mellon University
[LINK: Code](https://github.com/EvolvingLMMs-Lab/VideoMMMU)
Business Economics
Business Finance
Business Manage
Business Economics
Engineering Architecture
Engineering Energy
Engineering Electronics
Engineering Computer Science
Art Art Theory
Art Art Theory
Humanities Psychology
Humanities History
Science Physics
Science Chemistry
Medicine Clinical Medicine
Medicine Public Health

## Abstract

Humans acquire knowledge through three cognitive stages: perceiving information, comprehending knowledge, and adapting knowledge to solve novel problems. Videos serve as an effective medium for this learning process, facilitating a progression through these cognitive stages. However, existing video benchmarks fail to systematically evaluate the knowledge acquisition capabilities in Large Multimodal Models (LMMs). To address this gap, we introduce Video-MMMU , a multi-modal, multi-disciplinary benchmark designed to assess LMMs' ability to acquire and utilize knowledge from videos. Video-MMMU features a curated collection of 300 expert-level videos and 900 human-annotated questions across six disciplines, evaluating knowledge acquisition through stage-aligned question-answer pairs: Perception, Comprehension, and Adaptation. A proposed knowledge gain metric, Δ knowledge , quantifies improvement in performance after watching the relevant video lectures. Evaluation of LMMs reveals a steep decline in performance as cognitive demands increase and highlights a significant gap between human and model knowledge acquisition, underscoring the need to enhance LMMs' capability to learn and adapt from videos.

## Overview

We introduce Video-MMMU , a multi-modal and multi-disciplinary video benchmark that evaluates LMMs' knowledge acquisition capability from educational videos.
1) Video as a Knowledge Source: Traditional VideoQA benchmarks focus primarily on evaluating how well models interpret visual content. Video-MMMU is the first to treat videos as a source of knowledge , assessing how effectively LMMs acquire knowledge from educational videos. Our dataset comprises 300 lecture-style, college-level videos spanning 30 subjects in 6 professional disciplines: Art, Business, Science, Medicine, Humanities, and Engineering.
2) Knowledge Acquisition-based Question Design: Each video includes three question-answer pairs aligned with the three knowledge acquisition stages: Perception (identifying key information related to the knowledge), Comprehension (understanding the underlying concepts), and Adaptation (applying knowledge to new scenarios).
3) From Absolute Performance towards Learning Efficiency: Δ knowledge A key novelty of Video-MMMU is that it evaluates not only a model's final accuracy but also its delta accuracy —the improvement in performance after learning from a video. A model may initially fail to solve an MMMU-style exam question, but we give the model a video where a human learner could learn to solve the question by watching the video. Video-MMMU tests how well LMMs improve their performance after watching the videos. Video-MMMU introduces Δ knowledge to quantify the model's learning gain from the videos.  Δ knowledge is defined as the normalized performance gain on the Adaptation track questions:
Key Insights:
- 1) Progressive Performance Decline: Model performance decreases as cognitive demands increase. While models perform relatively better on perception tasks, their accuracy drops notably on comprehension tasks and declines further on adaptation tasks.
- 2) Knowledge Acquisition from Videos is Challenging: The knowledge acquisition metric Δ knowledge reveals a significant gap between human and model performance. While humans achieve substantial improvement ( Δ knowledge = 33.1%) after watching the videos, even the top-performing models show smaller knowledge gains ( GPT-4o : Δ knowledge = 15.6%, Claude-3.5-Sonnet : Δ knowledge = 11.4%).
This limitation underscores a challenge in current LMMs. While humans naturally acquire knowledge through video-based learning, having developed this capability through classroom learning and educational experiences throughout life, LMMs struggle to effectively learn from videos. These findings emphasize the need for further research to enhance how LMMs acquire and utilize video-based information, bringing them closer to human-level learning processes.

## Video-MMMU Leaderboard

We evaluate various open-source and proprietary LMMs. The table below provides a detailed comparison. To submit your model results, please send an email to videommmu2025@gmail.com.
[LINK: GLM-4V-PLUS-0111](https://www.bigmodel.cn/dev/api/normal-model/glm-4v)
[LINK: Gemini 1.5 Flash](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf)
[LINK: mPLUG-Owl3-7B](https://github.com/X-PLUG/mPLUG-Owl/tree/main/mPLUG-Owl3)
[LINK: MAmmoTH-VL-8B](https://mammoth-vl.github.io/)

## Demo Video

## Statistics

## Annotation Pipeline

## Error Analysis

## Error Examples in Adaptation track

## Wrong-to-Right Examples in Adaptation track

## Video-MMMU Examples

## Video-MMMU Examples - Art

Question: Which of the following does NOT appear in the video frame when the video introduces Painting?
Options:
- Intense, warm colors
- Strong contrasts of light and dark
- Focus on movement, drama, and emotion
- Abstraction
- Allegory
- Enhanced sense of movement
- Deliberately set apart from Renaissance and Mannerism
- Asymmetry
- Renaissance
- Mannerism
Ground truth: D. Abstraction
Question: Based on your understanding of the video, which of the following statements about Baroque painting is/are correct?
- Statement 1. Baroque paintings focused on calm, balanced scenes with even lighting.
- Statement 2. Baroque artists used strong contrasts of light and dark to highlight key figures.
- Statement 3. Baroque painting was known for symmetrical compositions and a sense of stability.
- Statement 4. Baroque artists avoided using allegory in their works.
Options:
- Statement 1 is correct
- Statement 1 and 2 are correct
- Statement 1, 2, and 3 are correct
- Statement 1, 3, and 4 are correct
- Statement 2 and 4 are correct
- Statement 3 is correct
- Statements 1 and 4 are correct
- Statements 1, 3, and 4 are correct
- Statement 2 is correct
- All are correct
Ground truth: I. Statement 2 is correct
Question: On the basis of style, this painting belongs to which of the following periods?
Options:
- Rococo
- Gothic
- Renaissance
- Baroque
- Neoclassicism
- Byzantine
- Mannerism
- Romanticism
- Art Nouveau
- Classical
Ground truth: I. Baroque

## Video-MMMU Examples - Business

Question: According to the video, a minimum price control for alcoholic drinks, the intention is to discourage consumption from Q1 to ____, due to the negative externalities, and the price is raised to ____ from the free market price of ____. Fill in the blanks based on the video content.
Options:
- (Q*, Pmin, P1)
- (Q*, P1, Pmin)
- (Q1, Pmin, P2)
- (Q2, P1, Pmin)
- (Q*, P2, P1)
- (Q1, P2, Pmin)
- (Q2, Pmin, P1)
- (Q*, Pmin, P2)
- (Q2, P2, P1)
- (Q1, P1, Pmin)
Ground truth: A. (Q*, Pmin, P1)
Question: Based on your understanding, what is the correct sequence of consequences when a minimum price is imposed on a good with negative externalities in consumption?
Options:
- Free market equilibrium at P1 and Q1 → Minimum price imposed above P1 → Consumption contracts to Q* → Externality internalized.
- Minimum price imposed above P1 → Free market equilibrium at P1 and Q1 → Consumption contracts to Q* → Externality internalized.
- Free market equilibrium at P1 and Q1 → Consumption contracts to Q* → Minimum price imposed above P1 → Externality internalized.
- Externality internalized → Free market equilibrium at P1 and Q1 → Minimum price imposed above P1 → Consumption contracts to Q*.
- Minimum price imposed above P1 → Consumption contracts to Q* → Externality internalized → Free market equilibrium at P1 and Q1.
- Consumption contracts to Q* → Minimum price imposed above P1 → Free market equilibrium at P1 and Q1 → Externality internalized.
- Free market equilibrium at P1 and Q1 → Minimum price imposed above P1 → Externality internalized → Consumption contracts to Q*.
- Minimum price imposed above P1 → Free market equilibrium at P1 and Q1 → Externality internalized → Consumption contracts to Q*.
- Externality internalized → Minimum price imposed above P1 → Free market equilibrium at P1 and Q1 → Consumption contracts to Q*.
- Consumption contracts to Q* → Externality internalized → Minimum price imposed above P1 → Free market equilibrium at P1 and Q1.
Ground truth: A. Free market equilibrium at P1 and Q1 → Minimum price imposed above P1 → Consumption contracts to Q* → Externality internalized.
Question: Suppose the government decided that, since gasoline is a necessity, its price should be legally capped at $1.30 per gallon. What do you anticipate would be the outcome in the gasoline market?
Options:
- A price below that of $1.30 would cause a situation of excess demand and hence a surplus.
- A price below that of $1.30 would cause a situation of excess demand and hence a shortage.
- Not certain.
- A price above that of $1.30 would cause a situation of excess demand and hence a shortage.
- A price above that of $1.30 would cause a situation of excess supply and hence a shortage.
- A price at $1.30 per gallon would result in an equilibrium where supply meets demand.
- A price below that of $1.30 would cause a situation of excess supply and hence a surplus.
- A price at $1.30 would eliminate any market shortages or surpluses.
- A price of $1.30 would result in both excess demand and excess supply, depending on consumer preferences.
- All situations are possible.
Ground truth: B. A price below that of $1.30 would cause a situation of excess demand and hence a shortage.

## Video-MMMU Examples - Humanities

Question: Based on the video, fill in the blanks about the Functionalist view of society's culture:
"Functionalists take a ________ view on society's culture and suggest it ________."
Options:
- Consensus, reflects the norms and values of the majority — a value consensus
- Unified, represents shared practices and beliefs of a group
- Conflict, reveals power struggles and competing interests within society
- Critical, critiques the dominant traditions that maintain inequalities
- Conservative, emphasizes the preservation of societal expectations
- Agreement, highlights the shared opinions and moral agreements
- Progressive, encourages the development of new cultural ideologies
- Stratified, reflects the rules that structure society into classes
- Divisive, showcases the competing customs and traditions in society
- Analytical, breaks down societal structures into individual roles
Ground truth: A. Consensus, reflects the norms and values of the majority — a value consensus
Question: Based on your understanding, which of the following statements about different sociological theories on culture is/are false?
Statements:
- Statement 1. Functionalists argue that society's culture is fragmented, and individuals create their own norms based on personal preferences and life experiences.
- Statement 2. Marxists suggest that culture is imposed by the ruling class (bourgeoisie) to maintain control over the working class and reinforce capitalist ideologies.
- Statement 3. Feminists believe that culture is male-dominated and reflects patriarchal values, prioritizing men's interests over women's.
- Statement 4. Postmodernists suggest that there is a single dominant culture, and individuals can choose their own cultural norms.
Options:
- Statement 1 is false
- Statement 2 is false
- Statement 3 is false
- Statement 4 is false
- Statements 1 and 2 are false
- Statements 3 and 4 are false
- Statements 1 and 4 are false
- Statements 1 and 3 are false
- Statements 2 and 4 are false
- None of the statements are false
Ground truth: G. Statements 1 and 4 are false
Question: Identify the theory that the following argument represents.
Options:
- Functionalism
- Marxism
- New Right
- Postmodernism
- Social action approaches
- Interactionism
- Feminism
- Conflict Theory
- Modernity
- Positivists
Ground truth: Functionalism

## Video-MMMU Examples - Science

Question: What is the equation used when solving the first question in the video?
Options:
- y = v 0y t + 1/2 g t 2
- y = y 0 + v 0x t - 1/2 g t 2
- y = v 0x t + g t 2
- y = y 0 + v 0y t - 1/2 g t 2
- y = v 0y t - g t
- y = y 0 + v 0x t + 1/2 g t 2
- y = y 0 + g t
- y = y 0 + v 0y t + g t 2
- y = v 0x t + 1/2 g t 2
- y = y 0 + 1/2 g t 2
Ground truth: D. y = y 0 + v 0y t - 1/2 g t 2
Question: If the angle theta is changed to 30 degrees, what is the result of the first question about the total time in the air?
Options:
- 4.00 seconds
- 2.82 seconds
- 3.50 seconds
- 2.50 seconds
- 3.04 seconds
- 2.00 seconds
- 3.15 seconds
- 1.85 seconds
- 2.25 seconds
- 3.85 seconds
Ground truth: E. 3.04 seconds
Question: A rocket is shot from the top of a tower at an angle of 45° above the horizontal (Fig. 19-1). It hits the ground in 5 seconds at a horizontal distance from the foot of the tower equal to three times the height of the tower. Find the height of the tower.
Options:
- h = 100 ft
- h = 80 ft
- h = 110 ft
- h = 85 ft
- h = 90 ft
- h = 95 ft
- h = 105 ft
- h = 120 ft
- h = 75 ft
- h = 115 ft
Ground truth: A. h = 100 ft

## Video-MMMU Examples - Medicine

Question: At the beginning of the video, what are the muscles in the lower left corner, upper left corner, and lower right corner, respectively?
Options:
- Cardiac muscle, Smooth muscle, Skeletal muscle
- Skeletal muscle, Cardiac muscle, Smooth muscle
- Skeletal muscle, Smooth muscle, Cardiac muscle
- Smooth muscle, Cardiac muscle, Skeletal muscle
- Smooth muscle, Skeletal muscle, Cardiac muscle
- Smooth muscle, Cardiac muscle, Cardiac muscle
- Skeletal muscle, Skeletal muscle, Smooth muscle
- Cardiac muscle, Smooth muscle, Smooth muscle
- Skeletal muscle, Smooth muscle, Smooth muscle
- Cardiac muscle, Skeletal muscle, Smooth muscle
Ground truth: J. Cardiac muscle, Skeletal muscle, Smooth muscle
Question: Based on the video, how many of the following characteristics can be used to identify the different types of muscle tissue?
Characteristics:
- (c1). Presence of striations
- (c2). Presence of intercalated discs
- (c3). Voluntary control
- (c4). Involuntary control
- (c5). Branching appearance
- (c6). Smooth, spindle-shaped cells
- (c7). Long, cylindrical fibers
- (c8). Multinucleated cells
- (c9). Location
Options:
Ground truth: H. 7
Question: What kind of tissue does this image depict?
Options:
- Cardiac muscle
- Skeletal muscle
- Cartilage
- Smooth muscle
- Tendon
- Ligament
- Adipose tissue
- Epithelium
- Connective tissue
- Nerve tissue
Ground truth: A. Cardiac muscle

## Video-MMMU Examples - Engineering

Question: Identify the correct sequence of steps to construct the minimum spanning tree using Kruskal's algorithm from the graph described in the video.
Options:
- Add CF, add AC, add EF, add BC, add FG.
- Add BE, add EF, add CF, add BC, add FG.
- Add BE, add EF, add FG, add BC, add CD.
- Add BE, add AC, add EF, add FC, add CD.
- Add BE, add BC, add AC, add EF, add FG.
- Add BE, add AC, add DF, add BC, add CD.
- Add BE, add AC, add EF, add BC, add FG.
- Add BE, add AC, add DF, add FG, add BC.
- Add BE, add EF, add BC, add FG, add CD.
- Add BE, add AC, add FG, add EF, add BC.
Ground truth: G. Add BE, add AC, add EF, add BC, add FG.
Question: Based on the graph example in the video, if you apply Kruskal's algorithm and the weight of the first few edges changes slightly, which would be the resulting edge sequence if the edge BE now has a weight of 1 and EF a weight of 0.5?
Options:
- EF, AC, BE, BC, FG
- BE, EF, AC, FG, BC
- BE, AC, BC, EF, FG
- AC, BE, EF, BC, FG
- EF, BE, FG, AC, BC
- EF, BE, AC, BC, FG
- BE, EF, FG, BC, AC
- EF, AC, BC, BE, FG
- BE, AC, FG, EF, BC
- AC, FG, BE, EF, BC
Ground truth: F. EF, BE, AC, BC, FG
Question: Consider the following graph: Which one of the following can be a valid sequence of edges added, in that order, to a minimum spanning tree using Kruskal's algorithm?
Options:
- (a-b), (b-f), (d-f), (d-c), (d-e)
- (a-b), (d-c), (d-f), (b-f), (d-e)
- (d-f), (d-e), (a-b), (d-c), (b-f)
- (d-f), (a-b), (b-f), (d-c), (d-e)
- (a-c), (b-f), (d-f), (d-c), (d-e)
- (d-f), (d-c), (a-b), (b-f), (d-e)
- (a-c), (d-f), (b-f), (d-e), (d-c)
- (d-c), (d-f), (a-b), (b-f), (d-e)
- (d-f), (b-f), (a-b), (d-c), (d-e)
- (a-c), (d-c), (d-f), (b-f), (d-e)
Ground truth: D. (d-f), (a-b), (b-f), (d-c), (d-e)

## Citation

This website is adapted from Panda-70M , 
			and all website content is licensed under Creative Commons Attribution-NonCommercial 4.0 International License .
[LINK: Panda-70M](https://snap-research.github.io/Panda-70M/)

--------------------
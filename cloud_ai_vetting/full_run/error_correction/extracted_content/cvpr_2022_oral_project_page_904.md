# **CVPR 2022 (Oral)**] [[**Project page**
**URL:** https://vision.cs.utexas.edu/projects/poni
**Page Title:** PONI: Potential Functions for ObjectGoal Navigation with Interaction-free Learning
--------------------


## PONI: Potential Functions for ObjectGoal Navigation with Interaction-free Learning

Santhosh Kumar Ramakrishnan 1,2 Devendra Singh Chaplot 1 Ziad Al-Halah 2 Jitendra Malik 1,3 Kristen Grauman 1,2
[LINK: Santhosh Kumar Ramakrishnan](https://srama2512.github.io/)
[LINK: Devendra Singh Chaplot](https://devendrachaplot.github.io)
1 Facebook AI Research 2 UT Austin 3 UC Berkeley
CVPR 2022 (Oral)

## Abstract

State-of-the-art approaches to ObjectGoal navigation rely on reinforcement
learning and typically require significant computational resources and time 
for learning. We propose Potential functions for ObjectGoal Navigation with 
Interaction-free learning (PONI), a modular approach that disentangles the 
skills of 'where to look?' for an object and 'how to navigate to (x, y)?'. 
Our key insight is that 'where to look?' can be treated purely as a perception 
problem, and learned without environment interactions. To address this, we 
propose a network that predicts two complementary potential functions 
conditioned on a semantic map and uses them to decide where to look for an 
unseen object.  We train the potential function network using supervised 
learning on a passive dataset of top-down semantic maps, and integrate it 
into a modular framework to perform ObjectGoal navigation. Experiments on 
Gibson and Matterport3D demonstrate that our method achieves the 
state-of-the-art for ObjectGoal navigation while incurring up to 1,600x less
computational cost for training.
[PDF] [Code] [Blog]
[LINK: [Code]](https://github.com/srama2512/PONI)

## Potential Functions for ObjectNav with Interaction-free Learning

## CVPR oral talk

## Demos of ObjectNav using PONI

## Source code and pretrained models

Code to reproduce our results along with pre-trained models are available now on GitHub .
[LINK: GitHub](https://github.com/srama2512/PONI)

## Citation

## Acknowledgements

UT Austin is supported in part by the IFML NSF AI Institute, the FRL 
Cog. Sci. Consortium, and DARPA L2M. We thank Vincent Cartiller for sharing 
image segmentation models for MP3D.

--------------------
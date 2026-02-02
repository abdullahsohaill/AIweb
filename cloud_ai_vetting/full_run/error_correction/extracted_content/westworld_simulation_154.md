# “Westworld” simulation
**URL:** https://theolvs.github.io/westworld
**Page Title:** Home - Westworld documentation
--------------------


## Westworld ¶

Photo by Alexander London on Unsplash

## Description ¶

Westworld is a multi-agent simulation library, its goal to simulate and optimize systems and environments with multiple agents interacting. Its inspiration is drawn from Unity software and Unity ML Agents , adapted in Python.
[LINK: Unity ML Agents](https://github.com/Unity-Technologies/ml-agents)
The goal is to be able to simulate environments in logistics, retail, epidemiology, providing pre-coded spatial environments and communication between agents. Optimization can be included using heuristics as well as Reinforcement Learning.
Experimental
This library is extremely experimental, under active development and alpha-release
Don't expect the documentation to be up-to-date or all features to be tested
Please contact us if you have any question
The name is of course inspired by the TV series Westworld, which is actually a gigantic multi-agent simulation system.

## Quickstart ¶

Let's model an ecosystem of rabbits looking and competing for food

## Features ¶

### Current features ¶

- Easy creation of Grid and non-grid environments
- Objects (Agents, Obstacles, Collectibles, Triggers)
- Subclassing of different objects to create custom objects
- Spawner to generate objects randomly in the environment
- Basic rigid body system for all objects
- Simple agent behaviors (pathfinding, wandering, random walk, fleeing, vision range)
- Automatic maze generation
- Layer integration to convert image to obstacle and snap it to a grid
- Sample simulations and sample agents for classic simulations
- Simulation visualization, replay and export (gif or video)

### Roadmap features ¶

- More classic simulations and tutorials (boids, sugarscape)
- Better pathfinding
- Easy Reinforcement Learning integration with Stable Baselines
- Other visualization functions than PyGame for web integration

## Installation ¶

### Install from PyPi ¶

The library is available on PyPi via

### For developers ¶

- You can clone the github repo / fork and develop locally
- Poetry is used for environment management, dependencies and publishing, after clone you can run

## Contributors ¶

- Théo Alves Da Costa

## Javascript version ¶

A javascript version is being developed at https://github.com/TheoLvs/westworldjs

--------------------
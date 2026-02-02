# RVT: Robotic View Transformer
**URL:** https://robotic-view-transformer.github.io
**Page Title:** RVT: Robotic View Transformer for 3D Object Manipulation
--------------------


## RVT: Robotic View Transformer for 3D Object Manipulation

[LINK: Ankit Goyal](https://imankgoyal.github.io/)
[LINK: Code](https://github.com/nvlabs/rvt)
A single RVT model can solve multiple tasks with just ~10 demonstrations per task.
RVT is an order of magnitude more scalable and efficient than existing state-of-the-art method.

## Overview Video

## Summary

For 3D object manipulation, methods that build an explicit 3D representation perform better than those relying only on camera images. 
	 But using explicit 3D representations like voxels comes at large computing cost, adversely affecting scalability.
We propose RVT, a multi-view transformer for 3D manipulation that is both scalable and accurate. RVT takes camera images and task language description as inputs and predicts the gripper pose action.
	 In simulations, we find that a single RVT model works well across 18 RLBench tasks with 249 task variations , achieving 26% higher relative success than existing state-of-the-art method (PerAct). 
	 It also trains 36X faster than PerAct for achieving the same performance and achieves 2.3X the inference speed of PerAct. 
	 Further, RVT can perform a variety of manipulation tasks in the real world with just a few (~10) demonstrations per task.

## Experiment Results

We trained a single RVT model from real world data and a single RVT model from RLBench simulation data. In both settings, the single trained RVT model is used to evaluate the performance on all tasks.

## Real World Videos (2X Default Speed)

## Put Object in Drawer

Success : Put orange bottle in drawer
Success : Put orange bottle in drawer
Success : Put orange bottle in drawer
Failure : Put blue marker in drawer

## Put Object in Shelf

Success : Put yellow block in top shelf
Success : Put yellow block in bottom shelf
Success : Put yellow block in top shelf
Failure : Put yellow block in top shelf

## Stack Blocks

Success : Put yellow block on blue block
Success : Put blue block on red block
Success : Put red block on yellow block

## Press Sanitizer

Success : Press Sanitizer
Success : Press Sanitizer
Success : Press Sanitizer
Failure : Press Sanitizer

## Put Marker in Bowl/Mug

Failure : Put green marker in bowl
Failure : Put blue marker in bowl
Failure : Put green marker in mug

## Simulation Videos

## Put in Drawer

Success : put the item in the top drawer
Success : put the item in the bottom drawer
Success : put the item in the top drawer
Failure : put the item in the middle drawer

## Sweep to Dustpan

Success : sweep dirt to the short dustpan
Success : sweep dirt to the short dustpan
Success : sweep dirt to the tall dustpan
Failure : sweep dirt to the tall dustpan

## Meat off Grill

Success : take the steak off the grill
Success : take the steak off the grill
Success : take the steak off the grill
Failure : take the steak off the grill

## Open Drawer

Success : open the top drawer
Success : open the middle drawer
Success : open the bottom drawer
Failure : open the top drawer

## Turn Tap

Success : turn right tap
Success : turn left tap
Success : turn left tap
Success : turn right tap

## Close Jar

Success : close the cyan jar
Success : close the orange jar
Success : close the navy jar
Failure : close the red jar

## Drag Stick

Success : use the stick to drag the cube onto the navy target
Success : use the stick to drag the cube onto the gray target
Success : use the stick to drag the cube onto the red target
Success : use the stick to drag the cube onto the silver target

## Stack Blocks

Success : stack 3 teal blocks
Success : stack 3 gray blocks
Success : stack 4 navy blocks
Failure : stack 2 maroon blocks

## Screw Bulb

Success : screw in the rose light bulb
Success : screw in the gray light bulb
Success : screw in the violet light bulb
Failure : screw in the silver light bulb

## Slide Block

Success : slide the block to pink target
Success : slide the block to yellow target
Success : slide the block to green target
Failure : slide the block to pink target

## Put in Safe

Success : put the money away in the safe on the top shelf
Success : put the money away in the safe on the bottom shelf
Success : put the money away in the safe on the middle shelf
Failure : put the money away in the safe on the top shelf

## Place Wine

Success : stack the wine bottle to the left of the rack
Success : stack the wine bottle to the middle of the rack
Success : stack the wine bottle to the right of the rack
Failure : stack the wine bottle to the middle of the rack

## Put in Cupboard

Success : put the coffee in the cupboard
Success : put the mustard in the cupboard
Success : put the chocolate jello in the cupboard
Failure : put the coffee in the cupboard

## Sort Shape

Success : put the cylinder in the shape sorter
Success : put the star in the shape sorter
Success : put the moon in the shape sorter
Failure : put the star in the shape sorter

## Push Buttons

Success : push the maroon button, then push the green button, then push the navy button
Success : push the maroon button
Success : push the maroon button
Failure : push the maroon button

## Insert Peg

Success : put the ring on the violet spoke
Success : put the ring on the black spoke
Failure : put the ring on the green spoke
Failure : put the ring on the azure spoke

## Stack Cups

Success : stack the other cups on top of the lime cup
Success : stack the other cups on top of the gray cup
Success : stack the other cups on top of the red cup
Failure : stack the other cups on top of the maroon cup

## Place Cups

Failure : place 3 cups on the cup holder
Failure : place 2 cups on the cup holder
Failure : place 2 cups on the cup holder

## BibTeX


--------------------
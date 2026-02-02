# they made a jacket
**URL:** https://www.cs.umd.edu/~tomg/projects/invisible
**Page Title:** Invisibility cloak
--------------------


## Invisibility cloak

### Overview

This paper studies the art and science of creating adversarial attacks on object detectors.  Most work on real-world adversarial attacks has focused on classifiers , which assign a holistic label to an entire image, rather than detectors which localize objects within an image.  Detectors work by considering thousands of “priors” (potential bounding boxes) within the image with different locations, sizes, and aspect ratios.  To fool an object detector, an adversarial example must fool every prior in the image, which is much more difficult than fooling the single output of a classifier.
In this work, we present a systematic study of adversarial attacks on state-of-the-art object detection frameworks.  Using standard detection datasets, we train patterns that suppress the objectness scores produced by a range of commonly used detectors, and ensembles of detectors. Our ultimate goal is to build a wearable “invisibility” cloak that renders the wearer imperceptible to detectors.
Making an Invisibility Cloak: Real World Adversarial Attacks on Object Detectors

### Video Demo

While a full-scale demo had been delayed due to COVID, here’s a short composite
of some of our test footage.

### Approach

We load images from the COCO detection dataset, and pass them
through a detector.  When a person is detected, and pattern is rendered over that person with random
perspective, brightness, and contrast deformations.  A gradient descent algorithm is then used to
find the pattern that minimizes the “objectness scores” (confidence in the presence of an object)
for every object prior.

### Gallery

### Thanks

Thanks to Facebook AI for their support on this project!

### Search

### Categories

- adversarial-learning (5)
- audio (1)
- image-processing (1)
- machine-learning (13)
- medical-imaging (1)
- optimization (8)
- recurrance (1)
- thinking (1)

--------------------
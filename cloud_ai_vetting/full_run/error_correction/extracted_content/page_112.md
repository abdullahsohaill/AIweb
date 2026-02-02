# [page]
**URL:** https://scene-verse.github.io
**Page Title:** SceneVerse
--------------------


## SceneVerse: Scaling 3D Vision-Language Learning for Grounded Scene Understanding

[LINK: Baoxiong Jia](https://buzz-beater.github.io/)
[LINK: Yixin Chen](https://yixchen.github.io/)
[LINK: Yan Wang](https://github.com/jetpackfirstme)
[LINK: Xuesong Niu](https://nxsedson.github.io/)
[LINK: Qing Li](https://liqing-ustc.github.io/)
✶ indicates equal contribution
[LINK: Code](https://github.com/scene-verse/sceneverse)
TL;DR We propose SceneVerse, the first million-scale 3D vision-language dataset
        with 68K 3D indoor scenes and 2.5M vision-language pairs. 
        We demonstrate the scaling effect by (i) achieving state-of-the-art on all existing 3D visual grounding benchmarks and (ii) showcasing zero-shot transfer capabilities
        with our GPS (Grounded Pre-training for Scenes) model.

## Abstract

3D vision-language grounding, which focuses on aligning language with the 3D physical environment, stands as a cornerstone in the development of embodied agents.
              In comparison to recent advancements in the 2D domain, grounding language in 3D scenes faces several significant challenges: 
              (i) the inherent complexity of 3D scenes due to the diverse object configurations, their rich attributes, and intricate relationships; 
              (ii) the scarcity of paired 3D vision-language data to support grounded learning; and (iii) the absence of a unified learning framework to distill knowledge from grounded 3D data. 
              In this work, we aim to address these three major challenges in 3D vision-language by examining the potential of systematically upscaling 3D vision-language learning in indoor environments. 
              We introduce the first million-scale 3D vision-language dataset, SceneVerse , 
              encompassing about 68K 3D indoor scenes and comprising 2.5M vision-language pairs derived from both human annotations and our scalable scene-graph-based generation approach. 
              We demonstrate that this scaling allows for a unified pre-training framework, Grounded Pre-training for Scenes (GPS), for 3D vision-language learning. 
              Through extensive experiments, we showcase the effectiveness of GPS by achieving state-of-the-art performance on all existing 3D visual grounding benchmarks. 
              The vast potential of SceneVerse and GPS is unveiled through zero-shot transfer experiments in the challenging 3D vision-language tasks.

## Data

SceneVerse contains 3D scenes curated from diverse existing datasets of both real and synthetic environments.
              Harnessing the power of 3D scene graphs and LLMs, we introduce an automated pipeline to generate comprehensive and high-quality language for both object-level
              and scene-level descriptions. We additionally incorporate the most extensive human-annotated object referrals to date, providing new training sources and benchmarks in this field.

## ARKitScene Examples

## ScanNet Examples

## MultiScan Examples

## 3RScan Examples

## Model

Grounded Pre-training for Scenes (GPS) is a transformer-based model trained with multi-level contrastive losses for aligning 3D scenes and texts.
            We echo the language descriptions collected to form scene-language pairs at both object-level, referral-object-level, and scene-level for contrastive objectives in GPS.
            The resulting model shows scaling effect in pre-train/fine-tune and zero-shot settings.

## Data Explorer

To use the interactive data explorer, first select from the available scenes in the select bar and then choose a type of language description
            available in the buttons. Click the "Scene Caption" button for scene captions. To visualize other types, check the corresponding box and double click an object in the scene for visualizing
            the results. All available objects could be found according to the segmentation visualization. Best viewed on monitors. Control : Click + Drag = Rotate Ctrl + Drag = Translate Scroll Up/Down = Zoom In/Out Double Click = Select Object

## BibTeX


--------------------
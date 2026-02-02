# TAO-Amodal
**URL:** https://tao-amodal.github.io
**Page Title:** TAO-Amodal: A Benchmark for Tracking Any Object Amodally
--------------------


## TAO-Amodal: A Benchmark for Tracking Any Object Amodally

[LINK: Cheng-Yen (Wesley) Hsieh](https://WesleyHsieh0806.github.io/)
[LINK: Code](https://github.com/WesleyHsieh0806/TAO-Amodal)
TAO-Amodal dataset features diverse (880 categories) annotations for both Traditional tracking (top) and Amodal tracking (bottom) .

## Abstract

Amodal perception, the ability to comprehend complete object structures from partial visibility, is a
              fundamental skill, even for infants. Its significance extends to applications like autonomous driving,
              where a clear understanding of heavily occluded objects is essential.
              However, modern detection and tracking algorithms often overlook this critical capability,
              perhaps due to the prevalence of modal annotations in most benchmarks.
              To address the scarcity of amodal benchmarks, we introduce TAO-Amodal,
              featuring 833 diverse categories in thousands of video sequences.
              Our dataset includes amodal and modal bounding boxes for visible and partially or fully occluded
              objects,
              including those that are partially out of the camera frame.
              We investigate the current lay of the land in both amodal tracking and detection by benchmarking
              state-of-the-art modal trackers and amodal segmentation methods.
              We find that existing methods, even when adapted for amodal tracking, struggle to detect and track objects
              under heavy occlusion.
              To mitigate this, we explore simple finetuning schemes that can increase the amodal tracking and detection
              metrics of occluded objects by 2.1% and 3.3% .

## Traditional vs. Amodal Tracking

Traditional perception (top) concentrates on identifying
              visible segments. Consequently, they face peculiar outputs such as vanishing bounding boxes or tiny box
              sizes under occlusion scenarios. Amodal
                perception (bottom) advances beyond conventional approaches by inferring complete object
              boundaries, even
              when
              certain portions are occluded.

## TAO-Amodal Dataset

Our dataset augments the TAO dataset with amodal bounding box
              annotations for fully
              invisible, out-of-frame, and occluded objects across 880 categories. Note that this implies TAO-Amodal
              also
              includes modal
              segmentation masks.

## Amodal Expander

Our Amodal Expander serves as a plug-in module that can ``amodalize" any existing detector or tracker
                with limited (amodal) training data. Here we provide qualitative results of both modal (top) and amodal
                (bottom) predictions from amodal expander.

## Acknowledgements

[LINK: BURST](https://github.com/Ali2500/BURST-benchmark)

## BibTeX


--------------------
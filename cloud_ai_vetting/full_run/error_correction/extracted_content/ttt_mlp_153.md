# TTT-MLP
**URL:** https://test-time-training.github.io/video-dit
**Page Title:** One-Minute Video Generation with Test-Time Training
--------------------


## One-Minute Demo Videos

Click any video to see the text prompt used to generate it.

## Abstract

Transformers today still struggle to generate one-minute videos because self-attention layers are inefficient
          for long context.
          Alternatives such as Mamba layers struggle with complex multi-scene stories because their hidden states are
          less expressive.
          We experiment with Test-Time Training (TTT) layers, whose hidden states themselves can be neural networks,
          therefore more expressive.
          Adding TTT layers into a pre-trained Transformer enables it to generate one-minute videos from text
          storyboards.
          For proof of concept, we curate a dataset based on Tom and Jerry cartoons.
          Compared to baselines such as Mamba 2, Gated DeltaNet, and sliding-window attention layers, TTT layers
          generate much more coherent videos that tell complex stories, leading by 34 Elo points in a human evaluation
          of 100 videos per method.
          Although promising, results still contain artifacts, likely due to the limited capability of the pre-trained
          5B model.
          The efficiency of our implementation can also be improved.
          We have only experimented with one-minute videos due to resource constraints, but the approach can be extended
          to longer videos and more complex stories.
[LINK: Code](https://github.com/test-time-training/ttt-video-dit)

## Adding TTT Layers to a Pre-Trained Transformer

Adding TTT layers into a pre-trained Transformer enables it to generate one-minute videos with strong
          temporal consistency and motion smoothness.
Local Attention struggles with consistency in Tom's color, Jerry's mousehole, and distorts Tom's body.
TTT-MLP demonstrates strong character and temporal consistency across the entire duration of the video.

## Baseline Comparisons

TTT-MLP outperforms all other baselines in temporal consistency, motion smoothness, and overall aesthetics, as
          measured by human evaluation Elo scores.
TTT-MLP preserves temporal consistency over scene changes and across angles.
TTT-MLP preserves temporal consistency over scene changes, producing smooth actions.
Gated DeltaNet lacks temporal consistency across different angles of Tom.
Sliding-window attention alters the kitchen environment and duplicates Jerry stealing the pie.

## Limitations

The generated one-minute videos demonstrate clear potential as a proof of concept, but still contain notable
          artifacts.
Temporal consistency: The boxes morph between 3-second segments of the same scene.
Motion naturalness: The cheese hovers in mid-air rather than falling naturally to the ground.
Aesthetics: The lighting in the kitchen becomes dramatically brighter as Tom turns around.

## Acknowledgements

We thank Hyperbolic Labs for compute support, Yuntian Deng for help with running experiments, and Aaryan
          Singhal, Arjun Vikram, and Ben Spector for help with systems questions.
          Yue Zhao would like to thank Philipp Krähenbühl for discussion and feedback.
          Yu Sun would like to thank his PhD advisor Alyosha Efros for the insightful advice of looking at the pixels
          when working on machine learning.
[LINK: Yue
                  Zhao †5](https://zhaoyue-zephyrus.github.io)
[LINK: Tatsunori
                  Hashimoto 2](https://thashim.github.io)
[LINK: Yu
                  Sun 1,2](https://yueatsprograms.github.io)
[LINK: Xiaolong
                  Wang 1,3](https://xiaolonw.github.io)
[LINK: Code](https://github.com/test-time-training/ttt-video-dit)

--------------------
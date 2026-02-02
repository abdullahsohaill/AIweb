# Project
**URL:** https://sadilkhan.github.io/text2cad-project
**Page Title:** NeurIPS 2024 (Spotlight) - Text2CAD
--------------------

- Contribution
- Data Annotation
- Text2CAD Transformer
- Visual Results
- Quantitative Results
Text2CAD: Designers can efficiently generate parametric CAD models from text
            prompts. The prompts can vary from abstract shape descriptions to detailed parametric instructions.

## Contribution

Our proposed Text2CAD is the first AI framework for generating parametric CAD designs using multi-level textual descriptions . Our main contributions are:
- A Novel Data Annotation Pipeline that leverages open-source
                        LLMs and VLMs to annotate DeepCAD dataset with
                        text prompts containing varying level of complexities and parametric details.
- Text2CAD Transformer: An end-to-end Transformer based
                        autoregressive architecture for generating CAD design history from input text prompts.

## Data Annotation

Our data annotation pipeline generates multi-level text prompts describing the construction workflow of a
                CAD model with varying complexities. We use a two-stage method -
- Stage 1 : Shape description generation using VLM ( LlaVA-NeXT ).
[LINK: LlaVA-NeXT](https://llava-vl.github.io/blog/2024-01-30-llava-next/)
- Stage 2 : Multi-Level textual annotation generation using LLM ( Mixtral-50B ).

## Text2CAD Transformer

Text2CAD Transformer converts natural
                language descriptions into parametric 3D CAD models by deducing all its intermediate design steps
                autoregres-
                sively. Our model takes as input a text prompt T and a CAD subsequence C 1 : t − 1 of
                length t − 1 . The text embedding T a d a p t is extracted from T using a pretrained BeRT
                Encoder followed by a trainable Adaptive layer. The resulting embedding T a d a p t and the CAD
                sequence embedding F t − 1 0 is passed through L decoder blocks to generate the full
                CAD sequence in auto-regressive way.

## Visual Results

Visual examples of 3D CAD model generation using varied prompts.
                        ( 1 ) Three different prompts yielding the same
                        ring-like model, some without explicitly mentioning ’ ring ’.
                        ( 2 ) Three diverse prompts resulting in same star-shaped
                            model , each emphasizing different star characteristics .
Qualitative results of the reconstructed CAD models of DeepCAD and Text2CAD
                        on DeepCAD dataset. From top to bottom - Input
                            Texts, Reconstructed CAD models using DeepCAD and Text2CAD respectively and GPT-4V
                            Evaluation.
Qualitative results of the reconstructed CAD models of DeepCAD and Text2CAD
                        on DeepCAD dataset. From top to bottom - Input
                            Texts, Reconstructed CAD models using DeepCAD and Text2CAD respectively and GPT-4V
                            Evaluation.
Visual examples of 3D CAD model generation using varied prompts.
                        ( 1 ) Three different prompts yielding the same
                        ring-like model, some without explicitly mentioning ’ ring ’.
                        ( 2 ) Three diverse prompts resulting in same star-shaped
                            model , each emphasizing different star characteristics .
Qualitative results of the reconstructed CAD models of DeepCAD and Text2CAD
                        on DeepCAD dataset. From top to bottom - Input
                            Texts, Reconstructed CAD models using DeepCAD and Text2CAD respectively and GPT-4V
                            Evaluation.

## Quantitative Results

We evaluated the performance of Text2CAD using two strategies.
- CAD Sequence Evaluation: We assess the parametric correspondence between the generated CAD
                    sequences with the input texts. This is done using the following metrics: F1 Scores of Line, Arc, Circle and Extrusion using the
                            method proposed in CAD-SIGNet . Chamfer Distance (CD) measures geometric alignment
                            between the ground truth and reconstructed CAD models of Text2CAD and DeepCAD . Invality Ratio (IR) Measures the invalidity of the
                            reconstructed CAD models.
- F1 Scores of Line, Arc, Circle and Extrusion using the
                            method proposed in CAD-SIGNet .
[LINK: CAD-SIGNet](http://skazizali.com/cadsignet.github.io/)
- Chamfer Distance (CD) measures geometric alignment
                            between the ground truth and reconstructed CAD models of Text2CAD and DeepCAD .
- Invality Ratio (IR) Measures the invalidity of the
                            reconstructed CAD models.
- Visual Inspection: We compare the performance of Text2CAD and DeepCAD with GPT-4 and Human evaluation.

## Acknowledgement

This work was in parts supported by the EU Horizon Europe Framework under grant agreement 101135724 (LUMINOUS).

## Citation

If you use our dataset, please cite our works.

--------------------
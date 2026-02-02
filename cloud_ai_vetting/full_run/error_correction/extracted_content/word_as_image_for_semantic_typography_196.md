# Word-As-Image for Semantic Typography
**URL:** https://wordasimage.github.io/Word-As-Image-Page
**Page Title:** Word-As-Image for Semantic Typography
--------------------


## Word-As-Image for Semantic Typography

[LINK: Shir Iluz](https://shiriluz.github.io/)
[LINK: Yael Vinker](https://yael-vinker.github.io/website/index.html)
[LINK: Amir Hertz](https://amirhertz.github.io/)
[LINK: Code](https://github.com/WordAsImage/Word-As-Image)

## A few examples of our W ord- A s- I mage illustrations in various fonts and for
                different textual concept. The semantically adjusted letters are created completely automatically using our method, and can then be used for further creative design as we
                illustrate here.

## Abstract

A word-as-image is a semantic typography technique where a word illustration presents a visualization
                of the meaning of the word, while also preserving its readability.
                We present a method to create word-as-image illustrations automatically. This task is highly challenging
                as it requires semantic understanding of the word and a creative idea of where and how to depict these
                semantics in a visually pleasing and legible manner.
                We rely on the remarkable ability of recent large pretrained language-vision models to distill textual
                concepts visually.
                We target simple, concise, black-and-white designs that convey the semantics clearly. We deliberately do
                not change the color or texture of the letters and do not use embellishments.
                Our method optimizes the outline of each letter to convey the desired concept, guided by a pretrained
                Stable Diffusion model.
                We incorporate additional loss terms to ensure the legibility of the text and the preservation of the
                style of the font.
                We show high quality and engaging results on numerous examples and compare to alternative techniques

## Our method can handle a large variety of semantic concepts and use any font, while preserving the legibility of the text and the font’s style. Note how styles of different fonts are preserved by the semantic modification:

## How does it work?

Our word-as-image illustrations concentrate on changing only the geometry of the letters to
                convey the meaning.
                We deliberately do not change color or texture and do not use embellishments.
                This allows simple, concise, black-and-white designs that convey the semantics clearly.

                We rely on the prior of a pretrained Stable Diffusion model to connect between text and images, and utilize
                the Score Distillation Sampling approach to encourage the appearance of the letter to reflect the
                provided textual concept.

                Given an input word, our method is applied separately for each letter.

                We represent each letter as a closed vectorized shape.
Given an input letter represented by a set of control points 𝑃, and a concept (shown in purple),
            our goal is to optimize its parameters to reflect the meaning of the word, while still preserving its original style and design.

            we optimize the new positions 𝑃ˆ of the deformed letter iteratively. At each iteration, we use a differentiable rasterizer (DiffVG marked in blue) that allows to backpropagate gradients from a raster-based loss to
            the shape’s parameters.
            We then augmented the rasterized deformed letter and passed into a pretrained frozen Stable
            Diffusion model, that drives the letter shape to convey the semantic concept using the Lsds loss (1).
            To preserve the shape of the original letter and ensure legibility
            of the word, we utilize two additional loss functions. The first loss
            preserves the local tone and structure of the
            letter by comparing the low-pass filter (LPF marked in yellow) of the resulting rasterized
            letter to the original one to compute L𝑡𝑜𝑛𝑒 (2).
            The second loss regulates the shape modification by constraining the deformation
            to be as-conformal-as-possible over a triangulation of the letter’s
            shape (D marked in green), defining L𝑎𝑐𝑎𝑝 (3).

## The same word in a variety of fonts.

## Additional Editing

## Word-as-image applied on Chinese characters. In Chinese, a whole word can be represented by one character.
        Here we show from left: bird, rabbit, cat and surfing (two last characters
        together).

## Utilizing Depth-to-image in Stable Diffusion 2 as a post-processing step for our model's results to incorporate color and texture .

## Results


--------------------
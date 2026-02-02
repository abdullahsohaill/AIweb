# [code
**URL:** https://videogamebunny.github.io
**Page Title:** VideoGameBunny: Towards vision assistants for video games
--------------------


## VideoGameBunny : Towards vision assistants for
                        video games

by Mohammad Reza Taesiri , & Cor-Paul Bezemer
We introduce VideoGameBunny , a LLaVA-style model
                        designed specifically
                        for understanding video game images. We present a comprehensive dataset of game images and
                        instruction pairs, demonstrating that our model can outperform larger state-of-the-art models in
                        game-related tasks, paving the way for
                        advanced AI assistants in video game understanding, playing, commentary, and debugging.
WACV 2025

## Abstract

Large multimodal models (LMMs) hold substantial promise across various domains, from personal assistance in
            daily
            tasks to sophisticated applications like medical diagnostics. However, their capabilities have limitations
            in the
            video game domain, such as challenges with scene understanding, hallucinations, and inaccurate descriptions
            of video
            game content, especially in open-source models. This paper describes the development of VideoGameBunny , a LLaVA-style model based on Bunny, specifically tailored
            for
            understanding images from video games. We release intermediate checkpoints, training logs, and an extensive
            dataset
            comprising 185,259 video game images from 413 titles, along with 389,565 image-instruction pairs that
            include image
            captions, question-answer pairs, and a JSON representation of 16 elements of 136,974 images. Our experiments
            show
            that our high quality game-related data has the potential to make a relatively small model outperform the
            much
            larger state-of-the-art model LLaVa-1.6-34b (which has more than 4x the number of parameters). Our study
            paves the
            way for future research in video game understanding on tasks such as playing, commentary, and debugging.

## VideoGameBunny Model Architecture

VideoGameBunny is based on Bunny , an efficient and lightweight large multimodal
            language model.
[LINK: Bunny](https://github.com/BAAI-DCAI/Bunny)

## Dataset

We collect a diverse dataset of 185,259 high-resolution images from 413 video games sourced from YouTube
            videos to
            address the lack of game-specific instruction-following data. We generate various types of instructions for
            these images
            using different large multimodal models: short captions, long captions, image-to-JSON conversions, and
            image-based
            question-answering pairs. The image-to-JSON format provides structured, detailed descriptions of game
            elements, while
            the question-answering data is generated using both text-based models (LLama-3) and image-based models
            (GPT-4o), where
            we feed an image to a model and ask a question about its contents. This comprehensive dataset aims to
            improve the
            ability of open-source models to understand and respond to video game content.
We also use Gemini-1.5-Pro to create an evaluation set of 3,375 samples containig multiple choice
            questions about the images in 10 different categories.
Categories of questions in our dataset, along with a sample question for each category.
Our dataset contains 389,565 image-instruction pairs that include image captions, question-answer pairs,
                and a JSON representation of 16 elements of 136,974 images.
Note: Click on the circles in the image to view detailed annotations.

## Model Training and Results

We instruction tune Bunny using image-instruction pairs that contain image captions, image-based
            question
            answering, and
            image-to-JSON conversion.

## Which type of data has the potential to improve the model’s performance?

We investigate which type of data has the potential to improve the model's performance. To do this, we
            fine-tune the
            Bunny model using a single dataset at a time, varying the subset size from 2K to 60K samples. We
            perform this
            fine-tuning only once for each dataset and subset size combination. Our goal is to observe overall
            performance trends
            rather than optimizing for the best performance. We continue increasing the subset size until we observe a
            sharp decline
            in performance, at which point we stop the experiment for that particular dataset. This approach allows us
            to
            efficiently explore the impact of different data types on the model's performance and identify which
            datasets are most
            promising for further investigation.
Relative performance improvement (pp) of Bunny fine-tuned on different subsets of each
                dataset. The image-to-JSON
                dataset shows a strong positive trend, while the short captions dataset degrades performance.

## Which type of data has the potential to improve the model's performance?

We explore different data mixing strategies to determine which approach improves the model's performance the
            most. We
            evaluate four strategies: Random, Equal, Stratified, and Weighted. The Random strategy involves sampling
            without
            replacement from all datasets combined. The Equal strategy selects an equal number of samples from each
            dataset. The
            Stratified approach mixes datasets based on video games to ensure a balanced representation of different
            games. The
            Weighted strategy prioritizes the three most effective datasets identified in our previous experiment:
            image-based
            question-answering (GPT-4o), long captions, and image-to-JSON.
            We fine-tune the Bunny model on these mixture
            strategies
            with dataset sizes ranging from 2K to 30K samples. Each experiment is repeated three times with
            different samples
            to report mean performance and standard deviation. We stop at 30K samples due to limitations in our
            smallest dataset
            (GPT-4o with 10K samples), which would be exhausted for the Equal and Weighted strategies at this point.
Performance of models fine-tuned on a mixture of data with various strategies. The Weighted
            strategy leads
            to better performance with smaller dataset sizes, but as the size increases, both Equal and Weighted
            strategies
            perform similarly.
Looking at the average improvement per category reveals that most improvements come from game-related
            categories
            (Anomalies and Glitches, and HUD and UI).
Average improvement for different sizes for each category

## How does VideoGameBunny perform compared to SOTA open-source models on
            game understanding tasks?

We assess the effectiveness of fine-tuning a smaller model on game-specific data by comparing our method to
            state-of-the-art open-source models. To do this, we fine-tune our model on a dataset of 50K
            image-instruction samples
            compiled from all previously introduced datasets. We then evaluate our model's performance against
            LLaVA-1.6, a
            state-of-the-art open-source model with 4.2 times more parameters. This comparison allows us to determine
            how well our
            approach of fine-tuning a smaller model on game-specific data performs compared to larger, more general
            models on game
            understanding tasks.
Performance of various models on the evaluation set (%).
Question: Are there any visible
                                glitches
                                or errors in the
                                game
                                environment?
VideoGameBunny: (D) No, there
                            are no apparent glitches. ✓
Bunny: (B) Yes, the glowing orb is
                            clipping through the
                            counter. ✗
LLaVA-1.6-34B: (C) Yes, the 'Additional
                            Download' progress bar
                            seems
                            stuck. ✗
Question: Based on the score and time
                                remaining, which team is
                                likely to win the match?
VideoGameBunny: (B) The blue
                            team is likely to win ✓
Bunny: (C) The red team is likely to
                            win. ✗
LLaVA-1.6-34B: (C) The red team is likely to
                            win. ✗

### JSON Representation

### JSON Representation

### JSON Representation

### JSON Representation

### JSON Representation

### JSON Representation

## Conclusion

We introduce a new instruction-following dataset, with 389,565 image-instruction pairs, specifically
            designed for video
            game understanding. We investigate the effectiveness of fine-tuning LMMs on different instruction-following
            dataset
            types and mixtures of them, and finally introduce VideoGameBunny , an
            8B parameter model that outperforms a SOTA
            model,
            LLaVA-1.6-34B, on a game-related question answering benchmark.

--------------------
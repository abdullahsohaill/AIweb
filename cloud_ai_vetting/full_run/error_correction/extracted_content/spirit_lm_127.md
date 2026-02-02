# Spirit LM
**URL:** https://speechbot.github.io/spiritlm
**Page Title:** 
--------------------


## 🔥Spirit LM

### Interleaved Spoken and Written Language Model

[LINK: Code](https://github.com/facebookresearch/spiritlm)
In Transactions of the Association for Computational Linguistics
Tu Anh Nguyen a,1,2 , Benjamin Muller a,1 , Bokai Yu a,1 , Marta R. Costa-jussa b,1 , Maha Elbayad b,1 , Sravya Popuri b,1 , Christophe Ropers b,1 Paul-Ambroise Duquenne b,1 , Robin Algayres b,3 , Ruslan Mavlyutov b,1 , Itai Gat b,1 , Mary Williamson b,1 Gabriel Synnaeve c,1 , Juan Pino c,1 , Benoît Sagot c,2 , Emmanuel Dupoux c,1,3
1 Meta AI, 2 Inria, Paris, 3 EHESS, ENS-PSL, CNRS, Paris
{ntuanh, benjaminmuller, bokai, dpx}@meta.com
a,b,c Equally contributed as co-first, co-second and co-last authors, resp.
We introduce Spirit LM , a foundation multimodal language model
            that freely mixes text and speech. Our model is based on a 7B pretrained text language
            model that we extend to the speech modality by continuously training it on text and
            speech units. Speech and text sequences are concatenated as a single stream of tokens,
            and trained with a word-level interleaving method using a small automatically-curated
            speech-text parallel corpus. Spirit LM comes in two versions:
            a Base version that uses speech phonetic units (HuBERT) and an Expressive version that models expressivity using pitch and
            style units in addition to the phonetic units. For both versions, the text is encoded
            with subword BPE tokens. The resulting model displays both the semantic abilities of
            text models and the expressive abilities of speech models. Additionally, we demonstrate
            that Spirit LM can learn new tasks in a few-shot fashion across
            modalities (i.e. ASR, TTS, Speech Classification).

## Spirit LM Model Overview

## Generation samples from Spirit LM Base

We prompt the model with either Text or Speech, and generate with either the same or different modality.

            We give the model with a tag [Text] or [Speech] to signal a change of modality.
            The (cherry picked) samples illustrate the capacity
        of the model to continue a prompt in a semantically coherent
        fashion across modalities.
f g h i j k l m n o p q r s t u v w x y z
the northwest corner of Wyoming. It is located in the Greater Yellowstone area and is one of the most popular National Parks in the States. It is visited by over three million people each year. Yellowstone was established as the first national park in the United States on March 1st, 1872 the lake is sometimes referred to as the largest high-elevation lake in the world. It is the largest alkaline lake in the world and the second-largest freshwater lake in the United States after Lake Michigan.

## Generation samples from Spirit LM Expressive

We prompt the model with an expressive prompt in either
        Text or Speech modality. For Speech prompt, we use the same
        prompt content with different speaking styles to express the
        emotion. The (cherry-picked) examples show that Spirit LM Expressive is able to transfer
        the expressive style of the prompt onto the continuation
        within or across a change in modality.

--------------------
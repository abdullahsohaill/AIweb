# AudioCraft
**URL:** https://audiocraft.metademolab.com
**Page Title:** Home
--------------------

- Home
- MusicGen
- AudioGen
- EnCodec
- Home
- MusicGen
- AudioGen
- EnCodec

## AudioCraft: AI research for audio

[LINK: Go to the code](https://github.com/facebookresearch/audiocraft)

## Model overview

With AudioCraft, we simplify the overall design of generative models for audio compared to prior work.
Both MusicGen and AudioGen consist of a single autoregressive Language Model (LM) that operates over streams of compressed discrete music representation, i.e., tokens. We introduce a simple approach to leverage the internal structure of the parallel streams of tokens and show that, with a single model and elegant token interleaving pattern, our approach efficiently models audio sequences, simultaneously capturing the long-term dependencies in the audio and allowing us to generate high-quality audio.
Our models leverage the EnCodec neural audio codec to learn the discrete audio tokens from the raw waveform. EnCodec maps the audio signal to one or several parallel streams of discrete tokens. We then use a single autoregressive language model to recursively model the audio tokens from EnCodec. The generated tokens are then fed to EnCodec decoder to map them back to the audio space and obtain the output waveform. Finally, different types of conditioning models can be used to control the generation such as using a pretrained text encoder for text-to-audio applications.

## Audio generation tasks overview

### Text-to-sound generation

AudioGen is focused on text-to-sound generation and learned to produce audio from environmental sounds.

### Text-to-music generation

MusicGen produces diverse and long music samples from user provided text inputs.

## Explore more on AudioCraft

[LINK: Code](https://github.com/facebookresearch/audiocraft)
[LINK: Model cards](https://github.com/facebookresearch/audiocraft/tree/main/model_cards)

--------------------
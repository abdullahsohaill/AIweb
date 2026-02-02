# VOICES.md
**URL:** https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md
**Page Title:** VOICES.md · hexgrad/Kokoro-82M at main
--------------------


## Voices

- 🇺🇸 American English : 11F 9M
- 🇬🇧 British English : 4F 4M
- 🇯🇵 Japanese : 4F 1M
- 🇨🇳 Mandarin Chinese : 4F 4M
- 🇪🇸 Spanish : 1F 2M
- 🇫🇷 French : 1F
- 🇮🇳 Hindi : 2F 2M
- 🇮🇹 Italian : 1F 1M
- 🇧🇷 Brazilian Portuguese : 1F 2M
For each voice, the given grades are intended to be estimates of the quality and quantity of its associated training data, both of which impact overall inference quality.
Subjectively, voices will sound better or worse to different people.
Support for non-English languages may be absent or thin due to weak G2P and/or lack of training data. Some languages are only represented by a small handful or even just one voice (French).
Most voices perform best on a "goldilocks range" of 100-200 tokens out of ~500 possible. Voices may perform worse at the extremes:
- Weakness on short utterances, especially less than 10-20 tokens. Root cause could be lack of short-utterance training data and/or model architecture. One possible inference mitigation is to bundle shorter utterances together.
- Rushing on long utterances, especially over 400 tokens. You can chunk down to shorter utterances or adjust the speed parameter to mitigate this.
Target Quality
- How high quality is the reference voice? This grade may be impacted by audio quality, artifacts, compression, & sample rate.
- How well do the text labels match the audio? Text/audio misalignment (e.g. from hallucinations) will lower this grade.
Training Duration
- How much audio was seen during training? Smaller durations result in a lower overall grade.
- 10 hours <= HH hours < 100 hours
- 1 hour <= H hours < 10 hours
- 10 minutes <= MM minutes < 100 minutes
- 1 minute <= M minutes 🤏 < 10 minutes

### American English

- lang_code='a' in misaki[en]
[LINK: misaki[en]](https://github.com/hexgrad/misaki)
- espeak-ng en-us fallback

### British English

- lang_code='b' in misaki[en]
[LINK: misaki[en]](https://github.com/hexgrad/misaki)
- espeak-ng en-gb fallback

### Japanese

- lang_code='j' in misaki[ja]
[LINK: misaki[ja]](https://github.com/hexgrad/misaki)
- Total Japanese training data: H hours
[LINK: gongitsune](https://github.com/koniwa/koniwa/blob/master/source/tnc/tnc__gongitsune.txt)
[LINK: nezuminoyomeiri](https://github.com/koniwa/koniwa/blob/master/source/tnc/tnc__nezuminoyomeiri.txt)
[LINK: tebukurowokaini](https://github.com/koniwa/koniwa/blob/master/source/tnc/tnc__tebukurowokaini.txt)
[LINK: kumonoito](https://github.com/koniwa/koniwa/blob/master/source/tnc/tnc__kumonoito.txt)

### Mandarin Chinese

- lang_code='z' in misaki[zh]
[LINK: misaki[zh]](https://github.com/hexgrad/misaki)
- Total Mandarin Chinese training data: H hours

### Spanish

- lang_code='e' in misaki[en]
[LINK: misaki[en]](https://github.com/hexgrad/misaki)
- espeak-ng es

### French

- lang_code='f' in misaki[en]
[LINK: misaki[en]](https://github.com/hexgrad/misaki)
- espeak-ng fr-fr
- Total French training data: <11 hours

### Hindi

- lang_code='h' in misaki[en]
[LINK: misaki[en]](https://github.com/hexgrad/misaki)
- espeak-ng hi
- Total Hindi training data: H hours

### Italian

- lang_code='i' in misaki[en]
[LINK: misaki[en]](https://github.com/hexgrad/misaki)
- espeak-ng it
- Total Italian training data: H hours

### Brazilian Portuguese

- lang_code='p' in misaki[en]
[LINK: misaki[en]](https://github.com/hexgrad/misaki)
- espeak-ng pt-br

--------------------
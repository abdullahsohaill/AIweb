# Kokoro-82M TTS
**URL:** https://huggingface.co/spaces/Remsky/Kokoro-TTS-Zero
**Page Title:** Kokoro TTS Zero - a Hugging Face Space by Remsky
--------------------


## runtime error

## Exit code: 1. Reason: Traceback (most recent call last):
  File "/home/user/app/app.py", line 12, in <module>
    from tts_factory import TTSFactory
  File "/home/user/app/tts_factory.py", line 2, in <module>
    from tts_model_v1 import TTSModelV1
  File "/home/user/app/tts_model_v1.py", line 6, in <module>
    from kokoro import KPipeline
  File "/usr/local/lib/python3.10/site-packages/kokoro/__init__.py", line 23, in <module>
    from .pipeline import KPipeline
  File "/usr/local/lib/python3.10/site-packages/kokoro/pipeline.py", line 5, in <module>
    from misaki import en, espeak
  File "/usr/local/lib/python3.10/site-packages/misaki/espeak.py", line 10, in <module>
    EspeakWrapper.set_data_path(espeakng_loader.get_data_path())
AttributeError: type object 'EspeakWrapper' has no attribute 'set_data_path'. Did you mean: 'data_path'?

Container logs:

--------------------
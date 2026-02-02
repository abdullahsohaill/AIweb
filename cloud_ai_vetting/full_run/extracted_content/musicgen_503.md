# MusicGen
**URL:** https://huggingface.co/spaces/facebook/MusicGen
**Page Title:** MusicGen - a Hugging Face Space by facebook
--------------------


## runtime error

## Exit code: 1. Reason: ib/python3.9/site-packages/torchaudio/compliance/kaldi.py:22: UserWarning: Failed to initialize NumPy: _ARRAY_API not found (Triggered internally at ../torch/csrc/utils/tensor_numpy.cpp:84.)
  EPSILON = torch.tensor(torch.finfo(torch.float).eps)
Traceback (most recent call last):
  File "/home/user/app/demos/musicgen_app.py", line 26, in <module>
    from audiocraft.data.audio_utils import convert_audio
  File "/home/user/app/audiocraft/__init__.py", line 24, in <module>
    from . import data, modules, models
  File "/home/user/app/audiocraft/data/__init__.py", line 10, in <module>
    from . import audio, audio_dataset, info_audio_dataset, music_dataset, sound_dataset
  File "/home/user/app/audiocraft/data/info_audio_dataset.py", line 19, in <module>
    from ..modules.conditioners import SegmentWithAttributes, ConditioningAttributes
  File "/home/user/app/audiocraft/modules/conditioners.py", line 21, in <module>
    import spacy
  File "/home/user/.pyenv/versions/3.9.23/lib/python3.9/site-packages/spacy/__init__.py", line 6, in <module>
    from .errors import setup_default_warnings
  File "/home/user/.pyenv/versions/3.9.23/lib/python3.9/site-packages/spacy/errors.py", line 2, in <module>
    from .compat import Literal
  File "/home/user/.pyenv/versions/3.9.23/lib/python3.9/site-packages/spacy/compat.py", line 38, in <module>
    from thinc.api import Optimizer  # noqa: F401
  File "/home/user/.pyenv/versions/3.9.23/lib/python3.9/site-packages/thinc/api.py", line 1, in <module>
    from .backends import (
  File "/home/user/.pyenv/versions/3.9.23/lib/python3.9/site-packages/thinc/backends/__init__.py", line 17, in <module>
    from .cupy_ops import CupyOps
  File "/home/user/.pyenv/versions/3.9.23/lib/python3.9/site-packages/thinc/backends/cupy_ops.py", line 16, in <module>
    from .numpy_ops import NumpyOps
  File "thinc/backends/numpy_ops.pyx", line 1, in init thinc.backends.numpy_ops
ValueError: numpy.dtype size changed, may indicate binary incompatibility. Expected 96 from C header, got 88 from PyObject

Container logs:

--------------------
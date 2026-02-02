# component
**URL:** https://firefox-source-docs.mozilla.org/toolkit/components/ml
**Page Title:** Firefox AI Runtime — Firefox Source Docs  documentation
--------------------

- Firefox AI Runtime
- Report an issue / View page source
[LINK: Report an issue](https://bugzilla.mozilla.org/enter_bug.cgi?product=Developer+Infrastructure&component=Firefox+Source+Docs%3A+Content&short_desc=Documentation+issue+on+toolkit/components/ml/index&comment=URL+=+https://firefox-source-docs.mozilla.org/toolkit/components/ml/index.html&bug_file_loc=https://firefox-source-docs.mozilla.org/toolkit/components/ml/index.html)

## Firefox AI Runtime 

This component is an experimental machine learning local inference runtime based on Transformers.js and
the ONNX runtime . You can use the component to leverage
the inference runtime in the context of the browser. To try out some inference tasks,
you can refer to the 1000+ models that are available in the Hugging Face Hub that are compatible with this runtime.
[LINK: Transformers.js](https://huggingface.co/docs/transformers.js/index)
To enable it, flip the browser.ml.enable preference to true in about:config then visit about:inference (Nightly only) or add the following snippet of code
into your (privileged) Javascript code in Firefox or in the browser console:
In case of problem, go to about:logging find the Machine Learning preset
in the dropdown, start logging, reproduce you issue, upload or save the profile,
and open a bug with the link or profile file in Core :: Machine Learning
Learn more about the platform:
- Architecture
- APIs
[LINK: APIs](api.html)
- Notifications
- Models management
- How to perftest a model
- WebExtensions AI API

--------------------
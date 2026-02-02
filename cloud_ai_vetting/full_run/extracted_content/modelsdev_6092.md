# Models.dev
**URL:** https://models.dev
**Page Title:** Models.dev — An open-source database of AI models
--------------------


## How to use

Models.dev is a comprehensive open-source database of AI model specifications, pricing, and features.
There's no single database with information about all the available AI models. We started Models.dev as a community-contributed project to address this. We also use it internally in opencode .

## API

You can access this data through an API.
[LINK: https://models.dev/api.json](/api.json)
Use the Model ID field to do a lookup on any model; it's the identifier used by AI SDK .

## Logos

Provider logos are available at /logos/{provider}.svg where {provider} is the Provider ID .
If we don't have a provider's logo, a default logo is served instead.

## Contribute

The data is stored in the GitHub repo as TOML files; organized by provider and model. The logo is stored as an SVG. This is used to generate this page and power the API.
[LINK: GitHub repo](https://github.com/sst/models.dev)
We need your help keeping this up to date. Feel free to edit the data and submit a pull request. Refer to the README for more information.
[LINK: README](https://github.com/sst/models.dev/blob/dev/README.md)
[LINK: Edit on GitHub](https://github.com/sst/models.dev)

--------------------
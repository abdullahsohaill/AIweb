# Django REST Framework
**URL:** https://www.django-rest-framework.org
**Page Title:** Home - Django REST framework
--------------------

[LINK: GitHub](https://github.com/encode/django-rest-framework)
[LINK: Search](#mkdocs_search_modal)
- Home
- Tutorial Quickstart 1 - Serialization 2 - Requests and responses 3 - Class based views 4 - Authentication and permissions 5 - Relationships and hyperlinked APIs 6 - Viewsets and routers
- Quickstart
- 1 - Serialization
- 2 - Requests and responses
- 3 - Class based views
- 4 - Authentication and permissions
- 5 - Relationships and hyperlinked APIs
[LINK: 5 - Relationships and hyperlinked APIs](tutorial/5-relationships-and-hyperlinked-apis/)
- 6 - Viewsets and routers
- API Guide Requests Responses Views Generic views Viewsets Routers Parsers Renderers Serializers Serializer fields Serializer relations Validators Authentication Permissions Caching Throttling Filtering Pagination Versioning Content negotiation Metadata Schemas Format suffixes Returning URLs Exceptions Status codes Testing Settings
- Requests
[LINK: Requests](api-guide/requests/)
- Responses
[LINK: Responses](api-guide/responses/)
- Views
[LINK: Views](api-guide/views/)
- Generic views
[LINK: Generic views](api-guide/generic-views/)
- Viewsets
[LINK: Viewsets](api-guide/viewsets/)
- Routers
[LINK: Routers](api-guide/routers/)
- Parsers
[LINK: Parsers](api-guide/parsers/)
- Renderers
[LINK: Renderers](api-guide/renderers/)
- Serializers
[LINK: Serializers](api-guide/serializers/)
- Serializer fields
[LINK: Serializer fields](api-guide/fields/)
- Serializer relations
[LINK: Serializer relations](api-guide/relations/)
- Validators
[LINK: Validators](api-guide/validators/)
- Authentication
[LINK: Authentication](api-guide/authentication/)
- Permissions
[LINK: Permissions](api-guide/permissions/)
- Caching
[LINK: Caching](api-guide/caching/)
- Throttling
[LINK: Throttling](api-guide/throttling/)
- Filtering
[LINK: Filtering](api-guide/filtering/)
- Pagination
[LINK: Pagination](api-guide/pagination/)
- Versioning
[LINK: Versioning](api-guide/versioning/)
- Content negotiation
[LINK: Content negotiation](api-guide/content-negotiation/)
- Metadata
[LINK: Metadata](api-guide/metadata/)
- Schemas
[LINK: Schemas](api-guide/schemas/)
- Format suffixes
[LINK: Format suffixes](api-guide/format-suffixes/)
- Returning URLs
[LINK: Returning URLs](api-guide/reverse/)
- Exceptions
[LINK: Exceptions](api-guide/exceptions/)
- Status codes
[LINK: Status codes](api-guide/status-codes/)
- Testing
[LINK: Testing](api-guide/testing/)
- Settings
[LINK: Settings](api-guide/settings/)
- Topics Documenting your API Internationalization AJAX, CSRF & CORS HTML & Forms Browser Enhancements The Browsable API REST, Hypermedia & HATEOAS
- Documenting your API
[LINK: Documenting your API](topics/documenting-your-api/)
- Internationalization
- AJAX, CSRF & CORS
- HTML & Forms
- Browser Enhancements
- The Browsable API
[LINK: The Browsable API](topics/browsable-api/)
- REST, Hypermedia & HATEOAS
- Community Tutorials and Resources Third Party Packages Contributing to REST framework Project management Release Notes 3.16 Announcement 3.15 Announcement 3.14 Announcement 3.13 Announcement 3.12 Announcement 3.11 Announcement 3.10 Announcement 3.9 Announcement 3.8 Announcement 3.7 Announcement 3.6 Announcement 3.5 Announcement 3.4 Announcement 3.3 Announcement 3.2 Announcement 3.1 Announcement 3.0 Announcement Kickstarter Announcement Mozilla Grant Jobs
- Tutorials and Resources
- Third Party Packages
- Contributing to REST framework
- Project management
- Release Notes
- 3.16 Announcement
- 3.15 Announcement
- 3.14 Announcement
- 3.13 Announcement
- 3.12 Announcement
- 3.11 Announcement
- 3.10 Announcement
- 3.9 Announcement
- 3.8 Announcement
- 3.7 Announcement
- 3.6 Announcement
- 3.5 Announcement
- 3.4 Announcement
- 3.3 Announcement
- 3.2 Announcement
- 3.1 Announcement
- 3.0 Announcement
- Kickstarter Announcement
- Mozilla Grant
- Jobs

### Documentation search

- Django REST framework
- Requirements
- Installation
- Example
- Quickstart
- Development
- Support
- Security
- License
GitGuardian protects your code and enforces security policies for developers and teams.
[LINK: GitGuardian protects your code and enforces security policies for developers and teams.](https://www.gitguardian.com/developer)
Fund Django REST framework

## Django REST Framework

Django REST framework is a powerful and flexible toolkit for building Web APIs.
Some reasons you might want to use REST framework:
- The Web browsable API is a huge usability win for your developers.
- Authentication policies including packages for OAuth1a and OAuth2 .
[LINK: Authentication policies](api-guide/authentication/)
[LINK: OAuth1a](api-guide/authentication/#django-rest-framework-oauth)
[LINK: OAuth2](api-guide/authentication/#django-oauth-toolkit)
- Serialization that supports both ORM and non-ORM data sources.
[LINK: Serialization](api-guide/serializers/)
[LINK: ORM](api-guide/serializers#modelserializer)
[LINK: non-ORM](api-guide/serializers#serializers)
- Customizable all the way down - just use regular function-based views if you don't need the more powerful features .
[LINK: regular function-based views](api-guide/views#function-based-views)
[LINK: more](api-guide/generic-views/)
[LINK: powerful](api-guide/viewsets/)
[LINK: features](api-guide/routers/)
- Extensive documentation, and great community support .
- Used and trusted by internationally recognized companies including Mozilla , Red Hat , Heroku , and Eventbrite .

## Requirements

REST framework requires the following:
- Django (4.2, 5.0, 5.1, 5.2)
- Python (3.10, 3.11, 3.12, 3.13, 3.14)
We highly recommend and only officially support the latest patch release of
each Python and Django series.
The following packages are optional:
- PyYAML , uritemplate (5.1+, 3.0.0+) - Schema generation support.
- Markdown (3.3.0+) - Markdown support for the browsable API.
- Pygments (2.7.0+) - Add syntax highlighting to Markdown processing.
- django-filter (1.0.1+) - Filtering support.
- django-guardian (1.1.1+) - Object level permissions support.
[LINK: django-guardian](https://github.com/django-guardian/django-guardian)

## Installation

Install using pip , including any optional packages you want...
...or clone the project from github.
Add 'rest_framework' to your INSTALLED_APPS setting.
If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views.  Add the following to your root urls.py file.
Note that the URL path can be whatever you want.

## Example

Let's take a look at a quick example of using REST framework to build a simple model-backed API.
We'll create a read-write API for accessing information on the users of our project.
Any global settings for a REST framework API are kept in a single configuration dictionary named REST_FRAMEWORK .  Start off by adding the following to your settings.py module:
Don't forget to make sure you've also added rest_framework to your INSTALLED_APPS .
We're ready to create our API now.
Here's our project's root urls.py module:
You can now open the API in your browser at http://127.0.0.1:8000/ , and view your new 'users' API. If you use the login control in the top right corner you'll also be able to add, create and delete users from the system.

## Quickstart

Can't wait to get started? The quickstart guide is the fastest way to get up and running, and building APIs with REST framework.

## Development

See the Contribution guidelines for information on how to clone
the repository, run the test suite and help maintain the code base of REST
Framework.

## Support

For support please see the REST framework discussion group , try the #restframework channel on irc.libera.chat , or raise a question on Stack Overflow , making sure to include the 'django-rest-framework' tag.

## Security

Please report security issues by emailing security@encode.io .
The project maintainers will then work with you to resolve any issues where required, prior to any public disclosure.

## License

Copyright © 2011-present, Encode OSS Ltd .
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
- Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.
Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
- Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.
Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

--------------------
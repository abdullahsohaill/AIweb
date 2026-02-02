# their API
**URL:** https://haveibeenpwned.com/API/v3
**Page Title:** Have I Been Pwned: API Documentation
--------------------


## API Documentation

The API allows the list of pwned accounts (email addresses, usernames and phone numbers) to be quickly searched via a RESTful service

## Index

You're reading about v3 of the API which is presently the current version and contains
                    breaking changes over previous versions for searching breaches and pastes via email address.
- Overview Authorisation Test API Key Specifying the API version Specifying the user agent
- Authorisation
- Test API Key
[LINK: Test API Key](#TestAPIKey)
- Specifying the API version
[LINK: Specifying the API version](#APIVersion)
- Specifying the user agent
- Breaches Getting all breaches for an account Getting all breached email addresses for a domain Getting all subscribed domains Getting all breached sites in the system Getting a single breached site by name Getting the most recently added breach Getting all data classes The breach model Sample breach response
- Getting all breaches for an account
- Getting all breached email addresses for a domain
- Getting all subscribed domains
- Getting all breached sites in the system
- Getting a single breached site by name
- Getting the most recently added breach
- Getting all data classes
- The breach model
- Sample breach response
- Stealer logs Overview Getting all stealer log domains for an email address Getting all stealer log email addresses for a website domain Getting all stealer log email aliases for an email domain
- Overview
- Getting all stealer log domains for an email address
- Getting all stealer log email addresses for a website domain
- Getting all stealer log email aliases for an email domain
- Pastes Getting all pastes for an account The paste model Sample paste response
- Getting all pastes for an account
- The paste model
- Sample paste response
- Subscription Getting the subscription status
- Getting the subscription status
- Pwned Passwords Overview Searching by a range Introducing padding Incremental searches Searching for NTLM hashes Downloading all Pwned Passwords hashes
- Overview
- Searching by a range
- Introducing padding
- Incremental searches
- Searching for NTLM hashes
- Downloading all Pwned Passwords hashes
- Further reading HTTPS Response codes Test accounts Cross-origin resource sharing (CORS) Rate limiting Abuse Acceptable use License
- HTTPS
- Response codes
- Test accounts
- Cross-origin resource sharing (CORS)
- Rate limiting
- Abuse
- Acceptable use
- License

## Overview

### Authorisation

Authorisation is required for all APIs that enable searching HIBP by email address or domain, namely retrieving all breaches for an account , retrieving all pastes for an account , retrieving all breached email addresses for a domain and retrieving all stealer log domains for a breached email addresses . There
                    is no authorisation required for the free Pwned Passwords API .
                    An HIBP subscription key is required to make an authorised call and can be obtained on the API key page . The key is then passed in a "hibp-api-key" header:
[LINK: the API key page](/API/Key)
Semantic HTTP response codes are used to indicate the result of the API call:
Additional information may be present in the response body when an API call fails, for
                    example:
HIBP API keys must be 32-character hexadecimal strings. Keys undergo an initial
                    format check, followed by validation to confirm their authenticity before any
                    processing occurs.

### Test API Key

Where supported, a test API key can be used instead of a paid subscription.
                    Test keys provide limited access (typically to test accounts ) and may be any value that conforms
                    to the required key format. For example:

### Specifying the API version

Version 3 of the API is consumable only by specifying the API version in the URL. All API
                    endpoints are requested with the following pattern:

### Specifying the user agent

Each request to the API must be accompanied by a user agent request header. Typically this
                    should be the name of the app consuming the service. A missing user agent will result in an
                    HTTP 403 response. A valid request would look like:
The user agent should accurately describe the nature of the API consumer such that it can be
                    clearly identified in the request. Not doing so may result in the request being blocked.

## Breaches

### Getting all breaches for an account

The most common use of the API is to return a list of all breaches a particular account has
                    been involved in. The API takes a single parameter which is the account to be searched for.
                    The account is not case-sensitive and will be trimmed of leading or trailing white spaces.
                    The account should always be URL encoded. This is an authenticated API and an HIBP API key must be passed with the request.
If the account is found in a breach, an HTTP 200 response is returned. By default, only the
                    name of the breach is returned rather than the complete breach data, thus reducing the
                    response body size by approximately 98% compared to returning the full breach model .
The name can then be used to
                    either retrieve a single breach or it can be found in the list of all breaches in the system . If you'd like complete
                    breach data returned in the API call, a non-truncated response can be specified via query
                    string parameter:
Which returns the complete model for each breach :
The result set can also be filtered by passing one of the following query strings:
Note: the public API will not return accounts from any breaches flagged as sensitive or retired . By default, the API will return breaches
                    flagged as unverified , however these can be excluded by
                    using the following parameter:
If the account is not found in a breach, an HTTP 404 response will be returned. See the response codes section of the API docs for more information,
                    including other response codes that may be returned.
This API supports test API keys that can be used to
                    query any email address on the test accounts domain. For example, the following queries can be made without needing a paid
                    subscription:
[LINK: test API keys](#TestAPIKey)

### Getting all breached email addresses for a domain

All email addresses on a given domain and the breaches they've appeared in can be returned
                    via the domain search API. Only domains that have been successfully added to the domain search dashboard after verifying control can be
                    searched. The API takes a single parameter which is the domain to be searched for and
                    is an authenticated API requiring an HIBP API key .
If one or more results are found, an HTTP 200 response is returned. For each breached email
                    address on the domain, only the alias is returned along with each breach it has
                    appeared in. Only the name attribute of the breach is returned which can then be used to retrieve a single breach or it can be found in the list of all breaches in the system .
In the above example, if the domain searched for is example.com then 3 email addresses have
                    been found:
- alias1@example.com is in the Adobe data breach
- alias2@example.com is in the Adobe, Gawker and Stratfor data breaches
- alias3@example.com is in the Ashley Madison data breach
If the domain does not have any email addresses in any breaches, an HTTP 404
                    response will be returned. See the response codes section of the API docs for more information, including other response codes that me be returned.
Typically, there is no need to query a domain unless a new breach has been added since the
                    last query. Whilst there's no formal rate limit on the domain search API, reguarly querying
                    it beyond what is practically necessary may result in an HTTP 429 response. To optimise your
                    querying, you can aggressively query the unauthenticated most recent breach API (it's heavily cached at Cloudflare) and once a new breach is seen, query the domain search
                    API for each of your domains.
Note: the domain search API will return sensitive data breaches as it can only be
                    called after demonstrating control of the domain.

### Getting all subscribed domains

Domains that have been successfully added to the domain search dashboard after verifying control are returned via this API. This is an authenticated API requiring an HIBP API key which will then return all domains associated
                    with that key.
The API returns a list of subscribed domains including the following attributes:

### Getting all breached sites in the system

A "breach" is an instance of a system having been compromised by an attacker and
                    the data disclosed. For example, Adobe was a breach, Gawker was a breach etc. It is possible
                    to return the details of each of breach in the system which currently stands at 943 breaches .
click here to test
[LINK: click here to test](/api/v3/breaches)
The result set can also be filtered by passing one of the following query strings:
[LINK: test](/api/v3/breaches?Domain=adobe.com)
[LINK: test](/api/v3/breaches?IsSpamList=true)

### Getting a single breached site by name

Sometimes just a single breach is required and this can be retrieved by the breach
                    "Name". This is the stable value which may or may not be the same as the breach
                    "Title", which can change. See the breach model below for more info.
click here to test
[LINK: click here to test](/api/v3/breach/Adobe)

### Getting the most recently added breach

Often, it's most efficient to monitor for new breaches before performing other actions, for
                    example querying an account or domain. Issuing queries over and over again when no new
                    breaches have been loaded since the last query is usually sub-optimal. This API returns the
                    most recently added breach based on the "AddedDate" attribute of the breach model.
                    This may not be the most recent breach to occur as there may be significant lead
                    time between a service being breached and the data later appearing on HIBP. See the breach model below for more info.
click here to test
[LINK: click here to test](/api/v3/latestbreach)

### Getting all data classes in the system

A "data class" is an attribute of a record compromised in a breach. For example,
                    many breaches expose data classes such as "Email addresses" and
                    "Passwords". The values returned by this service are ordered alphabetically in a
                    string array and will expand over time as new breaches expose previously unseen classes of
                    data.
click here to test
[LINK: click here to test](/api/v3/dataclasses)

### The breach model

Each breach contains a number of attributes describing the incident. In the future, these
                    attributes may expand without the API being versioned. The current attributes are:

### Sample breach response

All responses return breach models either in a collection (breaches for account or all
                    breaches in the system) or as a single item (retrieving a breach by name). When a collection
                    is returned, it's sorted alphabetically by the title of the breach.

## Stealer Logs

### Overview

Stealer logs typically appear as a combination of website address, email address and
                    password. For example, typical stealer log entries appear as follows.
The first row illustrates that when logging onto Netflix, Jane's email address and password
                    were captured by an info stealer .
                    Andy's details were also captured against Netflix, and both Jane and Max's credentials were
                    captured against Spotify. The nomenclature is used to describe the four attributes the HIBP
                    APIs deal with:
HIBP stores the website domain (netflix.com) alongside the email addresses (john@gmail.com).
                    The logs are then searchable in 3 different ways:
- By email address: searching for jane@gmail.com would return netflix.com and spotify.com
- By email address domain: searching for gmail.com would return both Jane and Andy's email
                      addresses along with the domains of the websites they appeared against
- By website domain: searching for netflix.com would return both Jane and Andy's email
                      addresses
Each search can only be performed against domains that have been successfully added to the domain search dashboard after verifying control. For example, the
                    first two searches above can only be done by parties who control gmail.com, and the last
                    search by those who control netflix.com. Where an email address might appear in a stealer log
                    breach but not have a corresponding website domain against it (i.e. because the source data
                    was presented such that one coulnd't be parsed out, no stealer log record will be returned.
All stealer log APIs require a Pwned 5 subscription or higher ,
                    regardless of domain size. The number of email addresses seen against a website domain is
                    displayed next to the domain on the domain search dashboard, for example spotify.com would
                    show 2 results based on the sample data above.
[LINK: a Pwned 5 subscription or higher](/API/Key)
The stealer log APIs that search by domain implement their own rate limit which is entirely
                    independent of the rate limit for the subscription level. For example, whilst a Pwned 5
                    subscription with a 1,000 RPM rate limit will allow that many queries of the breached account API ,
                    the domain-based stealer log APIs have a separate rate limit set much lower. This is due to a
                    combination of the size of the data being queried and the nature of the APIs not requiring
                    the same rate of requests.
Note: there are no API endpoints that return the password for a user. Passwords are
                    independently searchable via the Pwned Passwords service.

### Getting all stealer log domains for an email address

This search is based on the full email address captured by an info stealer as the owner
                    authenticated to a website.
This search returns an array of domains sorted alphabetically:
If no stealer log entries are present for the address, the response will return HTTP 404. The
                    email address being searched for must be on a domain already added to the domain search dashboard .
                    If the searched address is test@example.com, it requires adding example.com to the dashboard
                    and successfully demonstrating control of this domain. Read more about stealer logs in HIBP.

### Getting all stealer log email addresses for a website domain

This search is by the domain of the website URLs that appear in stealer logs. This is the website the info stealer victim was entering credentials into when their
                    data was captured.
This search returns an array of email addresses sorted alphabetically:
Typically, this search would be performed by a website operator looking to identify which of
                    their customers is likely to be the subject of an account takeover attack.
Note: The domain being searched for must be already added to the domain search dashboard .

### Getting all stealer log email aliases for an email domain

This search is by the domain of the email address, which is a similar approach to getting
                      all breached email addresses for a domain , it just returns stealer log data instead.
This search returns a two-dimensional array of email address aliases and associated stealer
                    log website domains, both sorted alphabetically:
This API would normally be used to identify individuals within an organisation who've had
                    credentials taken by an info stealer, and the services for which those credentials have been
                    exposed.
Note: The domain being searched for must be already added to the domain search dashboard .

## Pastes

### Getting all pastes for an account

The API takes a single parameter which is the email address to be searched for. The address
                    is not case-sensitive and will be trimmed of leading or trailing white spaces. The address
                    should always be URL encoded. This is an authenticated API and an HIBP API key must be passed with the request.

### The paste model

Each paste contains a number of attributes describing it. In the future, these
                    attributes may expand without the API being versioned. The current attributes are:

### Sample paste response

Searching an account for pastes always returns a collection of the paste entity. The
                    collection is sorted chronologically with the newest paste first.

## Subscription

### Getting the subscription status

This API returns details of the current subscription and is an authenticated API requiring an HIBP API key :
The API returns the following attributes for the current subscription:

## Pwned Passwords

### Overview

Pwned Passwords are hundreds of millions of passwords which have previously been exposed in
                    data breaches. The service is detailed in the launch blog post and most recently in this post about the FBI and NCA feeding data into the service. . The data is queryable online via the Pwned Passwords webpage ,
                    accessible via the API or downloadable as an entire corpus of data that can be queried
                    offline. The Pwned Passwords API is freely accessible without the need for a subscription and
                    API key.
Each password is stored as both a SHA-1 and an NTLM hash of a UTF-8 encoded password. The downloadable source
                    data delimits the hash and the password count with a colon (:) and each line with a CRLF.

### Searching by range

In order to protect the value of the source password being searched for, Pwned Passwords also
                    implements a k-Anonymity model that
                    allows a password to be searched for by partial hash. This allows the first 5 characters of
                    either a SHA-1 or an NTLM hash (not case-sensitive) to be passed to the API:
click here to test
[LINK: click here to test](https://api.pwnedpasswords.com/range/21BD1)
When a password hash with the same first 5 characters is found in the Pwned Passwords
                    repository, the API will respond with an HTTP 200 and include the suffix of every
                    hash beginning with the specified prefix, followed by a count of how many times it appears in
                    the data set. The API consumer can then search the results of the response for the presence
                    of their source hash and if not found, the password does not exist in the data set. A sample
                    SHA-1 response for the hash prefix "21BD1" would be as follows:
A range search typically returns approximately 800 hash suffixes, although this number will
                    differ depending on the hash prefix being searched for and will increase as more passwords
                    are added. There are 1,048,576 different hash prefixes between 00000 and FFFFF (16^5) and
                    every single one will return HTTP 200; there is no circumstance in which the API should
                    return HTTP 404.
Read more about how k-Anonymity and the Pwned Passwords range search protects searched passwords.

### Introducing padding

In order to further enhance privacy, padding can be added to responses such that anyone
                    able to intercept encrypted responses to the API cannot reasonably determine which hash
                    prefix was searched for by observing the response size. Padding is enabled by a request
                    header and ensures that all responses contain between 800 and 1,000 results regardless of
                    the number of hash suffixes returned by the service. Read the full blog post on padding.
Note: Padded entries always have a password count of 0 and can be discarded once received.

### Incremental searching

Incremental searching involves performing a search for the password as each character is
                    typed by the user, for example via an asynchronous request from their browser. This may provide a 3rd party (namely someone with access to view inbound requests at Cloudflare) with the ability to observe the API requests with sufficient information to discern the original password being searched for .
                    Waiting until the entire password is entered before checking Pwned Passwords (for example,
                    when the blur event is raised on the password field), mitigates this risk.
[LINK: the blur event](https://developer.mozilla.org/en-US/docs/Web/API/Element/blur_event)

### Searching for NTLM hashes

Whilst Pwned Passwords defaults to SHA-1, password hashes can also be requested in NTLM form.
                    API requests still pass the first 5 characters of the hash, but the response returns NTLM
                    hash suffixes of 27 characters rather than SHA-1 suffixes of 35 characters (an NTLM hash is 8
                    characters shorter than a SHA-1 equivalent). The hash format can be specified via the mode
                    query string:

### Downloading all Pwned Passwords hashes

Pwned Passwords works best when directly querying the k-Anonymity API; it's fast, always up
                    to date and enables anonymous queries without disclosing the password being searched for.
                    However, all password hashes are also available for download as either SHA-1 or NTLM so they
                    can be used without the API dependency. The Pwned Passwords Downloader is freely available from GitHub and enables the API to be queried for every single hash
                    prefix and the results saved offline. Read more in the launch blog post.
[LINK: Pwned Passwords Downloader](https://github.com/HaveIBeenPwned/PwnedPasswordsDownloader)

## Further Reading

### HTTPS

All API endpoints must be invoked over HTTPS. Any requests over HTTP will result in a 301
                    response with a redirect to the same path on the secure scheme. Only TLS versions 1.2 and 1.3
                    are supported; older versions of the protocol will not allow a connection to be made.

### Response codes

Semantic HTTP response codes are used to indicate the result of the search:

### Test accounts

Test accounts exist to demonstrate different behaviours. All accounts are on the domain
                    "hibp-integration-tests.com", for example "account-exists@hibp-integration-tests.com".

### Cross-origin resource sharing (CORS)

CORS is only
                    supported for non-authenticated APIs. APIs requiring a key should not be hit directly from
                    the client side as it exposes the secret to other users. Instead, proxy the request through
                    your own API and handle the authorisation between there and the client in your own code.
On supported APIs, CORS accepts all origins — you can hit the API from websites on any
                    other domain.

### Rate limiting

Requests to the breaches, pastes and stealer log APIs are rate limited. The rate limits
                    depends on the the API key you've purchased . Any request that exceeds
                    the limit will receive an HTTP 429 "Too many requests" response. The response also includes an accompanying "retry-after" response header
                    expressing the number of seconds remaining before the client can make a successful API
                    call with the same key (the value is rounded up to the next whole second). The response body explains the rate limit and refers to the acceptable use documentation.
[LINK: the API key you've purchased](/API/Key)
A typical response looks like this:
It's advisable to avoid querying the API at exactly the rate limit as network behaviour may
                    result in some requests arriving within the retry period and causing a 429. Adding a short
                    delay between requests on top of the rate limit will usually ensure this won't happen.
There is no official rate limit for the domain search API, although the intention is to query
                    it infrequently, usually only after a new breach is loaded. Regular querying of the domain
                    search API beyond what is practically necessary may result in measures being applied to
                    reduce the query rate and respond with an HTTP 429.
Where the rate limit is consistently exceeded, further defences may be employed to limit the
                    ability to query the API. These defences include blocks or JavaScript challenges by
                    Cloudflare which may result in an HTTP 503 "Service Unavailable" response.
There is no rate limit on the Pwned Passwords API.

### Abuse

There's not much point; if you want to build up a treasure trove of pwned email addresses or
                    usernames, go and download the dumps (they're usually just a Google search away) and save
                    yourself the hassle and time of trying to enumerate an API one account at a time. That said,
                    use of the API should fall within acceptable use expectations:

### Acceptable use

The API has been designed to make it easy for people to do awesome things with it.
                    Things that are not awesome include:
- Querying the data for purposes that are intended to cause harm to the victims of data breaches
- Anything deliberately intended to limit service availability such as denial of service attacks
- Deliberate attempts to circumvent measures designed to ensure acceptable use
- Not properly identifying the user agent such that it accurately describes the consumer of the API
- Misrepresenting the consuming client by impersonating other user agents in an attempt to obfuscate API requests
- Other services designed to fraudulently represent the Have I Been Pwned name or brand
- Misrepresenting the source of the data as originating from somewhere other than Have I Been Pwned
- Not adhering to the Creative Commons Attribution License as described below
- Automating the consumption of other APIs not explicitly documented on this page
- Using the service in a fashion that brings Have I Been Pwned into disrepute
Abusing these objectives may limit your ability to query the service via a range of
                    countermeasures. Those countermeasures may impact other consumers of the API if they share
                    network services with an abusive user. If in doubt, get in touch and outline how you'd like to use the service in a way that's consistent with these
                    objectives.

### License — breach & paste APIs

This work is licensed under a Creative Commons Attribution 4.0 International License .
In other words, you're welcome to use the public API to build other services, but you must identify Have I Been Pwned as the source of the data . Clear and visible attribution
                    with a link to haveibeenpwned.com should be present
                    anywhere data from the service is used including when searching breaches or pastes and when
                    representing breach descriptions. It doesn't have to be overt, but the interface in which
                    Have I Been Pwned data is represented should clearly attribute the source per the Creative Commons Attribution 4.0 International License .
In order to help maximise adoption, there is no licencing or attribution requirements on the
                    Pwned Passwords API, although it is welcomed if you would like to include it.

--------------------
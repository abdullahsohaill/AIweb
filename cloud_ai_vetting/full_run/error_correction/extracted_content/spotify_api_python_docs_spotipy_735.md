# Spotify API Python Docs (Spotipy)
**URL:** https://spotipy.readthedocs.io
**Page Title:** Welcome to Spotipy! — spotipy 2.0 documentation
--------------------

- Welcome to Spotipy!
- View page source

## Welcome to Spotipy! 

Spotipy is a lightweight Python library for the Spotify Web API . With Spotipy you get full access to all of the music data provided by the Spotify platform.
[LINK: Spotify Web API](https://developer.spotify.com/documentation/web-api/)

## Features 

Spotipy supports all of the features of the Spotify Web API including access
to all end points, and support for user authorization. For details on the
capabilities you are encouraged to review the Spotify Web
API documentation.
[LINK: Spotify Web
API](https://developer.spotify.com/documentation/web-api/)

## Installation 

Install or upgrade Spotipy with:
You can also obtain the source code from the Spotipy GitHub repository .
[LINK: Spotipy GitHub repository](https://github.com/plamere/spotipy)

## Getting Started 

All methods require user authorization. You will need to register your app at My Dashboard to get the credentials necessary to make authorized calls
(a client id and client secret ).
[LINK: My Dashboard](https://developer.spotify.com/dashboard/applications)
Spotipy supports two authorization flows:
- Authorization Code flow This method is suitable for long-running applications
which the user logs into once. It provides an access token that can be refreshed. Note Requires you to add a redirect URI to your application at My Dashboard .
See Redirect URI for more details.
Authorization Code flow This method is suitable for long-running applications
which the user logs into once. It provides an access token that can be refreshed.
Note
Requires you to add a redirect URI to your application at My Dashboard .
See Redirect URI for more details.
[LINK: My Dashboard](https://developer.spotify.com/dashboard/applications)
- Client Credentials flow This method makes it possible
to authenticate your requests to the Spotify Web API and to obtain
a higher rate limit than you would with the Authorization Code flow.
Client Credentials flow This method makes it possible
to authenticate your requests to the Spotify Web API and to obtain
a higher rate limit than you would with the Authorization Code flow.
For guidance on setting your app credentials watch this video tutorial or follow the Spotipy Tutorial for Beginners .
[LINK: Spotipy Tutorial for Beginners](https://github.com/spotipy-dev/spotipy/blob/2.22.1/TUTORIAL.md)
For a longer tutorial with examples included, refer to this video playlist .

## Authorization Code Flow 

This flow is suitable for long-running applications in which the user grants
permission only once. It provides an access token that can be refreshed.
Since the token exchange involves sending your secret key, perform this on a
secure location, like a backend service, and not from a client such as a
browser or from a mobile app.

## Quick start 

To support the Client Authorization Code Flow Spotipy provides a
class SpotifyOAuth that can be used to authenticate requests like so:
or if you are reluctant to immortalize your app credentials in your source code,
you can set environment variables like so (use $env:"credentials" instead of export on Windows):

## Scopes 

See Using
Scopes for information
about scopes.
[LINK: Using
Scopes](https://developer.spotify.com/documentation/web-api/concepts/scopes/)

## Redirect URI 

The Authorization Code Flow needs you to add a redirect URI to your application at My Dashboard (navigate to your application and then [Edit Settings] ).
[LINK: My Dashboard](https://developer.spotify.com/dashboard/applications)
The redirect_uri argument or SPOTIPY_REDIRECT_URI environment variable
must match the redirect URI added to your application in your Dashboard.
The redirect URI can be any valid URI (it does not need to be accessible)
such as http://example.com or http://127.0.0.1:9090 .
Note
If you choose an http -scheme URL, and it’s for 127.0.0.1 , AND it specifies a port, then spotipy will instantiate
a server on the indicated response to receive the access token from the
response at the end of the oauth flow [see the code]( https://github.com/plamere/spotipy/blob/master/spotipy/oauth2.py#L483-L490 ).
[LINK: https://github.com/plamere/spotipy/blob/master/spotipy/oauth2.py#L483-L490](https://github.com/plamere/spotipy/blob/master/spotipy/oauth2.py#L483-L490)

## Client Credentials Flow 

The Client Credentials flow is used in server-to-server authentication. Only
endpoints that do not access user information can be accessed. The advantage here
in comparison with requests to the Web API made without an access token,
is that a higher rate limit is applied.
As opposed to the Authorization Code Flow, you will not need to set SPOTIPY_REDIRECT_URI ,
which means you will never be redirected to the sign in page in your browser:
To support the Client Credentials Flow Spotipy provides a
class SpotifyClientCredentials that can be used to authenticate requests like so:

## IDs URIs and URLs 

Spotipy supports a number of different ID types:
- Spotify URI - The resource identifier that you can enter, for example, in
the Spotify Desktop client’s search box to locate an artist, album, or
track. Example: spotify:track:6rqhFgbbKwnb9MLmUQDhG6
Spotify URI - The resource identifier that you can enter, for example, in
the Spotify Desktop client’s search box to locate an artist, album, or
track. Example: spotify:track:6rqhFgbbKwnb9MLmUQDhG6
- Spotify URL - An HTML link that opens a track, album, app, playlist or other
Spotify resource in a Spotify client. Example: http://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6
Spotify URL - An HTML link that opens a track, album, app, playlist or other
Spotify resource in a Spotify client. Example: http://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6
- Spotify ID - A base-62 number that you can find at the end of the Spotify
URI (see above) for an artist, track, album, etc. Example: 6rqhFgbbKwnb9MLmUQDhG6
Spotify ID - A base-62 number that you can find at the end of the Spotify
URI (see above) for an artist, track, album, etc. Example: 6rqhFgbbKwnb9MLmUQDhG6
In general, any Spotipy method that needs an artist, album, track or playlist ID
will accept ids in any of the above form

## Customized token caching 

Tokens are refreshed automatically and stored by default in the project main folder.
As this might not suit everyone’s needs, spotipy provides a way to create customized
cache handlers.
https://github.com/plamere/spotipy/blob/master/spotipy/cache_handler.py
[LINK: https://github.com/plamere/spotipy/blob/master/spotipy/cache_handler.py](https://github.com/plamere/spotipy/blob/master/spotipy/cache_handler.py)
The custom cache handler would need to be a class that inherits from the base
cache handler CacheHandler . The default cache handler CacheFileHandler is a good example.
An instance of that new class can then be passed as a parameter when
creating SpotifyOAuth , SpotifyPKCE or SpotifyImplicitGrant .
The following handlers are available and defined in the URL above.
- CacheFileHandler
CacheFileHandler
- MemoryCacheHandler
MemoryCacheHandler
- DjangoSessionCacheHandler
DjangoSessionCacheHandler
- FlaskSessionCacheHandler
FlaskSessionCacheHandler
- RedisCacheHandler
RedisCacheHandler
- MemcacheCacheHandler : install with dependency using pip install "spotipy[pymemcache]"
MemcacheCacheHandler : install with dependency using pip install "spotipy[pymemcache]"
Feel free to contribute new cache handlers to the repo.

## Examples 

Here is an example of using Spotipy to list the
names of all the albums released by the artist ‘Birdy’:
Here’s another example showing how to get 30 second samples and cover art
for the top 10 tracks for Led Zeppelin:
Finally, here’s an example that will get the URL for an artist image given the
artist’s name:
There are many more examples of how to use Spotipy in the spotipy-examples
repository on GitHub.
[LINK: spotipy-examples
repository](https://github.com/spotipy-dev/spotipy-examples)

## API Reference 

## client Module 

A simple and thin Python library for the Spotify Web API
Bases: object
Example usage:
Creates a Spotify API client.
- auth – An access token (optional)
auth – An access token (optional)
- requests_session – A Requests session object or a truthy value to create one.
A falsy value disables sessions.
It should generally be a good idea to keep sessions enabled
for performance reasons (connection pooling).
requests_session – A Requests session object or a truthy value to create one.
A falsy value disables sessions.
It should generally be a good idea to keep sessions enabled
for performance reasons (connection pooling).
- client_credentials_manager – SpotifyClientCredentials object
client_credentials_manager – SpotifyClientCredentials object
- oauth_manager – SpotifyOAuth object
oauth_manager – SpotifyOAuth object
- auth_manager – SpotifyOauth, SpotifyClientCredentials,
or SpotifyImplicitGrant object
auth_manager – SpotifyOauth, SpotifyClientCredentials,
or SpotifyImplicitGrant object
- proxies – Definition of proxies (optional).
See Requests doc https://2.python-requests.org/en/master/user/advanced/#proxies
proxies – Definition of proxies (optional).
See Requests doc https://2.python-requests.org/en/master/user/advanced/#proxies
- requests_timeout – Tell Requests to stop waiting for a response after a given
number of seconds
requests_timeout – Tell Requests to stop waiting for a response after a given
number of seconds
- status_forcelist – Tell requests what type of status codes retries should occur on
status_forcelist – Tell requests what type of status codes retries should occur on
- retries – Total number of retries to allow
retries – Total number of retries to allow
- status_retries – Number of times to retry on bad status codes
status_retries – Number of times to retry on bad status codes
- backoff_factor – A backoff factor to apply between attempts after the second try
See urllib3 https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html
backoff_factor – A backoff factor to apply between attempts after the second try
See urllib3 https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html
[LINK: https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html](https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html)
- language – The language parameter advertises what language the user prefers to see.
See ISO-639-1 language code: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
language – The language parameter advertises what language the user prefers to see.
See ISO-639-1 language code: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
Adds a song to the end of a user’s queue
If device A is currently playing music, and you try to add to the queue
and pass in the id for device B, you will get a
‘Player command failed: Restriction violated’ error
I therefore recommend leaving device_id as None so that the active device is targeted
- uri – song uri, id, or url
uri – song uri, id, or url
- device_id – the id of a Spotify device.
If None, then the active device is used.
device_id – the id of a Spotify device.
If None, then the active device is used.
returns a single album given the album’s ID, URIs or URL
- album_id - the album ID, URI or URL
album_id - the album ID, URI or URL
- market - an ISO 3166-1 alpha-2 country code
market - an ISO 3166-1 alpha-2 country code
Get Spotify catalog information about an album’s tracks
- album_id - the album ID, URI or URL
album_id - the album ID, URI or URL
- limit  - the number of items to return
limit  - the number of items to return
- offset - the index of the first item to return
offset - the index of the first item to return
- market - an ISO 3166-1 alpha-2 country code.
market - an ISO 3166-1 alpha-2 country code.
returns a list of albums given the album IDs, URIs, or URLs
- albums - a list of  album IDs, URIs or URLs
albums - a list of  album IDs, URIs or URLs
- market - an ISO 3166-1 alpha-2 country code
market - an ISO 3166-1 alpha-2 country code
returns a single artist given the artist’s ID, URI or URL
- artist_id - an artist ID, URI or URL
artist_id - an artist ID, URI or URL
Get Spotify catalog information about an artist’s albums
This method is deprecated and may be removed in a future version. Use artist_albums(…, include_groups=’…’) instead.
- artist_id - the artist ID, URI or URL
artist_id - the artist ID, URI or URL
- include_groups - the types of items to return. One or more of ‘album’, ‘single’, ‘appears_on’, ‘compilation’. If multiple types are desired,
pass in a comma separated string; e.g., ‘album,single’.
‘appears_on’, ‘compilation’. If multiple types are desired,
pass in a comma separated string; e.g., ‘album,single’.
- country - limit the response to one particular country.
country - limit the response to one particular country.
- limit  - the number of albums to return
limit  - the number of albums to return
- offset - the index of the first album to return
offset - the index of the first album to return
Get Spotify catalog information about artists similar to an
identified artist. Similarity is based on analysis of the
Spotify community’s listening history.
This endpoint has been removed by Spotify and is no longer available.
- artist_id - the artist ID, URI or URL
artist_id - the artist ID, URI or URL
Get Spotify catalog information about an artist’s top 10 tracks
by country.
- artist_id - the artist ID, URI or URL
artist_id - the artist ID, URI or URL
- country - limit the response to one particular country.
country - limit the response to one particular country.
returns a list of artists given the artist IDs, URIs, or URLs
- artists - a list of  artist IDs, URIs or URLs
artists - a list of  artist IDs, URIs or URLs
Get audio analysis for a track based upon its Spotify ID
This endpoint has been removed by Spotify and is no longer available.
- track_id - a track URI, URL or ID
track_id - a track URI, URL or ID
Get audio features for one or multiple tracks based upon their Spotify IDs
This endpoint has been removed by Spotify and is no longer available.
- tracks - a list of track URIs, URLs or IDs, maximum: 100 ids
tracks - a list of track URIs, URLs or IDs, maximum: 100 ids
Get the list of markets where Spotify is available.
Returns a list of the countries in which Spotify is available, identified by their
ISO 3166-1 alpha-2 country code with additional country codes for special territories.
Get a list of categories
- country - An ISO 3166-1 alpha-2 country code.
country - An ISO 3166-1 alpha-2 country code.
- locale - The desired language, consisting of an ISO 639-1 alpha-2
language code and an ISO 3166-1 alpha-2 country code, joined
by an underscore.
locale - The desired language, consisting of an ISO 639-1 alpha-2
language code and an ISO 3166-1 alpha-2 country code, joined
by an underscore.
- limit - The maximum number of items to return. Default: 20.
Minimum: 1. Maximum: 50
limit - The maximum number of items to return. Default: 20.
Minimum: 1. Maximum: 50
- offset - The index of the first item to return. Default: 0
(the first object). Use with limit to get the next set of
items.
offset - The index of the first item to return. Default: 0
(the first object). Use with limit to get the next set of
items.
Get info about a category
- category_id - The Spotify category ID for the category.
category_id - The Spotify category ID for the category.
- country - An ISO 3166-1 alpha-2 country code.
country - An ISO 3166-1 alpha-2 country code.
- locale - The desired language, consisting of an ISO 639-1 alpha-2
language code and an ISO 3166-1 alpha-2 country code, joined
by an underscore.
locale - The desired language, consisting of an ISO 639-1 alpha-2
language code and an ISO 3166-1 alpha-2 country code, joined
by an underscore.
Get a list of playlists for a specific Spotify category
This endpoint has been removed by Spotify and is no longer available.
- category_id - The Spotify category ID for the category.
category_id - The Spotify category ID for the category.
- country - An ISO 3166-1 alpha-2 country code.
country - An ISO 3166-1 alpha-2 country code.
- limit - The maximum number of items to return. Default: 20.
Minimum: 1. Maximum: 50
limit - The maximum number of items to return. Default: 20.
Minimum: 1. Maximum: 50
- offset - The index of the first item to return. Default: 0
(the first object). Use with limit to get the next set of
items.
offset - The index of the first item to return. Default: 0
(the first object). Use with limit to get the next set of
items.
Get information about user’s current playback.
- market - an ISO 3166-1 alpha-2 country code.
market - an ISO 3166-1 alpha-2 country code.
- additional_types - episode to get podcast track information
additional_types - episode to get podcast track information
Get detailed profile information about the current user.
An alias for the ‘me’ method.
Add the current authenticated user as a follower of a playlist.
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
Gets a list of the artists followed by the current authorized user
- limit - the number of artists to return
limit - the number of artists to return
- after - the last artist ID retrieved from the previous request
request
Check if the current user is following certain artists
Returns list of booleans respective to ids
- ids - a list of artist URIs, URLs or IDs
ids - a list of artist URIs, URLs or IDs
Check if the current user is following certain users
Returns list of booleans respective to ids
- ids - a list of user URIs, URLs or IDs
ids - a list of user URIs, URLs or IDs
Get information about the current users currently playing track.
- market - An ISO 3166-1 alpha-2 country code or the string from_token.
string from_token.
- additional_types - list of item types to return. valid types are: track and episode
valid types are: track and episode
Get current user playlists without required getting his profile
Parameters:
- limit  - the number of items to return
limit  - the number of items to return
- offset - the index of the first item to return
offset - the index of the first item to return
Get the current user’s recently played tracks
- limit - the number of entities to return
limit - the number of entities to return
- after - unix timestamp in milliseconds. Returns all items after (but not including) this cursor position.
Cannot be used if before is specified.
after (but not including) this cursor position.
Cannot be used if before is specified.
- before - unix timestamp in milliseconds. Returns all items before (but not including) this cursor position.
Cannot be used if after is specified
before (but not including) this cursor position.
Cannot be used if after is specified
Gets a list of the albums saved in the current authorized user’s
“Your Music” library
- limit - the number of albums to return (MAX_LIMIT=50)
limit - the number of albums to return (MAX_LIMIT=50)
- offset - the index of the first album to return
offset - the index of the first album to return
- market - an ISO 3166-1 alpha-2 country code.
market - an ISO 3166-1 alpha-2 country code.
Add one or more albums to the current user’s
“Your Music” library.
Parameters:
- albums - a list of album URIs, URLs or IDs
albums - a list of album URIs, URLs or IDs
Check if one or more albums is already saved in
the current Spotify user’s “Your Music” library.
- albums - a list of album URIs, URLs or IDs
albums - a list of album URIs, URLs or IDs
Remove one or more albums from the current user’s
“Your Music” library.
- albums - a list of album URIs, URLs or IDs
albums - a list of album URIs, URLs or IDs
Gets a list of the episodes saved in the current authorized user’s
“Your Music” library
- limit - the number of episodes to return
limit - the number of episodes to return
- offset - the index of the first episode to return
offset - the index of the first episode to return
- market - an ISO 3166-1 alpha-2 country code
market - an ISO 3166-1 alpha-2 country code
Add one or more episodes to the current user’s
“Your Music” library.
- episodes - a list of episode URIs, URLs or IDs
episodes - a list of episode URIs, URLs or IDs
Check if one or more episodes is already saved in
the current Spotify user’s “Your Music” library.
- episodes - a list of episode URIs, URLs or IDs
episodes - a list of episode URIs, URLs or IDs
Remove one or more episodes from the current user’s
“Your Music” library.
- episodes - a list of episode URIs, URLs or IDs
episodes - a list of episode URIs, URLs or IDs
Gets a list of the shows saved in the current authorized user’s
“Your Music” library
- limit - the number of shows to return
limit - the number of shows to return
- offset - the index of the first show to return
offset - the index of the first show to return
- market - an ISO 3166-1 alpha-2 country code
market - an ISO 3166-1 alpha-2 country code
Add one or more albums to the current user’s
“Your Music” library.
Parameters:
- shows - a list of show URIs, URLs or IDs
shows - a list of show URIs, URLs or IDs
Check if one or more shows is already saved in
the current Spotify user’s “Your Music” library.
- shows - a list of show URIs, URLs or IDs
shows - a list of show URIs, URLs or IDs
Remove one or more shows from the current user’s
“Your Music” library.
- shows - a list of show URIs, URLs or IDs
shows - a list of show URIs, URLs or IDs
Gets a list of the tracks saved in the current authorized user’s
“Your Music” library
- limit - the number of tracks to return
limit - the number of tracks to return
- offset - the index of the first track to return
offset - the index of the first track to return
- market - an ISO 3166-1 alpha-2 country code
market - an ISO 3166-1 alpha-2 country code
Add one or more tracks to the current user’s
“Your Music” library.
- tracks - a list of track URIs, URLs or IDs
tracks - a list of track URIs, URLs or IDs
Check if one or more tracks is already saved in
the current Spotify user’s “Your Music” library.
- tracks - a list of track URIs, URLs or IDs
tracks - a list of track URIs, URLs or IDs
Remove one or more tracks from the current user’s
“Your Music” library.
- tracks - a list of track URIs, URLs or IDs
tracks - a list of track URIs, URLs or IDs
Get the current user’s top artists
- limit - the number of entities to return (max 50)
limit - the number of entities to return (max 50)
- offset - the index of the first entity to return
offset - the index of the first entity to return
- time_range - Over what time frame are the affinities computed
Valid-values: short_term, medium_term, long_term
time_range - Over what time frame are the affinities computed
Valid-values: short_term, medium_term, long_term
Get the current user’s top tracks
- limit - the number of entities to return
limit - the number of entities to return
- offset - the index of the first entity to return
offset - the index of the first entity to return
- time_range - Over what time frame are the affinities computed
Valid-values: short_term, medium_term, long_term
time_range - Over what time frame are the affinities computed
Valid-values: short_term, medium_term, long_term
Unfollows (deletes) a playlist for the current authenticated
user
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
Get user’s currently playing track.
- market - an ISO 3166-1 alpha-2 country code.
market - an ISO 3166-1 alpha-2 country code.
- additional_types - episode to get podcast track information
additional_types - episode to get podcast track information
Get a list of user’s available devices.
returns a single episode given the episode’s ID, URIs or URL
- episode_id - the episode ID, URI or URL
episode_id - the episode ID, URI or URL
- market - an ISO 3166-1 alpha-2 country code. The episode must be available in the given market.
If user-based authorization is in use, the user’s country
takes precedence. If neither market nor user country are
provided, the content is considered unavailable for the client.
The episode must be available in the given market.
If user-based authorization is in use, the user’s country
takes precedence. If neither market nor user country are
provided, the content is considered unavailable for the client.
returns a list of episodes given the episode IDs, URIs, or URLs
- episodes - a list of episode IDs, URIs or URLs
episodes - a list of episode IDs, URIs or URLs
- market - an ISO 3166-1 alpha-2 country code. Only episodes available in the given market will be returned.
If user-based authorization is in use, the user’s country
takes precedence. If neither market nor user country are
provided, the content is considered unavailable for the client.
Only episodes available in the given market will be returned.
If user-based authorization is in use, the user’s country
takes precedence. If neither market nor user country are
provided, the content is considered unavailable for the client.
Get a list of Spotify featured playlists
This endpoint has been removed by Spotify and is no longer available.
- locale - The desired language, consisting of a lowercase ISO
639-1 alpha-2 language code and an uppercase ISO 3166-1 alpha-2
country code, joined by an underscore.
locale - The desired language, consisting of a lowercase ISO
639-1 alpha-2 language code and an uppercase ISO 3166-1 alpha-2
country code, joined by an underscore.
- country - An ISO 3166-1 alpha-2 country code.
country - An ISO 3166-1 alpha-2 country code.
- timestamp - A timestamp in ISO 8601 format:
yyyy-MM-ddTHH:mm:ss. Use this parameter to specify the user’s
local time to get results tailored for that specific date and
time in the day
timestamp - A timestamp in ISO 8601 format:
yyyy-MM-ddTHH:mm:ss. Use this parameter to specify the user’s
local time to get results tailored for that specific date and
time in the day
- limit - The maximum number of items to return. Default: 20.
Minimum: 1. Maximum: 50
limit - The maximum number of items to return. Default: 20.
Minimum: 1. Maximum: 50
- offset - The index of the first item to return. Default: 0
(the first object). Use with limit to get the next set of
items.
offset - The index of the first item to return. Default: 0
(the first object). Use with limit to get the next set of
items.
Get Spotify catalog information for a single audiobook identified by its unique
Spotify ID.
Parameters:
- id - the Spotify ID for the audiobook
- market - an ISO 3166-1 alpha-2 country code.
Get Spotify catalog information about an audiobook’s chapters.
Parameters:
- id - the Spotify ID for the audiobook
- market - an ISO 3166-1 alpha-2 country code.
- limit - the maximum number of items to return
- offset - the index of the first item to return
Get Spotify catalog information for multiple audiobooks based on their Spotify IDs.
Parameters:
- ids - a list of Spotify IDs for the audiobooks
- market - an ISO 3166-1 alpha-2 country code.
Get detailed profile information about the current user.
An alias for the ‘current_user’ method.
Get a list of new album releases featured in Spotify
- country - An ISO 3166-1 alpha-2 country code.
country - An ISO 3166-1 alpha-2 country code.
- limit - The maximum number of items to return. Default: 20.
Minimum: 1. Maximum: 50
limit - The maximum number of items to return. Default: 20.
Minimum: 1. Maximum: 50
- offset - The index of the first item to return. Default: 0
(the first object). Use with limit to get the next set of
items.
offset - The index of the first item to return. Default: 0
(the first object). Use with limit to get the next set of
items.
returns the next result given a paged result
- result - a previously returned paged result
result - a previously returned paged result
Skip user’s playback to next track.
- device_id - device target for playback
device_id - device target for playback
Pause user’s playback.
- device_id - device target for playback
device_id - device target for playback
Gets playlist by id.
- playlist - the id of the playlist
playlist - the id of the playlist
- fields - which fields to return
fields - which fields to return
- market - An ISO 3166-1 alpha-2 country code or the string from_token.
string from_token.
- additional_types - list of item types to return. valid types are: track and episode
valid types are: track and episode
Adds tracks/episodes to a playlist
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- items - a list of track/episode URIs or URLs
items - a list of track/episode URIs or URLs
- position - the position to add the tracks
position - the position to add the tracks
Changes a playlist’s name and/or public/private state,
collaborative state, and/or description
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- name - optional name of the playlist
name - optional name of the playlist
- public - optional is the playlist public
public - optional is the playlist public
- collaborative - optional is the playlist collaborative
collaborative - optional is the playlist collaborative
- description - optional description of the playlist
description - optional description of the playlist
Get cover image of a playlist.
- playlist_id - the playlist ID, URI or URL
playlist_id - the playlist ID, URI or URL
Check to see if the given users are following the given playlist
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- user_ids - the ids of the users that you want to check to see if they follow the playlist. Maximum: 5 ids.
if they follow the playlist. Maximum: 5 ids.
Get full details of the tracks and episodes of a playlist.
- playlist_id - the playlist ID, URI or URL
playlist_id - the playlist ID, URI or URL
- fields - which fields to return
fields - which fields to return
- limit - the maximum number of tracks to return
limit - the maximum number of tracks to return
- offset - the index of the first track to return
offset - the index of the first track to return
- market - an ISO 3166-1 alpha-2 country code.
market - an ISO 3166-1 alpha-2 country code.
- additional_types - list of item types to return. valid types are: track and episode
valid types are: track and episode
Removes all occurrences of the given tracks/episodes from the given playlist
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- items - list of track/episode ids to remove from the playlist
items - list of track/episode ids to remove from the playlist
- snapshot_id - optional id of the playlist snapshot
snapshot_id - optional id of the playlist snapshot
Removes all occurrences of the given tracks from the given playlist
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- items - an array of objects containing Spotify URIs of the tracks/episodes to remove with their current positions in
the playlist.  For example: [  { “uri”:”4iV5W9uYEdYUVa79Axb7Rh”, “positions”:[2] },
{ “uri”:”1301WleyT98MSxVHPZCA6M”, “positions”:[7] } ]
tracks/episodes to remove with their current positions in
the playlist.  For example:
[  { “uri”:”4iV5W9uYEdYUVa79Axb7Rh”, “positions”:[2] },
{ “uri”:”1301WleyT98MSxVHPZCA6M”, “positions”:[7] } ]
- snapshot_id - optional id of the playlist snapshot
snapshot_id - optional id of the playlist snapshot
Reorder tracks in a playlist
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- range_start - the position of the first track to be reordered
range_start - the position of the first track to be reordered
- range_length - optional the number of tracks to be reordered (default: 1)
(default: 1)
- insert_before - the position where the tracks should be inserted
inserted
- snapshot_id - optional playlist’s snapshot ID
snapshot_id - optional playlist’s snapshot ID
Replace all tracks/episodes in a playlist
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- items - list of track/episode ids to comprise playlist
items - list of track/episode ids to comprise playlist
Get full details of the tracks of a playlist.
This method is deprecated and may be removed in a future version. Use playlist_items(playlist_id, …, additional_types=(‘track’,)) instead.
- playlist_id - the playlist ID, URI or URL
playlist_id - the playlist ID, URI or URL
- fields - which fields to return
fields - which fields to return
- limit - the maximum number of tracks to return
limit - the maximum number of tracks to return
- offset - the index of the first track to return
offset - the index of the first track to return
- market - an ISO 3166-1 alpha-2 country code.
market - an ISO 3166-1 alpha-2 country code.
- additional_types - list of item types to return. valid types are: track and episode
valid types are: track and episode
Replace the image used to represent a specific playlist
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- image_b64 - image data as a Base64 encoded JPEG image string (maximum payload size is 256 KB)
(maximum payload size is 256 KB)
returns the previous result given a paged result
- result - a previously returned paged result
result - a previously returned paged result
Skip user’s playback to previous track.
- device_id - device target for playback
device_id - device target for playback
Gets the current user’s queue
Get a list of genres available for the recommendations function.
This endpoint has been removed by Spotify and is no longer available.
Get a list of recommended tracks for one to five seeds.
(at least one of seed_artists , seed_tracks and seed_genres are needed)
This endpoint has been removed by Spotify and is no longer available.
- seed_artists - a list of artist IDs, URIs or URLs
seed_artists - a list of artist IDs, URIs or URLs
- seed_tracks - a list of track IDs, URIs or URLs
seed_tracks - a list of track IDs, URIs or URLs
- seed_genres - a list of genre names. Available genres for recommendations can be found by calling
recommendation_genre_seeds
recommendations can be found by calling
recommendation_genre_seeds
- country - An ISO 3166-1 alpha-2 country code. If provided, all results will be playable in this country.
all results will be playable in this country.
- limit - The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 100
Minimum: 1. Maximum: 100
- min/max/target_<attribute> - For the tuneable track attributes listed in the documentation, these values
provide filters and targeting on results.
attributes listed in the documentation, these values
provide filters and targeting on results.
Set repeat mode for playback.
- state - track , context , or off
state - track , context , or off
- device_id - device target for playback
device_id - device target for playback
searches for an item
- q - the search query (see how to write a query in the official documentation https://developer.spotify.com/documentation/web-api/reference/search/ )  # noqa
official documentation https://developer.spotify.com/documentation/web-api/reference/search/ )  # noqa
[LINK: https://developer.spotify.com/documentation/web-api/reference/search/](https://developer.spotify.com/documentation/web-api/reference/search/)
- limit - the number of items to return (min = 1, default = 10, max = 50). The limit is applied within each type, not on the total response.
within each type, not on the total response.
- offset - the index of the first item to return
offset - the index of the first item to return
- type - the types of items to return. One or more of ‘artist’, ‘album’, ‘track’, ‘playlist’, ‘show’, and ‘episode’.  If multiple types are desired,
pass in a comma separated string; e.g., ‘track,album,episode’.
‘track’, ‘playlist’, ‘show’, and ‘episode’.  If multiple types are desired,
pass in a comma separated string; e.g., ‘track,album,episode’.
- market - An ISO 3166-1 alpha-2 country code or the string from_token.
from_token.
(experimental) Searches multiple markets for an item
- q - the search query (see how to write a query in the official documentation https://developer.spotify.com/documentation/web-api/reference/search/ )  # noqa
official documentation https://developer.spotify.com/documentation/web-api/reference/search/ )  # noqa
[LINK: https://developer.spotify.com/documentation/web-api/reference/search/](https://developer.spotify.com/documentation/web-api/reference/search/)
- limit  - the number of items to return (min = 1, default = 10, max = 50). If a search is to be done on multiple markets, then this limit is applied to each market. (e.g. search US, CA, MX each with a limit of 10).
If multiple types are specified, this applies to each type.
markets, then this limit is applied to each market. (e.g. search US, CA, MX each with a limit of 10).
If multiple types are specified, this applies to each type.
- offset - the index of the first item to return
offset - the index of the first item to return
- type - the types of items to return. One or more of ‘artist’, ‘album’, ‘track’, ‘playlist’, ‘show’, or ‘episode’. If multiple types are desired, pass in a comma separated string.
‘track’, ‘playlist’, ‘show’, or ‘episode’. If multiple types are desired, pass in a comma separated string.
- markets - A list of ISO 3166-1 alpha-2 country codes. Search all country markets by default.
markets - A list of ISO 3166-1 alpha-2 country codes. Search all country markets by default.
- total - the total number of results to return across multiple markets and types.
total - the total number of results to return across multiple markets and types.
Seek to position in current track.
- position_ms - position in milliseconds to seek to
position_ms - position in milliseconds to seek to
- device_id - device target for playback
device_id - device target for playback
returns a single show given the show’s ID, URIs or URL
- show_id - the show ID, URI or URL
show_id - the show ID, URI or URL
- market - an ISO 3166-1 alpha-2 country code. The show must be available in the given market.
If user-based authorization is in use, the user’s country
takes precedence. If neither market nor user country are
provided, the content is considered unavailable for the client.
The show must be available in the given market.
If user-based authorization is in use, the user’s country
takes precedence. If neither market nor user country are
provided, the content is considered unavailable for the client.
Get Spotify catalog information about a show’s episodes
- show_id - the show ID, URI or URL
show_id - the show ID, URI or URL
- limit  - the number of items to return
limit  - the number of items to return
- offset - the index of the first item to return
offset - the index of the first item to return
- market - an ISO 3166-1 alpha-2 country code. Only episodes available in the given market will be returned.
If user-based authorization is in use, the user’s country
takes precedence. If neither market nor user country are
provided, the content is considered unavailable for the client.
Only episodes available in the given market will be returned.
If user-based authorization is in use, the user’s country
takes precedence. If neither market nor user country are
provided, the content is considered unavailable for the client.
returns a list of shows given the show IDs, URIs, or URLs
- shows - a list of show IDs, URIs or URLs
shows - a list of show IDs, URIs or URLs
- market - an ISO 3166-1 alpha-2 country code. Only shows available in the given market will be returned.
If user-based authorization is in use, the user’s country
takes precedence. If neither market nor user country are
provided, the content is considered unavailable for the client.
Only shows available in the given market will be returned.
If user-based authorization is in use, the user’s country
takes precedence. If neither market nor user country are
provided, the content is considered unavailable for the client.
Toggle playback shuffling.
- state - true or false
state - true or false
- device_id - device target for playback
device_id - device target for playback
Start or resume user’s playback.
Provide a context_uri to start playback of an album,
artist, or playlist.
Provide a uris list to start playback of one or more
tracks.
Provide offset as {“position”: <int>} or {“uri”: “<track uri>”}
to start playback at a particular offset.
- device_id - device target for playback
device_id - device target for playback
- context_uri - spotify context uri to play
context_uri - spotify context uri to play
- uris - spotify track uris
uris - spotify track uris
- offset - offset into context by index or track
offset - offset into context by index or track
- position_ms - (optional) indicates from what position to start playback. Must be a positive number. Passing in a position that is
greater than the length of the track will cause the player to
start playing the next song.
Must be a positive number. Passing in a position that is
greater than the length of the track will cause the player to
start playing the next song.
returns a single track given the track’s ID, URI or URL
- track_id - a spotify URI, URL or ID
track_id - a spotify URI, URL or ID
- market - an ISO 3166-1 alpha-2 country code.
market - an ISO 3166-1 alpha-2 country code.
returns a list of tracks given a list of track IDs, URIs, or URLs
- tracks - a list of spotify URIs, URLs or IDs. Maximum: 50 IDs.
tracks - a list of spotify URIs, URLs or IDs. Maximum: 50 IDs.
- market - an ISO 3166-1 alpha-2 country code.
market - an ISO 3166-1 alpha-2 country code.
Transfer playback to another device.
Note that the API accepts a list of device ids, but only
actually supports one.
- device_id - transfer playback to this device
device_id - transfer playback to this device
- force_play - true: after transfer, play. false: keep current state.
keep current state.
Gets basic profile information about a Spotify User
- user - the id of the usr
user - the id of the usr
Follow one or more artists
Parameters:
- ids - a list of artist IDs
ids - a list of artist IDs
Follow one or more users
Parameters:
- ids - a list of user IDs
ids - a list of user IDs
Gets a single playlist of a user
This method is deprecated and may be removed in a future version. Use playlist(playlist_id) instead.
- user - the id of the user
user - the id of the user
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- fields - which fields to return
fields - which fields to return
This function is no longer in use, please use the recommended function in the warning!
Adds episodes to a playlist
This method is deprecated and may be removed in a future version. Use playlist_add_items(playlist_id, episodes) instead.
- user - the id of the user
user - the id of the user
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- episodes - a list of track URIs, URLs or IDs
episodes - a list of track URIs, URLs or IDs
- position - the position to add the episodes
position - the position to add the episodes
This function is no longer in use, please use the recommended function in the warning!
Adds tracks to a playlist
This method is deprecated and may be removed in a future version. Use playlist_add_items(playlist_id, tracks) instead.
- user - the id of the user
user - the id of the user
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- tracks - a list of track URIs, URLs or IDs
tracks - a list of track URIs, URLs or IDs
- position - the position to add the tracks
position - the position to add the tracks
This function is no longer in use, please use the recommended function in the warning!
Changes a playlist’s name and/or public/private state
This method is deprecated and may be removed in a future version. Use playlist_change_details(playlist_id, …) instead.
- user - the id of the user
user - the id of the user
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- name - optional name of the playlist
name - optional name of the playlist
- public - optional is the playlist public
public - optional is the playlist public
- collaborative - optional is the playlist collaborative
collaborative - optional is the playlist collaborative
- description - optional description of the playlist
description - optional description of the playlist
Creates a playlist for a user
- user - the id of the user
user - the id of the user
- name - the name of the playlist
name - the name of the playlist
- public - is the created playlist public
public - is the created playlist public
- collaborative - is the created playlist collaborative
collaborative - is the created playlist collaborative
- description - the description of the playlist
description - the description of the playlist
This function is no longer in use, please use the recommended function in the warning!
Add the current authenticated user as a follower of a playlist.
This method is deprecated and may be removed in a future version. Use current_user_follow_playlist(playlist_id) instead.
- playlist_owner_id - the user id of the playlist owner
playlist_owner_id - the user id of the playlist owner
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
This function is no longer in use, please use the recommended function in the warning!
Check to see if the given users are following the given playlist
This method is deprecated and may be removed in a future version. Use playlist_is_following(playlist_id, user_ids) instead.
- playlist_owner_id - the user id of the playlist owner
playlist_owner_id - the user id of the playlist owner
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- user_ids - the ids of the users that you want to check to see if they follow the playlist. Maximum: 5 ids.
if they follow the playlist. Maximum: 5 ids.
This function is no longer in use, please use the recommended function in the warning!
Removes all occurrences of the given tracks from the given playlist
This method is deprecated and may be removed in a future version. Use playlist_remove_all_occurrences_of_items(playlist_id, tracks) instead.
- user - the id of the user
user - the id of the user
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- tracks - the list of track ids to remove from the playlist
tracks - the list of track ids to remove from the playlist
- snapshot_id - optional id of the playlist snapshot
snapshot_id - optional id of the playlist snapshot
This function is no longer in use, please use the recommended function in the warning!
Removes specific occurrences of the given tracks from the given playlist
This endpoint has been removed by Spotify and is no longer available.
- user - the id of the user
user - the id of the user
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- tracks - an array of objects containing Spotify URIs of the tracks to remove with their current positions in the
playlist.  For example: [  { “uri”:”4iV5W9uYEdYUVa79Axb7Rh”, “positions”:[2] },
{ “uri”:”1301WleyT98MSxVHPZCA6M”, “positions”:[7] } ]
tracks to remove with their current positions in the
playlist.  For example:
[  { “uri”:”4iV5W9uYEdYUVa79Axb7Rh”, “positions”:[2] },
{ “uri”:”1301WleyT98MSxVHPZCA6M”, “positions”:[7] } ]
- snapshot_id - optional id of the playlist snapshot
snapshot_id - optional id of the playlist snapshot
This function is no longer in use, please use the recommended function in the warning!
Reorder tracks in a playlist from a user
This method is deprecated and may be removed in a future version. Use playlist_reorder_items(playlist_id, …) instead.
- user - the id of the user
user - the id of the user
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- range_start - the position of the first track to be reordered
range_start - the position of the first track to be reordered
- range_length - optional the number of tracks to be reordered (default: 1)
(default: 1)
- insert_before - the position where the tracks should be inserted
inserted
- snapshot_id - optional playlist’s snapshot ID
snapshot_id - optional playlist’s snapshot ID
This function is no longer in use, please use the recommended function in the warning!
Replace all tracks in a playlist for a user
This method is deprecated and may be removed in a future version. Use playlist_replace_items(playlist_id, tracks) instead.
- user - the id of the user
user - the id of the user
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- tracks - the list of track ids to add to the playlist
tracks - the list of track ids to add to the playlist
Get full details of the tracks of a playlist owned by a user.
This method is deprecated and may be removed in a future version. Use playlist_tracks(playlist_id) instead.
- user - the id of the user
user - the id of the user
- playlist_id - the id of the playlist
playlist_id - the id of the playlist
- fields - which fields to return
fields - which fields to return
- limit - the maximum number of tracks to return
limit - the maximum number of tracks to return
- offset - the index of the first track to return
offset - the index of the first track to return
- market - an ISO 3166-1 alpha-2 country code.
market - an ISO 3166-1 alpha-2 country code.
This function is no longer in use, please use the recommended function in the warning!
Unfollows (deletes) a playlist for a user
This method is deprecated and may be removed in a future version. Use current_user_unfollow_playlist(playlist_id) instead.
- user - the id of the user
user - the id of the user
- name - the name of the playlist
name - the name of the playlist
Gets playlists of a user
- user - the id of the usr
user - the id of the usr
- limit  - the number of items to return
limit  - the number of items to return
- offset - the index of the first item to return
offset - the index of the first item to return
Unfollow one or more artists
Parameters:
- ids - a list of artist IDs
ids - a list of artist IDs
Unfollow one or more users
Parameters:
- ids - a list of user IDs
ids - a list of user IDs
Set playback volume.
- volume_percent - volume between 0 and 100
volume_percent - volume between 0 and 100
- device_id - device target for playback
device_id - device target for playback
Bases: SpotifyBaseException

## oauth2 Module 

Bases: SpotifyAuthBase
Creates a Client Credentials Flow Manager.
The Client Credentials flow is used in server-to-server authentication.
Only endpoints that do not access user information can be accessed.
This means that endpoints that require authorization scopes cannot be accessed.
The advantage, however, of this authorization flow is that it does not require any
user interaction
You can either provide a client_id and client_secret to the
constructor or set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
environment variables
- client_id: Must be supplied or set as environment variable
client_id: Must be supplied or set as environment variable
- client_secret: Must be supplied or set as environment variable
client_secret: Must be supplied or set as environment variable
- proxies: Optional, proxy for the requests library to route through
proxies: Optional, proxy for the requests library to route through
- requests_session: A Requests session
requests_session: A Requests session
- requests_timeout: Optional, tell Requests to stop waiting for a response after a given number of seconds
a given number of seconds
- cache_handler: An instance of the CacheHandler class to handle getting and saving cached authorization tokens.
Optional, will otherwise use CacheFileHandler .
(takes precedence over cache_path and username )
getting and saving cached authorization tokens.
Optional, will otherwise use CacheFileHandler .
(takes precedence over cache_path and username )
If a valid access token is in memory, returns it
Else fetches a new token and returns it
Parameters:
- as_dict: (deprecated) a boolean indicating if returning the access token
as a token_info dictionary, otherwise it will be returned
as a string.
Bases: SpotifyAuthBase
Implements Implicit Grant Flow for client apps
This auth manager enables user and non-user endpoints with only
a client secret, redirect uri, and username. The user will need to
copy and paste a URI from the browser every hour.

## Security Warning 

The OAuth standard no longer recommends the Implicit Grant Flow for
client-side code. Spotify has implemented the OAuth-suggested PKCE
extension that removes the need for a client secret in the
Authentication Code flow. Use the SpotifyPKCE auth manager instead
of SpotifyImplicitGrant.
SpotifyPKCE contains all the functionality of
SpotifyImplicitGrant, plus automatic response retrieval and
refreshable tokens. Only a few replacements need to be made:
- get_auth_response()[‘access_token’] ->
get_access_token(get_authorization_code())
get_auth_response()[‘access_token’] ->
get_access_token(get_authorization_code())
- get_auth_response() ->
get_access_token(get_authorization_code()); get_cached_token()
get_auth_response() ->
get_access_token(get_authorization_code()); get_cached_token()
- parse_response_token(url)[‘access_token’] ->
get_access_token(parse_response_code(url))
parse_response_token(url)[‘access_token’] ->
get_access_token(parse_response_code(url))
- parse_response_token(url) ->
get_access_token(parse_response_code(url)); get_cached_token()
parse_response_token(url) ->
get_access_token(parse_response_code(url)); get_cached_token()
The security concern in the Implicit Grant flow is that the token is
returned in the URL and can be intercepted through the browser. A
request with an authorization code and proof of origin could not be
easily intercepted without a compromised network.
Creates Auth Manager using the Implicit Grant flow
See help(SpotifyImplicitGrant) for full Security Warning

### Parameters 

- client_id: Must be supplied or set as environment variable
client_id: Must be supplied or set as environment variable
- redirect_uri: Must be supplied or set as environment variable
redirect_uri: Must be supplied or set as environment variable
- state: May be supplied, no verification is performed
state: May be supplied, no verification is performed
- scope: Optional, either a list of scopes or comma separated string of scopes. e.g, “playlist-read-private,playlist-read-collaborative”
e.g, “playlist-read-private,playlist-read-collaborative”
- cache_handler: An instance of the CacheHandler class to handle getting and saving cached authorization tokens.
May be supplied, will otherwise use CacheFileHandler .
(takes precedence over cache_path and username )
getting and saving cached authorization tokens.
May be supplied, will otherwise use CacheFileHandler .
(takes precedence over cache_path and username )
- cache_path: (deprecated) May be supplied, will otherwise be generated (takes precedence over username )
(takes precedence over username )
- username: (deprecated) May be supplied or set as environment variable (will set cache_path to .cache-{username} )
(will set cache_path to .cache-{username} )
- show_dialog: Interpreted as boolean
show_dialog: Interpreted as boolean
Gets Auth Token from cache (preferred) or user interaction

### Parameters 

- state: May be given, overrides (without changing) self.state
state: May be given, overrides (without changing) self.state
- response: URI with token, can break expiration checks
response: URI with token, can break expiration checks
- check_cache: Interpreted as boolean
check_cache: Interpreted as boolean
Gets a new auth token with user interaction
Gets the URL to use to authorize this app
Gets the cached token for the app
This method is deprecated and may be removed in a future version.
Parse the response code in the given response url
Bases: SpotifyAuthBase
Implements Authorization Code Flow for Spotify’s OAuth implementation.
Creates a SpotifyOAuth object
- client_id: Must be supplied or set as environment variable
client_id: Must be supplied or set as environment variable
- client_secret: Must be supplied or set as environment variable
client_secret: Must be supplied or set as environment variable
- redirect_uri: Must be supplied or set as environment variable
redirect_uri: Must be supplied or set as environment variable
- state: Optional, no verification is performed
state: Optional, no verification is performed
- scope: Optional, either a list of scopes or comma separated string of scopes. e.g, “playlist-read-private,playlist-read-collaborative”
e.g, “playlist-read-private,playlist-read-collaborative”
- cache_path: (deprecated) Optional, will otherwise be generated (takes precedence over username )
(takes precedence over username )
- username: (deprecated) Optional or set as environment variable (will set cache_path to .cache-{username} )
(will set cache_path to .cache-{username} )
- proxies: Optional, proxy for the requests library to route through
proxies: Optional, proxy for the requests library to route through
- show_dialog: Optional, interpreted as boolean
show_dialog: Optional, interpreted as boolean
- requests_session: A Requests session
requests_session: A Requests session
- requests_timeout: Optional, tell Requests to stop waiting for a response after a given number of seconds
a given number of seconds
- open_browser: Optional, whether the web browser should be opened to authorize a user
authorize a user
- cache_handler: An instance of the CacheHandler class to handle getting and saving cached authorization tokens.
Optional, will otherwise use CacheFileHandler .
(takes precedence over cache_path and username )
getting and saving cached authorization tokens.
Optional, will otherwise use CacheFileHandler .
(takes precedence over cache_path and username )
Gets the access token for the app given the code
- code: the response code
code: the response code
- as_dict: (deprecated) a boolean indicating if returning the access token as a token_info dictionary, otherwise it will be returned
as a string.
as a token_info dictionary, otherwise it will be returned
as a string.
Gets the URL to use to authorize this app
Gets the cached token for the app
This method is deprecated and may be removed in a future version.
Parse the response code in the given response url
- url - the response url
url - the response url
Bases: SpotifyBaseException
Error during Auth Code or Implicit Grant flow
Bases: SpotifyAuthBase
Implements PKCE Authorization Flow for client apps
This auth manager enables user and non-user endpoints with only
a client ID, redirect URI, and username. When the app requests
an access token for the first time, the user is prompted to
authorize the new client app. After authorizing the app, the client
app is then given both access and refresh tokens. This is the
preferred way of authorizing a mobile/desktop client.
Creates Auth Manager with the PKCE Auth flow.
- client_id: Must be supplied or set as environment variable
client_id: Must be supplied or set as environment variable
- redirect_uri: Must be supplied or set as environment variable
redirect_uri: Must be supplied or set as environment variable
- state: Optional, no verification is performed
state: Optional, no verification is performed
- scope: Optional, either a list of scopes or comma separated string of scopes. e.g, “playlist-read-private,playlist-read-collaborative”
e.g, “playlist-read-private,playlist-read-collaborative”
- cache_path: (deprecated) Optional, will otherwise be generated (takes precedence over username )
(takes precedence over username )
- username: (deprecated) Optional or set as environment variable (will set cache_path to .cache-{username} )
(will set cache_path to .cache-{username} )
- proxies: Optional, proxy for the requests library to route through
proxies: Optional, proxy for the requests library to route through
- requests_timeout: Optional, tell Requests to stop waiting for a response after a given number of seconds
a given number of seconds
- requests_session: A Requests session
requests_session: A Requests session
- open_browser: Optional, whether the web browser should be opened to authorize a user
authorize a user
- cache_handler: An instance of the CacheHandler class to handle getting and saving cached authorization tokens.
Optional, will otherwise use CacheFileHandler .
(takes precedence over cache_path and username )
getting and saving cached authorization tokens.
Optional, will otherwise use CacheFileHandler .
(takes precedence over cache_path and username )
Gets the access token for the app
If the code is not given and no cached token is used, an
authentication window will be shown to the user to get a new
code.
- code - the response code from authentication
code - the response code from authentication
- check_cache - if true, checks for a locally stored token before requesting a new token
before requesting a new token
Gets the URL to use to authorize this app
Parse the response code in the given response url
- url - the response url
url - the response url
Bases: SpotifyOauthError
The state sent and state received were different

## util Module 

Prompt the user to login if necessary and returns a user token
suitable for use with the spotipy.Spotify constructor.
Deprecated since version This: method is deprecated and may be removed in a future version.
- username - the Spotify username. (optional)
username - the Spotify username. (optional)
- scope - the desired scope of the request. (optional)
scope - the desired scope of the request. (optional)
- client_id - the client ID of your app. (required)
client_id - the client ID of your app. (required)
- client_secret - the client secret of your app. (required)
client_secret - the client secret of your app. (required)
- redirect_uri - the redirect URI of your app. (required)
redirect_uri - the redirect URI of your app. (required)
- cache_path - path to location to save tokens. (required)
cache_path - path to location to save tokens. (required)
- oauth_manager - OAuth manager object. (optional)
oauth_manager - OAuth manager object. (optional)
- show_dialog - If True, a login prompt always shows or defaults to False. (optional)
show_dialog - If True, a login prompt always shows or defaults to False. (optional)

## Support 

You can ask questions about Spotipy on Stack Overflow.   Don’t forget to add the Spotipy tag, and any other relevant tags as well, before posting.
http://stackoverflow.com/questions/ask
If you think you’ve found a bug, let us know at Spotipy Issues
[LINK: Spotipy Issues](https://github.com/plamere/spotipy/issues)

## Contribute 

If you are a developer with Python experience, and you would like to contribute to Spotipy, please
be sure to follow the guidelines listed below:
export SPOTIPY_CLIENT_ID=client_id_here
export SPOTIPY_CLIENT_SECRET=client_secret_here
export SPOTIPY_CLIENT_USERNAME=client_username_here # This is actually an id not spotify display name
export SPOTIPY_REDIRECT_URI=http://127.0.0.1:8080 # Make url is set in app you created to get your ID and SECRET
$ virtualenv –python=python3.12 env
(env) $ pip install –user -e .
(env) $ python -m unittest discover -v tests
Lint
pip install autopep8
autopep8 –in-place –aggressive –recursive .
pip install flake8
flake8 .
pip install isort
isort . -c -v
Publishing (by maintainer)
- Bump version in setup.py
Bump version in setup.py
- Bump and date changelog
Bump and date changelog
- Add to changelog:
Add to changelog:
## Unreleased
// Add your changes here and then delete this line
- Commit changes
Commit changes
- Package to pypi:
Package to pypi:
python setup.py sdist bdist_wheel
python3 setup.py sdist bdist_wheel
twine check dist/*
twine upload –repository-url https://upload.pypi.org/legacy/ –skip-existing dist/ .(whl|gz|zip)~dist/*linux .whl
- Create github release https://github.com/plamere/spotipy/releases with the changelog content for the version and a short name that describes the main addition
Create github release https://github.com/plamere/spotipy/releases with the changelog content for the version and a short name that describes the main addition
[LINK: https://github.com/plamere/spotipy/releases](https://github.com/plamere/spotipy/releases)
- Build the documentation again to ensure it’s on the latest version
Build the documentation again to ensure it’s on the latest version
Changelog
Don’t forget to add a short description of your change in the CHANGELOG !
[LINK: CHANGELOG](https://github.com/plamere/spotipy/blob/master/CHANGELOG.md)

## License 

(Taken from https://github.com/plamere/spotipy/blob/master/LICENSE.md ):
[LINK: https://github.com/plamere/spotipy/blob/master/LICENSE.md](https://github.com/plamere/spotipy/blob/master/LICENSE.md)

## Indices and tables 

- Index
Index
- Module Index
Module Index
- Search Page
Search Page

--------------------
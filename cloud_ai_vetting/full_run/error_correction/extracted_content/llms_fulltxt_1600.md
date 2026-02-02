# llms-full.txt
**URL:** https://docs.beyondwords.io/llms-full.txt
**Page Title:** 
--------------------

### (Raw Extraction Fallback)

# Create ad
Source: https://docs.beyondwords.io/api-reference/ads/create

post /projects/{project_id}/ads
Creates an ad in a project

# Delete ad
Source: https://docs.beyondwords.io/api-reference/ads/delete

delete /projects/{project_id}/ads/{id}
Deletes an ad from a project

# List ads
Source: https://docs.beyondwords.io/api-reference/ads/list

get /projects/{project_id}/ads
Lists ads within a project

# Get ad
Source: https://docs.beyondwords.io/api-reference/ads/show

get /projects/{project_id}/ads/{id}
Gets an ad from a project

# Update ad
Source: https://docs.beyondwords.io/api-reference/ads/update

put /projects/{project_id}/ads/{id}
Updates an ad in a project

# Get ad analytics
Source: https://docs.beyondwords.io/api-reference/analytics/ad-analytics

get /projects/{project_id}/ads/{id}/analytics
Retrieve analytics for a single ad in a project.

# List ads analytics
Source: https://docs.beyondwords.io/api-reference/analytics/ads-analytics

get /projects/{project_id}/ads/analytics
Retrieve analytics overview for all ads in a project.

# Get content analytics
Source: https://docs.beyondwords.io/api-reference/analytics/content-analytics

get /projects/{project_id}/content/{id}/analytics
Retrieve analytics for some specific content.

# List content analytics
Source: https://docs.beyondwords.io/api-reference/analytics/contents-analytics

get /projects/{project_id}/content/analytics
Retrieves an analytics overview for all content items in a project

# Get organization analytics
Source: https://docs.beyondwords.io/api-reference/analytics/organization-analytics

get /organization/analytics
Retrieves analytics for all projects within an organization

# Get project analytics
Source: https://docs.beyondwords.io/api-reference/analytics/project-analytics

get /projects/{id}/analytics
Retrieves analytics for a project

# List projects analytics
Source: https://docs.beyondwords.io/api-reference/analytics/projects-analytics

get /projects/analytics
Retrieves an analytics overview for all projects within an organization

# Create content
Source: https://docs.beyondwords.io/api-reference/content/create

post /projects/{project_id}/content
Creates a content item in your project

# Delete content
Source: https://docs.beyondwords.io/api-reference/content/delete

delete /projects/{project_id}/content/{id}
Delete a content item from your project

# List content
Source: https://docs.beyondwords.io/api-reference/content/list

get /projects/{project_id}/content
Lists content within a project

# Content overview
Source: https://docs.beyondwords.io/api-reference/content/overview

Overview of the content object and its properties

This object represents an item of content that belongs to a project.

| Property                       | Type    | Description                                                                                                                                                                                                                                                                                    |
| ------------------------------ | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                           | string  | Unique UUID for the object.                                                                                                                                                                                                                                                                    |
| `status`                       | string  | The current status of the content processing operation. This value will change as the content is processed. Possible values are `draft`, `queued`, `processing`, `processed`, `skipped`, `error`                                                                                               |
| `type`                         | string  | The type. Possible values are `auto_segmet`, `manual_segment` or `audio_upload`                                                                                                                                                                                                                |
| `title`                        | string  | The content title.                                                                                                                                                                                                                                                                             |
| `summary`                      | string  | The content summary.                                                                                                                                                                                                                                                                           |
| `body`                         | string  | The content body.                                                                                                                                                                                                                                                                              |
| `source_id`                    | string  | The externally-provided source identifier of the content. For example, this could be the id of the content in your CMS.                                                                                                                                                                        |
| `source_url`                   | string  | The URL that contains the source content. For example, this could be the public URL of the content.                                                                                                                                                                                            |
| `author`                       | string  | The author of the content.                                                                                                                                                                                                                                                                     |
| `image_url`                    | string  | The feature image URL of the content.                                                                                                                                                                                                                                                          |
| `metadata`                     | object  | The arbitrary metadata associated with content. For example, this could be `{"category": "sport"}`                                                                                                                                                                                             |
| `audio`                        | array   | The array of generated audio files for the entire content.                                                                                                                                                                                                                                     |
| `audio.id`                     | integer | Unique identifier for the audio object.                                                                                                                                                                                                                                                        |
| `audio.content_type`           | string  | The MIME type of the audio file according to the IANA specification.                                                                                                                                                                                                                           |
| `audio.url`                    | string  | The URL of the generated audio file.                                                                                                                                                                                                                                                           |
| `audio.duration`               | integer | The duration of the generated audio file in milliseconds.                                                                                                                                                                                                                                      |
| `video`                        | array   | The array of generated video files for the entire content.                                                                                                                                                                                                                                     |
| `segments`                     | array   | The array of segments in the content                                                                                                                                                                                                                                                           |
| `segments.id`                  | integer | Unique identifier for the segment object                                                                                                                                                                                                                                                       |
| `segments.marker`              | string  | The marker associated with the segment. To support playback from segments (i.e. paragraphs), you need to use the [BeyondWords Player](/docs-and-guides/distribution/player/overview) and [add markers to the elements](/docs-and-guides/distribution/player/sdk/javascript/segments-playback). |
| `segments.section`             | string  | The section type of the segment. Possible values are `title`, `summary`, or `body`                                                                                                                                                                                                             |
| `segments.content_type`        | string  | The content type of the segment. Possible values are `text`, `audio`, or `image`. Text and audio will be included in generated audios. Text, audio, and images will be included in generated videos (coming soon).                                                                             |
| `segments.text`                | string  | The plain text for this segment if `segment.content_type` is `text`                                                                                                                                                                                                                            |
| `segments.audio_url`           | string  | The URL of the uploaded audio file for this segment if the `segment.content_type` is `audio`                                                                                                                                                                                                   |
| `segments.image_url`           | string  | The URL of the uploaded image file for this segment if the `segment.content_type` is `image`                                                                                                                                                                                                   |
| `segments.language`            | object  | The language object associated with this segment if the `segment.content_type` is `text`                                                                                                                                                                                                       |
| `segments.language.code`       | string  | The language code of the segment if the `segment.content_type` is `text`                                                                                                                                                                                                                       |
| `segments.language.name`       | string  | The language name of the segment if the `segment.content_type` is `text`                                                                                                                                                                                                                       |
| `segments.voice`               | object  | The voice object associated with this segment if the `segment.content_type` is `text`                                                                                                                                                                                                          |
| `segments.voice.id`            | integer | The id of the voice used to generate the audio of the segment if the `segment.content_type` is text                                                                                                                                                                                            |
| `segments.voice.name`          | string  | The name of voice used to generate the audio of the segment if the `segment.content_type` is `text`                                                                                                                                                                                            |
| `segments.start_time`          | integer | The start time of this segment in milliseconds. This may not exactly match the summed durations because of audio alignment gaps.                                                                                                                                                               |
| `segments.duration`            | integer | The duration of this segment in milliseconds.                                                                                                                                                                                                                                                  |
| `segments.created`             | string  | Time at which the segment object was created (ISO 8601).                                                                                                                                                                                                                                       |
| `segments.updated`             | string  | Time at which the segment object was updated (ISO 8601).                                                                                                                                                                                                                                       |
| `published`                    | boolean | Whether the content will appear in the BeyondWords Players                                                                                                                                                                                                                                     |
| `publish_date`                 | string  | Time at which the content was published or is scheduled to be published (ISO 8601).                                                                                                                                                                                                            |
| `ads_enabled`                  | boolean | Whether adverts will play for this content in the BeyondWords Players. If you don't have any ads then no ads will play.                                                                                                                                                                        |
| `auto_segment_updates_enabled` | boolean | Whether the media files will be regenerated when the `title`, `summary` or `body` content is updated with `auto_segment`                                                                                                                                                                       |
| `created`                      | string  | Time at which the object was created (ISO 8601).                                                                                                                                                                                                                                               |
| `updated`                      | string  | Time at which the object was updated (ISO 8601).                                                                                                                                                                                                                                               |

# Regenerate content
Source: https://docs.beyondwords.io/api-reference/content/regenerate

post /projects/{project_id}/content/{id}/regenerate
Reprocess content in a project.

# Introduction to segments
Source: https://docs.beyondwords.io/api-reference/content/segments

## Segments

Each content item can have multiple segments. For instance, an article typically includes a title, a summary and a body. The body itself typically contains multiple paragraphs, which may include multimedia elements such as images, audio clips, and videos. These individual components are referred to as segments. Segmenting content enables flexibility, allowing for a range of features when combined with the [BeyondWords Player](https://github.com/beyondwords-io/player). These include skipping between segments, initiating playback from specific segments (e.g., clicking play on a paragraph), and highlighting segments during playback (e.g., paragraph highlighting as it plays).

You have three options when it comes to generating audio: `auto_segment`, `manual_segment`, or `audio_upload`.

### auto\_segment

We recommend the `auto_segment` option for publishers seeking a simple way to generate audio versions of their articles.

To use this option set `type` property to `auto_segment` whenever you create or update a content item.

Using this option, you are required to submit data for the `body` property, with the `title` and `summary` properties being optional additions.

Once submitted, BeyondWords will automatically segment the `body` data into `segments`. In the initial response, the `segments` will be an empty array, as automatic segmenting is an asynchronous operation. However, once the audio has been generated and you retrieve a content item using the `?segments=full` query parameter, you will be able to view the individual segments.

**Example request and responses:**

<CodeGroup>
  ```json Example POST request theme={null}
  {
    "type": "auto_segment",
    "title": "<h1>Your content title text</h1>",
    "summary": "<h2>Your content summary text</h2>",
    "body": "<p>Your content body text</p>",
    "source_id": "article-id-in-your-cms",
    "source_url": "https://example.com/some-article",
    "author": "Steve Jobs",
    "image_url": "https://example.com/image.jpeg",
    "metadata": {
      "key": "value"
    },
    "published": true,
    "publish_date": null,
    "ads_enabled": true,
    "auto_segment_updates_enabled": true
  }
  ```

  ```json Example POST response theme={null}
  {
    "type": "auto_segment",
    "status": "queued",
    "id": "d7dfd636-098c-4b1b-83e5-15a3cba5a0bd",
    "title": "<h1>Your content title text</h1>",
    "summary": "<h2>Your content summary text</h2>",
    "body": "<p>Your content body text</p>",
    "source_id": "article-id-in-your-cms",
    "source_url": "https://example.com/some-article",
    "author": "Steve Jobs",
    "image_url": "https://example.com/image.jpeg",
    "audio": [],
    "video": [],
    "segments": [],
    "is_copy": false,
    "ads_enabled": true,
    "title_voice_id": null,
    "summary_voice_id": null,
    "body_voice_id": null,
    "metadata": {
      "key": "value"
    },
    "created": "2023-01-01T00:00:00Z",
    "updated": "2023-01-01T00:00:05Z",
    "published": true,
    "publish_date": "2023-01-01T00:00:00Z",
    "auto_segment_updates_enabled": true
  }
  ```

  ```json Example GET response (processed) theme={null}
  {
    "type": "auto_segment",
    "status": "processed",
    "id": "d7dfd636-098c-4b1b-83e5-15a3cba5a0bd",
    "title": "<h1>Your content title text</h1>",
    "summary": "<h2>Your content summary text</h2>",
    "body": "<p>Your content body text</p>",
    "source_id": "article-id-in-your-cms",
    "source_url": "https://example.com/some-article",
    "author": "Steve Jobs",
    "image_url": "https://example.com/image.jpeg",
    "audio": [
      {
        "id": 36553942,
        "content_type": "application/x-mpegURL",
        "url": "https://example.com/media.m3u8",
        "duration": 7051
      },
      {
        "id": 36553929,
        "content_type": "audio/mpeg",
        "url": "https://example.com/media_compiled.mp3",
        "duration": 7056
      }
    ],
    "video": [],
    "segments": [
      {
        "marker": "0a2bae2e-542f-498e-95c4-91dfc403eb8b",
        "section": "title",
        "start_time": 45,
        "duration": 1730,
        "id": 95737414,
        "content_type": "text",
        "text": "Your content title text",
        "audio_url": null,
        "image_url": null,
        "language": {
          "code": "en_US",
          "name": "English (USA)"
        },
        "voice": {
          "id": 298,
          "name": "Matthew"
        },
        "created": "2023-07-26T05:02:24Z",
        "updated": "2023-07-26T05:02:25Z"
      },
      {
        "marker": "b012ad1b-7366-4ed1-a6f2-b855665065ad",
        "section": "summary",
        "start_time": null,
        "duration": null,
        "id": 95737415,
        "content_type": "text",
        "text": "Your content summary text",
        "audio_url": null,
        "image_url": null,
        "language": {
          "code": "en_US",
          "name": "English (USA)"
        },
        "voice": {
          "id": 776,
          "name": "Sara"
        },
        "created": "2023-07-26T05:02:24Z",
        "updated": "2023-07-26T05:02:25Z"
      },
      {
        "marker": "ad212f8f-8356-4059-9ee9-c5b1406f70b7",
        "section": "body",
        "start_time": 1841,
        "duration": 2595,
        "id": 95737416,
        "content_type": "text",
        "text": "Your content summary text",
        "audio_url": null,
        "image_url": null,
        "language": {
          "code": "en_US",
          "name": "English (USA)"
        },
        "voice": {
          "id": 776,
          "name": "Sara"
        },
        "created": "2023-07-26T05:02:24Z",
        "updated": "2023-07-26T05:02:25Z"
      },
      {
        "marker": "76bfc232-2755-4da7-86b1-222a66434444",
        "section": "body",
        "start_time": 4503,
        "duration": 2559,
        "id": 95737417,
        "content_type": "text",
        "text": "Your content body text",
        "audio_url": null,
        "image_url": null,
        "language": {
          "code": "en_US",
          "name": "English (USA)"
        },
        "voice": {
          "id": 776,
          "name": "Sara"
        },
        "created": "2023-07-26T05:02:24Z",
        "updated": "2023-07-26T05:02:25Z"
      }
    ],
    "ads_enabled": true,
    "is_copy": false,
    "title_voice_id": null,
    "summary_voice_id": null,
    "body_voice_id": null,
    "metadata": {
      "key": "value"
    },
    "created": "2023-01-01T00:00:00Z",
    "updated": "2023-01-01T00:00:05Z",
    "published": true,
    "publish_date": "2023-01-01T00:00:00Z",
    "auto_segment_updates_enabled": true
  }
  ```
</CodeGroup>

### manual\_segment

We recommend the `manual_segment` option for publishers seeking enhanced control over the audio conversion of their content. This is particularly beneficial for those who wish to integrate the content API into their editorial interface or create videos with multiple images (coming soon).

To use this option set `type` property to `manual_segment` whenever you create or update a content item.

Using this option, you **should not** submit any data to the `title`, `body` or `summary` properties.

Instead, you will need to submit an array of one or multiple `segments`.

For each segment you submit you will need to submit data to the following properties:

| Property       | Options                                                                                                                                                                                                                       |
| :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `section`      | Use this property define the section type of a segment as either `title`, `summary` or `body`.                                                                                                                                |
| `content_type` | If `content_type` is `text` then submit plain text to be converted into audio. If no `voice_id` is submitted then the audio will be generated with the default project voices assigned title, summary or body in the project. |
|                | If `content_type` is `audio` then submit an `audio_url` to be uploaded.                                                                                                                                                       |
|                | If `content_type` is `image` then submit an `image_url` to be uploaded.                                                                                                                                                       |

Once submitted, BeyondWords will generate the audio for segments with text and then concatenate all segments into a single audio.

Text and audio will be included in generated audios and text, audio and images will be included in generated videos (coming soon).

**Example request and responses:**

<CodeGroup>
  ```json Example POST request theme={null}
  {
    "type": "manual_segment",
    "source_id": "example-source-id",
    "source_url": "https://example.com/some-article",
    "author": "Steve Jobs",
    "image_url": "https://example.com/image.jpeg",
    "metadata": {
      "key": "value"
    },
    "segments": [
      {
        "section": "title",
        "marker": "75aa616c-1849-4d70-bb3b-7691cc6310a5",
        "content_type": "text",
        "text": "This is a title",
        "voice": {
          "id": 1
        }
      },
      {
        "section": "body",
        "marker": "75aa616c-1849-4d70-bb3b-7691cc6310a2",
        "content_type": "text",
        "text": "This is a paragraph",
        "voice": {
          "id": 1
        }
      },
      {
        "section": "body",
        "content_type": "image",
        "image_url": "https://example.com/image.jpeg"
      },
      {
        "section": "body",
        "marker": "75aa616c-1849-4d70-bb3b-7691cc6311a5",
        "content_type": "text",
        "text": "This is another paragraph",
        "voice": {
          "id": 1
        }
      },
      {
        "section": "body",
        "marker": "75aa616c-1849-4d71-bb3b-7691cc6310a5",
        "content_type": "audio",
        "audio_url": "https://example.com/audio.mp3"
      },
      {
        "section": "body",
        "marker": "75aa416c-1849-4d70-bb3b-7691cc6310a5",
        "content_type": "text",
        "text": "This is another paragraph",
        "voice": {
          "id": 1
        }
      }
    ],
    "published": true,
    "ads_enabled": false,
    "auto_segment_updates_enabled": false
  }
  ```

  ```json Example GET response theme={null}
  {
    "id": "d7dfd636-098c-4b1b-83e5-15a3cba5a0bd",
    "status": "processed",
    "type": "manual_segment",
    "title": null,
    "summary": null,
    "body": null,
    "source_id": "example-source-id",
    "source_url": "https://example.com/some-article",
    "author": "Steve Jobs",
    "image_url": "https://example.com/image.jpeg",
    "metadata": {
      "key": "value"
    },
    "audio": [
      {
        "id": 1,
        "content_type": "application/vnd.apple.mpegurl",
        "url": "https://example.com/audio.m3u8",
        "duration": 10000
      },
      {
        "id": 2,
        "content_type": "audio/mpeg,",
        "url": "https://example.com/audio.mp3",
        "duration": 10000
      }
    ],
    "video": [],
    "segments": [
      {
        "id": 1,  
        "section": "title",
        "marker": "75aa616c-1849-4d70-bb3b-7691cc6310a5",
        "content_type": "text",
        "text": "This is a title",
        "audio_url": null,
        "image_url": null,
        "language": {
          "code": "en_US",
          "name": "English"
        },
        "voice": {
          "id": 123,
          "name": "Steve"
        },
        "start_time": 3,
        "duration": 2000,
        "created": "2023-01-01T00:00:00Z",
        "updated": "2023-01-01T00:00:05Z"
      },
      {
        "id": 2,
        "section": "body",
        "marker": "75aa616c-1849-4d70-bb3b-7691cc6310a2",
        "content_type": "text",
        "text": "This is a paragraph",
        "audio_url": null,
        "image_url": null,
        "language": {
          "code": "en_US",
          "name": "English"
        },
        "voice": {
          "id": 123,
          "name": "Steve"
        },
        "start_time": 3,
        "duration": 2000,
        "created": "2023-01-01T00:00:00Z",
        "updated": "2023-01-01T00:00:05Z"
      },
      {
        "id": 3,
        "section": "body",
        "content_type": "image",
        "text": null,
        "audio_url": null,
        "image_url": "https://example.com/image.jpeg",
        "start_time": 3,
        "duration": 2000,
        "created": "2023-01-01T00:00:00Z",
        "updated": "2023-01-01T00:00:05Z"
      },
      {
        "id": 4,
        "section": "body",
        "marker": "75aa616c-1849-4d70-bb3b-7691cc6311a5",
        "content_type": "text",
        "text": "This is another paragraph",
        "audio_url": null,
        "image_url": null,
        "language": {
          "code": "en_US",
          "name": "English"
        },
        "voice": {
          "id": 123,
          "name": "Steve"
        },
        "start_time": 3,
        "duration": 2000,
        "created": "2023-01-01T00:00:00Z",
        "updated": "2023-01-01T00:00:05Z"
      },
      {
        "id": 5,
        "section": "body",
        "marker": "75aa616c-1849-4d71-bb3b-7691cc6310a5",
        "content_type": "audio",
        "text": null,
        "audio_url": "https://example.com/image.mp3",
        "image_url": null,
        "start_time": 3,
        "duration": 2000,
        "created": "2023-01-01T00:00:00Z",
        "updated": "2023-01-01T00:00:05Z"
      },
      {
        "id": 6,
        "section": "body",
        "marker": "75aa416c-1849-4d70-bb3b-7691cc6310a5",
        "content_type": "text",
        "text": "This is another paragraph",
        "audio_url": null,
        "image_url": null,
        "language": {
          "code": "en_US",
          "name": "English"
        },
        "voice": {
          "id": 123,
          "name": "Steve"
        },
        "start_time": 3,
        "duration": 2000,
        "created": "2023-01-01T00:00:00Z",
        "updated": "2023-01-01T00:00:05Z"
      }
    ],
    "ads_enabled": true,
    "auto_segment_updates_enabled": true,
    "created": "2023-01-01T00:00:00Z",
    "updated": "2023-01-01T00:00:05Z"
  }
  ```
</CodeGroup>

### audio\_upload

We recommend `audio_upload` option for publishers that want to host podcasts or human-recorded articles on BeyondWords and leverage the BeyondWords Player, podcast feeds and analytics.

To use this option set the `type` property to `audio_upload` whenever you create or update a content item.

Using this option, you should submit a `title`, `body` and `segments` array with a single segment object with `section` set to `title`, `content_type` set to `audio` and an `audio_url` with a URL to the audio file to be upload.

<Info>
  The title and body text will not be converted into audio. However the text may be present in the player or podcast feeds depending on your player or playlist settings.
</Info>

**Example request:**

```json Example POST request theme={null}
{
  "type": "audio_upload",
  "title": "Podcast episode title",
  "body": "Podcast episode description",
  "source_id": "example-source-id",
  "source_url": "https://example.com/some-article",
  "author": "Harry Stebbings",
  "image_url": "https://example.com/image.jpeg",
  "metadata": {
    "key": "value"
  },
  "segments": [
    {
      "section": "title",
      "content_type": "audio",
      "audio_url": "https://example.com/audio.mp3"
    }
  ],
  "published": true,
  "ads_enabled": true,
  "auto_segment_updates_enabled": false
}
```

# Get content
Source: https://docs.beyondwords.io/api-reference/content/show

get /projects/{project_id}/content/{id}
Get a content item from your project

# Syndicated articles
Source: https://docs.beyondwords.io/api-reference/content/syndicated

Reuse audio articles across multiple projects or websites without generating audio for each one.

Syndicated articles let publishers reuse audio articles across different projects - such as multiple websites - without needing to generate new audio for each one. If you publish the same article on several sites (each represented as a separate project), you can simply reuse the original audio, ensuring consistency and reducing costs.

<Info>This feature must be enabled by the BeyondWords team. Please contact us if you’d like to discuss enabling it for your account.</Info>

## Example use case

A publisher has multiple websites (each as a separate project) and wants to publish the same article on all of them. Instead of generating new audio for each website, they can reuse the audio article from the first project.

By using the same `source_id` in both requests:

Project A (Website 1) will generate the audio.

Project B (Website 2) will create a new audio article that reuses Project A’s audio file.

## How it works

A user submits a POST request with a [source\_id](/api-reference/content/create#body-source-id):

1. If no audio article exists with that `source_id`, a new audio file is generated.

2. If an audio article with that `source_id` exists in any of your other projects, the existing audio file is reused. <br />
   <br />A new article is still created in the new project, but it references the existing audio file.

## Identifying duplicates via the API

You can distinguish between original and reused audio articles via the `is_copy` property that is returned in the response or the [`audio.updated`](/docs-and-guides/integrations/webhooks#audio-updated-payload) payload:

`is_copy`: false → The original (parent) article that generated the audio.

`is_copy`: true → A duplicated (child) article that reuses the audio.

## Inherited fields

When creating a new audio article using an existing `source_id`, certain fields are automatically inherited from the original (parent) article. These fields cannot be overwritten in the new (child) article:

* `status`
* `title`
* `type`
* `summary`
* `body`
* `audio`
* `video`
* `summarization`
* `segments`

Other fields, such as `source_url` can be modified as needed in the `POST` request.

This ensures that core audio content remains consistent across projects.

# Update content
Source: https://docs.beyondwords.io/api-reference/content/update

put /projects/{project_id}/content/{id}
Update a content item from your project

# Overview
Source: https://docs.beyondwords.io/api-reference/overview

Learn about the BeyondWords API

# BeyondWords API overview

The BeyondWords API is a RESTful API that provides headless access to the entire platform, allowing you to programmatically create, manage, and deliver audio content.

## API basics

* **Base URL**: `https://api.beyondwords.io/`
* **Format**: The API accepts form-encoded request bodies and returns JSON-encoded responses
* **Design**: Uses predictable resource-oriented URLs and standard HTTP methods
* **Status Codes**: Uses standard HTTP response codes to indicate success or failure

## Authentication

All API requests require authentication using your Project ID and API Key.

### Obtaining credentials

1. Create a project in the dashboard
2. Navigate to **Settings > Integrations > API** to find your Project ID and API Key

### Security best practices

* Your API key carries many privileges, so be sure to safeguard it
* Never share your API key in publicly accessible places such as client-side code or GitHub
* Consider using environment variables to store your API credentials

### Authentication methods

Most endpoints require the `X-Api-Key` header for authentication:

```bash theme={null}
# API request example
curl -X GET "https://api.beyondwords.io/v1/endpoint" \
  -H "X-Api-Key: YOUR_API_KEY"
```

Most endpoints also require your Project ID, which is typically included as a path parameter. Each endpoint in this documentation will clearly indicate whether a Project ID is required.

## Request guidelines

* All API requests must use HTTPS; requests over plain HTTP will fail
* Requests without proper authentication will be rejected with a 401 Unauthorized response
* Include a content-type header of `application/json` for requests with JSON bodies

## Versioning

The API uses versioned endpoints to ensure compatibility:

* Current stable version: `v1`
* Include the version in the URL path: `https://api.beyondwords.io/v1/endpoint`

## Error handling

The API uses conventional HTTP response codes:

* `2xx` - Success
* `4xx` - Client errors (invalid request)
* `5xx` - Server errors

Error responses include a JSON body with details:

```json theme={null}
{
  "error": {
    "code": "invalid_request",
    "message": "A detailed error message",
    "details": { /* Additional context */ }
  }
}
```

## Getting help

If you encounter issues or have questions:

* Contact [support@beyondwords.io](mailto:support@beyondwords.io)

# Get player by content ID
Source: https://docs.beyondwords.io/api-reference/player/show

get /projects/{project_id}/player/by_content_id/{id}
Gets player data related to a content item

# Get player by playlist ID
Source: https://docs.beyondwords.io/api-reference/player/show-1

get /projects/{project_id}/player/by_playlist_id/{id}
Gets player data related to a playlist

# Get player by source ID
Source: https://docs.beyondwords.io/api-reference/player/show-2

get /projects/{project_id}/player/by_source_id/{id}
Gets player data related to a content item

# Get player by source URL
Source: https://docs.beyondwords.io/api-reference/player/show-3

get /projects/{project_id}/player/by_source_url/{url}
Gets player data related to a content item

# Get player by multiple identifiers
Source: https://docs.beyondwords.io/api-reference/player/show-4

get /projects/{project_id}/player/by_identifiers/{array}
Gets player data related to a content item

# Create playlist
Source: https://docs.beyondwords.io/api-reference/playlists/create

post /projects/{project_id}/playlists
Creates a playlist in a project

# Delete playlist
Source: https://docs.beyondwords.io/api-reference/playlists/delete

delete /projects/{project_id}/playlists/{id}
Deletes a custom playlist from a project

# List playlists
Source: https://docs.beyondwords.io/api-reference/playlists/list

get /projects/{project_id}/playlists
Lists playlists within a project

# Get playlist
Source: https://docs.beyondwords.io/api-reference/playlists/show

get /projects/{project_id}/playlists/{id}
Gets a playlist from a project

# Get playlist settings
Source: https://docs.beyondwords.io/api-reference/playlists/show-1

get /projects/{project_id}/playlists/{playlist_id}/settings
Gets the feed settings for a playlist

# Update playlist
Source: https://docs.beyondwords.io/api-reference/playlists/update

put /projects/{project_id}/playlists/{id}
Updates a playlist in a project

# Update playlist settings
Source: https://docs.beyondwords.io/api-reference/playlists/update-1

put /projects/{project_id}/playlists/{playlist_id}/settings
Updates the feed settings for a playlist

# Create project
Source: https://docs.beyondwords.io/api-reference/projects/create

post /projects
Creates a project in your organization

# Delete project
Source: https://docs.beyondwords.io/api-reference/projects/delete

delete /projects/{id}
Deletes a project

# List projects
Source: https://docs.beyondwords.io/api-reference/projects/list

get /projects
Lists all projects in your organization

# Get project
Source: https://docs.beyondwords.io/api-reference/projects/show

get /projects/{id}
Gets a project from your organization

# Update project
Source: https://docs.beyondwords.io/api-reference/projects/update

put /projects/{id}
Updates a project in your organization

# Get project voices
Source: https://docs.beyondwords.io/api-reference/projects/voices

get /projects/{id}/voices
Gets a project voices

# Create pronunciation rule
Source: https://docs.beyondwords.io/api-reference/rules/create

post /rules
Creates a rule in a organization

# Delete pronunciation rule
Source: https://docs.beyondwords.io/api-reference/rules/delete

delete /rules/{id}
Deletes a rule from your organization

# List pronunciation rules
Source: https://docs.beyondwords.io/api-reference/rules/list

get /rules
Lists rules in a organization

# Get pronunciation rule
Source: https://docs.beyondwords.io/api-reference/rules/show

get /rules/{id}
Gets a rule from your organization

# Update pronunciation rule
Source: https://docs.beyondwords.io/api-reference/rules/update

put /rules/{id}
Updates rule in a organizaiton

# Get project summarization settings
Source: https://docs.beyondwords.io/api-reference/summarization-settings/show

get /projects/{project_id}/summarization_settings
Get the summarization settings for your project

# Update project summarization settings
Source: https://docs.beyondwords.io/api-reference/summarization-settings/update

put /projects/{project_id}/summarization_settings
Update the summarization settings for your project

# Get video settings
Source: https://docs.beyondwords.io/api-reference/video-settings/show

get /projects/{project_id}/video_settings
Get the video settings for your project

# Update video settings
Source: https://docs.beyondwords.io/api-reference/video-settings/update

put /projects/{project_id}/video_settings
Update the video settings for your project

# Members and Roles
Source: https://docs.beyondwords.io/docs-and-guides/administration/members-and-roles

Learn how to manage team members and their roles in BeyondWords

## Overview

In BeyondWords, you can manage team members and their roles in the **Members** section. Click on the top left menu and go to **Organization > Members**.

The Members page, which can be found by going to Organization > Members, shows a list of current members. Here, you can see each member that belong to your organization, their role, their status, and their join date.

## Invite a member to your organization

To invite a member to your organization:

1. Go to **Organization > Members > All members**.
2. Click the **Invite** button.
3. Enter the email address of the person you want to invite.
4. Enter the first name and last name of the person you want to invite.
5. Select the role for the person you want to invite.
6. Add a profile picture (optional).
7. You can select the project(s) you want your invitee to automatically join.
8. Click **Send invite**. New members will receive an invite link via email along with steps to join the project.

<Note>
  In case an email server is filtering out invitation emails, we recommend whitelisting [support@mail.beyondwords.io](mailto:support@mail.beyondwords.io) as a trusted sender in email settings.
</Note>

## Resend an invite

To resend an invite:

1. Go to **Organization > Members > All members**.
2. Click the **⋯** next to the member you want to resend the invite to and then click **Resend invite**.

## Remove a member from your organization

To remove a member from your organization:

1. Go to **Organization > Members > All members**.
2. Click the **⋯** next to the member you want to remove and then click **Delete**.

## Change a member's role

To change a member's role:

1. Go to **Organization > Members > All members**.
2. Click the **⋯** next to the member you want to change the role of and then click **Edit**.
3. Select the new role from the dropdown menu.
4. Click **Save changes**.

## Change a member's project access

To change a member's project access:

1. Go to **Organization > Members > All members**.
2. Click the **⋯** next to the member you want to change the project access of and then click **Edit**.
3. Add or remove projects from the member's project access.
4. Click **Save changes**.

Alternatively, you can change a member's project access by going to \*\*Project > **Settings > Members**.

## Create a new role

To create a new role:

1. Go to **Organization > Members > Roles**.
2. Click the **+ Role**.
3. Enter the name of the new role.
4. Select the permissions for the new role.
5. Click **Save changes**.

## Edit a role

To edit a role:

1. Go to **Organization > Members > Roles**.
2. Click the **⋯** next to the role you want to edit and then click **Edit**.
3. Edit the name and permissions of the role.
4. Click **Save changes**.

<Note>
  You cannot edit the Owner role.
</Note>

## Delete a role

To delete a role:

1. Go to **Organization > Members > Roles**.
2. Click the **⋯** next to the role you want to delete and then click **Delete**.
3. Click **Confirm** to delete the role.

<Note>
  You cannot delete the Owner, Admin or Collaborator roles.
</Note>

# Organization
Source: https://docs.beyondwords.io/docs-and-guides/administration/organization

Update your organization details in BeyondWords

### How to update your organization details

<Steps>
  <Step title="Go to the Organization settings">
    Click on the top left menu and select Organization.
  </Step>

  <Step title="Update organization details">
    <Info>
      Your organization name will be visible to your team.
    </Info>

    In organization settings, you can update the following:

    * Organization name
    * Legal name
    * Website
    * Address
      * Address line 1
      * Address line 2
      * City
      * State
      * Zip code / Post code
      * Country
  </Step>

  <Step title="Save changes">
    Click on the "Save changes" button to save the changes.
  </Step>
</Steps>

# Profile
Source: https://docs.beyondwords.io/docs-and-guides/administration/profile

Update your profile in BeyondWords

### How to update your profile details

<Steps>
  <Step title="Go to Profile settings">
    Click on the top left menu and select Profile.
  </Step>

  <Step title="Update profile details">
    <Info>
      Your profile details will be visible to your team.
    </Info>

    In profile settings, you can update the following:

    * First name
    * Last name
    * Profile picture
  </Step>

  <Step title="Save changes">
    Click on the "Save changes" button to save the changes.
  </Step>
</Steps>

<Tip>
  To update your email address, please contact support.
</Tip>

# Projects
Source: https://docs.beyondwords.io/docs-and-guides/administration/projects

Create and update your projects in BeyondWords

In BeyondWords, all your content is organized into Projects. A Project is your AI audio CMS.

## Create a project

<Steps>
  <Step title="Click + Project">
    Click on the top left menu and click **+ Project**.
  </Step>

  <Step title="Enter a name">
    Enter a name for your project.
  </Step>

  <Step title="Set your project language and accent">
    Select the language and accent for your project.
  </Step>

  <Step title="Upload a logo (optional)">
    Upload a logo for your project. This will make it easier to identify your project in the future.
  </Step>

  <Step title="Save changes">
    Click **Save changes** to create your project.
  </Step>
</Steps>

## Update project settings

Click on the top left menu and click on the project you want to update. Go to the **Settings** tab and click **General**. Here you will be able to update the following:

* **Project name** - The name of your project.
* **Project logo** - The logo of your project.
* **Project time zone** - The time zone of your project.

<Info>
  Choose the time zone for scheduling and analytics reporting in your project.
</Info>

* **Automatic publishing** - Whether to automatically publish articles. Enabled by default.

<Tip>
  To update the default project language, accent and voice, go to the **Voice** tab.
</Tip>

# Quota
Source: https://docs.beyondwords.io/docs-and-guides/administration/quota

Manage your usage limits and quotas

## Overview

Each BeyondWords plan has a fixed quota. This quota is shared between all your projects. You can see your quota in the quota widget in the bottom left corner of each project.

## Article quota

Each subscription plan includes a specific article quota, which is the maximum number of articles you can generate into audio each month. We consider one article to be up to 5,000 characters, including spaces. Therefore, if an article exceeds this limit, such as being 7,000 characters, it will count as two articles.

### Regenerating articles

When you edit an article, such as changing a word in a paragraph and regenerating the audio, this will not count towards your quota. However, changing voices or adding new paragraphs will affect your article limit if the total article size exceeds 5,000 characters.

### Rollover policy

Please note that unused articles will not roll over to the next billing cycle, and deleting audio will not restore your article count. The monthly quota renews based on the start date of your subscription.

## Plan changes

### Upgrading your plan

If you upgrade your plan, the upgrade takes effect immediately. Your quota will be refreshed with the new article quota limit, and any unused articles from your previous plan will not roll over. Your first payment will be adjusted accordingly if necessary.

### Downgrading your plan

If you downgrade your plan, the change will not take effect until the end of your current billing cycle. On the first day of your new billing cycle, your quota will be updated to reflect your new plan, and any unused articles from your previous plan's quota will be lost. Your subscription will automatically renew at the end of each billing cycle, and your article quota will reset.

## Usage-based pricing

For Personal, Pro, Plus, and Premium plans, you can enable usage-based pricing, which allows you to access additional articles after your monthly quota is exhausted.

The cost per additional article varies by plan:

* Personal: \$0.90 per article
* Pro: \$0.70 per article
* Plus: \$0.60 per article
* Premium: \$0.50 per article

You can enable usage-based billing and set a monthly limit in the **Organization > Subscriptions > Overage** section. Additional charges will be billed at the end of your billing cycle or whenever your account reaches \$25 in usage, whichever occurs first.

# SAML SSO
Source: https://docs.beyondwords.io/docs-and-guides/administration/saml-sso

Learn how to enable SAML for your Organization to manage logins through an Identity Provider

## SAML setup

Organizations on BeyondWords can enable SAML to centralize login management through their Identity Provider (IdP), such as Okta, Microsoft Entra ID, OneLogin, LastPass, Auth0, Bitium, and others.

<Note>
  Available to organizations on the Enterprise plan
</Note>

## 1. Setting up SAML

To set up SAML for your organization:

### Contact support

Reach out to our team at [support@beyondwords.io](mailto:support@beyondwords.io) from the account associated with the organization owner or an admin. Request SAML to be enabled.

### Receive your setup link

We'll share a unique configuration URL where you can connect your Identity Provider. We support most major providers including:

* Okta
* Microsoft Entra ID
* OneLogin
* LastPass
* Auth0
* Bitium
* … and other SAML 2.0-compliant providers.

### Configure the connection

Follow your Identity Provider's documentation to complete the SAML configuration using the URL we provide. If needed, we're happy to assist with setup or troubleshooting.

## What happens once SAML is enabled?

* All members of your organization will be required to log in via your Identity Provider using SAML.
* Email/password login and social sign-in methods (e.g. Google) will be disabled for those users.
* Sessions will remain active until logout, but users must use SAML to log back in.
* Members can sign in via your IdP's dashboard or click ["Continue with SAML SSO"](https://dash.beyondwords.io/auth/sso-login) on the BeyondWords login page.

## 2. Adding users with SAML enabled

Once SAML is enabled, inviting users requires two steps:

### Invite the user to your BeyondWords organization

1. In BeyondWords, navigate to Organization > Members.
2. Click Invite, then enter the user’s email address to send the invitation.

### Provision the user in your Identity Provider

1. Ensure the user is also added to your IdP and assigned to the BeyondWords SAML application.
2. If they are only invited in BeyondWords or only added in your IdP, they won't be able to log in.

<Note>
  Both steps must be completed. Inviting someone in BeyondWords without provisioning them in your IdP—or vice versa—won't grant them access.
</Note>

If you have questions during setup or encounter any issues, our support team is here to help at [support@beyondwords.io](mailto:support@beyondwords.io).

# Subscriptions
Source: https://docs.beyondwords.io/docs-and-guides/administration/subscriptions

Manage your subscription and billing

When you sign up, you’ll automatically start on the **Pilot** plan. To check your subscription, go to **Organization > Subscriptions > Plans**. You’ll find a breakdown of all available plans, plus a comparison table to help you see what’s included in each.

## Change your plan

To change your plan, go to **Organization > Subscriptions > Plans**. Select the plan you want to change to and click **Upgrade** or **Downgrade**.

We offer five public plans: Pilot, Personal, Pro, Plus, Premium. For larger organizations, there’s also an Enterprise option, tailored to specific needs and usage.

## Cancel your subscription

To cancel your subscription, go to **Organization > Subscriptions > Billing**. Click **Cancel** and follow the instructions.

## Change your billing information

To change your billing information, go to **Organization > Subscriptions > Billing**. Click **Manage billing**. You will be redirected to Stripe where you can update your billing information.

## Change your payment method

To change your payment method, go to **Organization > Subscriptions > Billing**. Click **Manage billing**. You will be redirected to Stripe where you can update your payment method.

## Change your billing email

To change your billing email, go to **Organization > Subscriptions > Billing**. Click **Manage billing**. You will be redirected to Stripe where you can update your billing email.

## Change your billing address

To change your billing address, go to **Organization > Subscriptions > Billing**. Click **Manage billing**. You will be redirected to Stripe where you can update your billing address.

## Add your Tax ID/VAT number

To add your Tax ID/VAT number, go to **Organization > Subscriptions > Billing**. Click **Manage billing**. You will be redirected to Stripe where you can add your Tax ID/VAT number.

## Change your billing country

To change your billing country, go to **Organization > Subscriptions > Billing**. Click **Manage billing**. You will be redirected to Stripe where you can change your billing country.

# Usage analytics
Source: https://docs.beyondwords.io/docs-and-guides/administration/usage

Track article and character usage across your whole organization.

## Overview

Usage analytics gives you a complete view of how your organization is using BeyondWords. You can track the total number of articles and characters processed, filter by date range, and adjust the level of detail (daily, weekly, monthly). You can also break usage down by project to understand where most activity is happening.

<img alt="usage" />

### Metric

#### Unique articles

The number of articles that have been processed and generated.

#### Billed articles

Articles counted for billing, where every **5,000 characters = 1 billed article**.

#### Billed characters

The characters that count towards your billing and quota.

#### Total characters

All characters processed, including those not billed (e.g. regenerated or edited content).

### Date range

Choose the time period you want to analyze. You can select the current **billing period**, **month**, **year**, or define a **custom date** range.

### Granularity

Set the level of detail for your analytics. Choose whether to view usage by **hour**, **day**, **week**, **month**, or **year**. You can also select **cumulative** to see totals over the entire date range.

### Breakdown

#### Voice

See which of your voices are being used for audio generation. Select a voice to view how many characters have been generated using it.

<Note>
  This option is only available when the selected metric is **Billed characters** or **Total characters**.
</Note>

#### Project

Break down your usage by project. You can select up to five projects at a time for comparison.

#### Content

Once a project is selected, you can further break down usage by individual articles. Filter results by entering either a **content ID** or **source ID**.

<Note>
  This option is only available when at least one **project** is selected.
</Note>

# Event Schema
Source: https://docs.beyondwords.io/docs-and-guides/analytics/event-schema

Learn about the structure of analytics events

## Overview

Analytics events are simple JSON objects that are emitted by the BeyondWords
Player. They contain information about user engagement. They are separate from
[player events](/docs-and-guides/distribution/player/sdk/javascript/player-events)
which contain information about the current state of the player.

Analytics events can be sent to three possible places:

1. The BeyondWords dashboard via our ingestion endpoint (metrics.beyondwords.io)

2. A custom analytics URL that you have configured (see [Analytics > Preferences](/docs-and-guides/analytics/preferences#send-data-to-custom-analytics-url)).

3. A Google Analytics account that you have configured (see [Analytics > Preferences](/docs-and-guides/analytics/preferences#send-data-to-custom-analytics-url)).

In all cases, the event schema is identical. You can inspect the events that
are sent by searching for metrics.beyondwords.io in the Network tab.

## Example event

```javascript Example event theme={null}
{
  "event_type": "play",
  "device_type": "desktop",
  "media_type": "content",
  "media_variant": "article"
  "project_id": 123,
  "content_id": "3f57001d-cb30-42c1-ad6f-047e813c360f",
  "source_id": "example-source-id",
  "analytics_id": 333,
  "ad_id": null,
  "media_id": 555,
  "media_format": "audio",
  "local_storage_id": "bef9218d-3871-450e-a7fa-5da65102f532",
  "listen_session_id": "839ff785-0cb8-4e74-a061-506f571c79ce",
  "session_created_at": 1672531200000,
  "duration": 123.45,
  "listen_length_seconds": 0.2,
  "listen_length_percent": 0.1620089105,
  "speed": 1,
  "segment_playback_enabled": true,
  "location": "https://example.com",
  "referrer": "https://example.com"
  "player_version": "1",
  "player_npm_version": "1.2.3",
}
```

## Event schema

<ParamField type="string">
  The type of analytics event. There are four types:

  * **load**: content loaded successfully and the media's duration is known
  * **play**: the media started playing for the current content item
  * **play\_progress**: playback reached the next 10% of the audio's duration
  * **ad\_link\_click**: the user clicked on the click-through URL for an advert
</ParamField>

<ParamField type="string">
  The type of device that emitted the event. There are three types:

  * **phone**: the width of the browser was between 0px and 499px
  * **tablet**: the width of the browser was between 500px and 999px
  * **desktop**: the width of the browser was 1000px or greater
  * **ios**: the event was sent from a native ios app (e.g. <a href="https://github.com/beyondwords-io/player-ios">player-ios</a>)
  * **android**: the event was sent from a native android app (e.g. <a href="https://github.com/beyondwords-io/player-android">player-android</a>)
</ParamField>

<ParamField type="string">
  The type of media loaded in the player. There are two types:

  * **content**: the event was emitted during content playback
  * **ad**: the event was emitted during advert playback
</ParamField>

<ParamField type="string">
  The variant of media loaded in the player. There are two types:

  * **article**: the media is for the original article
  * **summary**: the media is for a summary of the article
</ParamField>

<ParamField type="integer | null">
  The numeric ID of the project whose content is loaded into the player.
  This field might be null if content wasn't fetched from the API and is instead set manually in the player.
</ParamField>

<ParamField type="string | integer | null">
  The string UUID or numeric ID of the content currently loaded into the player.
  This field might be null if content wasn't fetched from the API and is instead set manually in the player.
</ParamField>

<ParamField type="string | null">
  The string ID that can optionally be associated with the content currently loaded into the player.
  This field might be null if the source\_id ID wasn't set in the BeyondWords API.
</ParamField>

<ParamField type="integer | null">
  A numeric ID used by BeyondWords for associating this event with your project.
  This field might be null if content wasn't fetched from the API and is instead set manually in the player.
</ParamField>

<ParamField type="integer | null">
  The numeric ID of the advert that is currently loaded into the player.
  This field is null when an advert isn't playing, i.e. when content is playing.
</ParamField>

<ParamField type="integer | null">
  The numeric ID of the content or advert media field that is currently loaded into the player.
  This field is null when VAST adverts are playing.
</ParamField>

<ParamField type="string">
  The format of media loaded in the player. There are two formats:

  * **audio**: the player is playing audio (or will play audio)
  * **video**: the player is playing video (or will play video)
</ParamField>

<ParamField type="string | null">
  A string UUID associated with the current user and stored in local storage under the 'beyondwords' key.
  This field is null if advertConsent is set to 'without-local-storage'.
</ParamField>

<ParamField type="string">
  A string UUID associated with the current player instance.
  This ID changes after the page is reloaded and is different for each player instance.
</ParamField>

<ParamField type="integer">
  The unix time in milliseconds at which the first analytics event was sent from the current player instance, as reported by the user's browser.
</ParamField>

<ParamField type="float">
  The duration in seconds of the content or advert media currently loaded into the player.
</ParamField>

<ParamField type="float">
  The duration in seconds that the user has listened to of the currently loaded media.
</ParamField>

<ParamField type="float">
  The percentage that the user has listened to of the currently loaded media.
</ParamField>

<ParamField type="float">
  The speed at which the user is listening to the media, e.g. 0.5, 1 or 2.
</ParamField>

<ParamField type="boolean">
  Whether playback from segments is enabled, i.e. whether the clickableSections player setting is anything other than "none".
</ParamField>

<ParamField type="string">
  The value of window\.location.href when the event was emitted.
</ParamField>

<ParamField type="string">
  The value of document.referrer when the event was emitted.
</ParamField>

<ParamField type="string">
  This will always be the string "1" but we may use this later, e.g. to run A/B tests.
</ParamField>

<ParamField type="string">
  The version of the NPM package as specified in the package.json file.
</ParamField>

## Sending your own events

If you are not using the BeyondWords player and have instead built your own
player, you can still send analytics to BeyondWords and we will aggregate them
and present them in the BeyondWords dashboard.

A **POST** request should be sent to `https://metrics.beyondwords.io` according to
the schema above. Please try to provide all fields so that events can be
aggregated and presented correctly to the user. However, if some fields are
missing, we will provide sensible defaults.

For example, `media_variant` will default to `"article"`, `media_format` will
default to `"audio"` and `device_type` will default to `'desktop"`. We recommend
you do not rely on these defaults if you are able to provide the data in the
unlikely event that the defaults change in the future.

Some fields may not be applicable (e.g. `player_npm_version`). In that case, it
is fine to leave the fields blank and they will be ignored. It may be helpful to
refer to the [player implementation](https://github.com/beyondwords-io/player/blob/main/src/helpers/sendToAnalytics.ts)
for more information about how a particular field is handled.

To test custom events, there may be a delay before they appear in the BeyondWords
dashboard. You may need to wait an hour or more for the events to appear.
If you are having trouble or are unsure what to set a field to, please contact
[support@beyondwords.io](mailto:support@beyondwords.io).

# Player
Source: https://docs.beyondwords.io/docs-and-guides/analytics/player

Track and analyze audio engagement

## Overview

The BeyondWords player tracks how your audience engage, distilling data into a set of key metrics for clear and actionable insights.

<img alt="player" />

## Metrics

BeyondWords tracks the following metrics on a per-project and per-article basis. The metrics are updated every few minutes.

### Plays

The number of times users hit play. We count one play per user session.

### Loads

The number of times a page was loaded with the player. We count one load per user session.

### Engagement rate

The percentage of Loads that converted into Plays. We calculate this as Plays divided by Loads.

### Unique users

The number of unique users who hit play. We identify users with an anonymous ID stored in their browser.

### Avg. playback duration

The average percentage completed per play. We measure this across all plays.

### Drop-off analysis

The percentage of users remaining at each 10% interval. Shows how many continue from start to finish.

### Playback time

The cumulative playback time of all plays. We measure this across all plays.

### Avg. playback time

The average time spent per play. We measure this across all plays.

### Device analysis

The percentage of users who played on each device.

## Filter metrics

You can filter the metrics by the following:

* **Content type**: Articles or Summaries
* **Device**: Desktop, Mobile (web), Tablet (web), iOS (SDK), Android (SDK)
* **Date range**: All time, Month to date, Today, Yesterday, Last 7 days, Last 14 days, Last 30 days, Last 90 days, Last 180 days, Custom

# Preferences
Source: https://docs.beyondwords.io/docs-and-guides/analytics/preferences

Configure analytics settings and preferences

## Overview

You can configure analytics preferences for your project. Go to **Project > Analytics > Preferences**

<img alt="player" />

### General

#### Track analytics

You can enable or disable analytics tracking for your project. You will need to **Save changes** to apply changes.

#### Track unique users

You can enable or disable unique user tracking for your project. You will need to **Save changes** to apply changes.

## Integrations

### Send data to Google Analytics

To send data to Google Analytics:

1. Enter your Google Analytics tracking ID.
2. Turn on **Send data to Google Analytics**.
3. Click **Save changes**.

#### BeyondWords metrics in Google Analytics

A page view involving an embedded BeyondWords Player will trigger one of five events, which together form the BeyondWords Player Event Category.

| Event        | Recorded When...                                              |
| ------------ | ------------------------------------------------------------- |
| Load         | The BeyondWords Player loads on the webpage.                  |
| Play         | A user clicks 'play' on a BeyondWords Player.                 |
| x% Listened  | A user plays a percentage of the audio (e.g. 10%, 20%, etc.)  |
| Advert Click | A user clicks the advertised link while an advert is playing. |
| Complete     | A user plays 100% of the audio.                               |

#### Create BeyondWords Player Event reports

You can create reports for specific events - for example, the **Play** action:

1. Go to **Explore** in the left sidebar and click on **Blank** to create a new exploration.
2. Give the exploration a name and then click **+** besides **Segments** followed by **Create a new segment**.
3. Choose **Event segment** as the segment type.
4. Enter a segment name and description — for example, **BeyondWords Player plays**.
5. In the **Add new condition** dropdown, select the dimension **Event** and choose **Event name**.
6. Press **Add filter** and edit the condition to contain the event **Play** and select **Apply**.
7. Add the dimension **Page title** in dimensions and metric **Event count** in metrics.
8. Add the imported segments, dimensions and metrics in the **Settings** tab to build a report.
9. You can now view the event count for specific pages which can better help you analyze your audience engagement. You can also import different dimensions and metrics to build meaningful reports that suit your needs.

### Send data to Custom analytics URL

To send data to a custom analytics URL:

1. Enter the URL to send data to.
2. Turn on **Send data to Custom analytics URL**.
3. Click **Save changes**.

You will need to provide an endpoint that can receive the events. Events will
be sent as POST requests according to the [Event Schema](/docs-and-guides/analytics/event-schema).

### Cross-origin requests

If your endpoint is located on a different domain than the player, you will
also need to support OPTIONS requests and respond with the necessary headers to
support cross-origin requests. Here are the headers we set on our own
metrics.beyondwords.io endpoint for reference:

```sh theme={null}
curl -I -X OPTIONS https://metrics.beyondwords.io

HTTP/2 204
date: Mon, 1 Jan 2026 12:00:00 GMT
content-type: text/plain; charset=utf-8
access-control-allow-origin: *
access-control-allow-credentials: true
access-control-allow-headers: Content-Type,Access-Control-Allow-Headers,Authorization,X-Requested-With
access-control-allow-methods: POST,OPTIONS
access-control-max-age: 1728000
```

The browser will send the OPTIONS request first and if it succeeds, the POST
request will be sent to the custom endpoint.

# Changelog
Source: https://docs.beyondwords.io/docs-and-guides/changelog

BeyondWords product updates and announcements

<Update label="January 19th 2025" description="Summarization update">
  ### Script Templates (formerly Summarization)

  We’ve renamed Summarization to Script templates, giving you more control over how articles are rewritten for audio and video.

  Instead of only summarizing content, BeyondWords can now adapt articles into different storytelling formats designed for listening and watching. Script Templates work seamlessly with both audio and video, helping you create content that fits the platform and audience.

  **Whats New:**

  * **Summaries → Scripts**: The feature has been renamed to reflect its broader purpose—transforming articles into scripts, not just summaries.

  * **Script Templates**: Choose from our default templates to control structure, tone, and length before audio and video are generated, or create your own custom template.

  * **Built for video & audio**: Scripts are optimized for spoken delivery and visual storytelling, improving performance in both audio and video formats.

  * **Pre-made storytelling formats**: Use ready-to-go templates like Summary, Hook & Payoff, and Presenter Voiceover for different engagement goals and platforms.

  * **Custom templates**: Create your own instructions to match your editorial style, brand voice, or video strategy.

  * **Works with Style Templates**: Pair Script Templates with Style Templates to control both the narrative and the visual presentation of your videos.

  Scripts can be enabled automatically for new content or applied manually on an article-by-article basis, giving you flexibility while scaling audio and video output.

  Want to explore how this could benefit your team’s workflow? Feel free to [reach out](mailto:support@beyondwords.io) or have a read of our [Script documentation](/docs-and-guides/content/preferences/summarization) to get started.
</Update>

<Update label="December 18th 2025" description="Video update">
  ### Video 2.0 (Beta)—Scalable video for every newsroom

  We’ve launched an update to our video feature in BeyondWords, making it even easier to turn articles into engaging, branded videos at scale. Visit the blog to see [article-to-video demos](https://beyondwords.io/blog/introducing-scalable-video-for-every-newsroom/) or learn how to get started in our [video docs](https://docs.beyondwords.io/docs-and-guides/content/preferences/video).

  **Whats New:**

  * **Style Templates**: Videos are generated using Style Templates that control layout and branding, ensuring consistent styling across all videos.

  * **Enhanced caption animations**: New caption styles and animations to improve readability and engagement.

  * **Enhanced media animations**: Improved transitions and motion effects for both images and video clips.

  * **Multiple formats**: Generate both vertical and horizontal videos, with image resizing to support different platforms.

  * **Video segments**: Articles can now include video clips as well as images, allowing generated videos to combine both media types within a single video.

  * **Getty Images integration**: Enhance videos with access to the Getty Images library.

  * **Featured Video**: Set a feature video to have a video —rather than images— play in the background of your video

  Video can be enabled [automatically](https://docs.beyondwords.io/docs-and-guides/content/preferences/video#create-videos-for-all-articles) for new content or generated [manually](https://docs.beyondwords.io/docs-and-guides/content/preferences/video#create-or-edit-a-video-for-a-specific-article) on an article-by-article basis.

  <Note>Please [reach out](mailto:support@beyondwords.io) if you’d like any assistance testing this or setting it up.</Note>
</Update>

<Update label="November 26th 2025" description="Voice update">
  ### ElevenLabs voices now available

  * We’ve added 91 new **[ElevenLabs voices](https://beyondwords.io/blog/elevenlabs-ai-voices-voice-cloning-live-in-beyondwords/)** to the dashboard.
  * Available across 20+ languages

  <Note>Feel free to [reach out](mailto:support@beyondwords.io) if you have any questions or would like personalized recommendations.</Note>

  ***

  ### New voice settings

  Gain finer control over the AI voices you use in BeyondWords. To update a voice’s settings, go to **“Content” → “Voices” → “Preferences”** in your dashboard and select `…` → `Settings` alongside the voice.

  * **Multilingual mode**: Automatically detects foreign words and switches languages when needed.
  * **Speaking rate**: Adjust the voice’s speaking speed.
  * **Expressiveness**: Controls how varied and emotional the delivery sounds.  *(Available on Azure HD and ElevenLabs voices)*
    * Lower values = steadier, more consistent
    * Higher values = more emotive and varied, but less consistent
  * **Similarity**: Determines how closely the output matches the original speaker’s tone and character. *(Available on ElevenLabs voices)*
  * **Style**: Controls how stylized or expressive the delivery is compared to the original speaker. *(Available on ElevenLabs voices)*
  * **Speaker boost**: Enhances clarity and presence to better match the original speaker. *(Available on ElevenLabs voices)*

  <Note>**Similarity**, **Style**, and **Speaker Boost** work best when used with professional voice clones, as these settings are designed to enhance high-quality voice recordings.</Note>
</Update>

<Update label="November 10th 2025" description="WordPress plugin">
  **Version 6.0.0**

  ### Enhancements and Features

  **[#449](https://github.com/beyondwords-io/wordpress-plugin/pull/449)** – Added support for Magic Embed integration within the plugin.

  * A new Magic Embed option has been added under **Content > Integration method** in the plugin settings.
  * This option is intended for users working with page builders such as **Elementor**, who may have experienced issues getting the REST API to function correctly during initial setup.
  * Enabling Magic Embed will automatically add the Magic Embed script to each of your posts.

  **For correct functionality:**

  * Magic Embed must be selected in the WordPress plugin.
  * Magic Embed must also be [enabled and configured](https://docs.beyondwords.io/docs-and-guides/integrations/magic-embed/overview#setup) in your BeyondWords dashboard.

  <Note>Posts previously created using the REST API will continue to use that method.</Note>

  Refer to our [Magic Embed documentation](https://docs.beyondwords.io/docs-and-guides/integrations/magic-embed/overview) for more information.

  If your plugin is already working as expected with the REST API, we recommend continuing to use that integration.

  ***

  ### Fixes

  **[#457](https://github.com/beyondwords-io/wordpress-plugin/pull/457)** – Removed segment marker assignment.

  * Fixes a reported JS issue where the block editor “+” button was not being displayed.

  #### Code Coverage

  **[#455](https://github.com/beyondwords-io/wordpress-plugin/pull/455)** – Increased PHPUnit test coverage.

  #### Refactoring

  **[#454](https://github.com/beyondwords-io/wordpress-plugin/pull/454)** – Added PHP type declarations.\
  **[#447](https://github.com/beyondwords-io/wordpress-plugin/pull/447)** – Made PHP methods static.

  #### Compatibility

  * **PHP 8.1** is now the minimum supported version.
</Update>

<Update label="October 2025" description="Administration update">
  **Usage analytics**

  Track detailed usage analytics across all your projects in one place.

  * **Quota visibility**: See exactly how your quota is being spent, making it easier to stay organized and plan ahead.
  * **Flexible filtering**: Filter by project, time range, or voice to understand usage patterns across different teams or brands.

  To explore your report, head to **Organization** → **Usage** in your dashboard. For more details, read our [documentation](/docs-and-guides/administration/usage).
</Update>

<Update label="September 2025" description="Product update">
  **Video podcast feeds**

  * Auto-distribute your BeyondWords videos to platforms like YouTube, Spotify, and Apple Podcasts
  * Create your feed under **Distribution** → **Podcast feeds**.

  **Fixes and improvements**

  * **Content extraction**: Introduced new AI-powered extraction mode for finer text-to-audio accuracy.

  * **Quota emails**: Added option to include additional recipients for quota limit alerts.

  * **Summary feeds**: Fix so only summaries (not full articles) appear in summary podcast feeds.

  * **Video text**: Updated to always display article text instead of pre-processed text.
</Update>

<Update label="July 2025" description="Product update">
  **AI preprocessing**

  * Uses context-aware text normalization to automatically correct mispronunciations, improving how dates, scores, measurements, and abbreviations are spoken.

  * Automatically recognises and converts foreign words into their native pronunciations (currently working for English language in German text - to be expanded soon).

  * Can be enabled at either a project level (**Content → Preferences → Pronunciations → AI preprocessing**) or at an article level within the Editor.

  **New editor**

  * Faster, cleaner, and more powerful text-to-speech editor

  * Voice cloning available from inside the Editor, so you can create and assign voices without leaving your workflow.

  * Adjust voice, summarization, and video settings per article.

  * Option to import from URL

  **Fixes and improvements**

  * **Video**: Control caption lines per scene, caption alignment, and article image playback behavior.

  * **Magic Embed**: Improved compatibility with dynamically rendered JavaScript articles.

  * **SAML**: Added Single Sign-On (SSO) support for streamlined and secure enterprise logins.
</Update>

<Update label="December 2024" description="Product update">
  **Magic IPA**

  * A new tool for generating accurate IPA transcriptions—no prompts required.

  * Created in collaboration with linguists and developers to ensure precise phonetic handling for tricky words.

  **Voices**

  * Updated and expanded our library of premade voices, with improved pronunciation and smoother delivery.

  * The latest multilingual voices now support the [language rule](https://docs.beyondwords.io/docs-and-guides/content/preferences/pronunciations#language), enabling accurate pronunciation of foreign words or phrases.
</Update>

<Update label="November 2024" description="Voice update">
  **Professional voice cloning**

  * Major updates to our voice models, improving naturalness while reducing data requirements and training times.

  * Professional voice cloning now supports [84 languages and accents](https://docs.beyondwords.io/docs-and-guides/voices/languages-and-accents).

  **Fixes and improvements**

  * Fixed a bug causing duplicate audio segments during regeneration with new voices.

  * Resolved an issue preventing audio uploads for some users.

  * Fixed a WordPress publishing bug that mistakenly published unpublished audio.

  * Deprecated X-SAMPA support in favor of IPA for phonetic spellings.
</Update>

<Update label="October 2024" description="Product update">
  **WordPress plugin v5.0.0**

  * Tabbed settings interface now includes options from the BeyondWords dashboard.

  * Changes sync automatically between WordPress and the BeyondWords dashboard.

  **Plugin fixes and improvements**

  * Legacy audio player deprecated—the new BeyondWords Player is now the standard for playback.

  * Removed built-in Elementor compatibility—player embeds still work, but won’t appear in Elementor edit screens.

  * Legacy parameter removed: `beyondwords_podcast_id` (posts created with v5.0.0+ won’t play on older plugin versions).

  * Deprecated filters removed—see updated list in our [WordPress Filters documentation](https://docs.beyondwords.io/docs-and-guides/integrations/wordpress/filters).

  **Fixes and improvements**

  * Added WebP image support in the Editor.

  * Updated JS Player SDK—you can now customise time formatting on the player.

  * Fixed issue with unnecessary article regeneration when API updates were off.

  * Added status and publication filters to project filtering.
</Update>

# Audio articles
Source: https://docs.beyondwords.io/docs-and-guides/content/articles

Learn how to manage your audio articles in BeyondWords

## Overview

Audio articles are the core content type in BeyondWords. Each article can also have an **audio summary**, **video article**, and **video summary** associated with it.

In the **Articles** section you will see a list of all your audio articles ordered by the date that they were published. For each article you will be able to see the **Title**, **Duration**, **Publication date**, **Feature image**, **Visibility status**, whether it has a **summary** and or **video**, and a direct link to **analytics**.

<img alt="editor" />

## Import via URL

You can import an article directly into the Editor using the **Import from URL** feature.

1. Click the dropdown arrow (`v`) next to **+ Article** in the top-right corner.
2. Select **Import from URL**.
3. Paste the URL of the article you’d like to import and click **Continue**.
4. Once imported, the article will open in the **Editor**, where it can be edited and generated for audio.

## Article actions

For each article you can do the following by clicking on the **⋯** button:

### Edit the article

This will open the **Editor** where you can edit the article content.

### Regenerate the audio

This will regenerate the audio for the article. Useful for applying new custom pronunciations.

### Replace the audio

This lets you replace the AI-generated audio with a human-recorded version.

### Duplicate the article

This will create a new draft copy of the article that you can edit.

### Download the audio

This will download the audio file for the article.

### Get the embed code

This will open a modal where you can demo the audio in the player and also copy the player embed code.

### Copy the shareable URL

This will copy a URL that you can share with others to listen to the article.

### Copy the identifiers

Here you can copy the **Content ID**, **Source ID**, or **Source URL** for the article.

### Set the visibility

This will toggle the visibility of the article between **Public** and **Private**.

### Delete the article

This will delete the article from your project.

## Summaries <Icon icon="bolt" />

Click the summary icon to generate an audio summary for the article. If a summary already exists, a dialog will open where you can copy the player embed code with the summary or download the summary audio.

## Article videos <Icon icon="https://cdn.jsdelivr.net/npm/@phosphor-icons/core/assets/bold/video-bold.svg" />

Click the video icon to generate a video for the article. If a video already exists, a dialog will open where you can copy the player embed code with the video or download the video.

## Sorting and Filtering

You can search your articles using:

* **Sort by**: Status, Creation Date, Duration, or Published Date
* **Filter by**: Status, Created Date, or Visibility

## Bulk actions

Apply changes to multiple articles at once:

* **Regenerate** audio for multiple articles (useful when updating pronunciations)
* **Set visibility** (Public or Private)
* **Delete** multiple articles

# Data attributes
Source: https://docs.beyondwords.io/docs-and-guides/content/data-attributes

Learn how content extraction can use data attributes.

## Overview

The [Magic Embed](/docs-and-guides/integrations/magic-embed/overview) and
[RSS](/docs-and-guides/integrations/rss-feed-importer) integrations automatically
extract content from your web page such as the title, author, and publish date.
If you wish to explicitly set these fields you can add some data attributes to
your HTML. Additionally, when submitting HTML content through the [API](/api-reference/content/create),
you can use data attributes to explicitly set these fields and control various
aspects of your content.

## Global attributes

The following data attributes can be added anywhere in your web page. In the
example below, they are added to the `<body>` tag:

```html theme={null}
<html>
  <head>
    <title>This title won't be used</title>
  </head>
  <body data-beyondwords-title="My Title"
    data-beyondwords-author="Jane Doe"
    data-beyondwords-publish-date="2023-01-01T12:00:00Z"
    data-beyondwords-published="false"
    data-beyondwords-ads-enabled="false"
    data-beyondwords-title-voice-id="784"
    data-beyondwords-body-voice-id="2194"
    data-beyondwords-summary-voice-id="2194"
    data-beyondwords-article-language="en_GB">
  </body>
</html>
```

**Publish date**

The date at which the article was published. If it is in the future then the
audio will not load in the player until the specified time.

<Note>
  A timezone suffix may be specified, e.g. `Z` or `+01:00`. Defaults to UTC.
</Note>

**Published**

If published is false then the audio will not load in the player, regardless
of the publish date attribute. The audio is still generated and the content will
still appear in the dashboard.

**Voice IDs**

The voices that should be used for the title, summary and body
section of your article. You can copy voice IDs from the voices in the dashboard
under **Project > Preferences > Voices** tab, or fetch them from the
[API](/api-reference/projects/voices#get-project-voices). If not specified, the
default voice for your project will be used.

**Article language**

The default language of your article which affects audio synthesis. If not
specified, the default language for your project will be used.

## Scoped attributes

The following data attributes can be added to your web page to override the
behavior for specific parts of your content.

**Voice IDs**

The following voice IDs will take precedence over the default voice IDs.

```html theme={null}
<p data-beyondwords-voice-id="784">
  This paragraph will be voiced by Joe.
</p>

<div data-beyondwords-voice-id="2194">
  <p>This paragraph will be voiced by Eddie.</p>
  <p>This one, too.</p>
</div>
```

**Language**

The following languages will take precedence over the default language:

```html theme={null}
<p data-beyondwords-language="en_GB">
  This paragraph will be read out in British English.
</p>

<p data-beyondwords-language="fr_FR">
  Ce paragraphe sera lu en français.
</p>
```

**Feature image**

The feature image attribute can be added to an image on your web page to make
it the primary image for your article:

```html theme={null}
<img
   data-beyondwords-feature-image="true"
   src="https://example.com/image.jpeg"
/>
```

The feature image will appear in videos along with any other images extracted
from the HTML.

# Editor
Source: https://docs.beyondwords.io/docs-and-guides/content/editor

Learn how to generate audio using the Editor

## Overview

You can use the Editor to generate and edit audio from text. You can:

* Paste text directly to create audio and make edits.
* Modify audio generated through our API, Magic Embed, or CMS plugins.

Each audio article is structured into segments, typically aligned with article paragraphs. By default, all segments use the project's language and voice, but you can adjust them individually as needed.

<img alt="editor" />

### Use the Editor to generate audio

<Steps>
  <Step title="Open the Editor">
    In your project, go to the Content section and click `"+ Article"` to open the Editor.
  </Step>

  <Step title="Paste your text">
    Paste your article text into the editor. The text paragraphs will be automaticlally split into segments and assigned the the default project language and voice.

    <Tip>
      You can edit the default project language and voice in the [voices tab](/docs-and-guides/content/preferences/voices).
    </Tip>
  </Step>

  <Step title="Generate audio">
    Click the "Generate" button to generate audio for your article.

    <Info>
      It can take a few seconds to generate audio depending on the length of the article. Once generated, the audio will be accessible in the Articles section.
    </Info>
  </Step>
</Steps>

### Use the Editor to modify audio

<Steps>
  <Step title="Open the Editor">
    In your project, go to the Content section, find the Article you want to modify and click on the (•••) menu next to it, and click "Edit".
  </Step>

  <Step title="Modify the audio">
    Edit the text of the segment you want to modify.
  </Step>

  <Step title="Regenerate the audio">
    Click the "Update" button to apply the changes and regenerate the audio for your article.

    <Info>
      It can take a few seconds to regenerate the audio depending on your changes. Once regenerated, the updated audio will be accessible in the Articles section.
    </Info>
  </Step>
</Steps>

## Editor sidepanel

For each audio article in the Editor, you can configure content preferences like voices, summarization, video, background music, visibility, pronunciations, and article information in the left sidebar - giving you full control over how your audio is generated and distributed.

### Voices

In the Voices tab, you can either select one of our premade voices or upload your own to create a custom voice clone for your articles.

1. **Premade voice**:  choose your preferred language and accent, click the dropdown (`⌄`) to view the available voices. To preview a voice, hover over the icon next to the name and click the Play button.
2. **Instant Voice Clone**: To clone a voice for your article click the `+` button and follow the instructions to create an instant voice clone. You’ll need to record or upload a voice sample along with a consent statement.

For more details, see the [Instant Voice Cloning](/docs-and-guides/voices/voice-cloning/instant-voice-cloning) section of our documentation.

### Summary

In the Summarization tab, you can manage your article's summary settings. Choose whether to generate a summary, and if enabled, customize it by editing the system prompt. Click `"Generate Summary"` to generate a summary, which you can edit. The final summary will be generated when you update the article.

You are also able to adjust the temperature of the summarized response. A lower value (closer to 0) will produce a more consistent and predictable summary, while a higher value allows for more variation and creative language.

<Note>
  You will need to generate the audio for your article before you can generate a summary.
</Note>

### Video

In the Video tab, you can manage your article’s video settings. Choose whether to generate a video, and if enabled, customize it using the available options. The video will be created when you generate or update the article.

For more detailed information on video settings and customization, visit the [video](/docs-and-guides/content/preferences/video) section of our documentation.

### Background track

In the Background Track tab, you can manage background audio settings for your article. You can choose to include a background track, upload your own, and apply it. The track will be added when you generate or update the article.

### Pronunciations

In the Pronunciations tab you can configure which custom pronunciations will be applied when generating the audio for your article.

Enable AI preprocessing to improve text normalization (e.g. numbers, scores) and automatic language detection.

You can enable this per article or across your project in [Content Preferences](/docs-and-guides/content/preferences/pronunciations).

<Note>
  This feature is in Beta, we recommend testing it to ensure compatibility with your content
</Note>

### Info

The Info tab lets you update your article’s settings and metadata.

#### Visibility

In the Visibility dropdown, you can manage your article’s visibility settings. Choose whether the player should be public (visible) or private (hidden).

Set when visibility should take effect by selecting `Once generated` or `Specific date`.

#### Author

The article author. This data can be used to create Smart Playlists.

#### IDs

* **ID**: Copy the article content ID. This is the ID that we assign to the article after it's generated.
* **Source ID**: Copy or edit the article source ID. This ID is user-defined at the time of audio generation.
  We recommend using the article ID from your CMS as the source ID.
* **Source URL**: Copy or edit the article Source URL. We recommend using the article URL as the source URL.

<Note>
  All three can be used as [identifiers](/docs-and-guides/distribution/player/overview#identifiers) to initalise the player.
</Note>

#### Title

Automatically taken from the first segment of your article, but can be edited here if needed.

#### Properties

Add or edit custom properties for the article using JSON format.
We recommend including metadata like the article’s category (e.g. `{ "category": "sport" }`).

These properties can be used to power [Smart Playlists](/docs-and-guides/distribution/playlists#smart-playlist) and [podcast feeds](/docs-and-guides/distribution/podcast-feeds#smart-feed).

#### API updates

This toggle allows updates made via the API to override the existing article content and regenerate the audio.
If disabled, API updates will be ignored, and the current content and audio will remain unchanged.

<Note>
  If you're using the WordPress plugin, this setting applies to you too as the plugin is built on top of our API.
</Note>

#### Play ads

Use this toggle to choose whether ads should be included in the audio article.

<Note>
  No ads will be included in the audio article if you don't have any ads in your project.
</Note>

# Background music
Source: https://docs.beyondwords.io/docs-and-guides/content/preferences/background-music

Learn how to add background music to your audio articles with BeyondWords

## Overview

You can include background music automatically whenever an audio article is created or manually add it to each article.

<img alt="background music" />

## Include background music on all articles

<Steps>
  <Step title="Turn on background music">
    Go to the **Background music** tab in the **Content** section and enable background music.
  </Step>

  <Step title="Upload a background track">
    Click the **+ Track** button, upload a background track, give it a name, set the volume, and scope.
  </Step>

  <Step title="Set the default background track">
    Set the default background track to be used for all articles.
  </Step>

  <Step title="Save changes">
    Click **Save** to apply your changes. Moving forward, the background track will be added automatically to all new audio articles.
  </Step>
</Steps>

<Tip>
  To include the background track on existing articles, manually update them in the **Editor** or by clicking **Regenerate**. Otherwise, background music will only be added to new articles.
</Tip>

## Add background music to a specific article

<Steps>
  <Step title="Find the article">
    Go to the **Articles** section and locate the article you want to add background music to.
  </Step>

  <Step title="Open the background music settings">
    * Click the **⋯** button next to the article and then click **Edit**.
    * This will open the **Editor**.
    * Click the **Background music** tab.
  </Step>

  <Step title="Add background music">
    Turn on background music and select the background track you want to use.

    <Note>
      If you don't see the background track you want to use, you will need to upload it first in the **Background music** tab in the **Content** section.
    </Note>
  </Step>

  <Step title="Update the article">
    Click **Update** to save changes and add the background music.
  </Step>
</Steps>

# Pronunciations
Source: https://docs.beyondwords.io/docs-and-guides/content/preferences/pronunciations

Learn how to customize the pronunciation of words in your articles with BeyondWords

## Overview

You can customize how words are pronounced in your audio articles by adding **Pronunciations**. These rules ensure names, acronyms, and industry-specific terms sound just right.

<img alt="pronunciations" />

## Create a pronunciation rule

To get started, you can either create pronunciations from the Pronunciations section of your project or through the Editor.

1. **Pronunciations tab** - Go to **Project > Content > Preferences** and click **+ Pronunciation**.
2. **Editor** - Highlight the word or phrase you want to add a pronunciation for and click **+ Pronunciation**.

<Steps>
  <Step title="Select type">
    Select the type of pronunciation rule you want to create:

    * **Substitute** – Replace a word with an alternative word or phrase.
    * **Say as Word** – Force an acronym to be pronounced as a word.
    * **Say as Letter Sequence** – Force an acronym to be pronounced as a sequence of letters.
    * **Language** – Force a word to be pronounced in a target language.
    * **Phonetic Spelling** – Customize the pronunciation of a word using a phonetic notation:
      * **IPA (International Phonetic Alphabet)**
      * **Jyutping (Cantonese Romanization)**
      * **Pinyin (Mandarin Romanization)**
  </Step>

  <Step title="Enter the word or phrase">
    Specify the exact text the rule should apply to.
  </Step>

  <Step title="Define the change">
    Depending on the pronunciation type, enter the substitute word, language, or phonetic spelling.
  </Step>

  <Step title="Set the language">
    Choose which language the pronunciation rule should apply to.
  </Step>

  <Step title="Preview the pronunciation">
    Use a premade voice to preview the pronunciation.

    <Note>
      At the moment, you cannot preview rules with custom voices.
    </Note>
  </Step>

  <Step title="Set the scope">
    Set where this pronunciation rule should apply:

    * **All projects**: Use this pronunciation in all your projects.
    * **This project only**: Use this pronunciation in this project only.
    * **This article only**: Use this pronunciation in this article only.

    <Tip>
      Update past articles to apply the new pronunciation. Otherwise, the pronunciation will only apply to new articles.
    </Tip>
  </Step>
</Steps>

<Note>
  You cannot add pronunciation rules for numbers on their own unless their scope is for a single article.
</Note>

### Pronunciation types

#### Substitute

Create a **Substitute** pronunciation to replace a word with an alternative word.

> Expand an acronym into words e.g. "CO2" as "carbon dioxide", or get your preferred pronunciation with a re-write e.g. read "scone" as "scon". Correct a heteronym e.g. choose "reed" for "read" not "red".

#### Say as word

Create a **Say as word** pronunciation to force an acronym to be said as a word.

> Make sure a word is read as a word e.g. UNESCO as "Unesco" not "U N E S C O".

#### Say as letter sequence

Create a **Say as letter sequence** pronunciation to force an acronym to be pronounced as a sequence of letters.

> Read a word out letter by letter e.g. " IT" as "I T" not "it".

#### Language

Create a **Language** pronunciation to force a word to be pronounced in a target language.

> For multilingual voices, switch to a second language for greater pronunciation accuracy e.g. tag "Frittura di paranza" to be read in Italian.

<Note>
  Not all voices support the Language rule type yet. This pronunciation type is only available for multilingual voices.
</Note>

#### Phonetic spelling

Create a **Phonetic spelling** pronunciation to define the pronunciation of a word using a notation type.

> Use the international phonetic alphabet to provide an exact pronunciation e.g. ˈniːs for Nice.

#### IPA

Select the IPA (international phonetic alphabet) notation type to force a word to be pronounced according to your preferences.

> Use IPA to provide an exact pronunciation e.g. ˈniːs for Nice.

To make it easier to create IPA pronunciations, you can use the Magic IPA tool by clicking the "Generate spelling" button.

#### Jyutping (Cantonese)

Select the Jyutping notation type to force a word to be pronounced according to your preferences.

#### Pinyin (Mandarin)

Select the Pinyin notation type to force a word to be pronounced according to your preferences.

## AI preprocessing (beta)

AI preprocessing automatically improves pronunciation by understanding the context of your article.

It better handles tricky content like dates, sports scores, and abbreviations.

It will also atuomatically detects foreign words and apply the correct language for accurate pronunciation.

<Note>Language detection is currently limited to German, with more languages planned in future updates.</Note>

#### Enabling preprocessing

**Project level**\
Go to **Project > Content > Preferences** and toggle **AI Preprocessing** on.

**Article level**\
Open the article in the **Editor** and toggle **AI Preprocessing** on in the **Pronunciations** tab in the sidebar.

# Summarization
Source: https://docs.beyondwords.io/docs-and-guides/content/preferences/summarization

Learn how to create audio summaries of your articles with BeyondWords

## Overview

You can set it to generate summaries automatically when an audio article is created or manually for each article.

<img alt="summarization" />

## Create summaries for all articles

<Steps>
  <Step title="Turn on summarization">
    Go to the **Summarization** tab in the **Content** section and enable summarization.
  </Step>

  <Step title="Customize the system prompt">
    Modify the system prompt to fine-tune how the AI generates the summary.
  </Step>

  <Step title="Save changes">
    Click **Save** to apply your changes. Moving forward, summaries will be generated automatically for all new audio articles.
  </Step>
</Steps>

<Tip>
  To generate summaries for existing articles, manually update them in the **Editor** or by clicking **Regenerate**. Otherwise, summaries will only be created for new articles.
</Tip>

## Create a summary for an article

<Steps>
  <Step title="Find the article">
    Go to the **Articles** section and locate the article you want to summarize.
  </Step>

  <Step title="Open the summary settings">
    Click the **summary** button next to the article. This will open the **Editor**.
  </Step>

  <Step title="Enable AI summarization">
    In the **Editor**, turn on AI summarization for the article.
  </Step>

  <Step title="Customize the system prompt">
    Modify the system prompt to fine-tune how the AI generates the summary.
  </Step>

  <Step title="Update the article">
    Click **Update** to save changes and generate the audio summary.
  </Step>
</Steps>

<Card title="Video summaries" href="/docs-and-guides/content/preferences/video">
  Turn on video generation to generate videos of article summaries.
</Card>

## Playing the Summary

Once the summary has been generated for your article, it can be loaded in the player by adding `summary: true` to the embed code:

<CodeGroup>
  ```javascript theme={null}
  <script async defer src="https://proxy.beyondwords.io/npm/@beyondwords/player@latest/dist/umd.js"
    onload="new BeyondWords.Player({
      target: this,
      projectId: <projectId>>,
      contentId: '<contentID>',
      summary: true
    })">
  </script>
  ```
</CodeGroup>

# Video
Source: https://docs.beyondwords.io/docs-and-guides/content/preferences/video

Learn how to turn your articles into videos with BeyondWords.

## Overview

BeyondWords lets you turn your articles and article summaries into videos. Video generation can be automated or triggered manually for individual articles and scripts.

## Create videos for all articles

<Steps>
  <Step title="Go to Video preferences">
    Go to **Content** → **Preferences** in your BeyondWords dashboard and open the **Video** tab.
  </Step>

  <Step title="Select video sizes">
    Choose the video format(s) you’d like to generate: **16:9** (horizontal) and/or **9:16** (vertical).

    <Note>If you’re interested in generating additional video sizes, please contact **[support@beyondwords.io](mailto:support@beyondwords.io)**.</Note>
  </Step>

  <Step title="Choose which articles to convert">
    Select whether you’d like to generate videos from:

    * Full articles
    * Article summaries
    * Both full articles and summaries
  </Step>

  <Step title="Choose a default template">
    Templates define the visual style of your videos. You can select an existing template or create a new one to act as your default.

    Learn more about creating and managing templates in the [Templates](/docs-and-guides/content/preferences/video#templates) section below.
  </Step>

  <Step title="Save changes">
    Click **Save changes** to apply your settings. These settings will apply to new and regenerated articles.
  </Step>
</Steps>

<Tip>
  To generate videos for an existing article, you’ll need to manually update or regenerate the article.
</Tip>

## Create or edit a video for a specific article

<Steps>
  <Step title="Find the article">
    Go to the **Content** → **Articles** section and locate the article you want to create a video for.
  </Step>

  <Step title="Open the video settings">
    Click the **Create video** button next to the article. This will open the **Video** section of the Editor.
  </Step>

  <Step title="Select video sizes">
    In the **Video** tab, choose the video formats you’d like to generate: **16:9** (landscape) and/or **9:16** (vertical).

    <Note>If you’re interested in generating additional video sizes, please contact **[support@beyondwords.io](mailto:support@beyondwords.io)**.</Note>
  </Step>

  <Step title="Choose which content to convert">
    Choose whether to convert the full article and/or the article summary into video.

    <Note>You can add your own summary to the “Summary” tab or use the “Generate summary” button.</Note>
  </Step>

  <Step title="Choose or create a template">
    Templates define the visual style of your videos. You can select an existing template or create a new one.

    If no template is selected, the default template will be used.

    Learn more about creating and managing templates in the [Templates](/docs-and-guides/content/preferences/video#templates) section.
  </Step>

  <Step title="Regenerate the article">
    Click **Regenerate** to save changes and generate the video.
  </Step>
</Steps>

## Templates

Templates allow you to define the visual style of your videos.

You can create templates and choose a default in **Content** → **Preferences** → **Video**.

To override the default for a specific article, go to the **Video** tab in the article editor.

### Name and slug

Give your template a name. This will automatically generate a corresponding slug.

<Note>The slug is useful when working with the API, as it allows you to apply a specific template without needing to reference individual video settings.</Note>

### Media

#### Background

Sets the background color used when an article does not have a featured image or video. Requires a hex color code (e.g., #000000).

#### Entrance and exit animation

Choose how images and videos animate as they enter and exit the frame:

* None
* Fade
* Zoom in
* Zoom out
* Slide up
* Slide down

#### Pan and zoom

Enable smooth pan and zoom motion on images and videos to add subtle movement.

#### Visual timing

Control how images and videos are timed throughout the video:

* **Cycle continuously**: Images will loop through continuously, repeating the sequence when reaching the end.
* **Space evenly**: Images will be distributed evenly across the video duration, showing each image for an equal amount of time.
* **Follow article**: Images will change based on the article content, syncing with the corresponding text segments as they are narrated.

#### Seconds

Available when **Cycle continuously** is selected. Sets how long each image or video is shown before transitioning to the next.

### Captions

Captions control the on-screen text shown alongside your article audio. Use the sections below to configure text styling, background, word highlights, and layout.

#### Text

* **Generate captions**: Toggle captions on/off. Captions follow the article’s audio.
* **Animation**: Choose how captions appear:

  * Classic
  * Reveal
  * Karaoke
  * Pop
* **Font**: Select a font from the list or upload your own.
* **Font size**: Choose a preset size or set a custom size (in pixels from 1 to 90).
* **Casing**: Choose how text casing is displayed.
* **Primary**: Main caption text colour. Requires a hex color code (e.g., #000000).
* **Secondary**: Optional alternate caption colour (will alternate scene-by-scene). Requires a hex color code (e.g., #000000).
* **Shadow**: Optional subtle shadow effect.
* **Outline**: Optional subtle outline effect.

#### Background

* **Color**: Sets the background color behind the caption text. Requires a hex color code (e.g., #000000).

#### Word highlights

Highlight styling for the active word as it’s being spoken. All settings require a hex color code (e.g., #000000).

* **Primary**: Main highlight color for the active word.
* **Secondary**: Optional alternate highlight color (alternates scene-by-scene).
* **Background**: Optional background color behind the active word.

#### Layout

* **Horizontal placement**: Sets where captions sit horizontally (left / centre / right).
* **Vertical placement**: Sets where captions sit vertically (top / middle / bottom).
* **Max lines**: Maximum number of caption lines per scene.
* **Max words**: Maximum number of words per caption scene.
* **Text width**: Maximum width of the caption area (percentage).

### Branding

* **Logo**: Upload an image to add a logo overlay to your videos.
* **Logo position**: Select whether the logo appears in the **top-right** or **top-left** of the video.
* **Waveform color**: Show a dynamic waveform to visualize the audio in your videos. Set the color of the waveform using a hex code (e.g., #000000).

<Note>Don’t forget to click **Save changes** when you’re happy with your template settings.</Note>

## Images and videos

By default, BeyondWords uses the images from your article within the generated video.

Within the Editor, you can:

* Delete, disable, or rearrange images from your article
* Upload additional images and videos to use in your video
* Add pre-licensed images and videos from our Getty Images integration

### Feature image

If a feature image is set, it will be used as the poster image (the image shown before playback begins). It will also be used as the first visual in the generated video, unless a feature video is set.

To upload a feature image, open the right-hand sidebar and select **Upload image**.

To set a feature image from Getty Images:

1. Open the right-hand sidebar
2. Go to the **Images** tab
3. Use the search bar and filtering options to find a suitable image
4. Click the video and select **Set as feature image**

### Feature video

If a feature video is set, the video will play in a continuous loop as the background for the entire video.

To upload a feature video, open the right-hand sidebar and select **Upload video**.

To set a feature video from Getty Images:

1. Open the right-hand sidebar
2. Go to the **Videos** tab
3. Use the search bar and filtering options to find a suitable video
4. Click the video and select **Set as feature video**

<Warning>Having a feature video will override all other media included in the article. (Except the feature image will still be used as the poster image.)</Warning>

### Image segments

Image segments will appear in the background of your video as per your template settings.

To upload an image segment, hover on the relevant part of your article and click **+** → **Add image** → **Upload**.

To add an image segment from Getty Images:

1. Click into the relevant part of your article
2. Open the right-hand sidebar
3. Go to the **Images** tab
4. Use the search bar and filtering options to find a suitable image
5. Click the image and click **Add to content**

### Video segments

Video segments are independent clips you can insert into your video. When a segment plays, the video cuts away from the automated content, then resumes afterward. No narration or captions are generated over video segments.

To upload a video segment, hover on the relevant part of your article and click **+** → **Add video** → **Upload**.

To add a video segment from Getty Images:

1. Click into the relevant part of your article
2. Open the right-hand sidebar
3. Go to the **Videos** tab
4. Use the search bar and filtering options to find a suitable video
5. Click the video and click **Add to content**

### Image cropping

BeyondWords automatically crops your images and videos where necessary to fit your selected format(s) (16:9 and/or 9:16).

To manually adjust the crop:

1. Click the image or video in your article
2. Select **16:9** or **9:16** to adjust the corresponding crop
3. Adjust the highlighted frame as needed
4. Click **Done**

## Video distribution

You can distribute a video by using the player embed code, getting a shareable URL, or downloading the MP4 file.

### Player embed

1. Click the **View video** icon next to your article
2. Choose whether to share the **Video article** or **Video summary**
3. Scroll down to “Copy player embed code” and click the copy icon
4. Add the embed code in your site’s code at the location where you’d like the video to appear

#### Modify the embed script

You can manually update an existing or new script by adding the `video: true` parameter to the player embed code.

<CodeGroup>
  ```javascript theme={null}
  <script async defer src="https://proxy.beyondwords.io/npm/@beyondwords/player@latest/dist/umd.js"
    onload="new BeyondWords.Player({
      target: this,
      projectId: <projectId>>,
      contentId: '<contentID>',
      video: true
    })">
  </script>
  ```
</CodeGroup>

#### Update WordPress Plugin Settings

If you're using the WordPress plugin, you can change the player style either in the [plugin settings](/docs-and-guides/integrations/wordpress/overview#player-style) or in the post edit screen in the [BeyondWords Sidebar](/docs-and-guides/integrations/wordpress/overview#player-style-2).

### Shareable URL

1. Click the **View video** icon next to your article
2. Choose whether to share the **Video article** or **Video summary**
3. Go to **Choose how to share** and select **Shareable URL**
4. Click the copy icon next to the shareable URL
5. Share the URL in your desired locations

### Download video

1. Click the **View video** icon next to your article
2. Choose whether to share the **Video article** or **Video summary**
3. Go to **Choose how to share** and select **Download**
4. Click **16:9 (Horizontal)** or **9:16 (Vertical)** to download the corresponding MP4 file

# Voices
Source: https://docs.beyondwords.io/docs-and-guides/content/preferences/voices

Configure voice preferences

## Overview

Go to the **Voices** tab in the **Content** section to configure your voice preferences. Here you will be able to access and preview all the voices, including **Premade** and **Custom** voices available for your project.

<img alt="voices" />

## Choose language and accent

Select the default language and accent for your project based on the language of your content.

## Choose voice

Find your preferred voice and click "Use voice" to set it as the default. This will be used for all articles unless otherwise specified.

### Choose a voice for article titles

If you want to use a different voice for the titles of your articles, you can click on the dropdown button next to each voice and select "Use as title voice". This will be used for all new article titles unless otherwise specified.

### Choose a voice for article content

If you want to use a different voice for the body text of your articles, you can click on the dropdown button next to each voice and select "Use as body voice". This will be used for all new article body text unless otherwise specified.

### Choose a voice for article summaries

If you want to use a different voice for the summaries of your articles, you can click on the dropdown button next to each voice and select "Use as summary voice". This will be used for all new article summaries unless otherwise specified.

### Speaking rate

You can also adjust the default speed of a voice by clicking on the **⋯** button next to each voice and selecting "Adjust speaking rate". This will allow you to increase or decrease the speaking rate of the voice. This will be applied to all new segments that use that voice.

### Voice ID

You can copy the voice ID of a voice by clicking on the **⋯** button next to each voice and selecting "Copy voice ID". This is useful when using the API or Magic Embed to generate audio.

# Overview
Source: https://docs.beyondwords.io/docs-and-guides/distribution/player/overview

Get started with the BeyondWords player

## Overview

BeyondWords Player is the easiest way to add BeyondWords audios into your website or app.

It is a fully-featured audio player for content generated and hosted on BeyondWords. It is fully integrated with analytics and monetization features on BeyondWords without the need for any extra configuration.

<img alt="player" />

<Info>
  Please note that the BeyondWords player is automatically installed if you are using any of the following integrations:

  * Magic Embed
  * WordPress
  * Ghost
</Info>

## Installation

Choose one of the following methods to install the BeyondWords player:

### Install via embed script

Add the script in your web app:

```javascript theme={null}
<script async defer src="https://proxy.beyondwords.io/npm/@beyondwords/player@latest/dist/umd.js"
    onload="new BeyondWords.Player({
        target: this,
        projectId: <ID>,
        contentId: '<ID>'
    })">
</script>
```

<Info>
  You'll need to replace `<ID>` with your actual project ID and content ID. See the [Identifiers](#identifiers) section below for details on all available identifier options.
</Info>

<Tip>
  For production environments, consider specifying a fixed version instead of using `@latest` to ensure stability.
</Tip>

### Install via NPM

<Steps>
  <Step title="Add the player NPM package">
    ```javascript theme={null}
    npm add @beyondwords/player
    ```
  </Step>

  <Step title="Add a target div in your web app">
    ```javascript theme={null}
    <div id='beyondwords-player'></div>
    ```
  </Step>

  <Step title="Initialize the player">
    ```javascript theme={null}
    import BeyondWords from '@beyondwords/player';

    new BeyondWords.Player({ target: '#beyondwords-player', projectId: <ID>, contentId: '<ID>' });
    ```
  </Step>
</Steps>

<Info>
  You'll need to replace `<ID>` with your actual project ID and content ID. See the [Identifiers](#identifiers) section below for details on all available identifier options.
</Info>

## Identifiers

You will need to replace project `ID` and content `ID` with your `projectId` and `contentId`. You can use any of the following properties in conjunction with the `projectId` to initialize the player:

| **Property** | **Description**                                                                                                                                                                                   |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contentId`  | Unique UUID string for the audio content.<br /> You can also pass the previous integer audio ID as a string for users migrating from the legacy API.                                              |
| `sourceId`   | The externally provided source identifier for a content item.<br />This could be the ID from your CMS, the `<guid>` from an RSS `<item>`, or the post ID if generated using the WordPress Plugin. |
| `sourceUrl`  | The URL containing the source content.<br /> This could be the public URL submitted via the API, the `<link>` from an RSS `<item>`, or the post URL from the WordPress Plugin.                    |
| `playlistId` | The unique ID for a playlist created in the dashboard or through the API.                                                                                                                         |

## Advanced customization

For developers looking to build custom interfaces or use the player in headless mode, additional documentation is available on GitHub. This includes guides on:

* Building your own UI on top of the BeyondWords player
* Using the player SDK programmatically
* Implementing custom analytics

For complete documentation on advanced customization options, visit the [BeyondWords Player GitHub repository](https://github.com/beyondwords-io/player?tab=readme-ov-file).

## Next steps

After installing the player, you'll likely want to customize its appearance and behavior to match your brand and user experience requirements.

<CardGroup>
  <Card title="Player settings" icon="sliders" href="/docs-and-guides/distribution/player/settings">
    Configure your player's appearance, branding, and interactive features
  </Card>

  <Card title="JavaScript SDK" icon="js" href="/docs-and-guides/distribution/player/sdk/javascript/getting-started">
    Integrate the player in web applications
  </Card>

  <Card title="iOS SDK" icon="apple" href="/docs-and-guides/distribution/player/sdk/ios/getting-started">
    Integrate the player in iOS applications
  </Card>

  <Card title="Android SDK" icon="android" href="/docs-and-guides/distribution/player/sdk/android/getting-started">
    Add the player to Android applications
  </Card>
</CardGroup>

# Getting started
Source: https://docs.beyondwords.io/docs-and-guides/distribution/player/sdk/android/getting-started

You will first need to have created a [project](/docs-and-guides/getting-started/concepts#projects) with some [articles](/docs-and-guides/getting-started/concepts#articles) generated.

## First steps

### Add the JitPack repository to your root build.gradle at the end of repositories

```javascript theme={null}
allprojects {
    repositories {
        ...
        maven { url 'https://jitpack.io' }
    }
}
```

### Add the dependency to your app build.gradle

```javascript theme={null}
dependencies {
    implementation 'com.github.beyondwords-io:player-android:+'
}
```

### Add playerView to your view hierarchy

There are two options:

1. Add PlayerView to your layout xml file

```javascript theme={null}
<io.beyondwords.player.PlayerView
    android:id="@+id/player_view"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

2. Add PlayerView programmatically

```javascript theme={null}
val playerView = PlayerView(context)
playerViewParent.addView(playerView)
```

### Load your content into the player

```javascript theme={null}
playerView.load(PlayerSettings(
    projectId = <ID>,
    contentId = <ID>
))
```

You will need to replace the `<ID>` placeholders with the real identifiers for your project and content.

playerView\.release() should be called after this PlayerView has been removed from the view system. No other methods may be called on this PlayerView after release.

After running the app, the player should load.

## How it works

The PlayerView uses a [Web Player](https://github.com/beyondwords-io/player?tab=readme-ov-file) under the hood to load the Web Player and provides a Kotlin interface which binds to the underlying JavaScript API.

You can check the API compatibility between the iOS and the Web player in the [compatibility settings](/docs-and-guides/distribution/player/sdk/javascript/player-settings#player-settings-compatibility-across-sdks).

To understand how the underlying Web Player works, please refer to its [documentation](/docs-and-guides/distribution/player/sdk/javascript/getting-started).

## How to configure it

The preferred way to configure the player is by logging into the BeyondWords dashboard, going to the Player tab, and changing its settings.

However, you can also override properties at the app level, for example:

```javascript theme={null}
playerView.load(PlayerSettings(
    projectId = <ID>,
    contentId = <ID>,
    playerStyle = "large",
    callToAction = "Listen to this recipe",
    backgroundColor = "yellow",
))
```

These settings will take precedence over those specified in the dashboard and allow more flexibility.

These settings can also be changed after loading the player, for example:

```javascript theme={null}
playerView.setPlayerStyle("large")
playerView.setBackgroundColor("yellow")
playerView.setPlaybackRate(1.5F)
```

You can also refer to [example app](https://github.com/beyondwords-io/player-android/tree/main/example) which showcases the core functionality of the player, including how to build a custom UI.

You can download a precompiled version of the example app from the assets of the [latest GitHub Release](https://github.com/beyondwords-io/player-android/releases).

## Android SDK Github repository

<Card title="Android SDK Documentation" icon="android" href="https://github.com/beyondwords-io/player-android">
  View the Android SDK documentation in our GitHub repository
</Card>

# Segments playback
Source: https://docs.beyondwords.io/docs-and-guides/distribution/player/sdk/android/segments-playback

The player supports a feature called 'Playback from Segments'. This lets you to click on a [segment](/api-reference/content/segments) in your app (i.e. a paragraph) to begin playback from that segment. If the segment is already playing then it will be paused instead.

The segments playback in the Android Player is based on the [Segments Playback in the Web Player](/docs-and-guides/distribution/player/sdk/javascript/segments-playback). The Android SDK cannot automatically identify segments, instead you should be able to manually link each text segment with its beyondwords marker.

You can find an example of how segment playback can be integrated in your app in [PlaybackFromSegmentsActivity.kt](https://github.com/beyondwords-io/player-android/tree/main/example/app/src/main/kotlin/io/beyondwords/example/PlaybackFromSegmentsActivity.kt) and [PlaybackFromSegmentsRecyclerActivity.kt](https://github.com/beyondwords-io/player-android/tree/main/example/app/src/main/kotlin/io/beyondwords/example/PlaybackFromSegmentsRecyclerActivity.kt)

## How it works

To highlight the current segment you have to listen for the `CurrentSegmentUpdated` event, then find the correspondig UI element to the `currentSegment` and apply the desired styling to it.

```kotlin theme={null}
object : EventListener {
    override fun onEvent(event: PlayerEvent, settings: PlayerSettings) {
        if (event.type == "CurrentSegmentUpdated") {
            val text = segments[settings.currentSegment?.marker]
            for (i in 0 until contentView.childCount) {
                val view = contentView.getChildAt(i)
                if (view !is TextView) continue
                if (view.text == text) {
                    view.setBackgroundColor(android.graphics.Color.LTGRAY)
                } else {
                    view.setBackgroundColor(android.graphics.Color.TRANSPARENT)
                }
            }
        }
    }
}
```

To change the current time of the player when a segment is clicked you have to set `View.OnClickListener` and call `setCurrentSegment` with the correspondig marker.

```kotlin theme={null}
fun onSegmentClick(segmentText: TextView) {
    val marker = segments.entries.firstOrNull { it.value == segmentText.text }?.key ?: return
    playerView.setCurrentSegment(segmentMarker = marker)
}
```

# Getting started
Source: https://docs.beyondwords.io/docs-and-guides/distribution/player/sdk/ios/getting-started

You will first need to have created a [project](/docs-and-guides/getting-started/concepts#projects) with some [articles](/docs-and-guides/getting-started/concepts#articles) generated.

## First steps

### Add the dependency to your Podfile

```javascript theme={null}
target 'MyApp' do
  pod 'BeyondWordsPlayer'
end
```

As an alternative you can also use the XCFramework attached to the assets of the latest [GitHub Release](https://github.com/beyondwords-io/player-ios/releases/)

### Add PlayerView to your view hierarchy

```javascript theme={null}
let playerView = PlayerView()
playerViewParent.addSubview(playerView)
```

### Load your content into the player

```javascript theme={null}
playerView.load(PlayerSettings(
    projectId: <ID>,
    contentId: <ID>
))
```

You will need to replace the `<ID>` placeholders with the real identifiers for your project and content.

After running the app, the player should load.

## How it works

The PlayerView uses a WKWebView under the hood to load the [Web Player](https://github.com/beyondwords-io/player?tab=readme-ov-file) and provides a Swift interface which binds to the underlying JavaScript API.

You can check the API compatibility between the iOS and the Web player in the [compatibility settings](/docs-and-guides/distribution/player/sdk/javascript/player-settings#player-settings-compatibility-across-sdks).

To understand how the underlying Web Player works, please refer to its [documentation](/docs-and-guides/distribution/player/sdk/javascript/getting-started).

## How to configure it

The preferred way to configure the player is by logging into the BeyondWords dashboard, going to the Player tab, and changing its settings.

However, you can also override properties at the app level, for example:

```javascript theme={null}
playerView.load(PlayerSettings(
    projectId: <ID>,
    contentId: <ID>,
    playerStyle: "large",
    callToAction: "Listen to this recipe",
    backgroundColor: "yellow",
))
```

These settings will take precedence over those specified in the dashboard and allow more flexibility.

These settings can also be changed after loading the player, for example:

```javascript theme={null}
playerView.setPlayerStyle("large")
playerView.setBackgroundColor("yellow")
playerView.setPlaybackRate(1.5F)
```

You can also refer to [example app](https://github.com/beyondwords-io/player-ios/tree/main/Example) which showcases the core functionality of the player, including how to build a custom UI.

## iOS SDK Github repository

<Card title="iOS SDK Documentation" icon="apple" href="https://github.com/beyondwords-io/player-ios">
  View the iOS SDK documentation in our GitHub repository
</Card>

Compatability

# Segments playback
Source: https://docs.beyondwords.io/docs-and-guides/distribution/player/sdk/ios/segments-playback

The player supports a feature called 'Playback from Segments'. This lets you to click on a [segment](/api-reference/content/segments) in your app (i.e. a paragraph) to begin playback from that segment. If the segment is already playing then it will be paused instead.

The segments playback in the iOS Player is based on the [Segments Playback in the Web Player](/docs-and-guides/distribution/player/sdk/javascript/segments-playback). The iOS SDK cannot automatically identify segments, instead you should be able to manually link each text segment with its beyondwords marker.

You can find an example of how segment playback can be integrated in your app in [PlaybackFromSegmentsViewController.swift](https://github.com/beyondwords-io/player-ios/blob/main/Example/Example/PlaybackFromSegmentsViewController.swift)

## How it works

To highlight the current segment you have to listen for the `CurrentSegmentUpdated` event, then find the correspondig UI element to the `currentSegment` and apply the desired styling to it.

```swift theme={null}
extension PlaybackFromSegmentsViewController : PlayerDelegate {
    public func player(_ playerView: PlayerView, onEvent event: PlayerEvent, settings: PlayerSettings) {
        if (self.playerView !== playerView) { return }

        if (event.type == "CurrentSegmentUpdated") {
            let text = settings.currentSegment?.marker.flatMap { self.segments[$0] }
            for view in self.contentView.arrangedSubviews {
                guard let label = view as? UILabel else { continue }
                if (label.text == text) {
                    label.backgroundColor = .lightGray
                } else {
                    label.backgroundColor = .clear
                }
            }
        }
    }
}
```

To change the current time of the player when a segment is clicked you have to set `UITapGestureRecognizer` and call `setCurrentSegment` with the correspondig marker.

```swift theme={null}
@objc private func segmentTapped(_ gesture: UITapGestureRecognizer) {
    guard let label = gesture.view as? UILabel else { return }
    guard let marker = self.segments.first(where: { $0.value == label.text })?.key else { return }
    playerView.setCurrentSegment(segmentMarker: marker)
}
```

# Building your own UI
Source: https://docs.beyondwords.io/docs-and-guides/distribution/player/sdk/javascript/building-ui

The player can be used in `headless` mode if you want to build your own user-interface on top of it.

If the player is initialized without a target, the UI will be disabled and it will be mounted at the end of the `<body>` tag.

Alternatively, you can set showUserInterface: false when initializing the player to disable the UI:

```javascript theme={null}
new BeyondWords.Player({
  projectId: <ID>,
  contentId: '<ID>',
  target: "#my-div",
  showUserInterface: false,
});
```

Note that the player will always be mounted in the DOM, even when you are using headless mode.

This is because the player is built on top of a native media element (a `<video>` tag).

If `playerStyle: "video"`, `showUserInterface: false` is set then the `<video>` tag will show without any controls.

### Overview

The simplest way to build your own UI is to repeatedly query the player instance and re-render.

For example, you can get `player.playbackState` and `player.currentTime` then update your UI accordingly.

More complex features like progress bars can be built using this technique.

The simplest way to repeatedly query the player is by registering an event listener for all events:

```javascript theme={null}
player.addEventListener("<any>", rerenderCustomUserInterface);

const rerenderCustomUserInterface = () => {
  // Update your user-interface by querying the player object.
};
```

Your function will then be called whenever anything changes in the player, such as the `currentTime` being updated.

See [Listening to Events](/docs-and-guides/distribution/player/sdk/javascript/player-events#listening-to-events) and [Player Events](/docs-and-guides/distribution/player/sdk/javascript/player-events#overview) for more information.

## Using React

If you're using React, here's how you might implement the above technique in a component:

```javascript theme={null}
import { useEffect, useState } from "react";

const CustomUserInterface = ({ player }) => {
  const [counter, setCounter] = useState(0);

  useEffect(() => {
    const listener = player.addEventListener("<any>", () => setCounter(i => i + 1));
    return () => player.removeEventListener("<any>", listener);
  }, []);

  return (
    <span>Current time: {player.currentTime}</span>
    <button onClick={() => player.playbackState = "playing"}>Play</button>
  );
};
```

In this example, the component is forced to re-render when the counter is updated.

Note that the counter isn't actually displayed, we are just using it to force the component to rerender.

## Using WordPress

If you're using our WordPress plugin, it supports a 'headless' mode which hides the default UI.

This feature is only available in private beta versions 4.x or greater. Please [contact us](mailto:support@beyondwords.io) for access.

The player script tag will be added for you when using the WordPress plugin so **do not** add it manually.

WordPress supports a filter called `beyondwords_player_script_onload` which can be used to initialize your UI:

```php theme={null}
function my_beyondwords_player_script_onload( $onload, $params ) {
    return $onload . 'initializeCustomUserInterface();';
}
add_filter( 'beyondwords_player_script_onload', 'my_beyondwords_player_script_onload', 10, 2 );
```

Then follow the instructions for the plain JavaScript example below to render your custom UI.

## Using JavaScript

If you're using plain Javascript, here's a working example that implements the above technique.

The user-interface in this example is very simple but should demonstrate the core technique.

Note that you will need to replace projectId and contentId with valid identifiers from your project.

If you're using the WordPress plugin (see above) then you can remove the line containing `new BeyondWords.Player(...)`.

```html theme={null}
<!DOCTYPE html>
<html lang='en'>
  <head>
    <meta charset='UTF-8' />
    <title>Custom User Interface</title>
  </head>
  <body>
    <div>
      <button id='play-button'>Play</button>
      <span id='content-title'>Loading...</span>
      <span id='time-indicator'>0:00</span>
    </div>

    <script>
      var player, playButton, contentTitle, timeIndicator;

      function initializeCustomUserInterface() {
        player = BeyondWords.Player.instances()[0];
        player = player || new BeyondWords.Player({ projectId: <ID>, contentId: '<ID>' });

        playButton = document.getElementById('play-button');
        contentTitle = document.getElementById('content-title');
        timeIndicator = document.getElementById('time-indicator');

        player.addEventListener('<any>', rerenderCustomUserInterface);
        playButton.addEventListener('click', playOrPause);
      }

      function rerenderCustomUserInterface() {
        var contentItem = player.content[player.contentIndex];
        var isPlaying = player.playbackState === 'playing';

        var minutes = Math.floor(player.currentTime / 60);
        var seconds = Math.floor(player.currentTime % 60);

        playButton.innerText = isPlaying ? 'Pause' : 'Play';
        contentTitle.innerText = contentItem ? contentItem.title : '';
        timeIndicator.innerText = minutes + ":" + seconds.toString().padStart(2, '0');
      }

      function playOrPause() {
        if (player.playbackState === 'playing') {
          player.playbackState = 'paused';
        } else {
          player.playbackState = 'playing';
        }
      };
    </script>

    <!-- Remove this script tag if you are using the WordPress plugin. It will be added for you. -->
    <script async deref
      src='https://proxy.beyondwords.io/npm/@beyondwords/player@latest/dist/umd.js'
      onload='initializeCustomUserInterface()'>
    </script>
  </body>
</html>
```

## Style overrides

Instead of building a completely custom user-interface, you might just want to tweak the player styles.

For example, if you don't want the rounded corners, you could add a CSS rule to your site to remove them:

```css theme={null}
.beyondwords-player .main {
  border-radius: 0;
}
```

However, this technique **will not work** because the player styles are extremely defensive against accidental overrides.

To intentionally change the player styles, you must use this very long selector that contains 15 classes:

```css theme={null}
.bwp.bwp.bwp.bwp.bwp.bwp.bwp.bwp.bwp.bwp.bwp.bwp.bwp.bwp.bwp .main {
  border-radius: 0 !important;
}
```

This will ensure that your style selectors have a higher specificity than those that are built into the player.

Please note that the player styles might change in the future which could mean your overrides stop working.

Because of this, we'd discourage this technique, but you're welcome to use it if you are prepared to monitor this yourself.

## Segment style overrides

If you want to override the highlight color of segments, you can use the following CSS:

```css theme={null}
[data-beyondwords-marker]:nth-child(3n) .beyondwords-highlight {
  background: #fcc !important;
}

[data-beyondwords-marker]:nth-child(3n+1) .beyondwords-highlight {
  background: #cfc !important;
}

[data-beyondwords-marker]:nth-child(3n+2) .beyondwords-highlight {
  background: #ccf !important;
}
```

Note that you do not need to use the `.bwp.bwp.bwp...` selector in this case
because that is only needed for the player user interface and for the segment
widget.

## Direct API calls

We'd strongly recommend using one of techniques above if you want to customize the user-interface of the player.

However, if you don't want to use any existing player code yourself and instead want direct access to the data then you can use [our APIs](/api-reference/overview).

Currently, all of the data for the player comes from the /player endpoint which is public and cached for five minutes. You could call this yourself and build your own user-interface on top of this data.

However, please keep in mind that you will lose out on many key features of the player, such as BeyondWords Analytics, support for Google Analytics, support for adverts, Segments Playback, Media Session API support, etc.

# Getting started
Source: https://docs.beyondwords.io/docs-and-guides/distribution/player/sdk/javascript/getting-started

## First Steps

### Installation

The first step is to create an account and generate some content.

Next, choose your installation method:

* [Embed script](/docs-and-guides/distribution/player/overview#install-via-embed-script)

* [NPM package](/docs-and-guides/distribution/player/overview#install-via-npm)

## How the embed script works

The script tag downloads the code for BeyondWords player and instantiates a new player instance.

The `async` and `defer` attributes mean that the browser won't stall while it downloads the script code.

The `onload` attribute initializes a JavaScript class called `BeyondWords.Player`.

By setting `target: this`, the player will be added immediately after the script tag in the `<body>`. That means it will appear at the position where you copy the script tag into your page.

### How to configure it

The preferred way to configure the player is by logging into the BeyondWords dashboard, going to the Player tab, and changing its settings.

However, you can also override properties at the script level, for example:

```javascript theme={null}
<script async defer
  src='https://proxy.beyondwords.io/npm/@beyondwords/player@latest/dist/umd.js'
  onload='new BeyondWords.Player({
    target: this,
    projectId: <ID>,
    contentId: "<ID>",
    playerStyle: "large",
    callToAction: "Listen to this recipe",
    backgroundColor: "yellow",
  })'>
</script>
```

These settings will take precedence over those specified in the dashboard and allow more flexibility.

These settings can also be changed after loading the player by using the [Player SDK](/docs-and-guides/distribution/player/sdk/javascript/player-sdk#overview).

Please refer to [Player Settings](/docs-and-guides/distribution/player/sdk/javascript/player-settings) for an explanation of all the settings that can be configured.

## How NPM installation works

The initialization is almost identical to how the [embed script](/docs-and-guides/distribution/player/sdk/javascript/getting-started#how-the-embed-script-works) works except we set target: `#beyondwords-player`.

This instructs the player to initialize inside the DOM node with `id='beyondwords-player'`.

Note that the DOM node must be on the page when the initializer is called or the player won't load.

### How to configure it

The preferred way to configure the player is by logging into the BeyondWords dashboard and changing its settings.

However, you can also override properties in the initializer, for example:

```javascript theme={null}
new BeyondWords.Player({
  target: '#beyondwords-player',
  projectID: <ID>,
  contentId: '<ID>',
  playerStyle: 'large',
  callToAction: 'Listen to this recipe',
  backgroundColor: 'yellow',
});
```

These settings will take precedence over those specified in the dashboard and allow more flexibility.

These settings can also be changed after loading the player by using the [Player SDK](/docs-and-guides/distribution/player/sdk/javascript/player-sdk#overview).

Please refer to [Player Settings](/docs-and-guides/distribution/player/sdk/javascript/player-settings) for an explanation of all the settings that can be configured.

## JavaScript Github repository

<Card title="JavaScript SDK Documentation" icon="js" href="https://github.com/beyondwords-io/player?tab=readme-ov-file">
  View the JavaScript SDK documentation in our GitHub repository
</Card>

# Player events
Source: https://docs.beyondwords.io/docs-and-guides/distribution/player/sdk/javascript/player-events

List of player events emitted and listening for events

## Overview

Player events are simple JSON objects that are emitted by the BeyondWords player.
They contain information about the current state of the player. They are separate
from [analytics events](/docs-and-guides/analytics/event-schema) which contain
information about user engagement.

You can [listen to](docs-and-guides/distribution/player/sdk/javascript/player-events#listening-to-events)
player events and perform your own actions after they are processed by the player
in its [RootController](https://github.com/BeyondWords-io/player/blob/main/src/controllers/rootController.ts).
Events have a set of fields that are always present and some events contain additional fields.
Here is an example:

```javascript Example event theme={null}
{
  id: "51178a37-d5a7-4d75-9a12-a26eabfe7839",
  type: "PressedPlaylistItem",
  description: "A playlist item was pressed.",
  index: 3,
  initiatedBy: "user",
  emittedFrom: "inline-player",
  status: "handled",
  createdAt: "2023-01-01T12:00:00.000Z",
  processedAt: "2023-01-01T12:00:00.005Z",
  changedProps: {
    contentIndex: { previousValue: 0, currentValue: 3 },
  },
}
```

For the above example, the 'index' field additional and is specific to the PressedPlaylistItem event.

All of the other fields are present in every event. Their schema is explained below.

## Event schema

* `id`: a random UUID generated and assigned to the event at creation
* `type`: the type of event, see the table below for a listing of event types
* `description`: a short human-readable description of the event
* `initiatedBy`: who initiated the event, one of: `{ user, media, browser, media-session-api, google-ima-sdk }`
* `emittedFrom`: which interface emitted the event, one of: `{ inline-player, bottom-widget, segment, segment-widget }`
* `status`: the status of the event, one of: `{ handled, ignored-due-to-advert, ignored-due-to-scrubbing, ignored-due-to-precedence }`
* `createdAt`: the time when the event was created in simplified extended ISO 8601 format
* `processedAt`: the time when the event was processed in simplified extended ISO 8601 format
* `changedProps`: an object listing the player properties that were changed by the event

It is recommended to not depend on `changedProps` and additional event fields (e.g. index) since these might change.

Instead, please query the player props directly using the [Player SDK](/docs-and-guides/distribution/player/sdk/javascript/player-sdk#overview) when listening to events.

## Event types

The following table lists all event types emitted by the player.

Initiators denoted with a plus `(+)` can also be initiated by media-session-api, e.g. using playback controls on a phone lock screen.

Initiators denoted with a star `(*)` can also be initiated by google-ima-sdk when VAST adverts are playing.

To inspect the events further, it is recommended you [listen to `"<any>"` event](/docs-and-guides/distribution/player/sdk/javascript/player-events#listening-to-events) and console log them.

| Type                         | Initiator | Description                                                                    |
| ---------------------------- | --------- | ------------------------------------------------------------------------------ |
| IdentifiersChanged           | browser   | The Player's content identifiers changed.                                      |
| ContentAvailable             | browser   | Content was loaded into the player and is ready to be played.                  |
| NoContentAvailable           | browser   | No published and processed content is available for the identifiers.           |
| FullScreenModeUpdated        | browser   | The browser entered or exited full screen mode.                                |
| PressedPlay                  | user+     | The play button was pressed.                                                   |
| PressedPause                 | user+     | The pause button was pressed.                                                  |
| PressedChangeRate            | user      | The change playback rate button was pressed.                                   |
| PressedEnterOnChangeRate     | user      | The enter key was pressed while change playback rate was focussed.             |
| PressedSpaceOnChangeRate     | user      | The space key was pressed while change playback rate was focussed.             |
| PressedUpOnChangeRate        | user      | The up key was pressed while change playback rate was focussed.                |
| PressedRightOnChangeRate     | user      | The right key was pressed while change playback rate was focussed.             |
| PressedDownOnChangeRate      | user      | The down key was pressed while change playback rate was focussed.              |
| PressedLeftOnChangeRate      | user      | The left key was pressed while change playback rate was focussed.              |
| PressedPrevSegment           | user+     | The previous segment button was pressed.                                       |
| PressedNextSegment           | user+     | The next segment button was pressed.                                           |
| PressedSeekBack              | user+     | The seek backward button was pressed.                                          |
| PressedSeekAhead             | user+     | The seek ahead button was pressed.                                             |
| PressedPrevTrack             | user+     | The previous track button was pressed.                                         |
| PressedNextTrack             | user+     | The next track button was pressed.                                             |
| PressedAdvertLink            | user      | The advert link was pressed to open the click-through URL in a new tab.        |
| PressedAdvertButton          | user      | The advert button was pressed to open the click-through URL in a new tab.      |
| PressedAdvertImage           | user      | The advert image was pressed to open the advert in a new tab.                  |
| PressedAdvertVideo           | user      | The video background was pressed to open the advert in a new tab.              |
| PressedBeyondWords           | user      | The BeyondWords logo was pressed to open the BeyondWords website in a new tab. |
| PressedSourceUrl             | user      | The source URL button was pressed to open the source article in a new tab.     |
| VisibilityChanged            | user      | The player was scrolled into or out of view.                                   |
| PressedVideoBackground       | user      | The video background was pressed.                                              |
| PressedEnterOnProgressBar    | user      | The enter key was pressed while the progress bar was focussed.                 |
| PressedSpaceOnProgressBar    | user      | The space key was pressed while the progress bar was focussed.                 |
| PressedEnterOnProgressCircle | user      | The enter key was pressed while the progress circle was focussed.              |
| PressedSpaceOnProgressCircle | user      | The space key was pressed while the progress circle was focussed.              |
| PressedLeftOnProgressBar     | user      | The left key was pressed while the progress bar was focussed.                  |
| PressedRightOnProgressBar    | user      | The right key was pressed while the progress bar was focussed.                 |
| PressedLeftOnProgressCircle  | user      | The left key was pressed while the progress circle was focussed.               |
| PressedRightOnProgressCircle | user      | The right key was pressed while the progress circle was focussed.              |
| PressedProgressBar           | user      | The progress bar was pressed at some ratio.                                    |
| ScrubbedProgressBar          | user+     | The user pressed on the progress bar then dragged.                             |
| FinishedScrubbingProgressBar | user      | The user let go after scrubbing the progress bar.                              |
| PressedMaximize              | user      | The maximize button was pressed.                                               |
| PressedPlaylistItem          | user      | A playlist item was pressed.                                                   |
| PressedDownload              | user      | The download button next to a playlist item was pressed.                       |
| PressedTogglePlaylist        | user      | The toggle playlist button was pressed.                                        |
| PressedCloseWidget           | user      | The close widget button was pressed.                                           |
| PressedSegment               | user      | The user pressed on a segment in the article.                                  |
| HoveredSegmentUpdated        | user      | The user hovered over a different segment in the article.                      |
| CurrentSegmentUpdated        | media     | The media's current segment was updated.                                       |
| MetadataLoaded               | media     | The media finished loading its metadata.                                       |
| MediaLoaded                  | media     | The media finished loading its first frame of data.                            |
| MediaSeeked                  | media     | The media completed the seek operation.                                        |
| DurationUpdated              | media\*   | The media's duration was updated.                                              |
| CurrentTimeUpdated           | media     | The media's current time was updated.                                          |
| PlaybackPaused               | media\*   | The media became paused at its current playback time.                          |
| PlaybackRateUpdated          | media     | The media's playback rate was updated.                                         |
| PlaybackPlaying              | media     | The media began playing from its current playback time.                        |
| PlaybackEnded                | media\*   | The media finished playing because it reached the end.                         |
| PlaybackNotAllowed           | media     | The media cannot play because there was no user event.                         |
| PlaybackErrored              | media\*   | The media failed to play.                                                      |
| CompanionAdvertChanged       | media\*   | The companion advert associated with the VAST advert changed.                  |

## Listening to events

The player emits events in response to user actions, playback time updates, entering full screen, etc.

You can listen to these events in your JavaScript code:

```javascript theme={null}
const player = BeyondWords.Player.instances()[0];

player.addEventListener("<any>", console.log);
```

The code above registers an event listener that listens to any event and logs it to the console.

If you only want to listen to a single event type, provide its name:

```javascript theme={null}
player.addEventListener("PressedPlay", console.log);

player.addEventListener("PlaybackEnded", console.log);
```

Events contain a standard set of fields such as `type` and `createdAt` and some contain additional fields.

Please refer to [Event schema](/docs-and-guides/distribution/player/sdk/javascript/player-events#event-schema) and [Event types](/docs-and-guides/distribution/player/sdk/javascript/player-events#event-types) for a full listing of event types and their fields.

### Cleaning up

The return value of `addEventListener` is a string that is a handle to the listener.

This allows you remove the listener, for example, if a React component is unmounted:

```javascript theme={null}
useEffect(() => {
  const listener = player.addEventListener("<any>", console.log);
  return () => player.removeEventListener("<any>", listener);
}, []);
```

Or when your Svelte component is unmounted:

```javascript theme={null}
onMount(() => {
  const listener = player.addEventListener("<any>", console.log);
  return () => player.removeEventListener("<any>", listener);
});
```

Otherwise, the callback function will continue to be called which may result in an error in your application.

# Programmatic control
Source: https://docs.beyondwords.io/docs-and-guides/distribution/player/sdk/javascript/player-sdk

## Overview

After the player has loaded, it can be controlled programmatically and its state can be queried.

The return value of the `new BeyondWords.Player(...)` call is a player instance:

```javascript theme={null}
const player = new BeyondWords.Player(...);
```

This instance can be used to get the current time, change the track, set the backgroundColor, etc:

```javascript theme={null}
console.log(player.currentTime);

player.contentIndex = 3;

player.backgroundColor = "red";
```

The player is reactive and will immediately update with these changes.

## How to get instances

If you have already initialized the player, e.g. via a script tag, you can get all of the player instances with:

```javascript theme={null}
BeyondWords.Player.instances() // Returns an array.
```

For example, if you only have one player on your page, you could set its backgroundColor with:

```javascript theme={null}
BeyondWords.Player.instances()[0].backgroundColor = "red";
```

For convenience the `BeyondWords` constant is added to the global `window` object.

## How overrides work

There are three different places settings can come from:

1. From the BeyondWords API after setting project and content identifiers
2. From the initialization code, e.g. in the script tag's 'onload' attribute
3. From Player SDK calls made by you after the player has loaded

The override order is shown above.

Firstly, the player will use properties from the API which can be overridden by the initialization code.

Secondly, the player's properties can be overridden by SDK calls, e.g. to change its backgroundColor.

If the player's identifiers change and a new API request is made, any temporary changes made by SDK calls will be reset.

Only changes that were included in the initializer of the player will be persisted when a new API request is made.

## Player settings

Please refer to the [Player Settings](/docs-and-guides/distribution/player/sdk/javascript/player-settings) for a full list of available settings that can be configured in the player.

Additionally, please refer to [Player Events](/docs-and-guides/distribution/player/sdk/javascript/player-events) if you want to register event listeners for player events.

## Top-level methods

The player has a few top-level methods that you may find useful:

```javascript theme={null}
BeyondWords.Player.version // The player version that is loaded, e.g. "0.1.23"

BeyondWords.Player.instances() // See above. This retrieves all initialized instances.

BeyondWords.Player.instances()[0].target // Returns the root DOM node of the player.

BeyondWords.Player.instances()[0].properties() // Returns all reactive properties as a key-value object.

BeyondWords.Player.instances()[0].destroy() // Removes a player instance, freeing its resources.

BeyondWords.Player.destroyAll() // Removes all player instances, freeing their resources.
```

It is recommended to remove player instances on single-page websites once they
are no longer needed to free up browser resources.

# Player settings
Source: https://docs.beyondwords.io/docs-and-guides/distribution/player/sdk/javascript/player-settings

List of configurable properties in the player

The table below contains a list of properties that can be configured in the player.

### Player settings

<ParamField type="string">
  The URL of the API that the player should fetch its data from. This is only really useful if you're a BeyondWords developer and want to use the internal staging environment to test something.

  Default: `https://api.beyondwords.io/v1/projects/{id}/player`
</ParamField>

<ParamField type="number">
  The numeric ID of your project. This can be retrieved from the BeyondWords dashboard by visiting a project and copying the numeric ID from within the URL.
</ParamField>

<ParamField type="string | number">
  The ID of content to load in the player. This can be retrieved from the BeyondWords dashboard by clicking on the embed button next to a piece of a content and copying it from within the code snippet. Normally this will be a string UUID, but legacy numeric IDs are also supported.

  **Note:** The player loads content from a projectId and one or more of the following identifiers: `{ contentId, playlistId, sourceId, sourceUrl, playlist }`. If multiple identifiers are provided, the player will load all of the published content into a playlist, which might include other playlists. The order that content is loaded into the player will match the order of identifiers in this table. If you want to use a different order set the playlist property to an array of identifiers.

  Note that the player will only load content that has been processed and published. If you want to preview audio before publishing, as part of a drafting workflow, refer to the previewToken setting.
</ParamField>

<ParamField type="number">
  The ID of a 'manual' or 'automatic' playlist to load in the player. This can be retrieved from the BeyondWords dashboard and appears as part of the URL. (see [note](/docs-and-guides/distribution/player/sdk/javascript/player-settings#param-content-id) above regarding identifiers)
</ParamField>

<ParamField type="string">
  An alternative ID that can be used to load content in the player. This ID is a string that can optionally be provided when creating content via the BeyondWords API. For example, it could be the ID your CMS system uses to identify content. (see [note](/docs-and-guides/distribution/player/sdk/javascript/player-settings#param-content-id) above regarding identifiers)
</ParamField>

<ParamField type="string">
  An alternative method for loading content into the player. The source URL is optional and is the URL of where the content can be found on the web. This method of identifying content is discouraged in case the article moves to a different URL. (see note above regarding identifiers)

  If no other identifiers are set then the player will set this property to window\.location.href. This allows the client-side integration to be used without having to specify an identifier.
</ParamField>

<ParamField type="object[]">
  An array of identifiers to load into the player. The four identifiers above are supported. The order that content is loaded into the player will match the order of the array:

  ```json theme={null}
  [
    { contentId: "67f86dca-02e5-466d-99bf-0d1103f6c6e9" },
    { contentId: "cc85c59c-7c68-4e5d-a225-eeecb40617e6" },
    { sourceId: "some-external-id-set-by-you" },
    { sourceUrl: "https://example.com/my-article" },
    { playlistId: 12345 },
    { playlistId: 67890 },
  ]
  ```

  If other top-level identifiers are set on the player such as contentId, these identifiers will be prepended to the playlist array and appear at the top. (see [note](/docs-and-guides/distribution/player/sdk/javascript/player-settings#param-content-id) above regarding identifiers)
</ParamField>

<ParamField type="boolean">
  Whether to load the AI-generated summary of the content item rather than the original. The summary must be generated beforehand in the BeyondWords dashboard.

  If a playlist is loaded, the summary of each playlist item will be loaded. If no summary is available, the player will be hidden or those items will not appear in the playlist.
</ParamField>

<ParamField type="string | node">
  The location in the DOM to use as the root node of the player. It supports the following values:

  * **this**: when used in a script tag, the player will be initialized in a new div after the script tag
  * **\<string>**: a query string to be passed to `document.querySelector`, e.g. "#some-id"
  * **\<node>**: a DOM node, e.g. returned from `document.getElementById("some-id")`

  If no target is specified then the player will be initialized in a new div at the end of the `<body>` and the user-interface will not be shown. See [Building your own UI](/docs-and-guides/distribution/player/sdk/javascript/building-ui)for more information.
</ParamField>

<ParamField type="boolean">
  Whether to enable the BeyondWords client-side integration which can simplify the process of importing content into the BeyondWords platform. See the dedicated [client-side integration documentation](/docs-and-guides/integrations/magic-embed/overview) for a setup tutorial and a more detailed explanation of this feature.
</ParamField>

<ParamField type="boolean">
  Whether to show the user-interface. This can be set to false if you want to build your own user-interface on top of the core player functionality (e.g. in our [iOS](https://github.com/beyondWords-io/player-ios)and [Android](https://github.com/beyondWords-io/player-android)SDKs).

  If the playerStyle is video then the `&lt;video&gt;` element will show without any controls. You can call `player.target.requestFullscreen()` as usual to enter fullscreen. See [Building your own UI](https://github.com/beyondwords-io/player/blob/main/doc/building-your-own-ui.md).
</ParamField>

<ParamField type="boolean">
  Whether to show the widget that slides up from the bottom of the screen once you scroll past the player. Normally this is toggled automatically and should not be set manually.

  If you are [Building your own UI](/docs-and-guides/distribution/player/sdk/javascript/building-ui)the widget will not automatically be shown/hidden when scrolling past the player so you will need to set this manually, e.g. using an [Intersection Observer](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API).

  Note that if widgetTarget is set then the widget will always appear inside the widgetTarget and no bottom widget will show, regardless of the value of this boolean. If showUserInterface is set to false then the bottom widget won't appear either, unless the widgetStyle is video.
</ParamField>

<ParamField type="boolean">
  Whether to show the 'X' button that allows users to close the widget.

  When the widget is closed, playback will be paused and the widgetStyle will be changed to `closed-by-user`. The widget can be shown again using the player SDK by setting it back to a supported widgetStyle, e.g. "small" or "standard".

  Due to space limitations, the close button will not show during adverts or for the "small" player style, regardless of this setting. The close button is not supported by the inline (static) player.
</ParamField>

<ParamField type="string">
  The style of player to display. There are five supported styles:

  * **small**: the smallest player that has the bare minimum of buttons
  * **standard**: the default player style that offers a good mix of functionality
  * **large**: a larger player that shows the playerTitle and an image
  * **screen**: a full screen player designed to be linked to from social media
  * **video**: a player that supports video adverts and scrolling text content

  If playerStyle is set to anything else (e.g. "none") then the player will be hidden.
</ParamField>

<ParamField type="boolean">
  An alias for `playerStyle: "video"`, added for convenience. When set to true, this setting will take precedence over any existing playerStyle setting. Not available through the player SDK.
</ParamField>

<ParamField type="string">
  The title to show at the top of the large, screen and video players. Normally this is automatically set to the name of your project but can be specified in the BeyondWords dashboard. It can also be overridden when initializing the player if you want to use a different title for the player.
</ParamField>

<ParamField type="string">
  The prompt to show on the small and standard players when it is stopped. If the value is falsy, it translates 'Listen to this article' into the user's language, according to their browser preference, assuming that language is supported by the player (see the list of supported languages).
</ParamField>

<ParamField type="string">
  The style of the skip buttons. There are four supported styles:

  * **auto**: skip by 'tracks' for a playlist and 'segments' for a single item
  * **segments**: skip backwards and forwards by one paragraph
  * **seconds**: seek backwards and forwards by 10 seconds
  * **tracks**: skip backwards and forwards by one playlist track

  By default, the 'seconds' style skips 10 seconds in both directions but you can control this with 'seconds-15' or 'seconds-15-30' to set a different number of seconds for backwards/forwards.
</ParamField>

<ParamField type="string">
  Whether to show the playlist. There are three supported styles:

  * **auto**: show the playlist when there is more than one content item
  * **show**: show the playlist by default (can still by toggled by the user)
  * **hide**: hide the playlist by default (can still be toggled by the user)

  By default, the 'auto' and 'show' styles display 5 items on desktop and 4 on mobile before a scrollbar appears but you can set a different number.

  For example, 'auto-3' will show 3 items and 'show-10-8' will show a different number on desktop and mobile. This can be set to a very large number, e.g. 'show-99999' to never show a scrollbar.
</ParamField>

<ParamField type="string">
  Whether to show the playlist toggle button in the player. There are three supported styles:

  * **auto**: show the toggle when there is more than one content item
  * **show**: show the toggle
  * **hide**: hide the toggle
</ParamField>

<ParamField type="string[]">
  An ordered list of file extensions, e.g. `["mp3", "mp4"]`, that is used to determine whether to show the download button next to playlist items. The first extension that matches one of the content item's audio/video URLs will be downloadable with a filename of `&lt;content title&gt;.&lt;extension&gt;`.
</ParamField>

<ParamField type="function">
  A function that controls how the duration of content is displayed in the player. By default, the duration will be shown as " min" but it can be overridden by setting your own function:

  ```js theme={null}
  durationFormat: (minutes, seconds, translate) => `${minutes} mins ${seconds} secs`
  ```

  By default, the player will attempt to translate " min" into the language of the user's browser. You can use the same `translate` function in your formatting function if you would like:

  ```js theme={null}
  durationFormat: (minutes, seconds, translate) => (
      translate("minutesSingularOrPlural").replace("{n}", `${minutes}:${seconds}`)
  )
  ```

  The available translation for each language can be found in the source. Please ensure that your durationFormat function does not error to ensure the player loads correctly. Note that it is not currently possible to customise the presentation of other time/duration formats in the player.
</ParamField>

<ParamField type="string">
  Whether to use the Media Session API. When enabled, the player will appear on your phone's lock screen and can be controlled using your native device buttons. There are three supported types:

  * **auto**: use the Media Session API if it is not already being used by your website
  * **override**: use the Media Session API and override your website's existing media session
  * **none**: do not use the Media Session API

  If there are multiple players on the page, the media session will be set to the player that is currently playing or that was most recently playing. Otherwise, the first player initialized is chosen. The media session is set whenever playback begins (when the [PlaybackPlaying event](/docs-and-guides/distribution/player/sdk/javascript/player-events#event-types) is emitted).

  The media session makes use of many player settings. For example:

  * It shows the title from the content that is currently playing or will play after the advert
  * It shows the image from the active advert or content item
  * It falls back to a speaker icon that uses iconColor and backgroundColor
  * It disables the skip buttons and prevents scrubbing when an advert is playing
  * It respects the skipButton style, e.g. it can skip between segments (depending on the device)

  If any player is set to 'override' then the media session may be overridden, including by players that are set to 'auto'. If there is no existing media session, 'auto' and 'override' behave the same.
</ParamField>

<ParamField type="object[]">
  The array of content to play in the player. Normally this is automatically set based on the identifiers but it can be overridden if you wish to set the content manually without making API requests. A playlist will be shown in the player if the array contains multiple items.

  <a />**Note:** Each content item can contain both audio and video media files. If the playerStyle or widgetStyle is 'video' and the HTML video element is visible when the track changes, the player will prefer video media and fall back to audio. Otherwise, it will prefer audio and fall back to video. The player will attempt to load media in array order until a file format that it is able to play is found.

  ```json theme={null}
  [
    {
      id: "27b760cb-0838-4354-bf86-ac514c2ad0ca",
      title: "Content Title",
      imageUrl: "https://example.com/image.jpeg",
      sourceUrl: "https://example.com/my-article",
      sourceId: "article-123",
      adsEnabled: true,
      duration: 123.45,
      audio: [{ id: 123, url: "https://x.com/audio.mp3", contentType: "audio/mpeg", duration: 123.45 }],
      video: [{ id: 124, url: "https://x.com/video.mp4", contentType: "video/mpeg", duration: 123.45 }],
      segments: [{ marker: "paragraph-1", section: "body", startTime: 0.05, duration: 9.95 }],
    },
  ]
  ```

  All fields are optional and the player will work with what it is given, rather than raise an error.

  * id will be included in events sent to analyticsCustomUrl and Google Analytics
  * title will be shown for the content item in the player
  * imageUrl will be shown in the large, screen and video players
  * sourceUrl will be used as the href of a link in the screen player
  * sourceId will be included in BeyondWords/custom/Google analytics events
  * adsEnabled will determine whether adverts play before/during/after this content item
  * duration is only used for display in the playlist and is normally fetched from the media
  * audio is an array of media sources for the content item (see note above)
  * video is an array of media sources for the content item (see note above)
  * segments is an array of timestamps used for skipping between paragraphs
</ParamField>

<ParamField type="number">
  The index of the active content item in the player. This can be set to change the track in a playlist.
</ParamField>

<ParamField type="object[]">
  An array of intros and outros to play before and after all of the content and adverts. Normally intros and outros are automatically set from your project but can be overridden if you wish to set the intros and outros manually. There are two different placements:

  * **pre-roll**: The element is an intro that plays before all content and adverts
  * **post-roll**: The element is an outro that plays after all content and adverts

  ```json theme={null}
  [
    {
      placement: "pre-roll",
      audio: [{ url: "https://example.com/intro.mp3", contentType: "audio/mpeg" }],
      video: [{ url: "https://example.com/intro.mp4", contentType: "video/mpeg" }],
    },
    {
      placement: "post-roll",
      audio: [{ url: "https://example.com/outro.mp3", contentType: "audio/mpeg" }],
      video: [{ url: "https://example.com/outro.mp4", contentType: "video/mpeg" }],
    },
  ]
  ```

  See the [note](#note2) above about content media which also applies to intro and outro media.

  If the array contains multiple intros or outros, the player will choose one of each at random which then will be used for all players currently loaded on the page to keep the experience consistent.

  If skipButtonStyle is set to 'segments', the user can skip past the intro to the content and they can skip back from the outro to the last segment of the content.

  If skipButtonStyle is set to 'tracks', the intro/outro will be considered part of the first/last content item and the user can skip past them in a single click.

  If content is replayed by the user, the intro and outro will play again. The intro will be skipped if the user begins playback from currentTime > 0, e.g. when clicking on a segment in the article.
</ParamField>

<ParamField type="number">
  The index of the active intro or outro in the player. This can be set to play an intro or outro, but it is recommended not to do this manually because pre/mid/post-roll placement will not apply.
</ParamField>

<ParamField type="object[]">
  An array of adverts to play in the player. Normally ads are automatically set from your project but can be overridden if you wish to set the adverts manually. There are two types of advert:

  * **custom**: An advert that specifies its own media sources and clickThroughUrl
  * **vast**: An advert that is fetched from the vastUrl, e.g. from Google Ads

  In the case of a 'custom' advert, the vastUrl field will be ignored. In the case of a 'vast' advert, the clickThroughUrl and media fields will be ignored. There are three different placements:

  * **pre-roll**: The advert plays before the content or between playlist items
  * **mid-roll**: The advert plays mid-way through a content item or between playlist items
  * **post-roll**: The advert plays after the content or between playlist items

  ```json theme={null}
  [
    {
      id: 123,
      type: "custom",
      placement: "pre-roll",
      clickThroughUrl: "https://example.com/buy-my-product",
      textColor: "#00f",
      backgroundColor: "rgba(255, 255, 200, 0.8)",
      iconColor: "red",
      videoTextColor: "yellow",
      videoIconColor: "yellow",
      audio: [{ id: 555, url: "https://x.com/advert.mp3", contentType: "audio/mpeg", duration: 12.34 }],
      video: [{ id: 556, url: "https://x.com/advert.mp4", contentType: "video/mpeg", duration: 12.34 }],
    },
    {
      id: 456,
      type: "vast",
      placement: "mid-roll",
      vastUrl: "https://pubads.g.doubleclick.net/gampad/ads?iu=/123456789/your/advert",
      textColor: "#00f",
      backgroundColor: "rgba(255, 255, 200, 0.8)",
      iconColor: "red",
      videoTextColor: "yellow",
      videoIconColor: "yellow",
    },
  ]
  ```

  See the [note](#note2) above about content media which also applies to advert media.

  While an advert is playing it can 'take over' the user interface to show an image and different color theme or it will fall back to the default player colors for those that are not specified in the advert.
</ParamField>

<ParamField type="number">
  The index of the active advert. This can be set to play an advert, but it is recommended not to do this manually because pre/mid/post-roll placement will not apply.
</ParamField>

<ParamField type="number">
  The minimum duration that a content item must have for a mid-roll advert to play. If a content item's duration is less than this time in seconds then a mid-roll advert won't play.

  Additionally, mid-roll adverts won't play *during* content items in playlists and will instead play *in-between* playlist items. Pre-roll and post-roll adverts will also play in-between items.

  Mid-roll adverts play after playback reaches 50% of the content item's duration at the next boundary between segments (paragraphs) to make the listening experience less jarring.
</ParamField>

<ParamField type="number">
  When seeking, this setting controls the minimum amount of time before the end of playback that the user must seek for mid-roll adverts to play. In other words, this prevents mid-roll adverts from playing within the last N seconds if the user seeks near to the end of the progress bar.

  When seeking past 50% of the duration and before the number of seconds specified by this setting, mid-roll adverts will play immediately and interrupt playback. Mid-roll adverts won't be aligned to the boundaries between segments (paragraphs) in this case (as per setting above).
</ParamField>

<ParamField type="boolean">
  Whether to show an advert image in the 'large' and 'screen' playerStyle during regular content playback. The image will be clickable if a clickThroughUrl is set on the advert.

  The persistent advert will change to whichever advert played most recently. If the content has started but no advert has played yet, the image will be set to the first pre-, mid-, or post-roll advert in the adverts array in that order of precedence, i.e. pre-roll will take precedence.

  This setting only applies to 'custom' adverts. Adverts with type 'vast' will not be persistent.
</ParamField>

<ParamField type="number">
  The index of the persistent advert in the player. The can be set to show an advert, but it is recommended not to do this manually because the selection process above will not apply.
</ParamField>

<ParamField type="number">
  The duration of the active content item in the player. The duration is fetched from the loaded media, rather than the duration field in the content item which is only used for the playlist display.

  This property is intended to be **read-only** and should not be set manually, otherwise the duration shown in the user-interface will be incorrect until the media is changed, e.g. by changing track.
</ParamField>

<ParamField type="number">
  The current playback time of the media. The currentTime automatically updates while the media is playing and can be retrieved using the [player SDK](/docs-and-guides/distribution/player/sdk/javascript/player-sdk) or set to a value to seek to the given time.

  If this setting is provided when initializing the player, the first track will begin from the given time. There is a brief period in which the currentTime will be 0 while the media loads and it will then revert back to the specified time after the [MediaLoaded event](/docs-and-guides/distribution/player/sdk/javascript/player-events#event-types) has been emitted.
</ParamField>

<ParamField type="string">
  The current playback state of the media. The can be set to start or stop playback, provided the programmatic call is on behalf of a user action such as clicking a button. There are three states:

  * **stopped**: playback has not yet started or it has finished
  * **playing**: the media for the content item is playing
  * **paused**: the media for the content item is paused
</ParamField>

<ParamField type="number">
  The current playback rate of the media. This can be set to speed up or slow down playback. The playbackRate will persist across tracks but temporarily resets to 1 during adverts.
</ParamField>

<ParamField type="number[]">
  The visible playback rates that can be cycled through in the user interface. It is not a requirement that the playbackRate setting above be set to one of these values when using the [player SDK](/docs-and-guides/distribution/player/sdk/javascript/player-sdk).

  Default value: `[0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 2, 2.5, 3]`
</ParamField>

<ParamField type="string">
  The style of widget to display at the bottom of the page once the user scrolls past the inline player. All five styles are supported (see playerStyle). Can be set to "none" to hide the widget.
</ParamField>

<ParamField type="string">
  The horizontal position of the widget when it is showing. There are four supported options:

  * **auto**: show the widget in the center for the standard player, otherwise right
  * **left**: show the widget on the bottom-left corner of the screen
  * **center**: show the widget at the bottom of the screen in the middle
  * **right**: show the widget in the bottom-right corner of the screen

  This setting has no effect when widgetTarget is set. Instead, you can position the widgetTarget as needed using your own css styles that are applied to the root element of the widget.
</ParamField>

<ParamField type="string">
  The width of the widget. Can be set to any CSS unit, including 500px, 50rem, 50% and fit-content. This property can be set to 0 to make the player use its smallest possible width.

  By default, the small playerStyle expands and collapses. You can force it to always be collapsed by setting this property to 0, or to always be expanded by setting this property to initial.
</ParamField>

<ParamField type="string">
  The margin of the widget. Can be set to any CSS unit, including 50px, 5rem and 5%.

  The margin for each side of the widget can be set separately, e.g. "10px 20px 30px 40px" will set the top, right, bottom and left margins, respectively. You may also use shorthands to set multiple margins at once, e.g. "10px 5px" to set top/bottom and left/right margins, respectively. If the widgetPosition is center, the left/right margins will be averaged.
</ParamField>

<ParamField type="string | node">
  The location in the DOM to use as the root node of the widget. It supports the following values:

  * **\<string>**: a query string to be passed to document.querySelector, e.g. "#some-id"
  * **\<node>**: a DOM node, e.g. returned from document.getElementById("some-id")

  If widgetTarget undefined then the widget will show as a fixed element at the bottom of the screen once the user has scrolled past the player. When widgetTarget is set, the widget will always show, regardless of the value of showUserInterface and the scroll position of the user.

  Please note that the singular `<video>` element can only show behind one user interface at a time. It will be relocated to/from the widget while active and a message will show in the other interface. Additionally, the widgetPosition setting will have no effect when widgetTarget is used.
</ParamField>

<ParamField type="string">
  The text color. Can be set to any CSS color, including red, #f00, #ff0000 and rgba(255, 0, 0, 0.8). This color can be overridden when an advert is playing by specifying it in the advert object.
</ParamField>

<ParamField type="string">
  The background color. Can be set to any CSS color, including red, #f00 and rgba(255, 0, 0, 0.8). This property can also be set to a linear gradient: linear-gradient(to right, #fcf, #fcc). This color can be overridden when an advert is playing by specifying it in the advert object.
</ParamField>

<ParamField type="string">
  The icon color. Can be set to any CSS color, including red, #f00, #ff000 and rgba(255, 0, 0, 0.8). This color can be overridden when an advert is playing by setting it in the advert object.
</ParamField>

<ParamField type="string">
  The highlight color for the current and hovered segments. Can be set to any CSS color, including red, #f00, #ff000 and rgba(255, 0, 0, 0.8). This color is not overridden when an advert is playing.
</ParamField>

<ParamField type="string">
  The text color of the surrounding user interface when playerStyle is video. Can be set to any CSS color, including red, #f00, #ff0000 and rgba(255, 0, 0, 0.8). This color can be overridden when an advert is playing by specifying it in the advert object. This setting does not affect the video itself.
</ParamField>

<ParamField type="string">
  The icon color of the surrounding user interface when playerStyle is video. Can be set to any CSS color, including red, #f00, #ff000 and rgba(255, 0, 0, 0.8). This color can be overridden when an advert is playing by setting it in the advert object. This setting does not affect the video itself.
</ParamField>

<ParamField type="boolean">
  Whether to show the BeyondWords logo icon.
</ParamField>

<ParamField type="string">
  The sections to enable when highlighting segments in the article. This helps readers follow along by highlighting the currentSegment as the currentTime of the player changes. It also helps users understand they can click on a segment in the article to begin playback. It supports the following:

  * **all**: allow all segments in the article to be highlighted
  * **body**: allow segments that have a section of 'body' to be highlighted
  * **summary**: allow segments that have a section of 'summary' to be highlighted
  * **none**: don't allow any segments to be highlighted

  Additionally, you can use a **double-barrelled** string to set the behavior for the currentSegment and hoveredSegment separately. For example, 'all-none' will enable highlighting for the currentSegment and disable it for the hoveredSegment. Alternatively, 'none-body' will disable highlighting for the currentSegment and enable it for hovered segments in the 'body' section.

  This feature will only work for elements that have been correctly marked up on your page with a 'data-beyondwords-marker' attribute. See [Segments Playback](/docs-and-guides/distribution/player/sdk/javascript/segments-playback) for more information.
</ParamField>

<ParamField type="string">
  The sections to enable for the 'Playback from Segments' feature. This allows users to click on a segment in the article to begin playback from that segment. It supports the following values:

  * **all**: allow playback by clicking on any of the segments in the article
  * **body**: allow playback by clicking on segments that have a section of 'body'
  * **summary**: allow playback by clicking on segments that have a section of 'summary'
  * **none**: don't allow playback by clicking on segments

  If the currentSegment is clicked, it will pause and resume playback from the current position. Otherwise, it will skip to the hoveredSegment's startTime and begin playback.

  If the segment contains links or other elements that have 'onclick' or 'onmousedown' handlers, this feature will not interfere and the user can click those elements without affecting playback. If event listeners are used, you can call event.preventDefault() to prevent triggering playback.

  This feature will only work for elements that have been correctly marked up on your page with a 'data-beyondwords-marker' attribute. See [Segments Playback](/docs-and-guides/distribution/player/sdk/javascript/segments-playback) for more information.
</ParamField>

<ParamField type="string">
  The sections to enable for showing the segment widget. This is a small user-interface that appears next to segments in the article. This allows users to click on a play/pause button next to the segment to begin playback from that segment. It supports the following values:

  * **all**: allow the segment widget to be shown next to all segments in the article
  * **body**: allow the segment widget to be shown next to segments that have a section of 'body'
  * **summary**: allow the segment widget to be shown next to segments that have a section of 'summary'
  * **none**: don't allow the segment widget to be shown next to any segments

  Additionally, you can use a **double-barrelled** string to set the behavior for the currentSegment and hoveredSegment separately. For example, 'all-none' will show the segment widget to next to the currentSegment and will not change when segments are hovered. Alternatively, 'none-body' will only show the segment widget next to segments that are hovered and have a section of 'body'.

  If the segment widget appears next to the current segment, it will show the play/pause button as usual. Otherwise, the segment widget will always show a play button and its circular progress bar will show the segment's startTime relative to the duration of the audio. The segment widget is 'sticky' which means that it continues to show when the user stops hovering over a segment.

  This feature will only work for elements that have been correctly marked up on your page with a 'data-beyondwords-marker' attribute. See [Segments Playback](/docs-and-guides/distribution/player/sdk/javascript/segments-playback) for more information.
</ParamField>

<ParamField type="string">
  The position of the segment widget relative to the segment text's rectangle. For convenience, hours of a clock are used for specifying the position. It supports the following values:

  * **1-oclock**: above the text, on the right
  * **2-oclock**: right of the text, at the top
  * **3-oclock**: right of the text, vertically centered
  * **4-oclock**: right of the text, at the bottom
  * **5-oclock**: below the text, on the right
  * **6-oclock**: below the text, horizontally centered
  * **7-oclock**: below the text, on the left
  * **8-oclock**: left of the text, at the bottom
  * **9-oclock**: left of the text, vertically centered
  * **10-oclock**: left of the text, at the top
  * **11-oclock**: above the text, on the left
  * **12-oclock**: above the text, horizontally centered

  The widget will be positioned approximately 50% of the widget's width away from the text. If the position is 7-oclock or 11-oclock the segment widget will be indented slightly to align with the play/pause button of the player, taking into account the current playerStyle.

  If the segment widget appears left or right of the text, a 'position: relative' style will be added to the data-beyondwords-marker element and the segment widget will be positioned absolutely.
</ParamField>

<ParamField type="object">
  The segment that aligns with the currentTime of the player. The currentSegment will be unaffected while an advert is playing and the audio will resume from the segment when the advert ends.

  The currentSegment additionally contains contentIndex and segmentIndex which refers to its position in the content array. The currentSegment is set and the CurrentSegmentUpdated event is emitted regardless of the segmentPlayback and highlightCurrent player settings (see above).

  This property will only be set for elements that have been correctly marked up on your page with a 'data-beyondwords-marker' attribute. See [Segments Playback](/docs-and-guides/distribution/player/sdk/javascript/segments-playback) for more information.

  This property is intended to be **read-only** and should not be set manually.
</ParamField>

<ParamField type="object">
  The segment that is currently being hovered over by the user. This will be set to null if the user hovers over a link or an element with 'onclick' or 'onmousedown' listeners so that highlighting does not apply to the segment from the highlightHovered setting. This helps explain to the user that playback will be unaffected if they click on a link or other elements within the segment.

  The hoveredSegment additionally contains contentIndex and segmentIndex which refers to its position in the content array. The hoveredSegment is set and the HoveredSegmentUpdated event is emitted regardless of the segmentPlayback and highlightHovered player settings (see above).

  This property will only be set for elements that have been correctly marked up on your page with a 'data-beyondwords-marker' attribute. See [Segments Playback](/docs-and-guides/distribution/player/sdk/javascript/segments-playback) for more information.

  This property is intended to be **read-only** and should not be set manually.
</ParamField>

<ParamField type="object">
  The media source that is currently loaded into the player. This is set to an element from the audio or video arrays within content, adverts or introsOutros.

  ```json theme={null}
  {
    id: 123,
    url: "https://example.com/audio.mp3",
    contentType: "audio/mpeg",
    duration: 123.45,
    format: "audio",
  }
  ```

  This property is intended to be **read-only** and should not be set manually. This property is set by either the MetadataLoaded or the MediaLoaded [event](/docs-and-guides/distribution/player/sdk/javascript/player-events#event-types) (both of them set this property).

  On iOS Safari, this event might not be emitted until the user presses play. It is recommended to use the ContentAvailable and NoContentAvailable [events](/docs-and-guides/distribution/player/sdk/javascript/player-events#event-types) for deciding when to show the player.
</ParamField>

<ParamField type="string">
  The preview token that should be used to load pre-published content into the player. This is useful if you want to preview the generated audio before publishing it as part of a draft workflow. For example, this setting is used in our <a href="https://wordpress.org/plugins/speechkit/">WordPress plugin</a> to initialize the player for draft posts.

  Preview tokens are generated automatically by BeyondWords when content is first created. You can retrieve the preview token for a content item from our [content API](https://developers.beyondwords.io/reference/content). For the previewToken setting to work, its value must match the preview token assigned to the content item.

  Note that there will still be a short delay while media is generated before the player will load.
</ParamField>

<ParamField type="string">
  The level of consent provided by the user of your website for whether personalized ads are allowed. This only applies to adverts of type 'vast' and maps onto the parameters documented [here](https://developers.google.com/interactive-media-ads/docs/sdks/html5/client-side/consent). You are responsible for requesting consent from your users. There are three levels:

  * **personalized**: adds the npa=0 parameter to vastUrl so that personalized ads will play
  * **non-personalized**: adds the npa=1 parameter to vastUrl which switches off personalized ads
  * **under-the-age-of-consent**: adds the tfua=1 parameter which disables many forms of tracking

  The player copies the approach taken by Google which is to enable personalized ads by default and place the burden on the integrator to ensure they have requested consent from their users.
</ParamField>

<ParamField type="string">
  The level of consent provided by the user of your website for whether usage analytics are allowed to be sent by the player to the BeyondWords dashboard and to the analyticsCustomUrl if it is set. You are responsible for requesting consent from your users. There are three supported levels:

  * **allowed**: analytics will be sent to BeyondWords and analyticsCustomUrl
  * **without-local-storage**: analytics will be sent but without local\_storage\_id
  * **none**: analytics will not be sent to BeyondWords or analyticsCustomUrl

  The player allows analytics by default because they do not contain any personally identifiable information and only contain random UUIDs to identify the same user across sessions. This UUID is persisted in local storage in the browser under the 'beyondwords' key.
</ParamField>

<ParamField type="string">
  A custom URL that analytics events should be sent to, in addition to BeyondWords. These events are exactly the same as those sent to BeyondWords. See [Custom Analytics](/docs-and-guides/analytics/preferences#send-data-to-custom-analytics-url) for more information.
</ParamField>

<ParamField type="string">
  The device\_type that should be sent in analytics events. There are six supported options:

  * **auto**: automatically detect the type of device (see below)
  * **desktop**: set the device\_type to 'desktop'
  * **tablet**: set the device\_type to 'tablet'
  * **phone**: set the device\_type to 'phone' (intended for mobile web rather than native apps)
  * **ios**: set the device\_type to 'ios' (intended for native iOS apps)
  * **android**: set the device\_type to 'android' (intended for native Android apps)

  If device\_type is set to **auto** then the player will use window width as a simple heuristic:

  * A value of 'desktop' will be sent if the width is >= 1000x
  * Otherwise, value of 'tablet' will be sent if the width is >= 500px
  * Otherwise, a value of 'mobile' will be sent

  This setting will apply to all analytics events emitted by the player, which includes those sent to the BeyondWords Dashboard, the analyticsCustomUrl and Google Analytics if analyticsTag is set.
</ParamField>

<ParamField type="string">
  The Google Measurement ID to use when sending events to Google Analytics. When analyticsTag is set, events will always be sent to Google Analytics, regardless of analyticsConsent.
</ParamField>

<ParamField type="string | node">
  The location in the DOM to use as a control panel for the player. It supports the following values:

  * **\<string>**: a query string to be passed to document.querySelector, e.g. "#some-id"
  * **\<node>**: a DOM node, e.g. returned from document.getElementById("some-id")

  The control panel allows you to change most of the player settings via dropdowns or text input fields. It automatically updates to show the current state of the player. The control panel appears on the right-hand side of the [player demo page](https://beyondwords-io.github.io/player) and the [playback from paragraphs prototype](https://beyondwords-io.github.io/player-demo).
</ParamField>

<ParamField type="array[]">
  An array of transitions to call at specific times during playback. Transitions can be used to modify the player using its SDK, e.g. to change its style and toggle various settings (all those above). Transitions are used extensively on the [player demo page](https://beyondwords-io.github.io/player/) to demonstrate its features.

  ```js theme={null}
  [
    [0, 5, p => p.backgroundColor = "red"],
    [0, 10, p => p.playerStyle = "large"],
    [0, 15, p => p.playbackState = "paused"],
  ]
  ```

  The array contains three elements: the contentIndex, the startTime and the transition function. The first transition above will set the backgroundColor during contentIndex 0 after 5 seconds.

  Transitions are applied based on the currentTime of the player. If the user scrubs to a later time, then all transitions up to that time will run in order. Additionally, if the user scrubs back to an earlier time then the player's state will be restored to before the transition was run.

  Transitions remain in place when the next contentIndex begins. For example, the backgroundColor will remain "red" when contentIndex 1 plays and will become red if the user skips forward. You may call arbitrary, non-player functions in transitions but their effects will not be reversible.
</ParamField>

<ParamField type="function">
  The function to call when an unhandled JavaScript error or promise rejection occurs. If this function returns true then the error will stop propagating. This can be useful, for example, to suppress error output from the player appearing in the JavaScript console.

  This function receives the error object as its only argument. In the case of a rejected promise, the function will receive [event.reason](https://developer.mozilla.org/en-US/docs/Web/API/Window/unhandledrejection_event#event_properties) which is usually the error object associated with the promise.

  If any player sets an onError function then all player instances on the page will use the function set first. This setting can only be used during initialization in new BeyondWords.Player(...). If the function is changed later through the [player SDK](/docs-and-guides/distribution/player/sdk/javascript/player-sdk), these changes will be ignored.
</ParamField>

### Player Settings Compatibility Across SDKs

Here's a summary of the [player settings](/docs-and-guides/distribution/player/sdk/javascript/player-settings) available across the SDKs:

| Setting                                                                       | JavaScript | Android | iOS |
| ----------------------------------------------------------------------------- | :--------: | :-----: | :-: |
| [playerApiUrl](#param-player-api-url)                                         |      ✓     |    ✓    |  ✓  |
| [projectId](#param-project-id)                                                |      ✓     |    ✓    |  ✓  |
| [contentId](#param-content-id)                                                |      ✓     |    ✓    |  ✓  |
| [playlistId](#param-playlist-id)                                              |      ✓     |    ✓    |  ✓  |
| [sourceId](#param-source-id)                                                  |      ✓     |    ✓    |  ✓  |
| [sourceUrl](#param-source-url)                                                |      ✓     |    ✓    |  ✓  |
| [playlist](#param-playlist)                                                   |      ✓     |    ✓    |  ✓  |
| [summary](#param-summary)                                                     |      ✓     |    ✓    |  ✓  |
| [target](#param-target)                                                       |      ✓     |         |     |
| [clientSideEnabled](#param-client-side-enabled)                               |      ✓     |         |     |
| [showUserInterface](#param-show-user-interface)                               |      ✓     |    ✓    |  ✓  |
| [showBottomWidget](#param-show-bottom-widget)                                 |      ✓     |         |     |
| [showCloseWidget](#param-show-close-widget)                                   |      ✓     |         |     |
| [playerStyle](#param-player-style)                                            |      ✓     |    ✓    |  ✓  |
| [video](#param-video)                                                         |      ✓     |         |     |
| [playerTitle](#param-player-title)                                            |      ✓     |    ✓    |  ✓  |
| [callToAction](#param-call-to-action)                                         |      ✓     |    ✓    |  ✓  |
| [skipButtonStyle](#param-skip-button-style)                                   |      ✓     |    ✓    |  ✓  |
| [playlistStyle](#param-playlist-style)                                        |      ✓     |    ✓    |  ✓  |
| [playlistToggle](#param-playlist-toggle)                                      |      ✓     |    ✓    |  ✓  |
| [downloadFormats](#param-download-formats)                                    |      ✓     |         |     |
| [durationFormat](#param-duration-format)                                      |      ✓     |         |     |
| [mediaSession](#param-media-session)                                          |      ✓     |    ✓    |     |
| [content](#param-content)                                                     |      ✓     |    ✓    |  ✓  |
| [contentIndex](#param-content-index)                                          |      ✓     |    ✓    |  ✓  |
| [introsOutros](#param-intros-outros)                                          |      ✓     |    ✓    |  ✓  |
| [introsOutrosIndex](#param-intros-outros-index)                               |      ✓     |    ✓    |  ✓  |
| [adverts](#param-adverts)                                                     |      ✓     |    ✓    |  ✓  |
| [advertIndex](#param-advert-index)                                            |      ✓     |    ✓    |  ✓  |
| [minDurationForMidroll](#param-min-duration-for-midroll)                      |      ✓     |    ✓    |  ✓  |
| [minTimeUntilEndForMidroll](#param-min-time-until-end-for-midroll)            |      ✓     |    ✓    |  ✓  |
| [persistentAdImage](#param-persistent-ad-image)                               |      ✓     |    ✓    |  ✓  |
| [persistentIndex](#param-persistent-index)                                    |      ✓     |    ✓    |  ✓  |
| [duration](#param-duration)                                                   |      ✓     |    ✓    |  ✓  |
| [currentTime](#param-current-time)                                            |      ✓     |    ✓    |  ✓  |
| [playbackState](#param-playback-state)                                        |      ✓     |    ✓    |  ✓  |
| [playbackRate](#param-playback-rate)                                          |      ✓     |    ✓    |  ✓  |
| [playbackRates](#param-playback-rates)                                        |      ✓     |    ✓    |  ✓  |
| [widgetStyle](#param-widget-style)                                            |      ✓     |         |     |
| [widgetPosition](#param-widget-position)                                      |      ✓     |         |     |
| [widgetWidth](#param-widget-width)                                            |      ✓     |         |     |
| [widgetMargin](#param-widget-margin)                                          |      ✓     |         |     |
| [widgetTarget](#param-widget-target)                                          |      ✓     |         |     |
| [textColor](#param-text-color)                                                |      ✓     |    ✓    |  ✓  |
| [backgroundColor](#param-background-color)                                    |      ✓     |    ✓    |  ✓  |
| [iconColor](#param-icon-color)                                                |      ✓     |    ✓    |  ✓  |
| [highlightColor](#param-highlight-color)                                      |      ✓     |         |     |
| [videoTextColor](#param-video-text-color)                                     |      ✓     |         |     |
| [videoIconColor](#param-video-icon-color)                                     |      ✓     |         |     |
| [logoIconEnabled](#param-logo-icon-enabled)                                   |      ✓     |    ✓    |  ✓  |
| [highlightSections](#param-highlight-sections)                                |      ✓     |         |     |
| [clickableSections](#param-clickable-sections)                                |      ✓     |         |     |
| [segmentWidgetSections](#param-segment-widget-sections)                       |      ✓     |         |     |
| [segmentWidgetPosition](#param-segment-widget-position)                       |      ✓     |         |     |
| [currentSegment](#param-current-segment)                                      |      ✓     |    ✓    |  ✓  |
| [hoveredSegment](#param-hovered-segment)                                      |      ✓     |         |     |
| [loadedMedia](#param-loaded-media)                                            |      ✓     |    ✓    |  ✓  |
| [previewToken](#param-preview-token)                                          |      ✓     |         |     |
| [advertConsent](#param-advert-consent)                                        |      ✓     |    ✓    |  ✓  |
| [analyticsConsent](#param-analytics-consent)                                  |      ✓     |    ✓    |  ✓  |
| [analyticsCustomUrl](#param-analytics-custom-url)                             |      ✓     |    ✓    |  ✓  |
| [analyticsDeviceType](#param-analytics-device-type)                           |      ✓     |         |     |
| [analyticsTag](#param-analytics-tag)                                          |      ✓     |    ✓    |  ✓  |
| [controlPanel](#param-control-panel)                                          |      ✓     |         |     |
| [transitions](#param-transitions)                                             |      ✓     |         |     |
| [onError](#param-on-error)                                                    |      ✓     |         |     |

# Segments playback
Source: https://docs.beyondwords.io/docs-and-guides/distribution/player/sdk/javascript/segments-playback

The player supports a feature called 'Playback from Segments'. This lets you to click on a segment on your website (i.e. a paragraph) to begin playback from that segment. If the segment is already playing then it will be paused instead.

The player will also highlight the current segment as it is being read out so that the user can read along with the article if they wish. This feature can be enabled in the BeyondWords Dashboard under Player > Settings.

The player should automatically identify segments and highlight them out-of-the-box without further integration work. However, this might not work 100% of the time, depending on the structure of your website.

We recommend you first try out this feature and see if it works out-of-the-box. If not, we recommend adding markers to elements of your page which will improve the quality of the detection:

```html theme={null}
<h1 data-beyondwords-marker="1af51b2a-72df-4b86-bb7c-87d057231ca0">
  This is the title.
</h1>

<p data-beyondwords-marker="5d2c6eba-f612-45c7-b987-00fde473d867">
  This is the first paragraph.
</p>

<p data-beyondwords-marker="d89257cd-ff53-476e-aef2-84dadcca1cc5">
  This is the second paragraph.
</p>
```

### Markers

If you do decide to add markers yourself, rather than rely on automatic detection, we recommend you set the markers to a randomly generated UUID. The UUID must be stable, that is to say, it must not change between page refreshes.

If you are using the [client-side integration](/docs-and-guides/integrations/magic-embed/overview), the markers will be automatically retrieved from your page when content is processed.

If you are sending HTML to the [BeyondWords API](/api-reference/overview), the markers will be automatically extracted from the HTML when content is processed.

If you are sending plaintext to the [BeyondWords API](/api-reference/overview), you will need to set the marker attribute on each segment alongside the text.

Alternatively, if a segment marker is not provided, BeyondWords will generate one for you. You can retrieve these from the `/content` endpoint and add them to the HTML of your article.

It is recommended to generate UUIDs as markers to avoid duplicates, in case there are multiple players on the same page.

### How it works

Once the player script has loaded, it will add global listeners to your page to detect clicks and mousemove events.

If the player detects that you are hovering or have clicked on an element, it will try to match that element against the segments using markers (see above), xpath or an MD5 fingerprint of the text content.

If a match is found, the player emits `HoveredSegmentUpdated` and `PressedSegment` [events](./player-events).

Additionally, when the currentTime of the media updates (i.e. by playing it), the player emits a CurrentSegmentUpdated event.

These events are then used to highlight segments on the page and to control playback, e.g. by setting its currentTime to the startTime of the segment that the user clicked on. The currentSegment and hoveredSegment props of the player are set.

To highlight segments, the player adds a `<mark>` element inside the segment on the page with some custom styles. All children of the segment are moved inside of the mark. The mark is removed again after highlighting has ended.

To avoid interfering with your page, highlighting and clicking on segments does not trigger if you are hovering over a link or other element with a 'click' or 'mousedown' handler. However, this does not apply to event listeners (see below).

### Event listeners

Unfortunately, the player cannot detect event listeners that have been registered on elements within the segment.

For example, this button does not have an 'onclick' property and therefore playback will be affected when it is clicked.

```html theme={null}
<p data-beyondwords-marker="5d2c6eba-f612-45c7-b987-00fde473d867">
  This is the first paragraph. <button id="my-button"></button>
</p>

<script>
  document.getElementById("my-button").addEventListener("click", event => {
    console.log("The button was clicked.");
  });
</script>
```

To avoid this, call `event.preventDefault()` at the top of the event listener:

```html theme={null}
<script>
  document.getElementById("my-button").addEventListener("click", event => {
    event.preventDefault();
    console.log("The button was clicked.");
  });
</script>
```

The above code will prevent the player from changing its current time when the button is clicked.

### Player settings

Playback from Segments supports various [Player Settings](./player-settings):

* **highlightColor** can be used to set a different highlight color for segments on the page
* **highlightSections** can be used to control which segments highlighting applies to (if any)
* **clickableSections** can be used to control which segments can be clicked on (if any)
* **segmentWidgetSections** can be used to control which segments the widget appears next to (if any)
* **segmentWidgetPosition** can be used to control which side the widget appears next to the segment
* **currentSegment** can be used to get the current segment (this is a read-only property)
* **hoveredSegment** can be used to get the hovered segment (this is a read-only property)

# Overview
Source: https://docs.beyondwords.io/docs-and-guides/distribution/player/sdk/overview

The BeyondWords player SDKs

## Overview

BeyondWords provides feature-rich player SDKs to help you integrate our player into your applications with ease.

We have SDKs for:

* [JavaScript](/docs-and-guides/distribution/player/sdk/javascript/getting-started)
* [iOS](/docs-and-guides/distribution/player/sdk/ios/getting-started)
* [Android](/docs-and-guides/distribution/player/sdk/android/getting-started)

All of these are designed to be flexible and customizable, allowing you to tailor the player to fit your specific needs.

## Example use cases

### Playback from paragraphs

If you only want the [playback from paragraphs](/docs-and-guides/distribution/player/settings#playback-from-paragraphs) and [text highlighting](/docs-and-guides/distribution/player/settings#highlight-paragraphs) features to become active after a user has interacted with the player, you can use the following example:

```javascript Player embed script theme={null}
<script async defer src="https://proxy.beyondwords.io/npm/@beyondwords/player@latest/dist/umd.js" onload="
  const player = new BeyondWords.Player({
    target: this,
    projectId: 26027,
    contentId: 'fcb3ab8e-0aa9-4eb2-a828-e84e3e140825'
  });

  player.addEventListener('<any>', () => {
    if (player.playbackState === 'stopped') {
      player.clickableSections = 'none';
      player.highlightSections = 'none';
    } else {
      player.clickableSections = 'all';
      player.highlightSections = 'all';
    }
  });
"></script>
```

# Settings
Source: https://docs.beyondwords.io/docs-and-guides/distribution/player/settings

Configure the BeyondWords player settings

# Player settings

Once you've installed the BeyondWords player, you can customize its appearance and behavior through various settings. This guide walks you through all available configuration options.

## General settings

### Player size

Control the overall size of the player interface:

* **Small**: Compact version for limited space
* **Standard** (default): Balanced size suitable for most websites
* **Large**: Expanded size with enhanced visibility

### Player widget

Enable or disable the floating mini-player widget that appears when scrolling away from the main player.

### Widget size

When the player widget is enabled, you can set its size:

* **Small**: Minimal floating player
* **Standard** (default): Medium-sized floating player
* **Large**: Prominent floating player

### Widget position

Choose where the floating widget appears on the screen:

* **Left**: Aligned to the left side of the viewport
* **Center**: Centered horizontally in the viewport
* **Right**: Aligned to the right side of the viewport

## Branding

### Logo

Upload a custom logo to display in the player.

* Limited to the Large player size
* Use PNG, JPG, or WebP format (max 10MB)
* Recommended dimensions: at least 300px × 300px

### Color theme

Choose the color scheme for your player:

* **System**: Adapts to the user's device settings (light/dark mode)
* **Light mode** (default): Always use light theme
* **Dark mode**: Always use dark theme

### Light mode colors

Customize colors for the light theme:

* **Background color**: The main player background (#F5F5F5 by default)
* **Icon color**: Color for player controls and icons (#000 by default)
* **Text color**: Color for text elements (#111 by default)

### Dark mode colors

Customize colors for the dark theme:

* **Background color**: The main player background (#000 by default)
* **Icon color**: Color for player controls and icons (#FFF by default)
* **Text color**: Color for text elements (#FFF by default)

### Call-to-action

Customize the text for the main player button (default: "Listen to this article")

### Include article title

Toggle whether to display the article title in the player.

* Limited to Large player size

### Intro

Add a custom audio clip to play at the beginning of your content:

* Upload MP3 or WAV format (max 50MB)
* Useful for branded intros or sponsorship messages

### Outro

Add a custom audio clip to play at the end of your content:

* Upload MP3 or WAV format (max 50MB)
* Perfect for calls-to-action or acknowledgments

## Controls

### Skipping

Choose how users can navigate through the audio:

* **Skip by paragraph**: Move forward or backward by logical segments of content
* **Skip by seconds**: Set a specific time jump (e.g., 15 seconds) for skipping

## Interactions

### Highlight paragraphs

Enable this feature to highlight the paragraph that's currently being read aloud, keeping users engaged with the content.

### Highlight colors

* **Light mode highlight**: Color used for highlighting in light mode (#A4FF00 by default)
* **Dark mode highlight**: Color used for highlighting in dark mode (#A4FF00 by default)

### Playback from paragraphs

Allow users to click or tap on any paragraph to begin playback from that point, boosting engagement with your content.

### Allow downloads

Enable listeners to download the audio from the player for offline listening.

## Saving your settings

After configuring your player settings, click the "Save changes" button to apply them. Your settings will be applied to all instances of the player using your project ID.

<Card title="Programmatic configuration" icon="js" href="/docs-and-guides/distribution/player/sdk/javascript/getting-started">
  All these settings can also be configured programmatically when initializing the player. See the JavaScript SDK documentation for details.
</Card>

# Playlists
Source: https://docs.beyondwords.io/docs-and-guides/distribution/playlists

Create, curate, publish, and share audio or video playlists.

## Overview

Playlists allow you to group audio or video articles into a single embedded experience for your audience.

There are three types of playlists:

* **Standard** - you manually choose which articles are included.
* **Smart** - articles are included automatically based on rules you define.
* **Dynamic** - allow your audience to create their own playlists from a collection of articles on your website.

<Warning>Dynamic Playlists requires using the JavaScript SDK and being comfortable working in JavaScript. You can find the [full guide](/docs-and-guides/distribution/playlists#dynamic-playlists) below.</Warning>

<img alt="player" />

***

## Create a playlist

1. Go to **Project > Distribution > Playlists**.
2. Click **+ Playlist**.
3. Enter a name.
4. Upload a cover image.
5. Select a playlist type:
   * **Standard**
   * **Smart**
6. Click **Continue**.

You’ll then be redirected into the playlist editor.

<Note>
  Whenever you create a playlist, a podcast feed is created automatically.
</Note>

***

## Curate your playlist

### **Standard playlist**

Use a Standard playlist to manually choose which articles you want in your playlist.

1. Click **Select articles**.
2. Choose the items to include.
3. Click **Save changes**.

***

### **Smart playlist**

Use a Smart playlist to automatically include content based on metadata - such as author, title, or publish date.

<Info>
  By default, a Smart playlist includes all articles until filters are applied.
</Info>

1. Click **Set rules**.
2. Click **+ Rule**.
3. Choose a metadata field (e.g., Title, Author, Published date).
4. Select an operator (`is`, `is not`, `contains`, `wildcard`).
5. Enter a value and click **Apply**.
6. Add more rules if needed (rules are combined with `AND`).
7. Click **Save changes**.

The playlist will update automatically when new matching articles are published.

***

## Embed your playlist on your website

You can embed your playlist as audio or video.

### Embed audio playlist

1. Click **Embed code**.
2. Select:
   * **Audio article**
   * **Audio summary**
3. Copy the embed code.
4. Paste into your website.

<Info>
  **Audio summary** is only available if your article has a summary generated.
</Info>

### Embed video playlist

1. Click **Embed code**.
2. Select:
   * **Video article**
   * **Video summary**
3. Copy the embed code.
4. Paste into your website.

<Info>
  * **Video article** is available only if a video exists for the article.<br />
  * **Video summary** is available only if the article has both a summary and a video.
</Info>

***

## Share your playlist URL

1. Click **Share**.
2. Choose:
   * **Articles**
   * **Summaries**
3. Click **Copy link**.
4. Share anywhere.

<Note>
  Your playlist must be set to **Public** to be viewable.
</Note>

***

## Copy your playlist ID

1. Click the **⋯** menu.
2. Click **Copy playlist ID**.

***

## Dynamic playlists

The playlists experience can be elevated and personalized by allowing your audience to create their own playlists from a collection of articles on your website.

This can be achieved by using our [Player JavaScript SDK](/docs-and-guides/distribution/player/sdk/javascript/getting-started).

<Note>This guide requires you to be comfortable with programming in JavaScript.</Note>

***

### Demo

Here is an interactive demo of a user-generated dynamic playlist that begins with a default set of articles which is totally optional.

You can add or remove articles from this playlist — simulating the user action of bookmarking — and it will be reflected live.

Changes to this demo playlist are stored in your browser for future visits. For real applications, user data should be saved in a database.

You can use your [BeyondWords project](/docs-and-guides/getting-started/concepts#projects) ID to load your articles.

<DynamicPlaylistDemo />

***

### Create a dynamic playlist

The BeyondWords player is quite flexible allowing you to dynamically load multiple articles and create a playlist from them.

The only required fields are the BeyondWords project ID and a list of article indentifiers which could be any of `contentId`, `sourceId`, `sourceUrl` or even another playlist's `playlistId`.

To create a dynamic playlist:

<Steps>
  <Step title="Create a project">
    Create a [project](/docs-and-guides/administration/projects) in BeyondWords. Generate some audio articles using the [Editor](/docs-and-guides/content/editor) or any of the [Integrations](/docs-and-guides/getting-started/overview#integrations).
  </Step>

  <Step title="Set up the player">
    Install the [player script](/docs-and-guides/distribution/player/sdk/javascript/getting-started#how-the-embed-script-works) or the [npm package](/docs-and-guides/distribution/player/sdk/javascript/getting-started#how-npm-installation-works) on your website.
  </Step>

  <Step title="Implement logic to save user data">
    This logic resides on your backend. You will need to store the user saved identifiers of the articles and their type so they can later be retrieved.
  </Step>

  <Step title="Initialize the player on your website">
    On the frontend, the player accepts a `playlist` param as an array of objects which should include one type of identifier each:

    ```js theme={null}
    import BeyondWords from '@beyondwords/player';

    new BeyondWords.Player({
      target: '#beyondwords-player',
      projectID: <ID>, // required
      playlist: [
        {
          // use only one of the following
          sourceId: "<SOURCE_ID>",
          contentId: "<CONTENT_ID>",
          sourceUrl: "<SOURCE_URL>",
          playlistId: <PLAYLIST_ID>,
        },
        // ... more items
      ],
    });
    ```

    It then fetches the requested content from your BeyondWords project and loads them as a playlist.

    Various other settings are also fetched from your project's [player settings](/docs-and-guides/distribution/player/settings) but they can be overriden through the [settings object](/docs-and-guides/distribution/player/sdk/javascript/player-settings) passed to the player.
  </Step>
</Steps>

<Note>You can load articles and playlist only from one project at a time.</Note>

# Podcast feeds
Source: https://docs.beyondwords.io/docs-and-guides/distribution/podcast-feeds

Create, curate, and share audio or video podcast feeds.

## Overview

Podcast feeds allow you to publish audio or video versions of your content to platforms such as Apple Podcasts, Spotify, Google Podcasts, and YouTube.

There are two ways to create your feed:

* **Standard feeds** - you manually choose which articles are included.
* **Smart feeds** - articles are included automatically based on rules you define.

This meanns you can create both one-off curated feeds and automatically updating dynamic feeds.

<img alt="podcast feed" />

***

## Create a podcast feed

To create a podcast feed:

1. Go to **Project > Distribution > Podcast Feeds**.
2. Click **+ Podcast Feed**.
3. Enter a title and description.
4. Upload a cover image.
5. Enter a feed URL (this will be used as your RSS link).
6. Choose a feed type:
   * **Standard** (manual curation)
   * **Smart** (rule-based curation)
7. Add categories and tags.
8. Add Author and Owner details.
9. Select the feed language.
10. Mark whether your feed contains explicit content.
11. Click **Continue**.

<Note>
  Every podcast feed automatically has a playlist associated with it.
</Note>

***

## Curate your podcast feeds

### Standard feed

Use a Standard feed when you want to hand-pick which articles become episodes.

To curate:

1. Click **Select articles**.
2. Choose any articles you want to include.
3. Click **Save changes**.

<Note>
  This feed only changes when you update it manually.
</Note>

### Smart feed

Use a Smart feed to automatically include content based on metadata - such as author, title, or publish date.

<Info>
  By default, a Smart feed includes all articles in your project until rules are added.
</Info>

To set rules:

1. Click **Set rules**.
2. Click **+ Rule**.
3. Choose a field to filter by (e.g., Title, Author, Published date).
4. Select an operator: `is`, `is not`, `contains`, or `wildcard`.
5. Enter a value.
6. Click **Apply**.
7. Add additional rules if needed (rules use `AND` logic).
8. Click **Save changes**.

<Note>Your feed will automatically update whenever new articles match your criteria.</Note>

***

## Share your feed

Share your feed as audio or video, in either full or summary format.

### Share as an audio feed

1. Click **Share**.
2. Select **Audio articles** or **Audio summaries**.
3. Click **Copy RSS Feed URL**.
4. Submit or publish the RSS URL to your website or podcast platforms.

### Share as a video feed

1. Click **Share**.
2. Select **Video articles** or **Video summaries**.
3. Click **Copy RSS Feed URL**.
4. Publish your feed to supported platforms.

<Note>
  Your feed must be set to **Public** in order to be accessible externally.
</Note>

# Concepts
Source: https://docs.beyondwords.io/docs-and-guides/getting-started/concepts

Understanding how BeyondWords is structured will help you get the most out of it.

## Basic concepts

### Organizations

An Organization is the highest-level entity in BeyondWords. Your account belongs to an Organization, and within it, you can create and manage multiple Projects. Organizations are typically set up at the company level, allowing teams to collaborate and manage audio content across different publications or categories.

### Projects

A Project is your AI audio CMS. Within a Project, you can manage CMS integrations, voice settings, audio articles, player settings, playlists, and podcast feeds. You can also track engagement with analytics, set up native ads, or connect to an ad server. This structure makes it easy to manage audio across different brands, topics, or content streams.

Each Project is organized into the following sections:

* **Content** - Create, edit, and manage your audio articles.
* **Distribution** - Publish your audio articles through players, playlists, and podcast feeds.
* **Analytics** - Track your audio performance and engagement metrics.
* **Monetization** - Create and manage direct ads or connect to your ad server.
* **Settings** - Connect your CMS and manage your project members.

#### Articles

An Article is a single item of AI-generated audio content, typically mapped 1:1 with your written articles.

Within each Project, you can create audio articles using the Editor, Magic Embed, API, or a CMS integration. Audio articles will be generated using the project's default voice, unless a different one is specified.

Articles are structured into segments, which correspond to paragraphs and other elements. Each segment can have its own language and voice settings, allowing for greater control over narration.

### Voices

We offer Premade and Custom voices.

* **Premade voices** are a selection of high-quality AI voices available for immediate use.
* **Custom voices** are voice clones based on your own Speakers. There are two types:
  * **Instant voice cloning** creates a voice clone from as little as 10 seconds of audio.
  * **Professional voice cloning** trains a hyper-realistic voice clone from as few as five article narrations.

By default, both Premade and Custom voices are available across all Projects. However, with Custom voices, you can control which Projects have access to them (coming soon).

### Members

Each Organization can have multiple Members. You can invite team members and control which Projects they can access.

Roles and permissions are managed at the Organization level, ensuring structured access control across Projects.

# Overview
Source: https://docs.beyondwords.io/docs-and-guides/getting-started/overview

BeyondWords connects publishers and their audiences through the possibilities of AI voice.

## Get started

<CardGroup>
  <Card title="Concepts" icon="lightbulb" href="/docs-and-guides/getting-started/concepts">
    Understanding how BeyondWords is structured will help you get the most out of it.
  </Card>

  <Card title="Quickstart" icon="forward-fast" href="/docs-and-guides/getting-started/quickstart">
    Get started with BeyondWords in minutes.
  </Card>
</CardGroup>

## Voices

<CardGroup>
  <Card title="Premade voices" icon="file-audio" href="/docs-and-guides/voices/premade-voices">
    Explore our library of high-quality premade voices for your content.
  </Card>

  <Card title="Instant voice cloning" icon="microphone" href="/docs-and-guides/voices/voice-cloning/instant-voice-cloning">
    Create a custom AI voice in minutes with our instant voice cloning technology.
  </Card>

  <Card title="Professional voice cloning" icon="microphone" href="/docs-and-guides/voices/voice-cloning/professional-voice-cloning">
    Get a studio-quality custom voice created by our professional team.
  </Card>
</CardGroup>

## Content

<CardGroup>
  <Card title="Editor" icon="pen-to-square" href="/docs-and-guides/content/editor">
    Learn how to generate audio articles using the Editor.
  </Card>

  <Card title="Articles" icon="newspaper" href="/docs-and-guides/content/articles">
    Learn how to manage your audio articles.
  </Card>

  <Card title="Voices" icon="file-audio" href="/docs-and-guides/voices/overview">
    Learn how to create and use voices.
  </Card>

  <Card title="Pronunciation" icon="ear-listen" href="/docs-and-guides/content/preferences/pronunciations">
    Learn how to customize the pronunciation of words in your audio articles.
  </Card>

  <Card title="Summarization" icon="comment-dots" href="/docs-and-guides/content/preferences/summarization">
    Learn how to create audio summaries of your audio articles.
  </Card>

  <Card title="Video" icon="video" href="/docs-and-guides/content/preferences/video">
    Learn how to create videos of your audio articles.
  </Card>

  <Card title="Background music" icon="music" href="/docs-and-guides/content/preferences/background-music">
    Learn how to add background music to your audio articles.
  </Card>

  <Card title="Filters" icon="filter" href="/docs-and-guides/integrations/extraction/filters">
    Learn how to filter what should be included or excluded in your audio articles.
  </Card>
</CardGroup>

## Distribution

<CardGroup>
  <Card title="Player" icon="play" href="/docs-and-guides/distribution/player/overview">
    Learn how to use the BeyondWords player.
  </Card>

  <Card title="Playlists" icon="list" href="/docs-and-guides/distribution/playlists">
    Create and manage playlists.
  </Card>

  <Card title="Podcast feeds" icon="podcast" href="/docs-and-guides/distribution/podcast-feeds">
    Create and manage podcast feeds.
  </Card>
</CardGroup>

## Analytics

<CardGroup>
  <Card title="Player" icon="chart-line" href="/docs-and-guides/analytics/player">
    Track and analyze audio engagement.
  </Card>
</CardGroup>

## Monetization

<CardGroup>
  <Card title="Custom ads" icon="rectangle-ad" href="/docs-and-guides/monetization/custom">
    Launch direct ads with BeyondWords.
  </Card>

  <Card title="VAST ads" icon="rectangle-ad" href="/docs-and-guides/monetization/vast">
    Launch programmatic ads with BeyondWords.
  </Card>
</CardGroup>

## Integrations

<CardGroup>
  <Card title="WordPress" icon="wordpress" href="/docs-and-guides/integrations/wordpress/overview">
    Integrate BeyondWords with WordPress.
  </Card>

  <Card title="Ghost" icon="code" href="/docs-and-guides/integrations/ghost">
    Integrate BeyondWords with Ghost.
  </Card>

  <Card title="API" icon="code" href="/docs-and-guides/integrations/api">
    Integrate with the BeyondWords API.
  </Card>

  <Card title="Webhooks" icon="code" href="/docs-and-guides/integrations/webhooks">
    Configure and manage webhooks.
  </Card>

  <Card title="RSS Feed Importer" icon="rss" href="/docs-and-guides/integrations/rss-feed-importer">
    Import content from RSS feeds.
  </Card>

  <Card title="Magic Embed" icon="wand-magic-sparkles" href="/docs-and-guides/integrations/magic-embed/overview">
    Use Magic Embed for seamless integration.
  </Card>
</CardGroup>

## Administration

<CardGroup>
  <Card title="Members" icon="user" href="/docs-and-guides/administration/members-and-roles">
    Manage your team and their access to BeyondWords.
  </Card>

  <Card title="Roles" icon="user-pen" href="/docs-and-guides/administration/members-and-roles#change-a-member’s-role">
    Assign team roles and craft custom ones tailored to your workflow.
  </Card>
</CardGroup>

# Quickstart
Source: https://docs.beyondwords.io/docs-and-guides/getting-started/quickstart

Learn how to make your first audio article with BeyondWords.

<Steps>
  <Step title="Create a project">
    Create a [project](/docs-and-guides/administration/projects) in BeyondWords.
  </Step>

  <Step title="Choose or clone a voice">
    [Choose a voice](/docs-and-guides/content/preferences/voices) or [clone a voice](/docs-and-guides/voices/voice-cloning/instant-voice-cloning) from our collection of voices.
  </Step>

  <Step title="Generate audio">
    Use the [Editor](/docs-and-guides/content/editor) to generate audio from your text.
  </Step>
</Steps>

### Next Steps

<CardGroup>
  <Card title="Distribution" icon="code" href="/docs-and-guides/getting-started/overview#distribution">
    Distribute your audio articles to your audience.
  </Card>

  <Card title="Integrations" icon="code" href="/docs-and-guides/getting-started/overview#integrations">
    Integrate BeyondWords with your existing tools and platforms.
  </Card>

  <Card title="API" icon="code" href="/api-reference/overview">
    Use the BeyondWords API to create and manage your audio articles.
  </Card>
</CardGroup>

# API
Source: https://docs.beyondwords.io/docs-and-guides/integrations/api

Learn how to use the BeyondWords API

# Overview

The BeyondWords API is a RESTful API that provides headless access to the entire platform. It has predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

## Base URL

The base URL for the API is: `https://api.beyondwords.io/v1/`

## Authentication

To access the API endpoints, you will need a Project ID and API Key. To obtain these, you will need to [create a project](/docs-and-guides/administration/projects#create-a-project) and go to **Project > Settings > Integrations > API**.

## Core Resources

The API provides access to several resources. The primary ones include:

### Projects

This object represents your project and its settings. You can list, create, retrieve, update and delete projects.

[Learn more about Projects](/api-reference/projects/list)

### Content

This object represents your generated content and its associated metadata. You can list, create, retrieve, update and delete content.

[Learn more about Content](/api-reference/content/overview)

### Player

You can use the API to retrieve audio and player configurations. The Player endpoints allow you to fetch player data using different identifiers such as:

* Content ID
* Source ID
* Source URL
* Playlist ID
* Multiple identifiers

[Learn more about Player](/api-reference/player/show)

### Analytics

You can use the API to retrieve analytics for an organization, project, content item, or ad. You can retrieve data for a specific time period and aggregate by year, month, week, day, or hour. You can also filter the data based on specific metrics.

[Learn more about Analytics](/api-reference/analytics/organization-analytics)

## Additional Resources

For complete API documentation, please refer to our [API Reference](/api-reference/overview).

# Content extraction
Source: https://docs.beyondwords.io/docs-and-guides/integrations/extraction/content-extraction

Content Extraction settings

## Overview

Content extraction is the process BeyondWords uses to pull article text into our platform. This is required for features like **Magic Embed**, **extraction-enabled RSS feeds**, and the **URL importer**.

<img alt="content-extraction" />

### Extraction mode

#### Automatic

In this mode, article content is automatically identified and structured using AI. The model recognises key elements on your webpage and outputs a clean, well-formatted article for audio generation. Any [content filters](/docs-and-guides/integrations/extraction/filters) you’ve configured are also applied during this process.

<Note>Recommended for all new projects setting up content extraction.</Note>

#### Manual

In this mode, article content is extracted using only the [content filters](/docs-and-guides/integrations/extraction/filters) you configure. This gives you full control over exactly which parts of the article are ingested.

#### Legacy

Content is extracted using a combination of [content filters](/docs-and-guides/integrations/extraction/filters) and rule-based heuristics. Unlike Automatic extraction it uses predefined conditions to locate content. This approach works well if the structure of your site is consistent, but it is less flexible than the Automatic mode.

<Note>This mode is recommended only for customers with existing projects already set up and working with this method.</Note>

### Request headers

For **paywalled or protected content**, you may need to provide authentication headers to grant our servers access to your content.

* Add a **Header Name** and **Header Value**.
* Click **+** to add multiple headers if needed.
* Ensure the headers grant full access to your content.

<Note>Requests will be made with **User-Agent: BeyondWords Importer**</Note>

### Static IP

If your website requires IP allowlisting, you may need to enable this option to grant our servers access to your content.

* Enable **Static IP**.
* Ensure your server allows full access to your content.

<Note>Requests will be sent from **20.234.8.180** or **176.34.249.78**</Note>

### Javascript enabled

Enable this option if your website is a single-page application (SPA) built with frameworks such as React, Vue.js, or Angular. When enabled, the extractor waits briefly for the page to finish loading and for network activity to stop before processing the HTML.

# Filters
Source: https://docs.beyondwords.io/docs-and-guides/integrations/extraction/filters

Content filter settings

## Overview

In BeyondWords, you can filter what should be included or excluded from audio generation. This is useful if you want to ensure that certain content is not included in the audio generation process.

<img alt="filters" />

## Create a filter

To add a filter go to **Settings > Extraction > Filters**.

1. Click **+ Filter**.
2. Select the type of filter you want to create.
3. Enter the filter value.
4. Select whether you want to include or exclude the content.
5. Set the scope of the filter.
6. Click **Save changes**.

<Steps>
  <Step title="Click + Filter">
    Click **+ Filter** to add a new filter.
  </Step>

  <Step title="Select the type of filter">
    Select the type of filter you want to create.

    > For example, you can select **Type** to filter by HTML element type.
  </Step>

  <Step title="Set the filter value">
    Specify the value you want to filter.

    > For example, you can enter **H2** to filter H2 elements.

    <Warning>
      When specifying elements, classes, or other HTML attributes, provide only the name or identifier. Avoid prefix characters like `<`, `.`, `#`, or any other syntax. The only exception is with `element_xpath`.
    </Warning>
  </Step>

  <Step title="Select whether you want to include or exclude the content.">
    Select whether you want to include or exclude the content.

    > For example, you can select **Include** to include H2 elements in the audio.
  </Step>

  <Step title="Set the scope">
    Set where this filter should apply:

    * **All projects**: Use this filter in all your projects.
    * **This project only**: Use this filter in this project only.
  </Step>

  <Step title="Save changes">
    Click **Save changes** to save the filter.

    <Tip>
      To apply the filter to past articles, go to **Project > Content > Articles** click **⋯** and then click **Regenerate**. Otherwise, the filter will only apply to new articles.
    </Tip>
  </Step>
</Steps>

## Filter types

### Element type

Create an **Element type** filter to include or exclude HTML elements based on their tag name.

> Filter content by HTML tag name such as `<H2>`, `<blockquote>`, `<ul>`, `<table>`, etc. This is useful for consistently including or excluding specific structural elements across your content.

### Element class

Create an **Element class** filter to include or exclude HTML elements based on their class attribute.

> Filter content by CSS class names such as `.header`, `.footer`, `.aside`, etc. This filter will be applied to any element that contains the specified class, allowing you to target styled components.

### Element ID

Create an **Element ID** filter to include or exclude HTML elements based on their ID attribute.

> Filter content by element IDs such as `#advert`, `#related`, `#navigation`, etc. This is useful for targeting unique elements on a page that you consistently want to include or exclude.

### Element data

Create an **Element data** filter to include or exclude HTML elements based on their data attributes.

> Filter content by data attributes such as `data-include`, `data-exclude`, etc. This allows you to add custom data attributes to your HTML specifically for controlling audio generation.

### Element XPath

Create an **Element XPath** filter to include or exclude HTML elements based on an XPath expression.

> Filter content using XPath expressions such as `//*[@role='dialog']`. This provides advanced targeting capabilities for complex document structures where other filter types may not be sufficient.

### Value

Create a **Value** filter to include or exclude HTML elements based on the text they contain.

> Filter content by searching for specific text such as "Sponsored". This filter will be applied to any element that contains the specified text value, allowing you to target elements based on their content rather than structure.

# Ghost
Source: https://docs.beyondwords.io/docs-and-guides/integrations/ghost

Integrate BeyondWords with Ghost

## Overview

The Ghost integration allows you to make your Ghost posts available in audio or video with BeyondWords. Once integrated, BeyondWords will automatically:

1. Create audio versions of your posts.
2. Embed the **BeyondWords Player** directly into your content.

## Set up

<Steps>
  <Step title="Access Ghost Admin settings">
    In Ghost Admin, go to **Settings > Integrations**.
  </Step>

  <Step title="Add custom integration">
    Click **Add custom integration**. Name it **BeyondWords**, then click **Add**.
  </Step>

  <Step title="Copy API credentials">
    Copy the **Admin API Key** and **API URL**, then paste them where needed.
  </Step>

  <Step title="Access Code Injection settings">
    In Ghost Admin, go to **Settings > Code injection**.
  </Step>

  <Step title="Add the BeyondWords script">
    Click **Open**, then navigate to **Site Footer**. Paste the BeyondWords Ghost Helper script and click **Save**.
  </Step>

  <Step title="Choose the content format">
    Select the embed code that matches the audio or video format you want to embed.

    ```html theme={null}
    <script async defer src="https://proxy.beyondwords.io/npm/@beyondwords/ghost-helper@latest" 
    onload="new BeyondWords.GhostHelper({
      projectId: <ID>
    })">
    </script>
    ```

    <Note>
      Replace `<ID>` with your project ID.
    </Note>
  </Step>
</Steps>

## Skipping audio for specific posts

If there’s a post you don’t want BeyondWords to convert into audio, you can use a tag to exclude it from audio generation.

To do this:

1. In the Ghost post editor, open the Post settings side panel.

2. Scroll to the Tags field.

3. Add the tag `#beyondwords-skip`.

When this tag is present, BeyondWords will not generate audio for that post, and no player will be embedded.

<Note>If you add this tag to a post that already has audio, any future changes to the post will not trigger new audio generation.</Note>

## Completion

You're all set! BeyondWords is now fully integrated with your Ghost site.

Next time you publish a post, an audio version will be created automatically. Once generated (this should take just a few minutes), it will be embedded in your post using the BeyondWords Player.

<Card title="Customize the BeyondWords Player" icon="play" href="/docs-and-guides/distribution/player/settings">
  Learn how to customize the appearance and behavior of the BeyondWords Player to match your website's design.
</Card>

# Overview
Source: https://docs.beyondwords.io/docs-and-guides/integrations/magic-embed/overview

Easily embed BeyondWords on any web page.

Magic Embed is a **lightweight, client-side solution** that lets you automatically
generate and embed audio into your articles. It will:

1. Extract the article content from your web page.
2. Generate the audio.
3. Load the **BeyondWords Player** on your web page.

Many of our customers choose Magic Embed because it is easy to set up. Once
Magic Embed has been added to your web page, the integration can be managed
through the BeyondWords dashboard.

## How it works

Magic Embed is built into the standard BeyondWords Player.
It can be enabled by setting a flag when initializing the player.

When enabled, the player will load as normal but it will send a signal to our
servers containing the URL of the page on which it was loaded.

Initially, no audio will be available and the player is hidden. However,
in the background our servers will fetch the HTML of your web page.

Content will be extracted using open-source tools and proprietary algorithms
to determine which article content is relevant.

Audio will begin generating in the background. Once it is ready, the player
will show for new visitors to the web page.

BeyondWords will continue to receive signals from the player and
automatically update the audio if your article has changed.

## Setup

<Steps>
  <Step title="Embed the player script">
    Copy the **Magic Embed script** and add it to your web page.

    ```html theme={null}
    <script async defer src="https://proxy.beyondwords.io/npm/@beyondwords/player@latest/dist/umd.js"
      onload="new BeyondWords.Player({
        target: this,
        projectId: <ID>,
        clientSideEnabled: true,
      })">
    </script>
    ```

    * Replace `<ID>` with your project ID.
    * Add other settings, such as [video](/docs-and-guides/content/preferences/video) or [summary](/docs-and-guides/content/preferences/summarization) to embed the audio summary, video summary, or video article instead of the default full audio article.
  </Step>

  <Step title="Set the source ID (optional)">
    We recommend that you associate the audio with your own ID, e.g. the
    article ID from your CMS.

    * Add the `sourceId: <ID>` [identifier](/docs-and-guides/distribution/player/overview#identifiers) to the embed code.

    <Note>
      By setting a sourceId, the audio will only be generated once even if the same content appears at multiple URLs.
    </Note>
  </Step>

  <Step title="Navigate to Magic Embed settings">
    Go to **Project → Settings → Integrations → Magic Embed**.\
    Toggle **Magic Embed** on to activate it.
  </Step>

  <Step title="Allow website domains">
    Add the domains where you want Magic Embed to work. This ensures BeyondWords only processes content from your authorized domains, not from any random domain where someone might embed your player.

    * Enter your domain (e.g., `yourwebsite.com`) and click **Add**.
    * Magic Embed will only function on pages under these domains.
    * Subdomains will need to be added separately:
      * e.g. `www.yourwebsite.com`
      * e.g. `app.yourwebsite.com`

    <Note>Make sure to save your changes once you have added the allowed domains.</Note>
  </Step>

  <Step title="Set request headers (optional)">
    For **paywalled or protected content**, you may need to provide
    authentication headers to grant our servers access to your content.

    To set this up navigate to [Extraction settings](/docs-and-guides/integrations/extraction/content-extraction): **Project > Settings > Extraction**

    * Add a **Header Name** and **Header Value**.
    * Click **+** to add multiple headers if needed.
    * Ensure the headers grant full access to your content.

    <Note>
      Requests will be made with `User-Agent: BeyondWords Importer`
    </Note>
  </Step>

  <Step title="Enable Static IP (optional)">
    If your website requires **IP allowlisting**, you may need to enable this
    option to grant our servers access to your content.

    * Enable **Static IP**.
    * Ensure your server allows full access to your content.

    <Note>
      Requests will be sent from `20.234.8.180` or `176.34.249.78`
    </Note>
  </Step>

  <Step title="Enable Magic Embed">
    After configuring all settings:

    1. Turn on the **Magic Embed** switch.
    2. Click **Save changes**.
  </Step>
</Steps>

<Note>
  For more control over content extraction and generation, you can use [data attributes](/docs-and-guides/content/data-attributes) to dynamically change the voice on a per-article basis, control publish dates, feature images, and other metadata.
</Note>

# Support
Source: https://docs.beyondwords.io/docs-and-guides/integrations/magic-embed/support

Frequently asked questions about setting up Magic Embed

### How can I test Magic Embed on localhost?

To test locally, your development environment must be accessible from the public internet - this allows our servers to fetch and process your page. Use a tool like [ngrok](https://ngrok.com/) or set up a
[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) to expose localhost via a secure, public URL.

### Why is no content being extracted from my website?

Make sure you've followed all of the [setup steps](/docs-and-guides/integrations/magic-embed/overview).

Common reasons include:

* Your domain (e.g. [www.yourwebsite.com](http://www.yourwebsite.com)) hasn’t been added under Magic Embed settings
* Your server is blocking our request - this can happen with paywalls or bot protection
* Your account has run out of credits, in which case Magic Embed will stop importing articles

If you’ve followed all setup steps and the issue persists, please contact [support@beyondwords.io](mailto:support@beyondwords.io).

### How can I exclude content that I *don't* want?

You can create [filters](/docs-and-guides/integrations/extraction/filters) to exclude content that should not be extracted from your web page. An exclude filter will exclude certain elements, whereas an include filter will exclude everything except the specified elements.

### How can I include content that I *do* want?

It's more difficult to force our content extractor to include specific content
once it has determined that it probably isn't part of the article. However, it
sometimes helps to exclude all other content using filters (see above).

Otherwise, please contact [support@beyondwords.io](mailto:support@beyondwords.io) and we will do our best to
help. If you need precise, fine-grained control then it might be worth
considering other options such as the
[RSS](/docs-and-guides/integrations/rss-feed-importer) or
[API](/docs-and-guides/integrations/api) integrations.

### How does image extraction work?

Images are considered part of your article's content and will also be extracted.
Images will show in the Editor relative to the text content of your article
and will be included in generated videos.

You can use [data attributes](/docs-and-guides/content/data-attributes)
to explicitly set the feature image.

### Why can I see content in the dashboard but not in the player?

We automatically extract the publish date from your content by checking various
metadata tags on your HTML page. If the publish date is in the future, then
audio won't be made available until that time in the player.

You can add [data attributes](/docs-and-guides/content/data-attributes)
to your HTML to control publish date more precisely and set various other
attributes such as the feature image.

### Why do I see a 404 error when loading the player?

This is normal. It means that no audio is available yet and the player has been
hidden. If Magic Embed is enabled then audio generation will be triggered and
load into the player once it's ready.

### How long does it take for audio to load in the player?

Usually five minutes after the first visitor. The content extraction and audio
generation happen more quickly but the player endpoint is cached for five
minutes. We support cache invalidation on our Enterprise plans.

### Does audio update if I change the article text?

Yes, Magic Embed will periodically extract content from your page and check if
it has changed. This only happens in response to the player being loaded on the
page and is subject to rate limits to avoid lots of requests.

### How do I avoid generating audio for old articles?

The simplest approach is to only embed the player on articles published after a certain date. You can check the publish date of your article and conditionally include the player embed code only for newer content.

Alternatively, you can set `clientSideEnabled: false` when initializing the player if the publish date of your article is before some cut-off date.

### Does Magic Embed work with single-page websites (JavaScript)?

Yes, our content extractor renders your page with full JavaScript support. It
waits a short amount of time for your page to settle and checks that the network
is no longer active before processing the HTML further.

This means that it will work with most single-page applications (SPAs) such as
client-side React apps, Vue.js and Angular. If you load content dynamically from
an API then the content should be extracted.

### I'm still stuck. What can I do?

Contact [support@beyondwords.io](mailto:support@beyondwords.io) and we can check our extraction logs and try to
help you diagnose issues with Magic Embed.

# RSS Feed Importer
Source: https://docs.beyondwords.io/docs-and-guides/integrations/rss-feed-importer

Turn articles from your RSS feeds into audio.

<Info>
  You will need to install the BeyondWords Player separately.
</Info>

## Overview

The RSS Feed Importer allows you to automatically convert articles from your RSS feeds into audio. Once enabled, BeyondWords will regularly check your feeds for new content and generate audio for each new article.

## Add a new feed

To get started go to **Project > Settings > Integrations > RSS Feed Importer**.

<Steps>
  <Step title="Click + Feed">
    Click the **+ Feed** button.
  </Step>

  <Step title="Select Feed type">
    Select the type of feed you want to add. You can choose between **XML** and **JSON**.
  </Step>

  <Step title="Add Feed URL">
    Enter the URL of your RSS feed.
  </Step>

  <Step title="Set request headers (optional)">
    For **paywalled or protected content**, you may need to provide authentication headers.

    * Add a **Header Name** and **Header Value** to authenticate requests.
    * Click **+** to add multiple headers if needed.
  </Step>

  <Step title="Enable Static IP (optional)">
    If your website requires **IP allowlisting**, enable this option to use a **static IP** for content extraction.
  </Step>

  <Step title="Enable page extraction (optional)">
    If your RSS feed only contains article links and not the full text, BeyondWords can fetch the content from article URLs.

    * If your articles are protected or behind a paywall and you need to set up [request headers](/docs-and-guides/integrations/extraction/content-extraction#request-headers) or a [static IP](/docs-and-guides/integrations/extraction/content-extraction#static-ip) this can be set up in [extraction settings](/docs-and-guides/integrations/extraction/content-extraction).
  </Step>
</Steps>

## Map the feed

After adding your feed, you'll need to map the RSS feed fields to BeyondWords article properties. This ensures the correct information - such as titles, descriptions, and content - is used to generate audio.

<Steps>
  <Step title="Required fields">
    Map these required fields from your feed:

    * **Title**: Select the field containing the article title
    * **Body**: Select the field containing the article content
    * **Source ID**: Select the field containing a unique identifier for each article (usually corresponds to your article ID in your CMS). This ID can be used to easily embed the audio on your articles using the BeyondWords Player.
    * **Source URL**: Select the field containing the URL for each article. This URL can also be used to easily embed the audio on your articles using the BeyondWords Player.
  </Step>

  <Step title="Optional fields">
    You can also map these optional fields:

    * **Summary**: Select the field containing a summary of the article. You can leave this empty if you use BeyondWords summarization.
    * **Author**: Select the field containing the article author's name
    * **Image URL**: Select the field containing the URL of the article's featured image
    * **Metadata**: Select the field containing additional metadata about the article
    * **Publish date**: Select the field containing when the article was published
      <Info>
        The publish date is used to check for updates to articles. When BeyondWords detects a change in the publish date, it will update the audio for that article.
      </Info>
  </Step>

  <Step title="Save and activate">
    Click **Save changes** to complete the setup. Your feed will automatically be enabled and BeyondWords will begin checking for articles.
  </Step>
</Steps>

## Managing your feed

Once your feed is set up:

* BeyondWords will automatically check your feed every 10 minutes for new or updated articles
* You can manually trigger an import by clicking the **⋯** button next to your feed and selecting **Run**
* New articles will be processed and converted to audio automatically
* Updated articles (detected by changes in the publish date) will have their audio updated

## Embed the Player

You can embed the audio on your website using either the Source ID or Source URL you mapped during setup.

<Card title="Embed the BeyondWords Player" icon="play" href="/docs-and-guides/distribution/player/overview">
  Once your content is imported and converted to audio, learn how to embed the BeyondWords Player on your website to deliver a seamless audio experience to your audience.
</Card>

# Webhooks
Source: https://docs.beyondwords.io/docs-and-guides/integrations/webhooks

Configure and manage webhooks

## Overview

Webhooks let you receive HTTP requests when an article's audio is created, updated, or deleted. Use them to automate workflows and keep your systems in sync with your BeyondWords content.

<img alt="webhooks" />

## Setting up a webhook

To get started go to **Project > Settings > Integrations > Webhooks**.

<Steps>
  <Step title="Create a new webhook">
    Click the **+ Webhook** button to create your first webhook.
  </Step>

  <Step title="Enter webhook URL">
    In the "Webhook URL" field, enter the URL where BeyondWords should send event notifications. This should be an endpoint on your server that's configured to receive and process webhook events.
  </Step>

  <Step title="Set request headers (optional)">
    If your webhook requires authentication or custom headers:

    * Enter a **Header name** (e.g., "Authorization")
    * Enter a **Header value** (e.g., "Bearer your-token-here")
    * Click the **+** button to add additional headers if needed
  </Step>

  <Step title="Enable the webhook">
    Toggle the **Enabled** switch to activate the webhook. You can disable it at any time without deleting the configuration.
  </Step>

  <Step title="Save your changes">
    Click the **Save changes** button to complete the setup.
  </Step>
</Steps>

## Webhook events

Once configured, your webhook will receive notifications for the following events:

* **Audio updated**: Triggered when newly generated audio or updated audio has finished processing.
* **Audio deleted**: When audio is removed from the system
* **Audio error**: If an error has occured during audio generation

## Webhook payloads

Each webhook notification includes a JSON payload with details about the event and the affected content. You can use this information to trigger appropriate actions in your systems.

### audio.updated

```javascript audio.updated payload expandable theme={null}
{
  "id": <id>,
  "title": "<title>",
  "project_id": "<project_id>",
  "external_id": "<source_id>",
  "state": "processed",
  "metadata": {},
  "media": [
    {
      "id": "<media_id>",
      "content_type": "mp3",
      "url": "<audio_url>",
      "duration": 281
    },
    {
      "id": "<media_id>",
      "content_type": "m3u8",
      "url": "<audio_url>",
      "duration": 281
    }
  ],
  "image_url": null,
  "deleted": false,
  "access_key": null,
  "processing_at": "2025-07-02T13:19:39.054Z",
  "published": true,
  "published_at": "2025-07-02T13:19:38.699Z",
  "content_id": "<content_id>",
  "source_id": "<source_id>",
  "is_copy": false,
  "action_type": "audio.updated"
}
```

### audio.deleted

```javascript audio.delete payload expandable theme={null}
{
  "id": <id>,
  "title": null,
  "project_id": "<project_id>",
  "external_id": "<source_id>",
  "state": "processed",
  "metadata": {},
  "media": [],
  "image_url": null,
  "deleted": true,
  "access_key": null,
  "processing_at": "2025-07-02T13:19:39.054Z",
  "published": true,
  "published_at": "2025-07-02T13:19:38.699Z",
  "content_id": "<content_id>",
  "source_id": "<source_id>",
  "is_copy": false,
  "action_type": "audio.deleted"
}
```

### audio.error

```javascript audio.error payload expandable theme={null}
{
  "id": <id>,
  "title": "<title>",
  "project_id": "<project_id>",
  "external_id": "<source_id>",
  "state": "processed",
  "metadata": {},
  "media": [
    {
      "id": "<media_id>",
      "content_type": "mp3",
      "url": "<audio_url>",
      "duration": 281
    },
    {
      "id": "<media_id>",
      "content_type": "m3u8",
      "url": "<audio_url>",
      "duration": 281
    }
  ],
  "image_url": null,
  "deleted": false,
  "access_key": null,
  "processing_at": "2025-07-02T13:19:39.054Z",
  "published": false,
  "published_at": "2025-07-02T13:19:38.699Z",
  "content_id": "<content_id>",
  "source_id": "<source_id>",
  "is_copy": false,
  "action_type": "audio.error"
}
```

## Managing webhooks

You can create multiple webhooks to integrate with different systems. For each webhook, you can:

* Edit the configuration
* Temporarily disable it
* Delete it when no longer needed

## Security considerations

For enhanced security:

* Use HTTPS URLs for your webhook endpoints
* Implement authentication using request headers
* Validate incoming webhook requests on your server

# Filters
Source: https://docs.beyondwords.io/docs-and-guides/integrations/wordpress/filters

We provide WordPress filters which allow you to modify the default data we use during the execution of our plugin.

## beyondwords\_content\_params

Filters the body params we send to the BeyondWords API when processing audio.

**Parameters** <br />

`$params` *array* <br />
The params we send to the BeyondWords API. <br />

`$post_id` *int* <br />
The WordPress Post ID

### Example 1

Prepend the author name and the published date to the audio body

```php theme={null}
function my_beyondwords_content_params( $params, $post_id ) {
    $name = get_the_author_meta( 'display_name', $post_id );
    $date = get_the_date( '', $post_id );
​
    $prepend = '';
​
    if ( $name ) {
        $prepend .= '<p>By ' . esc_html( $name ) . '</p>';
    }
​
    if ( $date ) {
        $prepend .= '<p>' . esc_html( $date ) . '</p>';
    }
​
    $params['body'] = $prepend . $params['body'];

    return $params;
}
​
add_filter( 'beyondwords_content_params', 'my_beyondwords_content_params', 10, 2 );
```

### Example 2

Send the value of a custom field called "my\_custom\_field" to the BeyondWords API as a metadata field named "my\_custom\_key".

```php theme={null}
function my_beyondwords_content_params( $params, $post_id ) {
    if ( is_object( $params['metadata'] ) ) {
        $params['metadata']->my_custom_key = get_post_meta( $post_id, 'my_custom_field', true );
    }
​
    return $params;
}
add_filter( 'beyondwords_content_params', 'my_beyondwords_content_params', 10, 2 );
```

### Example 3

Forward the value of a custom field to the BeyondWords API.

```php theme={null}
function my_beyondwords_content_params( $params, $post_id ) {
  // Use a custom field "my_ads_enabled" for the "ads_enabled" param for API requests
  $params[ 'ads_enabled' ] = (bool) get_post_meta( $post_id, 'my_ads_enabled', true );
​
  return $params;
}
add_filter( 'beyondwords_content_params', 'my_beyondwords_content_params', 10, 2 );
```

## BeyondWords\_player\_html

Filters the HTML of the BeyondWords Player.

**Parameters** <br />

`$html` *string* <br />
The HTML for the audio player. The audio player JavaScript may fail to locate the target element if you remove or replace the default contents of this parameter.

`$post_id` *int* <br />
The WordPress Post ID

`$project_id` *string* <br />
BeyondWords project ID.

`$content_id` *string* <br />
BeyondWords content ID.

### Example 1

Wrap the player in a container div.

```php theme={null}
function my_beyondwords_player_html( $html, $post_id, $project_id, $content_id ) {
    return '<div class="my-container">' . $html . '</div>'
}
add_filter( 'beyondwords_player_html', 'my_beyondwords_player_html', 10, 4 );
```

### Example 2

Hiding the BeyondWords player for non-signed in users.

```php theme={null}

function my_beyondwords_player_html( $html, $post_id, $project_id, $content_id ) {
    $current_user = wp_get_current_user();
​
    if ( $current_user->exists() ) {
        return $html;
    }
​
    return '';
}
add_filter( 'beyondwords_player_html', 'my_beyondwords_player_html', 10, 4 );
```

## beyondwords\_player\_script\_onload

Filters the onload attribute of the BeyondWords Player script.

<Note> The strings should be in double quotes, because the output of this is run through esc\_js() before it is output into the DOM.</Note>

**Parameters** <br />

`$onload` *string* <br />
The string value of the onload script.

`$params` *array* <br />
The SDK params for the current post, including `projectId` and `contentId`.

### Example 1

Append a custom command to the default onload script.

```php theme={null}
function my_beyondwords_player_script_onload( $onload, $params ) {
    return $onload . 'initializeCustomUserInterface();';
  }
add_filter( 'beyondwords_player_script_onload', 'my_beyondwords_player_script_onload', 10, 2 );
```

### Example 2

Log the player params to the browser console before the player initializes.

```php theme={null}
function my_beyondwords_player_script_onload( $onload, $params ) {
     // Console log the params we pass to the SDK
     $my_command = 'console.log("🔊", ' . wp_json_encode( $params, JSON_FORCE_OBJECT | JSON_UNESCAPED_SLASHES ) . ');';

     // Prepend the command to the default onload script
     return $my_command . $onload;
}
add_filter( 'beyondwords_player_script_onload', 'my_beyondwords_player_script_onload', 10, 2 );
```

## beyondwords\_player\_sdk\_params

Filters the BeyondWords Player SDK parameters.

Refer to the [Player Settings](/docs-and-guides/distribution/player/sdk/javascript/player-settings) for a the list of available parameters.

**Parameters** <br />

`$params` *array* <br />
The SDK parameters

`$post_id` *int* <br />
The post ID

### Example 1

Use a custom colour for the text in all players.

```php theme={null}
function my_beyondwords_player_sdk_params( $params, $post_id ) {
  $params[ 'textColor' ] = 'rgba(255, 0, 0, 0.8)';

  return $params;
}
add_filter( 'beyondwords_player_sdk_params', 'my_beyondwords_player_sdk_params', 10, 2 );
```

### Example 2

Set the Advert consent parameter for all users.

```php theme={null}
function my_beyondwords_player_sdk_params( $params, $post_id ) {
  $params[ 'advertConsent' ] = 'non-personalized';

  return $params;
}
add_filter( 'beyondwords_player_sdk_params', 'my_beyondwords_player_sdk_params', 10, 2 );
```

### Example 3

Use a blue icon colour for players in posts tagged with "News".

```php theme={null}
function my_beyondwords_player_sdk_params( $params, $post_id ) {
  $tags = get_the_tags( $post_id );

  foreach ( $tags as $tag ) {
    if ( isset( $tag->name ) && $tag->name === "News" ) {
      $params[ 'iconColor' ] = '#000080'; // Navy blue
    }
  }
  return $params;
}
add_filter( 'beyondwords_player_sdk_params', 'my_beyondwords_player_sdk_params', 10, 2 );
```

### Example 4

Skip ads for signed-in users.

```php theme={null}
function my_beyondwords_player_sdk_params( $params, $post_id ) {
  $current_user = wp_get_current_user();

  if ( $current_user->exists() ) {
    // This will override the project defaults
    $params['adverts'] = [];
  }

  return $params;
}
add_filter( 'beyondwords_player_sdk_params', 'my_beyondwords_player_sdk_params', 10, 2 );
```

## beyondwords\_settings\_player\_styles

Filters the player styles – the "Player style" `<select>` options presented on the plugin settings page and post edit screens.

**Parameters** <br />

`$styles` *array* <br />
Associative array of player styles.

### Example

Remove "Small" from the "Player style" select options to prevent editors from selecting it on the post edit screens.

```php theme={null}
function my_beyondwords_settings_player_styles( $styles ) {
  if ( array_key_exists( 'small', $styles ) ) {
    unset( $styles['small'] );
  }

  return $styles;
}
add_filter( 'beyondwords_settings_player_styles', 'my_beyondwords_settings_player_styles' );
```

## beyondwords\_settings\_post\_statuses

Filters the post statuses that BeyondWords considers for audio processing.

**Parameters** <br />

`$statuses` *string\[]* <br />
The post statuses that we consider for audio processing.

### Example

```php theme={null}
function my_beyondwords_settings_post_statuses( $statuses ) {
    // Add a custom status (which may be provided by another plugin)
    $statuses[] = 'your_custom_status';

    return $statuses;
}
add_filter( 'beyondwords_settings_post_statuses', 'my_beyondwords_settings_post_statuses' );
```

## beyondwords\_settings\_post\_types

Filters the post types supported by BeyondWords.

This defaults to all registered post types with `custom-fields` in their `supports` array. Our content and project IDs are stored in custom fields, so if any of the supplied post types do not support custom fields then audio will not work as expected.

**Parameters** <br />

`$post_types` *string\[]* <br />
An array of post type names.

### Example

```php theme={null}
function my_beyondwords_settings_post_types( $post_types ) {
    // $post_types contains the currently-supported post types

    // Only support 'posts'
    return [ 'posts' ];
}
add_filter( 'beyondwords_settings_post_types', 'my_beyondwords_settings_post_types' );
```

# Plugin Overview
Source: https://docs.beyondwords.io/docs-and-guides/integrations/wordpress/overview

Integrate BeyondWords with WordPress

<CardGroup>
  <Card title="Installation" icon="download" href="#install-the-plugin">
    Install and configure the BeyondWords WordPress plugin
  </Card>

  <Card title="Generate Audio" icon="microphone" href="#audio-generation">
    Create audio for new and existing posts
  </Card>

  <Card title="Categories" icon="folder-tree" href="#generate-audio-by-category">
    Control audio generation by category
  </Card>

  <Card title="Player" icon="circle-play" href="#player">
    Configure the BeyondWords Player
  </Card>

  <Card title="Sidebar" icon="sidebar" href="#beyondwords-sidebar">
    Access advanced audio options
  </Card>

  <Card title="Languages" icon="language" href="#language">
    Configure multiple languages
  </Card>
</CardGroup>

# Install the plugin

1. Install **BeyondWords-Text-To-Speech** from the WordPress plugin marketplace.
2. Activate the plugin and open the plugin Settings.
3. Enter your **API Key** and **Project ID** in the **Credentials** tab.
4. These can be found in **Project > Settings > Integrations > WordPress**.
5. Save changes.

**Video tutorial**

<iframe title="WordPress Plugin" />

## Audio Generation

With the plugin installed, each published article is automatically converted to audio, with the player being prepended to the top of your posts body.

### For new posts

1. Ensure the plugin is installed correctly.
2. Publish your post
3. Audio generation will be triggered within BeyondWords (can take a few minutes, depending on length)
4. Once the audio is generated the [BeyondWords Player](/docs-and-guides/distribution/player/overview) will be prepended to the body of your article.

### For previous posts

1. Navigate to the **All Posts** section in the WordPress dashboard.
2. Select all previous posts you want to generate audio for.
3. From the **Batch Actions** dropdown menu select **Generate Audio** and click Apply.
4. Selected posts will be sent for audio generation
5. The BeyondWords Player will be added to your article once generation is complete.

# BeyondWords plugin Settings

<img alt="tabs" />

<Info>
  Plugin and BeyondWords dashboard settings will sync automatically.
</Info>

## Content

The Content Section allows you to control which parts of your content are converted into audio.

### Integration method

#### REST API

This is the default setting for the plugin, audio generation is built on top of our API. It’s the most stable option for most WordPress users and the recommended choice to start with.

If you are having issues using the REST API and are using a page builder such as Elementor we would reccomend trying the Magic Embed integration method.

#### Magic Embed

This option is designed for users who are using themes or page builders that may cause the REST API to not function as expected. It injects the [Magic Embed](/docs-and-guides/integrations/magic-embed/overview) script directly onto your WordPress pages, running after the page is built.

<Note>For this to work correctly, Magic Embed must be selected in the plugin and configured within your [BeyondWords dashboard](/docs-and-guides/integrations/magic-embed/overview#setup).</Note>

### Auto-publish

With auto publishing enabled, audio is published as soon as it's generated. <br />
If disabled, audio must be manually published from the BeyondWords dashboard.

### Generate Audio by Category

You can choose to have the **Generate Audio** checkbox in the editor deselected by default for certain categories.

1. Uncheck "Posts/Pages" to reveal the category list.
2. Check the categories you want to automatically generate audio for.
3. Only posts in the selected categories will generate audio.

<Info>
  If a post belongs to both a selected and unselected category, audio will still be generated.
</Info>

## Voices

In the Voices tab, you can select your article language and preferred voice.

You can also manage your [voices](/docs-and-guides/content/preferences/voices) directly in the BeyondWords dashboard, where you’ll find sample audio clips to preview each option.

## Player

### Headless mode

The BeyondWords plugin now includes a headless mode, meaning a publisher can take advantage of audio processing and the audio CMS whilst building their own front-end players.

Once in headless mode you can [build your own UI](https://github.com/beyondwords-io/player/blob/main/doc/building-your-own-ui.md) on top of the player.

### Player style

You can set the default player style for all future generated posts. The available options are Standard, Small, Large, and Video.

<Note>The Video player option is only available if video generation is enabled in your BeyondWords Dashboard.</Note>

You can also enable **Text Highlighting** and **Playback from Paragraphs**.

Text Highlighting highlights the current paragraph as the audio is being read, helping users follow along.
Playback from Paragraphs allows users to click on any paragraph to begin playback from that specific point.

### Widget

The [player widget](/docs-and-guides/distribution/player/settings#player-widget) is a compact, floating audio player that appears when a user scrolls away from the main embedded player. It keeps essential controls visible and accessible, even as the user navigates around the page. You are able to set the widget style and position within the plugin or within the BeyondWords Dashboard.

## Summarization

Summarization can be toggled on or off from within the BeyondWords dashboard. The tab in the plugin will redirect you back to the dashboard settings.

For full details, please visit our dedicated [summarization](/docs-and-guides/content/preferences/summarization) section.

## Pronunciations

Pronunciation rules can be added or set from within the BeyondWords dashboard. The tab in the plugin will redirect you back to the dashboard settings.

For full details, please visit our dedicated [Pronunciation rules](/docs-and-guides/content/preferences/pronunciations) section.

## BeyondWords Sidebar

The BeyondWords sidebar is available on the post edit screen and allows you to configure advanced audio options on a post-by-post basis.

<img alt="sidepanel" />

### Player Style

Select the player style for the article. The available options are Standard, Small, Large, and Video.

### Player Content

If summarization is enabled, you can choose whether the player displays audio for the full article or just the summary.

### Language

For multilingual WordPress sites, you can specify the language in which the article should be generated.

### Voice

By default, this voice will be the primary voice that was selected within the plugin or BeyondWords dashboard. You can override this and choose a different voice for audio generation.

# Support
Source: https://docs.beyondwords.io/docs-and-guides/integrations/wordpress/support

To help our team debug any issues, or respond to your queries, please send us your WordPress site health and the inspect panel information of the affected post.

## Site health

In the left-hand sidebar select Tools > Site Health. Once in the Site Health panel click on the Info tab.

Copy the site health info to clipboard and add this to your support request.

<img alt="sitehealth" />

## Inspect Panel

The Inspect panel on the post edit screen allows you to view, copy, or remove the BeyondWords data stored in WordPress for each post.

Once you have located the Inspect panel in either the Block Editor or Classic Editor append the data from the affected post to your support request.

### Block editor

You can find the Inspect panel at the bottom the BeyondWords Sidebar. If it's closed (with the arrow pointing down) then click on the panel title to open it.

### Classic editor

You can enable or disable the BeyondWords Inspect panel using the Screen Options menu. Once enabled, it will appear at the bottom of your post editing screen.

## Support requests

### 404 not found

If there's been a disconnect between a WordPress post and the corresponding audio in BeyondWords, this can result in a 404 error. This should not be a frequent occurence and if it's happening regularly, please reach out to our support team who can investigate further.

<img alt="404" />

**Steps to fix the error**

<Steps>
  <Step title="Open BeyondWords Inspect Panel">
    Access the Inspect panel via the [Block Editor](#block-editor) or [Classic Editor](#classic-editor)
  </Step>

  <Step title="Remove BeyondWords data">
    Click **Remove** to delete the BeyondWords audio data and then save your post.
    Recent plugin versions will also attempt to delete the corresponding audio from your BeyondWords dashboard.

    <img alt="remove" />
  </Step>

  <Step title="Republish your post">
    Once the inspect panel data has been removed, republish your post and make sure the `Generate audio` checkbox is ticked to trigger new audio generation.
  </Step>
</Steps>

# API (Legacy)
Source: https://docs.beyondwords.io/docs-and-guides/migration-guides/api-legacy

Migrate from legacy API to current version

We're deprecating our legacy API at the end of Q2 2025.

To support this change, we've created a migration guide to help you update your integration. It includes example requests, responses and the steps needed to migrate.

If you're currently using the legacy API, please read this migration guide to ensure continued functionality. You can find our most up-to-date API documentation [here](/api-reference/overview).

## Updating your request header

|                           | Legacy API                          | New API                         |
| ------------------------- | ----------------------------------- | ------------------------------- |
| **Base URL**              | `https://app.beyondwords.io/api/v4` | `https://api.beyondwords.io/v1` |
| **Authentication header** | `'Authorization'`                   | `'X-Api-Key'`                   |
| **Authentication value**  | Your API key                        | Your API key                    |

### Example requests

<CodeGroup>
  ```javascript New API theme={null}
  curl --request POST \
       --url https://api.beyondwords.io/v1 \
       --header 'X-Api-Key: <APIKEY>' \
       --header 'Content-Type: application/json' \
  ```

  ```javascript Legacy API theme={null}
  curl -L \
    --request POST \
    --url 'https://app.beyondwords.io/api/v4' \
    --header 'Authorization: <APIKEY>' \
    --header 'Content-Type: application/json' \

  ```
</CodeGroup>

### Key differences

* Base URL: `https://api.beyondwords.io/v1` (replaces `https://app.beyondwords.io/api/v4`)

* Authentication: `X-Api-Key` (replaces `Authorization` header)

## Endpoint and request body updates

<br />

|                         | Legacy API                     | New API                                                                     |
| ----------------------- | ------------------------------ | --------------------------------------------------------------------------- |
| **Endpoint**            | `/projects/{project_id}/audio` | `/projects/{project_id}/content`                                            |
| **Title Format**        | Plain text                     | Plain text or HTML-formatted (e.g., `<h1>Title</h1>`) — **HTML preferred.** |
| **Body Format**         | Plain text                     | Plain text or HTML-formatted (e.g., `<p>Body</p>`) — **HTML preferred.**    |
| **Content ID Handling** | Set using `'external_id'`      | Set using `'source_id'`                                                     |

### Example requests

<CodeGroup>
  ```javascript New API theme={null}
  curl --request POST \
       --url https://api.beyondwords.io/v1/projects/{project_id}/content \
       --header 'X-Api-Key: <APIKEY>' \
       --header 'Content-Type: application/json' \
       --data '
  {
    "type": "auto_segment",
    "title": "<h1>Title</h1>",
    "body": "<p>Example body text.</p>",
    "source_id": "<articleId>"
  }'
  ```

  ```javascript Legacy API theme={null}
  curl -L \
    --request POST \
    --url 'https://app.beyondwords.io/api/v4/projects/{project_id}/audio' \
    --header 'Authorization: <API KEY>' \
    --header 'Content-Type: application/json' \
    --data '
  {
    "title":"Title",
    "body":"Example body text.",
    "external_id":"<articleId>"
  }'
  ```
</CodeGroup>

These examples compare requests made using the Legacy APIs create endpoint  with those using the new APIs create endpoint.

### Example response

<CodeGroup>
  ```javascript New API theme={null}
  {
    "id": "744429b3-d77e-4230-b29f-c301f9da3bdd",
    "title": "title",
    "type": "auto_segment",
    "source_id": "<articleId>",
    "source_url": null,
    "published": true,
    "publish_date": "2025-03-12T16:28:19Z",
    "auto_segment_updates_enabled": true,
    "ai_summary_updates_enabled": true,
    "summary": null,
    "body": "example body text"
  }
  ```

  ```javascript Legacy API theme={null}
  {
    "id": 15312327,
    "title": "Title",
    "external_id": "<articleId>",
    "state": "unprocessed",
    "metadata": {
      "key": "value"
    },
    "media": [],
    "image_url": null,
    "deleted": false,
    "access_key": null,
    "processing_at": "2025-02-18T16:33:35.537Z",
    "published": true,
    "published_at": "2025-02-18T16:33:35.315Z",
    "source_id": "<externallySetID>"
  }
  ```
</CodeGroup>

<Info>This is not a full response. It has been shortened to highlight the main differences. For more details on what a full response looks like, please visit our [documentation](#).</Info>

### Key differences

In the legacy API response, the returned ID is a numeric "podcast" id , which will no longer be used. In contrast, the new API returns a string `content_id`, which will remain the standard identifier moving forward.

While setting a `source_id` when creating content is optional, doing so eliminates the need to store the `content_id` from the response. Without a `source_id`, you may need to save the `content_id` separately to embed the player. By setting the `source_id` as the article ID you may have already set, you can easily use this to embed the BeyondWords player without additional data handling.

## Migration steps

<Steps>
  <Step title="Update the base URL">
    * Change all API requests from: `https://app.beyondwords.io/api/v4`
    * To: `https://api.beyondwords.io/v1`
      <Tip>Search your codebase for the legacy URL to find all instances</Tip>
  </Step>

  <Step title="Update request header method">
    * Legacy API: Uses the `Authorization` header with the API key.
    * New API: Requires the `X-Api-Key` header with the API key.
    * **Note**: The API key value itself remains the same
  </Step>

  <Step title="Update endpoints">
    Replace old API endpoints with the new ones:

    * Legacy API: `/projects/{project_id}/audio`
    * New API: `/projects/{project_id}/content`
    * **Also update**: Any other endpoints you're using (see our [full documentation](#))
  </Step>

  <Step title="Handle ID changes">
    * Legacy API: Returns a numeric "podcast" id (deprecated).
    * New API: Returns a string-based UUID "content" id.
    * **Action required**: Update any code that expects or processes the ID
  </Step>

  <Step title="Use source_id for easier integration">
    * Change field name from `external_id` to `source_id` in your requests
    * Setting a `source_id` when creating content is optional but recommended
    * If you set `source_id` to match your existing article ID, you can use it to embed the BeyondWords player without needing to store the content\_id from the response
  </Step>

  <Step title="Update Content Format (Optional)">
    * Consider using HTML formatting for title and body content
    * Example: `"title": "<h1>Title</h1>"` instead of `"title": "Title"`
    * This provides better control over how content is processed
  </Step>
</Steps>

## FAQ

**Q: Will my existing API key still work?**\
A: Yes, your API key will continue to work. Only the header name and endpoints are changing.

**Q: What happens if I don't migrate by the deadline?**\
A: After Q2 2025, the legacy API will be shut down and any applications using it will receive errors.

**Q: Can I use both APIs during the transition period?**\
A: Yes, both APIs will be available until the deprecation date to allow for a smooth transition.

📖 For full details, refer to our [API documentation](/api-reference/overview).\
💬 If you need further support, reach out on Slack or contact [support@beyondwords.io](mailto:support@beyondwords.io).

## Summary of key changes

| Feature            | Legacy API                          | New API                          | Notes                                    |
| ------------------ | ----------------------------------- | -------------------------------- | ---------------------------------------- |
| Base URL           | `https://app.beyondwords.io/api/v4` | `https://api.beyondwords.io/v1`  | All endpoints use the new base URL       |
| Authentication     | `Authorization` header              | `X-Api-Key` header               | Same API key, different header name      |
| Content creation   | `/projects/{project_id}/audio`      | `/projects/{project_id}/content` | Endpoint name change                     |
| Content identifier | Numeric `id`                        | String UUID `id`                 | Format change for BeyondWords content ID |
| Article identifier | `external_id`                       | `source_id`                      | Field name change (both string format)   |
| Content format     | Plain text only                     | Plain text or HTML (preferred)   | Enhanced formatting options              |

<Warning>
  Remember to update all instances where your application interacts with our API, including scheduled jobs, error handling, and any third-party integrations.
</Warning>

# Player (Legacy)
Source: https://docs.beyondwords.io/docs-and-guides/migration-guides/player-legacy

Migrate from legacy player to current version

We're deprecating our legacy Player at the end of Q2 2025.

To support this transition, we've created a migration guide to help you update your integration and take advantage of the new features.

This guide will walk you through the migration process, whether by updating the player embed script or using NPM.

## Whats new?

The updated player comes with several new customization features designed to enhance user engagement and improve the listening experience.

For more details on the new player’s features, visit our [player documentation](/docs-and-guides/distribution/player/settings). To explore customization options and test new features in a sandbox environment, check out our [player demo page](https://beyondwords-io.github.io/player-demo/).

## Update the Embed Script

To start using the new BeyondWords player, you’ll need to replace the legacy embed script with the one below.

<CodeGroup>
  ```javascript New Embed Script theme={null}
  <script async defer src="https://proxy.beyondwords.io/npm/@beyondwords/player@latest/dist/umd.js" 
    onload="new BeyondWords.Player({ 
      target: this, 
      projectId: <projectID>,
      contentId: '<ID>'
    })">
  </script>;
  ```

  ```javascript Legacy Embed Script theme={null}
  <iframe
    id="speechkit-io-iframe"
    data-src="https://audio.beyondwords.io/e/{contentID}"
    frameborder="0"
    scrolling="no"
    allowfullscreen="false"
    style="display: none;">
  </iframe>

  <script 
    src="https://proxy.beyondwords.io/npm/@beyondwords/audio-player@latest/dist/module/iframe-helper.js" 
    type="text/javascript">
  </script>

  ```
</CodeGroup>

* The `<script>` tag loads the BeyondWords Player and instantiates a new player instance.

* The async and defer attributes ensure the browser doesn’t stall while downloading the script.

* Setting `target: this` places the player immediately after the script tag in the `<body>`. If you need a different placement, you can specify another target.

* You must replace the `<ID>` placeholders in the script with your **projectId** and **contentId** to ensure the correct audio is played.

You can use any of the following properties along with **projectId** to initialise the player.

| **Property** | **Description**                                                                                                                                                                                   |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contentId`  | Unique UUID string for the audio content.<br /> You can also pass the previous integer audio ID as a string for users migrating from the legacy API.                                              |
| `sourceId`   | The externally provided source identifier for a content item.<br />This could be the ID from your CMS, the `<guid>` from an RSS `<item>`, or the post ID if generated using the WordPress Plugin. |
| `sourceUrl`  | The URL containing the source content.<br /> This could be the public URL submitted via the API, the `<link>` from an RSS `<item>`, or the post URL from the WordPress Plugin.                    |
| `playlistId` | The unique ID for a playlist created in the dashboard or through the API.                                                                                                                         |

## Update via NPM

<Steps>
  <Step title="Add the new player NPM package">
    <CodeGroup>
      ```javascript New theme={null}
      npm add @beyondwords/player
      ```

      ```javascript Legacy theme={null}
      npm install --save @beyondwords/audio-player
      ```
    </CodeGroup>
  </Step>

  <Step title="Add a target <div>">
    This will be where the player is shown in your web application.

    ```javascript theme={null}
    <div id='beyondwords-player'></div>
    ```
  </Step>

  <Step title="Initialize the player">
    ```javascript theme={null}
    import BeyondWords from '@beyondwords/player';

    new BeyondWords.Player({ target: '#beyondwords-player', projectID: <ID>, contentId: '<ID>' });
    ```

    You must replace the `<ID>` placeholders in the script with your **projectId** and **contentId** to ensure the correct audio is played.
  </Step>
</Steps>

You can use any of the following properties along with **projectId** to initialise the player.

| **Property** | **Description**                                                                                                                                                                                   |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contentId`  | Unique UUID string for the audio content.<br /> You can also pass the previous integer audio ID as a string for users migrating from the legacy API.                                              |
| `sourceId`   | The externally provided source identifier for a content item.<br />This could be the ID from your CMS, the `<guid>` from an RSS `<item>`, or the post ID if generated using the WordPress Plugin. |
| `sourceUrl`  | The URL containing the source content.<br /> This could be the public URL submitted via the API, the `<link>` from an RSS `<item>`, or the post URL from the WordPress Plugin.                    |
| `playlistId` | The unique ID for a playlist created in the dashboard or through the API.                                                                                                                         |

# Custom
Source: https://docs.beyondwords.io/docs-and-guides/monetization/custom

Launch direct ads with BeyondWords

## Overview

Use Custom ads to upload, launch, and track your own ads. You can launch both audio and video ads.

<img alt="monetization" />

<Info>
  Audio ads will play on audio articles or summaries. Video ads will play on video articles or summaries.
</Info>

## Create a Custom ad

To create a Custom ad:

1. Go to **Project > Monetization**.
2. Click **+ ad**.
3. Select **Custom**.
4. Upload the audio or video ad.
5. Enter a name for the ad. This will be visible to users.
6. Set the ad placement: pre-roll, mid-roll, or post-roll.
7. Set the ad schedule (optional).
8. Add a companion URL (optional). This will be a clickable link shown to users when the ad plays.
9. Add a companion image (optional). This will be a clickable image shown to users when the ad plays.
10. Customize the player appearance (optional). You can customize the player appearance to match the ad.
11. Click **Save changes**.

## Enable or disable a Custom ad

To enable or disable a Custom ad:

1. Go to **Project > Monetization**.
2. Toggle the ad to **Enabled** or **Disabled**.

## Edit a Custom ad

To edit a Custom ad:

1. Go to **Project > Monetization**.
2. Click the ad you want to edit.
3. Click the **⋯** button.
4. Select **Edit**.
5. Make the necessary changes.
6. Click **Save changes**.

## Delete a Custom ad

To delete a Custom ad:

1. Go to **Project > Monetization**.
2. Click the ad you want to edit.
3. Click the **⋯** button.
4. Select **Delete**.

## Ad metrics

BeyondWords tracks the following metrics on a per-ad basis. The metrics are updated every few minutes.

### Plays

The number of times an ad was played. We count one play per user session.

### Completion rate

The percentage of ad plays that reached completion. We calculate this as Completions divided by Plays.

### Completions

The number of ad plays that reached completion. We count this when the ad finishes playing.

### Click-through rate

The percentage of ad plays that resulted in clicks. We calculate this as Click divided by Plays.

### Clicks

The number of times an ad was clicked. We count one click per user session.

## Filter metrics

You can filter the ad metrics by the following:

* **Content type**: Articles or Summaries
* **Device**: Desktop, Mobile (web), Tablet (web), iOS (SDK), Android (SDK)
* **Date range**: All time, Month to date, Today, Yesterday, Last 7 days, Last 14 days, Last 30 days, Last 90 days, Last 180 days, Custom

# VAST
Source: https://docs.beyondwords.io/docs-and-guides/monetization/vast

Connect to an ad server via VAST to serve ads through the BeyondWords player

## Overview

Use VAST to serve ads through the BeyondWords player.

<img alt="monetization" />

<Info>
  Audio ads will play on audio articles or summaries. Video ads will play on video articles or summaries.
</Info>

## Create a VAST ad

To create a Custom ad:

1. Go to **Project > Monetization**.
2. Click **+ ad**.
3. Select **VAST**.
4. Enter a name for the ad. This will not be visible to users.
5. Set the ad placement: pre-roll, mid-roll, or post-roll.
6. Set the ad schedule (optional).
7. Click **Save changes**.

<Note>
  Having issues setting up a VAST ad? Contact [support](mailto:support@beyondwords.io) for help.
</Note>

## Enable or disable a VAST ad

To enable or disable a VAST ad:

1. Go to **Project > Monetization**.
2. Toggle the ad to **Enabled** or **Disabled**.

## Edit a VAST ad

To edit a VAST ad:

1. Go to **Project > Monetization**.
2. Click the ad you want to edit.
3. Click the **⋯** button.
4. Select **Edit**.
5. Make the necessary changes.
6. Click **Save changes**.

## Delete a VAST ad

To delete a VAST ad:

1. Go to **Project > Monetization**.
2. Click the ad you want to edit.
3. Click the **⋯** button.
4. Select **Delete**.

## Ad metrics

<Note>
  VAST ads are not tracked by BeyondWords.
</Note>

# Languages and accents
Source: https://docs.beyondwords.io/docs-and-guides/voices/languages-and-accents

Learn which languages and accents are supported in BeyondWords

| Language         | Accent                                  | Premade | Instant | Professional |
| :--------------- | :-------------------------------------- | :------ | :------ | :----------- |
| English          | American                                | ✓       | ✓       | ✓            |
| English          | Australian                              | ✓       | ✓       | ✓            |
| English          | British                                 | ✓       | ✓       | ✓            |
| English          | Canadian                                | ✓       | ✓       | ✓            |
| English          | Hong Kong                               | ✓       |         |              |
| English          | Irish                                   | ✓       | ✓       | ✓            |
| English          | Indian                                  | ✓       | ✓       | ✓            |
| English          | Kenyan                                  | ✓       |         | ✓            |
| English          | Nigerian                                | ✓       |         | ✓            |
| English          | New Zealand                             | ✓       |         | ✓            |
| English          | Filipino                                | ✓       | ✓       | ✓            |
| English          | Singaporean                             | ✓       |         | ✓            |
| English          | Tanzanian                               | ✓       |         | ✓            |
| English          | South African                           | ✓       |         | ✓            |
| Afrikaans        | South African                           | ✓       |         | ✓            |
| Albanian         | Albanian                                | ✓       |         |              |
| Amharic          | Ethiopian                               | ✓       | ✓       |              |
| Arabic           | Algerian                                | ✓       |         |              |
| Arabic           | Bahraini                                | ✓       |         |              |
| Arabic           | Egyptian                                | ✓       | ✓       | ✓            |
| Arabic           | Iraqi                                   | ✓       |         |              |
| Arabic           | Jordanian                               | ✓       |         |              |
| Arabic           | Kuwaiti                                 | ✓       |         |              |
| Arabic           | Lebanese                                | ✓       |         |              |
| Arabic           | Libyan                                  | ✓       |         |              |
| Arabic           | Moroccan                                | ✓       |         |              |
| Arabic           | Omani                                   | ✓       |         | ✓            |
| Arabic           | Qatari                                  | ✓       |         |              |
| Arabic           | Saudi Arabian                           | ✓       | ✓       | ✓            |
| Arabic           | Syrian                                  | ✓       |         | ✓            |
| Arabic           | Tunisian                                | ✓       |         | ✓            |
| Arabic           | Emirati                                 | ✓       |         |              |
| Arabic           | Yemeni                                  | ✓       |         |              |
| Armenian         | Armenian                                | ✓       |         |              |
| Assamese         | Indian                                  | ✓       |         |              |
| Azerbaijani      | Azerbaijani (Latin)                     | ✓       |         |              |
| Bangla           | Bangladeshi                             | ✓       |         |              |
| Basque           | Basque                                  | ✓       | ✓       |              |
| Bengali          | Indian                                  | ✓       | ✓       |              |
| Bosnian          | Bosnian and Herzegovinian               | ✓       | ✓       |              |
| Bulgarian        | Bulgarian                               | ✓       | ✓       | ✓            |
| Burmese          | Myanmar                                 | ✓       |         |              |
| Catalan          | Catalan                                 | ✓       | ✓       | ✓            |
| Chinese          | Cantonese (Simplified)                  | ✓       | ✓       | ✓            |
| Chinese          | Cantonese (Traditional)                 | ✓       | ✓       | ✓            |
| Chinese          | Mandarin (Simplified)                   | ✓       | ✓       | ✓            |
| Chinese          | Taiwanese Mandarin (Traditional)        | ✓       | ✓       | ✓            |
| Chinese          | Wu (Simplified)                         | ✓       | ✓       | ✓            |
| Chinese          | Guangxi Accent Mandarin (Simplified)    | ✓       | ✓       | ✓            |
| Chinese          | Zhongyuan Mandarin Henan (Simplified)   | ✓       | ✓       | ✓            |
| Chinese          | Northeastern Mandarin (Simplified)      | ✓       | ✓       | ✓            |
| Chinese          | Zhongyuan Mandarin Shaanxi (Simplified) | ✓       | ✓       | ✓            |
| Chinese          | Jilu Mandarin (Simplified)              | ✓       | ✓       | ✓            |
| Chinese          | Southwestern Mandarin (Simplified)      | ✓       | ✓       | ✓            |
| Croatian         | Croatian                                | ✓       | ✓       | ✓            |
| Czech            | Czech                                   | ✓       | ✓       |              |
| Danish           | Danish                                  | ✓       | ✓       | ✓            |
| Dutch            | Belgian                                 | ✓       | ✓       | ✓            |
| Dutch            | Dutch                                   | ✓       | ✓       | ✓            |
| Estonian         | Estonian                                | ✓       | ✓       |              |
| Filipino         | Filipino                                | ✓       |         |              |
| Finnish          | Finnish                                 | ✓       | ✓       | ✓            |
| French           | Belgian                                 | ✓       | ✓       | ✓            |
| French           | Canadian                                | ✓       | ✓       | ✓            |
| French           | French                                  | ✓       | ✓       | ✓            |
| French           | Swiss                                   | ✓       | ✓       | ✓            |
| Galician         | Galician                                | ✓       | ✓       |              |
| Georgian         | Georgian                                | ✓       |         |              |
| German           | Austrian                                | ✓       | ✓       | ✓            |
| German           | German                                  | ✓       | ✓       | ✓            |
| German           | Swiss                                   | ✓       | ✓       | ✓            |
| Greek            | Greek                                   | ✓       | ✓       | ✓            |
| Gujarati         | Indian                                  | ✓       |         |              |
| Hebrew           | Israeli                                 | ✓       | ✓       | ✓            |
| Hindi            | Indian                                  | ✓       | ✓       | ✓            |
| Hungarian        | Hungarian                               | ✓       | ✓       | ✓            |
| Icelandic        | Icelandic                               | ✓       |         |              |
| Indonesian       | Indonesian                              | ✓       | ✓       | ✓            |
| Inuktitut        | Canadian (Latin)                        | ✓       |         |              |
| Inuktitut        | Canadian (Syllabics)                    | ✓       |         |              |
| Irish            | Irish                                   | ✓       |         |              |
| Italian          | Italian                                 | ✓       | ✓       | ✓            |
| Japanese         | Japanese                                | ✓       | ✓       | ✓            |
| Javanese         | Indonesian (Latin)                      | ✓       | ✓       |              |
| Kannada          | Indian                                  | ✓       |         |              |
| Kazakh           | Kazakh                                  | ✓       |         |              |
| Khmer            | Cambodian                               | ✓       |         |              |
| Kiswahili        | Kenyan                                  | ✓       | ✓       |              |
| Kiswahili        | Tanzanian                               | ✓       |         |              |
| Korean           | Korean                                  | ✓       | ✓       | ✓            |
| Lao              | Laotian                                 | ✓       |         |              |
| Latvian          | Latvian                                 | ✓       |         |              |
| Lithuanian       | Lithuanian                              | ✓       |         |              |
| Macedonian       | North Macedonian                        | ✓       | ✓       |              |
| Malay            | Malaysian                               | ✓       | ✓       | ✓            |
| Malayalam        | Indian                                  | ✓       |         |              |
| Maltese          | Maltese                                 | ✓       |         |              |
| Marathi          | Indian                                  | ✓       |         |              |
| Mongolian        | Mongolian                               | ✓       |         |              |
| Nepali           | Nepali                                  | ✓       | ✓       |              |
| Norwegian Bokmål | Norwegian                               | ✓       | ✓       | ✓            |
| Odia             | Indian                                  | ✓       |         |              |
| Pashto           | Afghan                                  | ✓       | ✓       |              |
| Persian          | Iranian                                 | ✓       |         |              |
| Polish           | Polish                                  | ✓       | ✓       | ✓            |
| Portuguese       | Brazilian                               | ✓       | ✓       | ✓            |
| Portuguese       | Portuguese                              | ✓       | ✓       | ✓            |
| Punjabi          | Indian                                  | ✓       |         |              |
| Romanian         | Romanian                                | ✓       | ✓       | ✓            |
| Russian          | Russian                                 | ✓       | ✓       | ✓            |
| Serbian          | Serbian (Cyrillic)                      | ✓       |         |              |
| Serbian          | Serbian (Latin)                         | ✓       |         |              |
| Sinhala          | Sri Lankan                              | ✓       |         |              |
| Slovak           | Slovak                                  | ✓       | ✓       | ✓            |
| Slovenian        | Slovenian                               | ✓       | ✓       | ✓            |
| Somali           | Somali                                  | ✓       |         |              |
| Spanish          | Argentinian                             | ✓       |         | ✓            |
| Spanish          | Bolivian                                | ✓       |         |              |
| Spanish          | Chilean                                 | ✓       |         | ✓            |
| Spanish          | Colombian                               | ✓       |         |              |
| Spanish          | Costa Rican                             | ✓       |         |              |
| Spanish          | Cuban                                   | ✓       |         |              |
| Spanish          | Dominican                               | ✓       |         |              |
| Spanish          | Ecuadorian                              | ✓       |         |              |
| Spanish          | Equatorial Guinean                      | ✓       |         |              |
| Spanish          | Guatemalan                              | ✓       |         |              |
| Spanish          | Honduran                                | ✓       |         |              |
| Spanish          | Mexican                                 | ✓       | ✓       | ✓            |
| Spanish          | Nicaraguan                              | ✓       |         |              |
| Spanish          | Panamanian                              | ✓       |         |              |
| Spanish          | Paraguayan                              | ✓       |         |              |
| Spanish          | Peruvian                                | ✓       |         |              |
| Spanish          | Puerto Rican                            | ✓       |         |              |
| Spanish          | Salvadoran                              | ✓       |         |              |
| Spanish          | Spanish                                 | ✓       | ✓       | ✓            |
| Spanish          | American                                | ✓       |         | ✓            |
| Spanish          | Uruguayan                               | ✓       |         |              |
| Spanish          | Venezuelan                              | ✓       |         |              |
| Sundanese        | Indonesian                              | ✓       |         |              |
| Swedish          | Swedish                                 | ✓       | ✓       | ✓            |
| Tamil            | Indian                                  | ✓       | ✓       | ✓            |
| Tamil            | Malaysian                               | ✓       |         | ✓            |
| Tamil            | Singaporean                             | ✓       |         |              |
| Tamil            | Sri Lankan                              | ✓       |         |              |
| Telugu           | Indian                                  | ✓       | ✓       | ✓            |
| Thai             | Thai                                    | ✓       | ✓       | ✓            |
| Turkish          | Turkish                                 | ✓       | ✓       | ✓            |
| Ukrainian        | Ukrainian                               | ✓       | ✓       |              |
| Urdu             | Indian                                  | ✓       |         |              |
| Urdu             | Pakistani                               | ✓       |         |              |
| Uzbek            | Uzbek (Latin)                           | ✓       |         |              |
| Vietnamese       | Vietnamese                              | ✓       | ✓       | ✓            |
| Welsh            | British                                 | ✓       |         |              |
| isiZulu          | South African                           | ✓       | ✓       |              |

# Overview
Source: https://docs.beyondwords.io/docs-and-guides/voices/overview

Learn how to create and use voices with BeyondWords.

Speak to your audience in voices that resonate and delight. Turn writers
into narrators, or choose a signature voice to represent your brand.

BeyondWords provides you with multiple voice options to turn your articles into captivating audio.

## Voice options

<Card title="Premade Voices" href="/docs-and-guides/voices/premade-voices">
  Explore our collection of ready-to-use high-quality voices in various languages and accents.
</Card>

<Card title="Instant Voice Cloning" href="/docs-and-guides/voices/voice-cloning/instant-voice-cloning">
  Create a natural sounding voice in minutes with as little as 10 seconds of audio.
</Card>

<Card title="Professional Voice Cloning" href="/docs-and-guides/voices/voice-cloning/professional-voice-cloning">
  Create a highly natural sounding voice in 24 hours with as little as 30 minutes of audio.
</Card>

## Setting your project voice

In BeyondWords, you can set a default voice for your project. This voice will be used for all the audio generated in this project unless you specify otherwise.

<Steps>
  <Step title="Go to the Voices tab">
    In your project, go to the Content section, select Preferences, and then select the Voices tab.
  </Step>

  <Step title="Select Language and Accent">
    In the Voices tab, select the language and accent you want to use.
  </Step>

  <Step title="Choose a voice">
    You will be able to see a list of voices that match your language and accent. You can preview each voice by clicking on the play button. Click "Use voice" to set the voice as your default.

    **Pro tip:** Set a different default voice for titles, body text or summaries by clicking the down arrow and selecting whether to use as title, body, or summary voice.

    Once confirmed, this voice will be the default voice whenever you generate audio in this project unless you specify otherwise.
  </Step>
</Steps>

# Premade voices
Source: https://docs.beyondwords.io/docs-and-guides/voices/premade-voices

Our curated collection of high-quality voices.

Explore our collection of ready-to-use high-quality voices in various [languages and accents](/docs-and-guides/voices/languages-and-accents).

## Use a Premade voice

<Steps>
  <Step title="Go to the Voices tab">
    In your project, go to the Content section, select Preferences, and then select the Voices tab.
  </Step>

  <Step title="Select Language and Accent">
    In the Voices tab, select the language and accent you want to use.
  </Step>

  <Step title="Browse voices">
    You will be able to see a list of premade voices that match your language and accent. You can preview each voice by clicking on the play button. Click "Use voice" to set the voice as your default.

    **Pro tip:** Set a different default voice for titles, body text or summaries by clicking the down arrow and selecting whether to use as title, body, or summary voice.

    Once confirmed, this voice will be the default voice whenever you generate audio in this project unless you specify otherwise.
  </Step>
</Steps>

<Tip>
  Click the (⋯) button to the right of the voice to adjust the default speaking rate or copy the voice ID.
</Tip>

# Instant voice cloning
Source: https://docs.beyondwords.io/docs-and-guides/voices/voice-cloning/instant-voice-cloning

Learn how to create an instant voice clone with BeyondWords.

Instant voice cloning fine-tunes an existing model to sound just like you, delivering a voice so natural it's like having your own personal narrator on standby.

See [supported languages and accents](/docs-and-guides/voices/languages-and-accents).

<CardGroup>
  <Card title="10 seconds" icon="microphone">
    Record or upload a short clip of your voice.
  </Card>

  <Card title="Ready in seconds" icon="bolt">
    Turn your sample into a production-ready voice in seconds.
  </Card>

  <Card title="Multilingual" icon="globe">
    Your voice speaks multiple languages without additional recordings.
  </Card>

  <Card title="Custom pronunciations" icon="wand-magic-sparkles">
    Our Instant Voice Clones support full pronunciation customization—including IPA—across all languages.
  </Card>
</CardGroup>

## Create an instant voice clone

<Steps>
  <Step title="Go to the Voice cloning section">
    Click on the top left menu and select Voice cloning.
  </Step>

  <Step title="Create a Speaker">
    To create a voice, you need to create a speaker. Click on the "+ Speaker" button and enter your Speaker's first and last name.

    <Note>
      In the final step, the speaker will need to record a consent statement and their first and last name will be included in it.
    </Note>
  </Step>

  <Step title="Select Instant Voice Cloning">
    Click on the Speaker, click "+ Custom voice" and then select Instant voice cloning.
  </Step>

  <Step title="Add voice details">
    Give your voice a name that will help you identify it in the future. Select the language and accent of the voice you want to clone.
  </Step>

  <Step title="Upload audio">
    Record or upload a voice clip of the speaker recording the sample text.
  </Step>

  <Step title="Consent">
    Record or upload a voice clip of the speaker recording the consent statement and confirm that you have consent to clone the voice.

    <Note>
      The voice clone will only be available to your organization. No one else will be able to see or use it.
    </Note>
  </Step>
</Steps>

# Professional voice cloning
Source: https://docs.beyondwords.io/docs-and-guides/voices/voice-cloning/professional-voice-cloning

Learn how to create a professional voice clone with BeyondWords.

Professional voice cloning trains a highly natural-sounding voice model to sound just like you, delivering a voice so authentic your listeners will feel like they've got their favourite author in their pocket.<br /><br />

A professional voice clone will mirror the speaker data it is trained on. For an optimal clone, we require speakers to record a tailored script, such as articles, to ensure the model captures your desired speaking style.<br /><br />

See [supported languages and accents](/docs-and-guides/voices/languages-and-accents).<br /><br />

<CardGroup>
  <Card title="Record 10 articles" icon="microphone">
    Clone a voice with just 10 article recordings or 30 minutes of audio.
  </Card>

  <Card title="Ready in 24 hours" icon="clock">
    Get a highly natural voice clone within one day.
  </Card>

  <Card title="Hyper-realistic" icon="wand-magic-sparkles">
    Generate audio so authentic listeners will feel like they have their favorite author in their pocket.
  </Card>

  <Card title="Custom pronunciations" icon="wand-magic-sparkles">
    Our Professional Voice Clones support full pronunciation customization—including IPA—across all languages.
  </Card>
</CardGroup>

<br />

## Create a professional voice clone

Professional voice cloning isn't available through self-service just yet - but we'll guide you through the process.<br />
To get started, please [book a meeting](https://beyondwords.io/book-a-meeting/) or email [support@beyondwords.io](mailto:support@beyondwords.io).<br /><br />

<Steps>
  <Step title="Book a meeting">
    * Book a meeting or reach out to our team.<br />
    * We'll discuss your goals for the voice and walk you through each step of the cloning process.
  </Step>

  <Step title="Share 10-15 articles">
    * We believe voices sound best when trained on content that's authentically yours.<br />
    * Share 10 to 15 published articles - a Word doc is totally fine. We'll use these to create a customised recording script for your speaker.
  </Step>

  <Step title="Share your voice details">
    * We'll need your speaker's first and last name - this is required so they can record the voice cloning consent statement, which gives us permission to clone their voice.<br />
    * You can also give the voice a name - this helps you find and manage it in the platform later.<br />
    * Once we have these details, we'll send you a link to the recording script where you can upload the recordings.
  </Step>

  <Step title="Record and upload">
    * Your speaker will record both the script and the consent statement.<br />
    * We'll provide simple [recording guidelines](#recording-tips) and [audio requirements](#recording-requirements) to help you get the best results.<br />
    * Once recordings are complete, just upload the files and click "Submit."
  </Step>

  <Step title="Training">
    * Now it's over to us.<br />
    * Voice training typically takes 1-2 days, after which we'll review and deploy it to your account.
  </Step>

  <Step title="Use your voice">
    * We'll let you know as soon as the voice is ready.<br />
    * You can then start turning articles into audio using your new, professionally cloned voice.
  </Step>
</Steps>

<br />

## Recording tips

The voice clone will accurately replicate the style and performance of the speaker. For this reason, it is important that each article is recorded with the same energy, pace, and style that you would like the voice clone to have.<br /><br />

<AccordionGroup>
  <Accordion title="Read as separate articles">
    Please record and upload one audio file per article. This will allow the speaker to give correct meaning and structure to their performance.
  </Accordion>

  <Accordion title="Take breaks">
    We recommend adequate breaks during the recording process to reduce the risk of error and voice fatigue.
  </Accordion>

  <Accordion title="Correcting mistakes">
    If you make a mistake, please re-record from an appropriate place in the article to maintain the naturalness and fluency of the recording. It is permissible to "punch in". Please let us know if you would like guidelines on achieving this.
  </Accordion>

  <Accordion title="Indicating mistakes/issues with the script">
    Click the flag icon on the right-hand side of the script recording page to report any errors, provide comments, or let us know about any edits made to the script.
  </Accordion>

  <Accordion title="Recording location">
    It is important to record in a quiet location and to use the same recording equipment throughout. We recommend recording in a professional studio and sitting at a consistent distance from the microphone. You can create a temporary setup with thick fabrics like duvets or quilts to dampen unwanted sounds and echoes.
  </Accordion>

  <Accordion title="Distance">
    The speaker should ensure they are comfortable before recording to eliminate the need for movement. Two fists away is a good starting point.
  </Accordion>

  <Accordion title="Plosives">
    Employ a pop filter to minimise "p" and "b" sounds, ensuring crisp audio.
  </Accordion>

  <Accordion title="Pronunciations">
    To ensure that words are mapped to their correct sounds, words must be pronounced accurately and distinctly, precisely as they are in the script. The script may be normalised for text-to-speech, so you may notice some unusual punctuation and formatting (for example, "2020" might be written as "twenty-twenty"). Where letters should be pronounced individually, spaces or hyphens may be used to indicate breaks (for example, "I S S", "CAR-T"). The speaker should take the time to review the script beforehand and clarify the pronunciation of any unfamiliar or ambiguous words.
  </Accordion>

  <Accordion title="Speaking style">
    Use a natural speaking style that you can maintain consistently throughout the recordings. While some variance is natural and desirable, keeping volume, pitch, intonation, and tempo as consistent as possible is important.
  </Accordion>

  <Accordion title="Voice quality">
    To ensure consistency, the speaker should take regular water breaks and rest their voice. Rather than recording the script all at once, we recommend recording in multiple short sessions to reduce the risk of the voice becoming tired or strained.
  </Accordion>

  <Accordion title="Breathing and pausing">
    Pause naturally at punctuation and try to breathe away from the microphone. Keep your breathing at a low and consistent volume, or the voice clone's breaths can become unnatural and distracting.
  </Accordion>

  <Accordion title="Hydration and mouth noise">
    Mouth noise can be copied by the voice clone and cause unpredictable results. Mouth noise can be caused by not being sufficiently hydrated. To help reduce mouth noise, it is important to become well-hydrated on the days leading up to the recording sessions and throughout. Do not wait until the day of recordings to become hydrated — your body will get rid of it. Reducing caffeine and alcohol can help. If you're sufficiently hydrated and still have audible mouth noise, chewing gum with xylitol or a bite of green apple reduces mouth noise on the day of recording.
  </Accordion>
</AccordionGroup>

<br />

## Recording requirements

Save each file as an individual .wav audio file then upload it under the words of each article in the script recording interface. Optimum recordings are:<br /><br />

* **File format**: \*.wav, Mono<br />
* **Sampling rate**: Minimum of 22 kHz for clear audio capture.<br />
* **Sample format**: Minimum of 16-bit PCM (uncompressed) for lossless audio quality.<br />
* **Volume levels**: Between -23dB and -18dB RMS across the recording, with a maximum peak of -3dB to avoid clipping and distortion.<br />
* **Signal-to-noise ratio (SNR)**: Greater than 35dB (higher is better) for minimal background noise.<br />
* **Environment noise, echo**: Background noise level before speaking should be less than -70dB for optimal clarity.<br />
* **Send us the files as "unprocessed" as possible**: e.g. do not apply filters, compression, limiters and the like. We'll standardise your files in-house to ensure optimal settings perfect for voice cloning

## Voice Scoping

Voice scoping allows you to make a custom voice available on specific projects rather than across your entire account.
Can be useful for organizations with multiple projects and a large number of custom voice clones, where only certain voices should be available for certain projects.

<Steps>
  <Step title="Go to the Voice Cloning section">
    In the top-left menu, select `Voice cloning`.
  </Step>

  <Step title="Find the voice you want to scope">
    You will see a list of all available custom voices (both Instant and Professional voice clones). <br />
    Click the `⋯` menu next to the voice name and select `Edit`.
  </Step>

  <Step title="Select which projects to scope the voice to">
    Choose whether to make the voice available to `All projects` or to `Specific projects`.
  </Step>

  <Step title="Save changes">
    Your custom voice will be available in either `All Projects` or the `Specific projects` that you have selected.

    <Note>Scoping a voice to a project will not set it as the default voice for the project. You will have to do this via you [Voices Preferences](/docs-and-guides/content/preferences/voices)</Note>
  </Step>
</Steps>



--------------------
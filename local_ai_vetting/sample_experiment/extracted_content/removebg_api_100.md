# Remove.bg API
**URL:** https://www.remove.bg/api
**Page Title:** Background Removal API – remove.bg
--------------------


## Remove.bg API Documentation

## Remove Background automatically with 1 API call

Explore our API documentation and examples to integrate remove.bg into your application or workflow.
[LINK: Get API Key](/dashboard#api-key)
[LINK: Tools & Apps](/tools-api)

## Easy to integrate

Our API is a simple HTTP interface with various options:

## Get started

Our API is a simple HTTP interface with various options:
- Get your API Key . Your first 50 API calls per month are on us (see Pricing ).
[LINK: Get your API Key](/dashboard#api-key)
- Use the following code samples to get started quickly
- Review the reference docs to adjust any parameters

## Sample Code

## Libraries

Get up and running faster with official and third-party libraries.
[LINK: Tools & Apps](/tools-api)
[LINK: Official Commandline Tool Official by remove.bg](https://github.com/remove-bg/remove-bg-cli)
[LINK: Official Ruby Gem Official by remove.bg](https://github.com/remove-bg/ruby)
[LINK: PHP/Laravel Library by @mtownsend5512](https://github.com/mtownsend5512/remove-bg)
[LINK: Python: remove.bg by Brian Lam](https://github.com/brilam/remove-bg)

## Output formats

You can request one of four formats via the format parameter:
[LINK: Download 7 MB](https://static.remove.bg/remove-bg-web/77139bce0dcc0828bdade2e4110046e30e2c7d2b/assets/api-docs/example-tiger-9e6b2856e0b8c62af1e4c1a2b7b7d759f4653c7ba1f8f8e9b9fcc92edd25338a.png)
[LINK: Download 1 MB](https://static.remove.bg/remove-bg-web/77139bce0dcc0828bdade2e4110046e30e2c7d2b/assets/api-docs/example-tiger-d82d433bc9f0867381c7dd43d3042a3d86de34fd58b9fb4ed082bbcd5ccf10c3.jpg)
[LINK: Download 6 MB](https://static.remove.bg/remove-bg-web/77139bce0dcc0828bdade2e4110046e30e2c7d2b/assets/api-docs/example-tiger-512675bb89935ab63898cfc224e9373656be38f19fa59509cc3a580c3850db4b.webp)
[LINK: Download 3 MB](https://static.remove.bg/remove-bg-web/77139bce0dcc0828bdade2e4110046e30e2c7d2b/assets/api-docs/example-tiger-ea002b3b176b23e988a97e33dffa25960a19529bb0adcb5c75a96dbab189e7b3.zip)
Please note that PNG images above 10 megapixels are not supported . If you require transparency for images of that size, use either WebP or ZIP format (see below). For the fastest processing we recommend the ZIP format. If you don't need transparency (e.g. white background), we recommend JPG.

## How to use the ZIP format

The ZIP format has the best runtime performance for transparent images.
In comparison to PNG, the resulting file is up to 80% smaller (faster to download) and up to 40% faster to generate. For performance optimization we recommend using the ZIP format whenever possible.
The ZIP file always contains the following files:
[LINK: Show example](https://static.remove.bg/remove-bg-web/77139bce0dcc0828bdade2e4110046e30e2c7d2b/assets/api-docs/example-tiger-color-ed5f90da1ab8a94dbba5986580d7e76cde84b2b1ce6d44de2d86d186658e7332.jpg)
[LINK: Show example](https://static.remove.bg/remove-bg-web/77139bce0dcc0828bdade2e4110046e30e2c7d2b/assets/api-docs/example-tiger-alpha-e0ae0f94e34a25f1e9bd7a2a68a0bb34f1568a5bcdadd62e623b5cb021981032.png)
To compose the final image file:
- Extract the files from the ZIP
- Apply the alpha matte (alpha.png) to the color image (color.jpg).
- Save the result in a format of your choice (e.g. PNG)
Sample code for linux (requires zip and imagemagick ):
A zip2png command is integrated in our command line interface . More code samples can be found here .
[LINK: command line interface](https://github.com/remove-bg/remove-bg-cli/)
[LINK: here](https://github.com/remove-bg/integration/tree/master/)

## OAuth 2.0

If you want to authenticate users with the click of a button instead of having them enter an API Key, get in touch to try our OAuth 2.0 login.

## API Reference

## Background Removal API 1.0.0 OAS3

[LINK: /api/swagger.yaml](/api/swagger.yaml)
Remove the background of any image

### Background Removal

Removes the background of a JPG/PNG/WebP image.
- File size: up to 22 MB
- Input resolution: up to 50 megapixels
- Image source: File upload (binary or as base64 encoded string) or download from URL
- Image Content: Any photo with a foreground (e.g. people, products, animals, cars, etc.)
- Output resolutions available: Preview (up to 0.25 megapixels), Full (up to 25 megapixels), 50MP (up to 50 megapixels)
Requires either an API Key to be provided in the X-API-Key request header or an OAuth 2.0 access token to be provided in the Authorization request header.
No parameters
Source image file (binary). (If this parameter is present, the other image source parameters must be empty.)
Source image file (base64-encoded string). (If this parameter is present, the other image source parameters must be empty.)
Source image URL. (If this parameter is present, the other image source parameters must be empty.)
Maximum output image resolution:
- "preview" (default) = Resize image to 0.25 megapixels (e.g., 625×400 pixels) – 0.25 credits per image
- "full" = Use original image resolution, up to 25 megapixels (e.g., 6250×4000) with formats ZIP / JPG / WebP, or up to 10 megapixels (e.g., 4000×2500) with PNG – 1 credit per image
- "50MP" = Use original image resolution, up to 50 megapixels (e.g., 8000×6250) with formats ZIP / JPG / WebP, or up to 10 megapixels (e.g., 4000×2500) with PNG – 1 credit per image
- "auto" = Use highest available resolution, up to 25 megapixels (e.g. 6250×4000) (based on image size and available credits).
For backwards-compatibility this parameter also accepts the values "medium" (up to 1.5 megapixels) and "hd" (up to 4 megapixels) for 1 credit per image. The value "full" is also available under the name "4k" and the value "preview" is aliased as "small" and "regular".
Detect or set a foreground type .
We recommend using type = auto to automatically detect the type of foreground.
To specify only one type of foreground, set type to one of these values: car,  product, person, animal, graphic, transportation .
Classification level of the detected foreground type:
- "none" = No classification (X-Type Header won't bet set on the response)
- "1" = Use coarse classification classes: [person, product, animal, car, other]
- "2" = Use more specific classification classes: [person, product, animal, car, car_interior, car_part, transportation, graphics, other]
- "latest" = Always use the latest classification classes available
Result image format:
- "auto" = Use PNG format if transparent regions exist, otherwise use JPG format (default),
- "png" = PNG format with alpha transparency,
- "webp" = WebP format with alpha transparency,
- "jpg" = JPG format, no transparency,
- "zip" = ZIP format, contains color image and alpha matte image, supports transparency (recommended for fastest processing).
Region of interest: Only contents of this rectangular region can be detected as foreground. Everything outside is considered background and will be removed. The rectangle is defined as two x/y coordinates in the format "x1 y1 x2 y2". The coordinates can be in absolute pixels (suffix 'px') or relative to the width/height of the image (suffix '%'). By default, the whole image is the region of interest ("0% 0% 100% 100%").
Whether to crop off all empty regions (default: false). Note : Cropping has no effect on the amount of charged credits.
Adds a margin around the cropped subject (default: 0). Can be an absolute value (e.g. "30px") or relative to the subject size (e.g. "10%"). Can be a single value (all sides), two values (top/bottom and left/right) or four values (top, right, bottom, left). This parameter only has an effect when "crop=true". The maximum margin that can be added on each side is 50% of the subject dimensions or 500 pixels.
Scales the subject relative to the total image size. Can be any value from "10%" to "100%", or "original" (default). Scaling the subject implies "position=center" (unless specified otherwise).
Positions the subject within the image canvas. Can be "original" (default unless "scale" is given), "center" (default when "scale" is given) or a value from "0%" to "100%" (both horizontal and vertical) or two values (horizontal, vertical).
Request either the finalized image ("rgba", default) or an alpha mask ("alpha"). Note : Since remove.bg also applies RGB color corrections on edges, using only the alpha mask often leads to a lower final image quality. Therefore "rgba" is recommended.
Warning: add_shadow is deprecated and will be removed in the next major release, version 2.0. Please use shadow_type instead.
Setting add_shadow = true will set the shadow_type parameter to shadow_type [car] = car . A car shadow will only be generated if the foreground type is detected or specified as car .
Generate shadows based on your foreground type . remove.bg supports four different shadow types: car, 3D, drop, none .
Use shadow_type = auto to automatically assign the most suitable shadow_type for each foreground type . See the default assignments below. Use shadow_type = $shadow_type to specify a single type of shadow for all foreground types.
Replace shadow_type = auto with shadow_type [$type] = $shadow_type to assign specific shadow types per foreground type . Unmentioned foreground type(s) will return no shadow.
Default assignments: shadow_type [car] = car, shadow_type [product] = drop, shadow_type [person] = 3D, shadow_type [animal] = drop, shadow_type [transportation] = 3D, shadow_type [graphic] = drop, shadow_type [other] = drop
Set a shadow's opacity, i.e. darkness. Can be set to any value from 0 (lightest) to 100 (darkest) or auto for default values, shown below.
shadow_opacity = n (0 - 100), auto
Replace shadow_opacity = auto with shadow_opacity [$type] = $n to assign specific opacity values per foreground type . Unmentioned foreground type(s) with set shadows will fall back on default opacity assignments.
Default values: shadow_opacity [car] = 90 shadow_opacity [product] = 50 shadow_opacity [person] = 50 shadow_opacity [animal] = 50 shadow_opacity[transportation] = 50 shadow_opacity [graphic] = 50 shadow_opacity [other] = 50
Whether to have semi-transparent regions in the result (default: true). Note : Semitransparency is currently only supported for car windows (this might change in the future). Other objects are returned without semitransparency, even if set to true.
Adds a solid color background. Can be a hex color code (e.g. 81d4fa, fff) or a color name (e.g. green). For semi-transparency, 4-/8-digit hex codes are also supported (e.g. 81d4fa77). (If this parameter is present, the other bg_ parameters must be empty.)
Adds a background image from a URL. The image is centered and resized to fill the canvas while preserving the aspect ratio, unless it already has the exact same dimensions as the foreground image. (If this parameter is present, the other bg_ parameters must be empty.)
Adds a background image from a file (binary). The image is centered and resized to fill the canvas while preserving the aspect ratio, unless it already has the exact same dimensions as the foreground image. (If this parameter is present, the other bg_ parameters must be empty.)
Image background removed
Detected foreground type (How specific this classification is depends on the type_level parameter sent in the request)
Width of the result image
Height of the result image
Amount of credits charged for this call
Top position of the foreground image along the vertical axis. In case the input image resolution is higher than the limit (> 50 megapixels) this value is expressed with respect to the input image resolution.
Left position of the foreground image along the horizontal axis. In case the input image resolution is higher than the limit (> 50 megapixels) this value is expressed with respect to the input image resolution.
Width of the foreground image. In case the input image resolution is higher than the limit (> 50 megapixels) this value is expressed with respect to the input image resolution.
Height of the foreground image. In case the input image resolution is higher than the limit (> 50 megapixels) this value is expressed with respect to the input image resolution.
Error: Invalid parameters or input file unprocessable (no credits charged)
Error: Insufficient credits (no credits charged)
Error: Authentication failed (no credits charged)
Error: Rate limit exceeded (no credits charged)

### Improvement Program

Submit an image to the remove.bg Improvement program
- Contribute an image that remove.bg is currently not able to remove the background from properly
- Help us make remove.bg better
- Get better results for similiar images in the future
Notes:
- By submitting images through the API you agree to the Improvement Program Conditions
- File size: up to 22MB
- Input resolution: up to 50 megapixels
- up to 100 files per day. Higher rate limits are only available to high-volume solution users; get in touch here .
Requires either an API Key to be provided in the X-API-Key request header or an OAuth 2.0 access token to be provided in the Authorization request header.
Please note that submissions are used on a best-effort basis and the extent of expected improvement varies depending on many factors, including the number of provided images, their complexity and visual similarity. Improvements usually take several weeks to become effective.
No parameters
Source image file (binary). (If this parameter is present, the other image source parameters must be empty.)
Source image file (base64-encoded string). (If this parameter is present, the other image source parameters must be empty.)
Source image URL. (If this parameter is present, the other image source parameters must be empty.)
Filename of the image, if not provided it will be autodetected form the submitted data.
Images with the same tag are grouped together.
Image submitted
Error: Invalid parameters or input file unprocessable
Error: Authentication failed
Error: Rate limit exceeded

### Fetch account info

Get the current credit balance and number of free API calls.
Notes:
- Balance changes may be delayed by several seconds. To locally keep track of your credit balance, you should therefore only call this endpoint initially (or e.g. when the user manually triggers a refresh), then use the X-Credits-Charged response header returned with each image processing response to adjust the local balance.
- The " sizes " field is always "all", is deprecated and will soon be removed.
No parameters
Error: Authentication failed
Error: Rate limit exceeded

## Rate Limit

You can process up to 500 images per minute through the API, depending on the input image resolution in megapixels.
Examples:
Exceedance of rate limits leads to a HTTP status 429 response (no credits charged). Clients can use the following response headers to gracefully handle rate limits:
Higher rate limits are only available to high-volume solution users; get in touch here .

### Sample Code

Handling Rate Limits in your code using the HTTP Retry-After header:

## Exponential backoff

Exponential backoff is an error handling strategy in which a client periodically retries a failed request. This technique reduces the number of failed requests and prevents server overload by gradually increasing the waiting time between retries.
The delay increases between requests and often includes jitter (randomized delay) to avoid collisions when using concurrent clients.

              Clients should use exponential backoff whenever they receive a 5XX HTTP status code, such as 503 - Service Unavailable .
As a general rule, this should be avoided in case of 429 - Too Many Requests , as they are usually caused by client-side issues.

### Sample Code

## API Changelog

Most recent API updates:
- 2025-04-07: Drop Shadow is now more consistent across images, regardless of their resolution.
- 2025-03-31: Added support for WebP as an accepted input and output image format.
- 2024-12-13: Added code samples and tips in the Exponential Backoff section.
- 2024-06-03: Introduced new parameters: shadow_type and shadow_opacity . Deprecated parameter: add_shadow . Extended type parameter with new values: "graphic", "transportation" and "animal".
- 2024-03-17: Added new value for size parameter: 50MP for up to 50 megapixels (e.g., 8000x6250 pixels) with formats ZIP or JPG, or up to 10 megapixels (e.g., 4000x2500 pixels) with PNG – costs 1 credit per image. The "auto" option keeps supporting a maximum of 25MP for backwards compatibility.
- 2024-01-10: Final reminder - Deprecation of TLS 1.0 and 1.1 . Upgrade to TLS 1.2 or higher for uninterrupted service before 2024-02-05.
- 2023-12-06: Second notice - Deprecation of TLS 1.0 and 1.1 . Upgrade to TLS 1.2 or higher for uninterrupted service before 2024-02-05.
- 2023-11-22: First notice - Deprecation of TLS 1.0 and 1.1 . Upgrade to TLS 1.2 or higher for uninterrupted service before 2024-02-05.
- 2021-12-07: Added foreground position and size to background removal responses. (JSON fields: foreground_top , foreground_left , foreground_width and foreground_height . Response headers: X-Foreground-Top , X-Foreground-Left , X-Foreground-Width and X-Foreground-Height .)
- 2021-04-13: Removed deprecated shadow_method=legacy option and shadow_method parameter as it no longer has any effect.
- 2021-03-01: Added examples for 400 error codes.
- 2021-01-21: Added shadow_method parameter to control shadow appearance. Deprecated legacy value for shadow_method .
- 2020-09-30: Added type_level parameter and POST /improve endpoint.
- 2020-05-06: Added semitransparency parameter.
- 2019-09-27: Introduce ZIP format and support for images up to 25 megapixels.
- 2019-09-25: Increased maximum file size to 12 MB and rate limit to 500 images per minute. Rate limit is now resolution-dependent.
- 2019-09-16: Added enterprise credit balance field to account endpoint.
- 2019-08-01: Added add_shadow option for car images.
- 2019-06-26: Added crop_margin , scale and position parameters.
- 2019-06-19: Added support for animals and other foregrounds (response header X-Type: animal and X-Type: other )
- 2019-06-11: Credit balances can now have fractional digits, this affects the X-Credits-Charged value
- 2019-06-03: Added parameters bg_image_url , bg_image_file (add a background image), crop (crop off empty regions) and roi (specify a region of interest).
- 2019-05-13: Added car support ( type=car parameter and X-Type: car response header)
- 2019-05-02: Renamed size "regular" to "small" . Clients should use the new value, but the old one will continue to work (deprecated)
- 2019-05-01: Added endpoint GET /account for credit balance lookups
- 2019-04-15: Added parameter format to set the result image format
- 2019-04-15: Added parameter bg_color to add a background color to the result image

### Thanks for your feedback!

Want to help us improve? (optional)
- Contribute this image & help us make remove.bg better
- Teach the Artificial Intelligence
- Get better results for similar images in the future
Your image will be used for future improvements of remove.bg.
Your image will NOT be used for future improvements of remove.bg.
By using remove.bg you agree to the use of cookies. You can find details on how we use cookies in our Cookie Policy .
To provide you a great experience and for certain functions, we use so-called cookies. Cookies are small text files that are stored on your device. For more info and a full list of cookies we use go to our Cookie Policy .
are necessary for features which are essential to use our site, such as signing up, logging in or making purchases.
are used to enhance the functionality of this site, e.g. by remembering your settings and preferences to provide you with a better experience.
help us to measure traffic and usage data and to analyze how our Services are used in order to provide you with a better user experience and maintain, operate and improve our Services. These cookies may be set by us or third-party providers whose services we have added to our websites and apps.
help us show you ads that are useful to you on our websites or on third-party websites, and measure the effectiveness of the relevant ad campaigns.

--------------------
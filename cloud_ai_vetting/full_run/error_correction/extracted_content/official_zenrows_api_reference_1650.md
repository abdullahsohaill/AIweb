# official ZenRows API Reference
**URL:** https://docs.zenrows.com/universal-scraper-api/api-reference
**Page Title:** Introduction to the Universal Scraper API - ZenRows Docs
--------------------

[LINK: Universal Scraper API](/universal-scraper-api/api-reference)
[LINK: Scraping Browser](/scraping-browser/introduction)
[LINK: Scraper APIs](/scraper-apis/introduction)
- Introduction
[LINK: Introduction](/universal-scraper-api/api-reference)
- Universal Scraper API Setup
[LINK: Universal Scraper API Setup](/universal-scraper-api/universal-scraper-api-setup)
- Make Your First Request
[LINK: Make Your First Request](/universal-scraper-api/first-request)
- Common Use Cases and Recipes
[LINK: Common Use Cases and Recipes](/universal-scraper-api/common-use-cases)
- Adaptive Stealth Mode
[LINK: Adaptive Stealth Mode](/universal-scraper-api/features/adaptive-stealth-mode)
- Headers
[LINK: Headers](/universal-scraper-api/features/headers)
- Outputs
[LINK: Outputs](/universal-scraper-api/features/output)
- Concurrency
[LINK: Concurrency](/universal-scraper-api/features/concurrency)
- Other
[LINK: Other](/universal-scraper-api/features/other)
- Basic Troubleshooting
[LINK: Basic Troubleshooting](/universal-scraper-api/troubleshooting/troubleshooting-guide)
- IP Blocked / Connection Aborted
[LINK: IP Blocked / Connection Aborted](/universal-scraper-api/troubleshooting/ip-address-blocked)
- Empty or Partial Responses
[LINK: Empty or Partial Responses](/universal-scraper-api/troubleshooting/empty-or-partialresponses)
- Proxy and Geolocation
[LINK: Proxy and Geolocation](/universal-scraper-api/troubleshooting/troubleshooting-premium-proxies)
- Response Too Large
[LINK: Response Too Large](/universal-scraper-api/troubleshooting/response-too-large)
- FAQ
[LINK: FAQ](/universal-scraper-api/faq)
- Key Features
- JavaScript Rendering
- Premium Proxies
- Custom Headers
- Session Management
- Advanced Data Extraction
- Language agnostic
- Parameter Overview
- Pricing
- Concurrency and Response Size Limits
- Response Headers
- Additional Considerations
- Cancelled Request Behavior
- Security Best Practices
- Regional Performance Optimization
- Compression Support

## ​ Key Features

### ​ JavaScript Rendering

- E-commerce product listings that load items as you scroll
- Dashboards and analytics platforms that render charts/data with JavaScript
- Social media feeds that dynamically append content
- Sites that hide certain content until JavaScript is rendered
- Wait times to ensure elements are fully loaded
- Interaction with the page to click buttons, fill forms, or scroll
- Screenshot capabilities for visual verification
- CSS-based extraction of specific elements

### ​ Premium Proxies

- Scraping major e-commerce platforms (Amazon, Walmart)
- Accessing real estate listings (Zillow, Redfin)
- Gathering pricing data from travel sites (Expedia, Booking.com)
- Collecting data from financial or investment platforms
- Geolocation selection to access region-specific content
- Automatic IP rotation to prevent detection

### ​ Custom Headers

- Setting language preferences to get content in specific languages
- Adding a referer to avoid being blocked by bot detection systems

### ​ Session Management

- Multi-step forms processes
- Maintaining consistent session for search results and item visits

### ​ Advanced Data Extraction

- Extracting pricing information from product pages
- Gathering contact details from business directories
- Collecting specific metrics from analytics pages

### ​ Language agnostic

## ​ Parameter Overview

[LINK: apikey](#api-key)
[LINK: mode](/universal-scraper-api/features/adaptive-stealth-mode)
[LINK: Adaptive Stealth Mode vs Manual Parameters](/universal-scraper-api/features/adaptive-stealth-mode#adaptive-stealth-mode-vs-manual-configuration)
[LINK: js_render](/universal-scraper-api/features/js-rendering)
[LINK: Load dynamic pages (SPAs, dashboards, infinite scroll)](/universal-scraper-api/features/js-rendering#when-to-use-javascript-rendering)
[LINK: js_instructions](/universal-scraper-api/features/js-instructions)
[LINK: Submit forms or simulate user actions](/universal-scraper-api/features/js-instructions#common-use-cases-and-workflows)
[LINK: custom_headers](/universal-scraper-api/features/headers#custom-headers)
[LINK: Simulate browser behavior and avoid detection](/universal-scraper-api/features/headers#example-use-case%3A-using-referer)
[LINK: premium_proxy](/universal-scraper-api/features/premium-proxy)
[LINK: Access bypass anti-bot protection by using residential IPs](/universal-scraper-api/features/premium-proxy#basic-usage)
[LINK: proxy_country](/universal-scraper-api/features/proxy-country)
[LINK: Access geo-restricted content](/universal-scraper-api/features/proxy-country#common-use-cases)
[LINK: session_id](/universal-scraper-api/features/other#session-id)
[LINK: Keep session/IP across requests](/universal-scraper-api/features/other#session-id)
[LINK: original_status](/universal-scraper-api/features/other#original-http-code)
[LINK: Debug failed requests](/universal-scraper-api/features/other#original-http-code)
[LINK: allowed_status_codes](/universal-scraper-api/features/other#return-content-on-error)
[LINK: Debug failed requests and return the failed page](/universal-scraper-api/features/other#return-content-on-error)
[LINK: wait_for](/universal-scraper-api/features/wait-for)
[LINK: Capture elements that load at unpredictable times](/universal-scraper-api/features/wait-for#basic-usage)
[LINK: wait](/universal-scraper-api/features/wait)
[LINK: Pause the request process after the initial page load](/universal-scraper-api/features/wait#basic-usage)
[LINK: block_resources](/universal-scraper-api/features/block-resources)
[LINK: Optimize performance and minimize bandwidth](/universal-scraper-api/features/block-resources#basic-usage)
[LINK: json_response](/universal-scraper-api/features/json-response)
[LINK: Capture API calls and background requests](/universal-scraper-api/features/json-response#basic-usage)
[LINK: css_extractor](/universal-scraper-api/features/output#css-selectors)
[LINK: Extract only specific data fields](/universal-scraper-api/features/output#css-selectors)
[LINK: autoparse](/universal-scraper-api/features/output#auto-parsing)
[LINK: Parse data in JSON format automatically](/universal-scraper-api/features/output#auto-parsing)
[LINK: response_type](/universal-scraper-api/features/output#markdown-response)
[LINK: Extract only specific formats](/universal-scraper-api/features/output#markdown-response)
[LINK: screenshot](/universal-scraper-api/features/output#page-screenshot)
[LINK: Visual verification of page rendering](/universal-scraper-api/features/output#page-screenshot)
[LINK: screenshot_fullpage](/universal-scraper-api/features/output#page-screenshot)
[LINK: Capture complete page content](/universal-scraper-api/features/output#additional-options)
[LINK: screenshot_selector](/universal-scraper-api/features/output#page-screenshot)
[LINK: Capture specific page elements](/universal-scraper-api/features/output#additional-options)
[LINK: screenshot_format](/universal-scraper-api/features/output#image-format-and-quality)
[LINK: Choose appropriate image format](/universal-scraper-api/features/output#image-format-and-quality)
[LINK: screenshot_quality](/universal-scraper-api/features/output#image-format-and-quality)
[LINK: Control image compression levels](/universal-scraper-api/features/output#image-format-and-quality)
[LINK: outputs](/universal-scraper-api/features/output#output-filters)
[LINK: Extract only specific data fields](/universal-scraper-api/features/output#output-filters)

## ​ Pricing

- Basic request: Standard rate per 1,000 requests
- JS rendering: 5x cost
- Premium proxies: 10x cost
- Both (JS & proxies): 25x cost
- Basic: $0.10 per 1,000 requests
- JS: $0.45 per 1,000
- Proxies: $0.90 per 1,000
- Both: $2.50 per 1,000

### ​ Concurrency and Response Size Limits

- Canceling requests on the client side does NOT immediately free up concurrency slots
- The server continues processing canceled requests until completion
- If you exceed your concurrency limit, you’ll receive a 429 Too Many Requests error
- You’ll receive a 413 Content Too Large error
- No partial data will be returned when a size limit is hit
- Use CSS selectors : Target only the specific data you need with css_extractor parameter
- Use response_type : Convert to markdown or plaintext to reduce size
- Disable screenshots : If using screenshot features, these can significantly increase response size
- Segment your scraping : Break down large pages into smaller, more manageable sections

## ​ Response Headers

- Monitoring usage : Track your concurrent usage and stay within limits
- Support requests : When reporting issues, always include the X-Request-Id for faster troubleshooting
- Cost tracking : The X-Request-Cost helps you monitor your usage per request
- Redirection tracking : Zr-Final-Url shows where you ended up after any redirects

## ​ Additional Considerations

### ​ Cancelled Request Behavior

- The server continues processing the request until completion
- The concurrency slot remains occupied for up to 3 minutes
- This can result in unexpected 429 Too Many Requests errors
- Implement request timeouts carefully to avoid depleting concurrency slots

### ​ Security Best Practices

- Store API keys as environment variables, never hardcode them
- Monitor usage patterns to detect unauthorized use
- Rotate API keys periodically for critical applications

### ​ Regional Performance Optimization

- Consider the geographical distance between your servers and the target website
- For global applications, distribute scraping across multiple regions - the system does it by default
- Monitor response times by region to identify optimization opportunities
- For region-specific content, use the appropriate proxy_country parameter

### ​ Compression Support

- Reduced latency : Smaller response sizes mean faster data transfer times
- Lower bandwidth consumption : Minimize data transfer costs and usage
- Improved client performance : Less data to process means reduced memory usage
Was this page helpful?
[LINK: Universal Scraper API Setup](/universal-scraper-api/universal-scraper-api-setup)

--------------------
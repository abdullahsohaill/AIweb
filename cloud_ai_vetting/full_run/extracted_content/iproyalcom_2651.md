# IPRoyal.com
**URL:** https://iproyal.com
**Page Title:** IPRoyal | Premium Quality Proxies, Unbeatable Prices
--------------------


## Proxy Infrastructure Built for Scale and Speed

Own your infrastructure. Avoid vendor lock‑in. Stay in control of performance and costs.
As seen on
Best proxy servers 2025

## Solutions for Every Use Case

### Residential

### Residential

Ideal for anonymous high-volume web scraping, SEO monitoring, and geo-targeted research at scale.

### ISP

### ISP

Great for ecommerce automation, ad verification, and long-session reliability. Think datacenter speed with residential proxy anonymity.

### Datacenter

### Datacenter

Best for speed-critical use cases like software testing, scraping, and infrastructure monitoring.

### Mobile

### Mobile

Perfect for social platforms, mobile app QA, and regional ad testing with a network of over 4.5 million real mobile IPs.

### Web Unblocker

### Web Unblocker

Ideal for automated web scraping, bypassing blocks, and reliable access to geo-restricted content.

## Everything You Need for Hassle-Free Web Scraping

### Spend Smarter, Scale Faster

Non-expiring traffic, transparent pricing, and usage-based plans mean you control spend without losing unused data.

### Built for Performance, Ready to Scale

High-speed proxies, precision geo-targeting, and smart rotation options. Everything your engineers need to automate and optimize.

### Security-First Architecture

Strict KYC, IP whitelisting, 2FA, and account-level permissions give your team full control over proxy access and usage.

## Built to Integrate. Ready to Automate.

Connect IPRoyal to the tools you already use. Or build your own automations with our powerful API.
- Integrations third-party 650+ tools supported Seamless setup with scrapers, browsers, automation tools Full compliance with the latest standards See All Integrations

### Integrations

- 650+ tools supported
- Seamless setup with scrapers, browsers, automation tools
- Full compliance with the latest standards
- Powerful API Residential cURL curl - X GET https : / / resi - api . iproyal . com / v1 / me \ - H "Authorization: Bearer <your_api_token>" <?php $api_token = '<your_api_token>' ; $url = 'https://resi-api.iproyal.com/v1/me' ; $ch = curl_init ( ) ; curl_setopt ( $ch , CURLOPT_URL , $url ) ; curl_setopt ( $ch , CURLOPT_HTTPGET , true ) ; $headers = [ "Authorization: Bearer $api_token " ] ; curl_setopt ( $ch , CURLOPT_HTTPHEADER , $headers ) ; curl_setopt ( $ch , CURLOPT_RETURNTRANSFER , true ) ; $response = curl_exec ( $ch ) ; if ( curl_errno ( $ch ) ) { echo 'Error:' . curl_error ( $ch ) ; } else { echo $response ; } curl_close ( $ch ) ; ?> import requests

api_token = '<your_api_token>' url = 'https://resi-api.iproyal.com/v1/me' headers = { 'Authorization' : f'Bearer { api_token } ' } response = requests . get ( url , headers = headers ) print ( response . text ) const https = require ( 'https' ) ; const apiToken = '<your_api_token>' ; const url = 'https://resi-api.iproyal.com/v1/me' ; const options = { method : 'GET' , headers : { 'Authorization' : ` Bearer ${ apiToken } ` } } ; const req = https . request ( url , options , ( res ) => { let data = '' ; res . on ( 'data' , ( chunk ) => { data += chunk ; } ) ; res . on ( 'end' , ( ) => { console . log ( data ) ; } ) ; } ) ; req . on ( 'error' , ( error ) => { console . error ( 'Error:' , error . message ) ; } ) ; req . end ( ) ; import java . io . BufferedReader ; import java . io . InputStreamReader ; import java . net . HttpURLConnection ; import java . net . URL ; public class ApiRequest { public static void main ( String [ ] args ) { String apiToken = "<your_api_token>" ; String urlString = "https://resi-api.iproyal.com/v1/me" ; try { URL url = new URL ( urlString ) ; HttpURLConnection connection = ( HttpURLConnection ) url . openConnection ( ) ; connection . setRequestMethod ( "GET" ) ; connection . setRequestProperty ( "Authorization" , "Bearer " + apiToken ) ; int responseCode = connection . getResponseCode ( ) ; if ( responseCode == HttpURLConnection . HTTP_OK ) { BufferedReader in = new BufferedReader ( new InputStreamReader ( connection . getInputStream ( ) ) ) ; String inputLine ; StringBuilder content = new StringBuilder ( ) ; while ( ( inputLine = in . readLine ( ) ) != null ) { content . append ( inputLine ) ; } in . close ( ) ; System . out . println ( content . toString ( ) ) ; } else { System . out . println ( "GET request failed. Response Code: " + responseCode ) ; } } catch ( Exception e ) { e . printStackTrace ( ) ; } } } using System ; using System . Net . Http ; using System . Threading . Tasks ; class Program { static async Task Main ( string [ ] args ) { string apiToken = "<your_api_token>" ; string url = "https://resi-api.iproyal.com/v1/me" ; using ( HttpClient client = new HttpClient ( ) ) { client . DefaultRequestHeaders . Add ( "Authorization" , $ "Bearer {apiToken}" ) ; HttpResponseMessage response = await client . GetAsync ( url ) ; string responseText = await response . Content . ReadAsStringAsync ( ) ; Console . WriteLine ( responseText ) ; } } } package main import ( "io" "log" "net/http" "fmt" ) const ( apiToken = "<your_api_token>" meURL = "https://resi-api.iproyal.com/v1/me" ) func main ( ) { req , err := http . NewRequest ( http . MethodGet , meURL , nil ) if err != nil { log . Fatal ( "Error creating request:" , err ) } req . Header . Set ( "Authorization" , "Bearer " + apiToken ) client := & http . Client { } resp , err := client . Do ( req ) if err != nil { log . Fatal ( "Error making request:" , err ) } defer resp . Body . Close ( ) responseBody , err := io . ReadAll ( resp . Body ) if err != nil { log . Fatal ( "Error reading response body:" , err ) } fmt . Println ( string ( responseBody ) ) } curl - X GET "https://apid.iproyal.com/v1/reseller/balance" \ - H "X-Access-Token: <your_access_token>" \ - H "Content-Type: application/json" <?php $api_token = '<your_access_token>' ; $url = "https://apid.iproyal.com/v1/reseller/balance" ; $options = [ CURLOPT_URL => $url , CURLOPT_RETURNTRANSFER => true , CURLOPT_HTTPHEADER => [ "X-Access-Token: $api_token " , 'Content-Type: application/json' ] ] ; $ch = curl_init ( ) ; curl_setopt_array ( $ch , $options ) ; $response = curl_exec ( $ch ) ; if ( curl_errno ( $ch ) ) { echo 'Error:' . curl_error ( $ch ) ; } else { echo $response ; } curl_close ( $ch ) ; ?> import requests

api_token = '<your_access_token>' url = 'https://apid.iproyal.com/v1/reseller/balance' headers = { 'X-Access-Token' : api_token , 'Content-Type' : 'application/json' } response = requests . get ( url , headers = headers ) print ( response . status_code ) print ( response . json ( ) ) const https = require ( 'https' ) ; const api_token = '<your_access_token>' ; const options = { hostname : 'apid.iproyal.com' , path : '/v1/reseller/balance' , method : 'GET' , headers : { 'X-Access-Token' : api_token , 'Content-Type' : 'application/json' } } ; const req = https . request ( options , ( res ) => { let responseData = '' ; res . on ( 'data' , ( chunk ) => { responseData += chunk ; } ) ; res . on ( 'end' , ( ) => { console . log ( responseData ) ; } ) ; } ) ; req . on ( 'error' , ( error ) => { console . error ( 'Error:' , error . message ) ; } ) ; req . end ( ) ; import java . io . BufferedReader ; import java . io . InputStreamReader ; import java . net . HttpURLConnection ; import java . net . URL ; public class ApiRequest { public static void main ( String [ ] args ) { String apiToken = "<your_access_token>" ; String urlString = "https://apid.iproyal.com/v1/reseller/balance" ; try { URL url = new URL ( urlString ) ; HttpURLConnection connection = ( HttpURLConnection ) url . openConnection ( ) ; connection . setRequestMethod ( "GET" ) ; connection . setRequestProperty ( "X-Access-Token" , apiToken ) ; connection . setRequestProperty ( "Content-Type" , "application/json" ) ; int responseCode = connection . getResponseCode ( ) ; System . out . println ( "Response Code: " + responseCode ) ; if ( responseCode == HttpURLConnection . HTTP_OK ) { BufferedReader in = new BufferedReader ( new InputStreamReader ( connection . getInputStream ( ) ) ) ; String inputLine ; StringBuilder content = new StringBuilder ( ) ; while ( ( inputLine = in . readLine ( ) ) != null ) { content . append ( inputLine ) ; } in . close ( ) ; System . out . println ( "Response Body: " + content . toString ( ) ) ; } else { System . out . println ( "GET request failed. Response Code: " + responseCode ) ; } } catch ( Exception e ) { e . printStackTrace ( ) ; } } } using System ; using System . Net . Http ; using System . Text . Json ; using System . Threading . Tasks ; class Program { static async Task Main ( string [ ] args ) { string apiToken = "<your_access_token>" ; string url = "https://apid.iproyal.com/v1/reseller/balance" ; using ( HttpClient client = new HttpClient ( ) ) { client . DefaultRequestHeaders . Add ( "X-Access-Token" , apiToken ) ; HttpResponseMessage response = await client . GetAsync ( url ) ; Console . WriteLine ( ( int ) response . StatusCode ) ; string responseText = await response . Content . ReadAsStringAsync ( ) ; var jsonResponse = JsonSerializer . Deserialize < JsonElement > ( responseText ) ; Console . WriteLine ( jsonResponse ) ; } } } package main import ( "encoding/json" "fmt" "io" "log" "net/http" ) const ( apiToken = "<your_access_token>" url = "https://apid.iproyal.com/v1/reseller/balance" ) func main ( ) { req , err := http . NewRequest ( http . MethodGet , url , nil ) if err != nil { log . Fatal ( "Error creating request:" , err ) } req . Header . Set ( "X-Access-Token" , apiToken ) req . Header . Set ( "Content-Type" , "application/json" ) client := & http . Client { } resp , err := client . Do ( req ) if err != nil { log . Fatal ( "Error making request:" , err ) } defer resp . Body . Close ( ) fmt . Println ( "Status Code:" , resp . StatusCode ) responseBody , err := io . ReadAll ( resp . Body ) if err != nil { log . Fatal ( "Error reading response body:" , err ) } fmt . Printf ( string ( responseBody ) ) } curl - X GET "https://apid.iproyal.com/v1/reseller/balance" \ - H "X-Access-Token: <your_access_token>" \ - H "Content-Type: application/json" <?php $api_token = '<your_access_token>' ; $url = "https://apid.iproyal.com/v1/reseller/balance" ; $options = [ CURLOPT_URL => $url , CURLOPT_RETURNTRANSFER => true , CURLOPT_HTTPHEADER => [ "X-Access-Token: $api_token " , 'Content-Type: application/json' ] ] ; $ch = curl_init ( ) ; curl_setopt_array ( $ch , $options ) ; $response = curl_exec ( $ch ) ; if ( curl_errno ( $ch ) ) { echo 'Error:' . curl_error ( $ch ) ; } else { echo $response ; } curl_close ( $ch ) ; ?> import requests

api_token = '<your_access_token>' url = 'https://apid.iproyal.com/v1/reseller/balance' headers = { 'X-Access-Token' : api_token , 'Content-Type' : 'application/json' } response = requests . get ( url , headers = headers ) print ( response . status_code ) print ( response . json ( ) ) const https = require ( 'https' ) ; const api_token = '<your_access_token>' ; const options = { hostname : 'apid.iproyal.com' , path : '/v1/reseller/balance' , method : 'GET' , headers : { 'X-Access-Token' : api_token , 'Content-Type' : 'application/json' } } ; const req = https . request ( options , ( res ) => { let responseData = '' ; res . on ( 'data' , ( chunk ) => { responseData += chunk ; } ) ; res . on ( 'end' , ( ) => { console . log ( responseData ) ; } ) ; } ) ; req . on ( 'error' , ( error ) => { console . error ( 'Error:' , error . message ) ; } ) ; req . end ( ) ; import java . io . BufferedReader ; import java . io . InputStreamReader ; import java . net . HttpURLConnection ; import java . net . URL ; public class ApiRequest { public static void main ( String [ ] args ) { String apiToken = "<your_access_token>" ; String urlString = "https://apid.iproyal.com/v1/reseller/balance" ; try { URL url = new URL ( urlString ) ; HttpURLConnection connection = ( HttpURLConnection ) url . openConnection ( ) ; connection . setRequestMethod ( "GET" ) ; connection . setRequestProperty ( "X-Access-Token" , apiToken ) ; connection . setRequestProperty ( "Content-Type" , "application/json" ) ; int responseCode = connection . getResponseCode ( ) ; System . out . println ( "Response Code: " + responseCode ) ; if ( responseCode == HttpURLConnection . HTTP_OK ) { BufferedReader in = new BufferedReader ( new InputStreamReader ( connection . getInputStream ( ) ) ) ; String inputLine ; StringBuilder content = new StringBuilder ( ) ; while ( ( inputLine = in . readLine ( ) ) != null ) { content . append ( inputLine ) ; } in . close ( ) ; System . out . println ( "Response Body: " + content . toString ( ) ) ; } else { System . out . println ( "GET request failed. Response Code: " + responseCode ) ; } } catch ( Exception e ) { e . printStackTrace ( ) ; } } } using System ; using System . Net . Http ; using System . Threading . Tasks ; using Newtonsoft . Json . Linq ; class Program { static async Task Main ( string [ ] args ) { string apiToken = "<your_access_token>" ; string url = "https://apid.iproyal.com/v1/reseller/balance" ; using ( HttpClient client = new HttpClient ( ) ) { client . DefaultRequestHeaders . Add ( "X-Access-Token" , apiToken ) ; HttpResponseMessage response = await client . GetAsync ( url ) ; Console . WriteLine ( ( int ) response . StatusCode ) ; string responseText = await response . Content . ReadAsStringAsync ( ) ; var jsonResponse = JObject . Parse ( responseText ) ; Console . WriteLine ( jsonResponse ) ; } } } package main import ( "encoding/json" "fmt" "io" "log" "net/http" ) const ( apiToken = "<your_access_token>" url = "https://apid.iproyal.com/v1/reseller/balance" ) func main ( ) { req , err := http . NewRequest ( http . MethodGet , url , nil ) if err != nil { log . Fatal ( "Error creating request:" , err ) } req . Header . Set ( "X-Access-Token" , apiToken ) req . Header . Set ( "Content-Type" , "application/json" ) client := & http . Client { } resp , err := client . Do ( req ) if err != nil { log . Fatal ( "Error making request:" , err ) } defer resp . Body . Close ( ) fmt . Println ( "Status Code:" , resp . StatusCode ) responseBody , err := io . ReadAll ( resp . Body ) if err != nil { log . Fatal ( "Error reading response body:" , err ) } var jsonResponse map [ string ] interface { } err = json . Unmarshal ( responseBody , & jsonResponse ) if err != nil { log . Fatal ( "Error unmarshaling JSON:" , err ) } fmt . Printf ( "%+v\n" , jsonResponse ) } curl - X GET "https://apid.iproyal.com/v1/reseller/balance" \ - H "X-Access-Token: <your_access_token>" \ - H "Content-Type: application/json" <?php $api_token = '<your_access_token>' ; $url = "https://apid.iproyal.com/v1/reseller/balance" ; $options = [ CURLOPT_URL => $url , CURLOPT_RETURNTRANSFER => true , CURLOPT_HTTPHEADER => [ "X-Access-Token: $api_token " , 'Content-Type: application/json' ] ] ; $ch = curl_init ( ) ; curl_setopt_array ( $ch , $options ) ; $response = curl_exec ( $ch ) ; if ( curl_errno ( $ch ) ) { echo 'Error:' . curl_error ( $ch ) ; } else { echo $response ; } curl_close ( $ch ) ; ?> import requests

api_token = '<your_access_token>' url = 'https://apid.iproyal.com/v1/reseller/balance' headers = { 'X-Access-Token' : api_token , 'Content-Type' : 'application/json' } response = requests . get ( url , headers = headers ) print ( response . status_code ) print ( response . json ( ) ) const https = require ( 'https' ) ; const api_token = '<your_access_token>' ; const options = { hostname : 'apid.iproyal.com' , path : '/v1/reseller/balance' , method : 'GET' , headers : { 'X-Access-Token' : api_token , 'Content-Type' : 'application/json' } } ; const req = https . request ( options , ( res ) => { let responseData = '' ; res . on ( 'data' , ( chunk ) => { responseData += chunk ; } ) ; res . on ( 'end' , ( ) => { console . log ( responseData ) ; } ) ; } ) ; req . on ( 'error' , ( error ) => { console . error ( 'Error:' , error . message ) ; } ) ; req . end ( ) ; import java . io . BufferedReader ; import java . io . InputStreamReader ; import java . net . HttpURLConnection ; import java . net . URL ; public class ApiRequest { public static void main ( String [ ] args ) { String apiToken = "<your_access_token>" ; String urlString = "https://apid.iproyal.com/v1/reseller/balance" ; try { URL url = new URL ( urlString ) ; HttpURLConnection connection = ( HttpURLConnection ) url . openConnection ( ) ; connection . setRequestMethod ( "GET" ) ; connection . setRequestProperty ( "X-Access-Token" , apiToken ) ; connection . setRequestProperty ( "Content-Type" , "application/json" ) ; int responseCode = connection . getResponseCode ( ) ; System . out . println ( "Response Code: " + responseCode ) ; if ( responseCode == HttpURLConnection . HTTP_OK ) { BufferedReader in = new BufferedReader ( new InputStreamReader ( connection . getInputStream ( ) ) ) ; String inputLine ; StringBuilder content = new StringBuilder ( ) ; while ( ( inputLine = in . readLine ( ) ) != null ) { content . append ( inputLine ) ; } in . close ( ) ; System . out . println ( "Response Body: " + content . toString ( ) ) ; } else { System . out . println ( "GET request failed. Response Code: " + responseCode ) ; } } catch ( Exception e ) { e . printStackTrace ( ) ; } } } using System ; using System . Net . Http ; using System . Threading . Tasks ; using Newtonsoft . Json . Linq ; class Program { static async Task Main ( string [ ] args ) { string apiToken = "<your_access_token>" ; string url = "https://apid.iproyal.com/v1/reseller/balance" ; using ( HttpClient client = new HttpClient ( ) ) { client . DefaultRequestHeaders . Add ( "X-Access-Token" , apiToken ) ; HttpResponseMessage response = await client . GetAsync ( url ) ; Console . WriteLine ( ( int ) response . StatusCode ) ; string responseText = await response . Content . ReadAsStringAsync ( ) ; var jsonResponse = JObject . Parse ( responseText ) ; Console . WriteLine ( jsonResponse ) ; } } } package main import ( "encoding/json" "fmt" "io" "log" "net/http" ) const ( apiToken = "<your_access_token>" url = "https://apid.iproyal.com/v1/reseller/balance" ) func main ( ) { req , err := http . NewRequest ( http . MethodGet , url , nil ) if err != nil { log . Fatal ( "Error creating request:" , err ) } req . Header . Set ( "X-Access-Token" , apiToken ) req . Header . Set ( "Content-Type" , "application/json" ) client := & http . Client { } resp , err := client . Do ( req ) if err != nil { log . Fatal ( "Error making request:" , err ) } defer resp . Body . Close ( ) fmt . Println ( "Status Code:" , resp . StatusCode ) responseBody , err := io . ReadAll ( resp . Body ) if err != nil { log . Fatal ( "Error reading response body:" , err ) } var jsonResponse map [ string ] interface { } err = json . Unmarshal ( responseBody , & jsonResponse ) if err != nil { log . Fatal ( "Error unmarshaling JSON:" , err ) } fmt . Printf ( "%+v\n" , jsonResponse ) } Programmatic ordering & user management Multi-location support Advanced geo-targeting (city/state) Explore API Docs

### Powerful API

- Programmatic ordering & user management
- Multi-location support
- Advanced geo-targeting (city/state)
[LINK: Explore API Docs](https://docs.iproyal.com/proxies/residential/)

## Reliable Tools for Industry Leaders

Manage proxies at scale with secure access, user roles, detailed logs, and API-first workflows.
- Workspace Controls Add and manage team members with granular user roles and permissions.

### Workspace Controls

Add and manage team members with granular user roles and permissions.
- Built-in 2FA Security Enable two-factor authentication (2FA) and manage access across your organization.

### Built-in 2FA Security

Enable two-factor authentication (2FA) and manage access across your organization.
- Billing, Your Way Flexible invoicing and spend tracking for company-level account management.

### Billing, Your Way

Flexible invoicing and spend tracking for company-level account management.
- Extensive Documentation Full developer and team documentation for quick setup and scaling.

### Extensive Documentation

Full developer and team documentation for quick setup and scaling.
- Updates & Alerts In-dashboard notifications keep your team updated on usage, updates, and account activity.

### Updates & Alerts

In-dashboard notifications keep your team updated on usage, updates, and account activity.
- Your Feedback, Built In We prioritize what matters. Many features are developed directly from customer suggestions.

### Your Feedback, Built In

We prioritize what matters. Many features are developed directly from customer suggestions.

## How Companies Use Our Proxies

### Privacy Advantages

Stay anonymous online, mask your real IP,  and keep sensitive research or testing activities private across devices and networks.

### Email Protection

Stay one step ahead of email scammers and keep your enterprise IT infrastructure from getting compromised by malware, ransomware, and other attacks.

### SEO Proxies for SERP Scraping

Track keyword positions across locations and devices with reliable, block-free proxy access to real-time SERP data.

### Price Monitoring Proxies

Track competitor pricing, product availability, and retail trends across regions in real time without blocks or throttling.

### Proxies to Unblock Restricted Websites

Unblock any website that has placed restrictions with our residential or datacenter proxies.

### Ad Verification

Verify ad placement, targeting, and visibility from any region using stable, location-accurate proxy connections.

### Market Research

Collect real-time data from global sources to inform product strategy, brand positioning, and competitive research.

### Brand Protection

Detect IP misuse and brand infringement using reliable proxy-powered web scraping, without worrying about blocks or CAPTCHAs.

### Review Monitoring

Keep track of customer feedback from different sources (search engines, social media, forums, retail websites). Respond promptly and improve your brand reputation.

### Social Media

Manage your social media presence and promote your business without worrying about bans. Easily reach new markets without geographic restrictions.

### Stock Market Data Collection

Get real-time insight into the current state of different global markets. Monitor stock market trends and price updates to optimize your investments.

## Enterprise Solutions to Everyday Proxy Challenges

### Scalable Control & Insights

Take full control of your proxy usage with real-time analytics, project-based tracking, and granular team permissions. Easily monitor bandwidth, set limits, and manage access from one centralized dashboard.

### Enterprise-Grade Uptime

Run high-volume scraping, testing, and automation without interruptions. Built-in redundancy and zero third-party dependencies ensure 99.9% uptime for all your projects.

### Pinpoint Geo-Targeting

Get city- and state-level precision across Residential, ISP, and Datacenter proxies. Whether you’re running localized campaigns or testing geo-sensitive platforms, you get total targeting control.

## Backed by Partners Across Industries

We tested IPRoyal proxies across tens of thousands of websites and achieved a success rate of over 95%. It was a substantial improvement over our previous average of 80%. A success rate this high gave us the confidence to rely on IPRoyal’s solutions rather than building our own proxy layer in-house.

## Trusted & Secured Proxy Network

Why Trust IPRoyal?

## Compliance You Can Trust

Every IP in our 34M+ network is ethically sourced through clear, transparent agreements. No shady apps or grey areas. We follow a strict KYC policy to ensure safe, responsible use. We are also actively working towards SOC 2 and ISO 27001 certification as part of our broader security commitment. You can follow our progress in the Trust Center .

## Top Proxy Locations

- United States US 3,450,886 IPs
- United Kingdom GB 1,421,770 IPs
- Germany DE 1,439,883 IPs
- Netherlands NL 382,025 IPs
- Italy IT 1,393,154 IPs
- France FR 1,418,633 IPs

--------------------
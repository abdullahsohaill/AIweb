# Custom Connection
**URL:** https://developer.xero.com/documentation/guides/oauth2/custom-connections
**Page Title:** Custom Connections — Xero Developer
--------------------


## Documentation

- Getting started
- Development accounts
- SDKs and tools

### SDKs and tools

- Best Practices

### Best Practices

- Guides OAuth2 Overview The code flow The PKCE flow Custom Connections Client Credentials Token types Scopes Tenants Limits Troubleshooting

### Guides

- OAuth2 Overview The code flow The PKCE flow Custom Connections Client Credentials Token types Scopes Tenants Limits Troubleshooting
- Overview
- The code flow
- The PKCE flow
- Custom Connections
- Client Credentials
- Token types
- Scopes
- Tenants
- Limits
- Troubleshooting
- Xero App Store

### Xero App Store

## Custom Connections

NEW : Xero customers can now purchase as many Custom Connections as needed for their organisation – so you can build and connect even more bespoke solutions for businesses. Find out more .
Custom Connections are a premium integration option that utilise the client credentials grant type to access data from a single Xero organisation. If your app needs to connect to multiple Xero organisations then you should use the code flow or PKCE flow instead.
Custom Connections are only available for Xero organisations in Australia, New Zealand, the UK, and the US and require an additional monthly subscription. They can't be used to integrate with Xero Practice Manager or Xero HQ.
Custom Connections can be connected to the Xero Demo Company for free for development purposes and Custom Connection apps do not count toward the two uncertified app limit.

## Setting up a Custom Connection

### 1. Create the Custom Connection

Log in to My Apps and click “New App”. Give the integration a name and select “Custom connection” as the integration type.
[LINK: My Apps](https://developer.xero.com/app/manage)

### 2. Select scopes and the authorising user

Next you’ll need to select the API scopes your integration will need and who will authorise the connection. That user will then be emailed a link that takes them to the authorisation step. Once authorisation is complete you will receive an email to let you know the connection has been authorised.

### 3. Authorise the connection

After clicking the Connect button in the email, the authorising user will be taken to a consent screen where they can see which scopes are being requested and select the organisation to connect.
Note that an organisation needs to have purchased a subscription with sufficient Custom Connections to be authorised and connected. The only exception is the Xero Demo Company, which can be used for free for development purposes. Organisations without a subscription or with insufficient Custom Connections will be displayed but will be unavailable for connection.

### 4. Retrieve your client id and client secret

Once the custom connection has been authorised, the client id will be available on the app details page and you can generate the client secret. The Client Secret is private and should not be shared .

### 5. Requesting an access token

You can now exchange the client id and client secret for an access token. To do this you will need to make a POST request to our token endpoint:
The request will require an authorization header containing your app’s client_id and client_secret
- Authorization : "Basic " + base64encode(client_id + ":" + client_secret)
The request body will need to contain the grant type (client_credentials) and scope
- grant_type =client_credentials
- scope =A space separated list of the scopes required

### 6. Receive your tokens

The token endpoint will verify all the parameters in the request and, if everything checks out, it will generate your access token and return it in the response.
The response will contain the following parameters:
- access_token: The token used to call the API.
- expires_in: The amount of seconds until the access token expires.
- token_type: Bearer
- scope: The scopes this access token is authorised for
The access token is a JSON Web Token (JWT) which can be decoded to a JSON object containing information about the user and the authentication performed.

### 7. Call the Xero API

Make calls against the Xero APIs by simply adding the following headers to your request:
- Authorization : "Bearer " + access_token

## Purchasing Custom Connection subscriptions

Before a Xero customer can authorise and connect Custom Connection apps to their organisation, the organisation needs to have purchased a subscription with a sufficient quantity of Custom Connections. There is more Custom Connection information for Xero customers on Xero Central .
Xero customers can now have multiple Custom Connection apps connected to their organisation. The organisation needs a subscription with enough Custom Connections for all of their apps. If a Xero customer has already purchased a subscription but their organisation is unavailable to connect to your app ensure they have purchased sufficient Custom Connections.
A Custom Connection subscription is purchased from the Custom Connections page or from within the Xero organisation on the connected apps page where the subscription can be managed. Any user with the standard or advisor Xero user role can buy or managed a custom connection. Practice administrators and staff can only purchase a custom connection for their own practice's Xero organisation. We recommend clients purchase their organisation's custom connection themselves.

## Steps for building a Custom Connection on behalf of a client

- Develop and test the integration using your Demo Company (following the steps above).
- Instruct your client to purchase a Custom Connection subscription for their organisation or to upgrade their existing subscription, both of which they can do from the Custom Connections page. If they have any questions there is more information on Xero Central
- Create your new custom connection.
- Add the client as the authorising user. They will then receive the email to authorise the Custom Connection.
- Your client then grants authorisation to connect to their organisation. You will receive an email once the authorisation is complete.
- The custom connection is activated and you can return to My Apps to retrieve the client_id and client_secret to add to your production app.

## On this page

- Setting up a Custom Connection
- Purchasing Custom Connection subscriptions
- Steps for building a Custom Connection on behalf of a client

## Cookie settings

### Manage Consent Preferences

These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

### Cookie List


--------------------
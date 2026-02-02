# Kinde
**URL:** https://kinde.com/docs/developer-tools/nextjs-sdk
**Page Title:** Next.js App Router SDK - Kinde docs
--------------------

- SDKs and APIs
- Back end SDKs

## Next.js App Router SDK

This SDK is for Next.js version 13+ and uses Server Side Components and App Router.
New to Kinde? Get started here

## Install for a new project

The easiest way to get started is to use the Next.js starter kit , and watch a demo video .
[LINK: Next.js starter kit](https://github.com/kinde-starter-kits/kinde-nextjs-app-router-starter-kit)

## Install for an existing project

- npm
- yarn
- pnpm

## Set callback URLs

- In Kinde, go to Settings > Applications > [Your app] > View details .
- Add your callback URLs in the relevant fields. For example: Allowed callback URLs (also known as redirect URIs) - for example http://localhost:3000/api/auth/kinde_callback Allowed logout redirect URLs - for example http://localhost:3000
- Allowed callback URLs (also known as redirect URIs) - for example http://localhost:3000/api/auth/kinde_callback
- Allowed logout redirect URLs - for example http://localhost:3000
- Select Save .

## Configure environment variables

Put these variables in a .env.local file in the root of your Next.js app. You can find these variables on your Kinde Settings > Applications > [Your app] > View details page.
- KINDE_CLIENT_ID - Your business’s unique ID on Kinde
- KINDE_CLIENT_SECRET - Your business’s secret key (do not share)
- KINDE_ISSUER_URL - your kinde domain
- KINDE_SITE_URL - where your app is running
- KINDE_POST_LOGOUT_REDIRECT_URL - where you want users to be redirected to after logging out. Make sure this URL is under your allowed logout redirect URLs.
- KINDE_POST_LOGIN_REDIRECT_URL - where you want users to be redirected to after authenticating.
- KINDE_AUDIENCE - optional - a whitespace separated list of audiences to populate the aud claim in the token.
Replace the information in the example with your own information. You might also set different URLs depending where your project is running. They need to match the callback URLs you entered in Kinde, above.

## Set up Kinde Auth Route Handlers

Create the following file app/api/auth/[kindeAuth]/route.js inside your Next.js project. Inside the file route.js put this code:
This will handle Kinde Auth endpoints in your Next.js app.
Important! Our SDK relies on this file existing in this location specified above.

## Customising Kinde Auth API paths

[LINK: Link to this section](#customising-kinde-auth-api-paths)
The default path for the Kinde Auth API is /api/auth . If your Next.js application uses a custom base path for your API, you can override this setting by setting the following variable in your .env file:
You can also customise the Kinde Auth API sub-paths by setting the following variables in your .env file:
- KINDE_AUTH_LOGIN_ROUTE - defaults to login
- KINDE_AUTH_LOGOUT_ROUTE - defaults to logout
- KINDE_AUTH_REGISTER_ROUTE - defaults to register
- KINDE_AUTH_CREATEORG_ROUTE - defaults to create_org
- KINDE_AUTH_HEALTH_ROUTE - defaults to health
- KINDE_AUTH_SETUP_ROUTE - defaults to setup
Given the following .env file:
The Kinde login route for your application will be /my/custom/path/app_login .

## Set up middleware

Middleware is used to protect routes in your Next.js app, and is a requirement for a seamless authentication experience.
We provide a withAuth helper that will protect routes covered by the matcher. If the user is not authenticated then they are redirected to login and once they have logged in they will be redirected back to the protected page which they should now have access to.
We require this middleware to run on all routes beside Next.js internals and static files. The provided matcher will do this for you.
This means that by default, all routes will be protected. You must opt-out public routes - see opting routes out of middleware protection for more information.
Create a middleware.ts file in your project’s root directory and add the following code:
You can use the withAuth helper as shown below with a middleware callback function which has access to the req.kindeAuth object that exposes the token and user data.
As the middleware matcher is set to protect all routes, you can opt routes out of middleware protection by adding them to the publicPaths array.
There are options that can be passed into the middleware function to configure its functionality.
- isReturnToCurrentPage - redirect the user back to the page they were trying to access
- loginPage - define the path of the login page (where the users are redirected to when not authenticated)
- publicPaths - define the public paths
- isAuthorized - define the criteria for authorization

## Set up the Kinde Auth Provider

Wrap your app in the Kinde Auth Provider. This will give you access to the Kinde Auth data in your app and will ensure that the tokens are refreshed when needed.
Create a file AuthProvider.tsx in your app directory.
Then wrap your app in the AuthProvider component.

## Authentication

### Sign up and sign in

The SDK ships with <LoginLink> and <RegisterLink> components which can be used to start the auth flow.

### Redirecting after authentication

Static redirect
If you want to redirect users to a certain page after logging in, you can set the KINDE_POST_LOGIN_REDIRECT_URL environment variable in your .env.local file.
Dynamic redirect
You can also set a postLoginRedirectURL parameter to tell us where to redirect after authenticating.
This appends post_login_redirect_url to the search params when redirecting to Kinde Auth. You can achieve the same result as above, like this:

### Logout

This is implemented in much the same way as signing up or signing in. A component is provided for you.

## Kinde Auth data - Server

You can get an authorized user’s Kinde Auth data from any server component using the getKindeServerSession helper.

### isAuthenticated

Check if the user is authenticated.

### getUser

Get the logged in user’s details.

### getOrganization

Get the current user’s organization

### getUserOrganizations

Get all the organizations the current user belongs to

### getPermission

Check if the current user has a permission.

### getPermissions

Get the current user’s permissions.

### getFlag

Get a feature flag

### getBooleanFlag

Get a boolean feature flag

### getIntegerFlag

Get a boolean feature flag

### getStringFlag

Get a string feature flag

### refreshTokens

Refresh tokens to get up-to-date Kinde data

### getAccessToken

Get the decoded access token

### getAccessTokenRaw

Get the access token

### getIdToken

Get the decoded ID token

### getIdTokenRaw

Get the ID token

### getClaim

Get a claim from either token

## Kinde Auth data - Client

You can get an authorized user’s Kinde Auth data from any client component using the useKindeBrowser helper.
Tip : Use isLoading to ensure the data is up to date. You can return a loading spinner or something similar if you want.

### isAuthenticated

Check if the user is authenticated.

### user / getUser

Get the logged in user’s details.

### organization / getOrganization

Get the current user’s organization

### userOrganizations / getUserOrganizations

Get all the organizations the current user belongs to

### getPermission

Check if the current user has a permission.

### permissions / getPermissions

Get the current user’s permissions.

### getFlag

Get a feature flag

### getBooleanFlag

Get a boolean feature flag

### getIntegerFlag

Get a boolean feature flag

### getStringFlag

Get a string feature flag

### refreshData

Refresh tokens to get up-to-date Kinde data

### accessToken / getAccessToken

Get the decoded access token

### accessTokenRaw / getAccessTokenRaw

Get the access token

### idToken / getIdToken

Get the decoded ID token

### idTokenRaw / getIdTokenRaw

Get the ID token

### isLoading

Is Kinde data loading

### error

Error message if there is an error

## Protecting routes

It’s likely that your application will have both pages that are publicly available and private ones which should only be available to logged in users. There are multiple ways you can protect pages with Kinde Auth.

### Protect routes with Kinde Auth data

On the page you want to protect, you can check if the user is authenticated and then handle it right then and there by grabbing the Kinde Auth data.
- In Server Components you can get the Kinde Auth data by using the getKindeServerSession helper
- In Client Components you can get the Kinde Auth Data using the useKindeBrowserClient helper
In the example above, we show different content based on whether or not the user is authenticated. If you want to automatically send the user to the sign in screen, you can do something like the following:
If you want the user to be redirected back to that route after signing in, you can set post_login_redirect_url in the search params of the redirect.

## Refreshing Kinde data

Our middleware will automatically refresh the tokens in your session in the background.
Sometimes, you may want to refresh these tokens on demand. An example of this is when you update Kinde data via the UI or with the Management API.
To immediately get the most up-to-date Kinde data in your session, use the refreshData function provided by useKindeBrowserClient .

## Kinde Management API

[LINK: Link to this section](#kinde-management-api)
To use our management API please see @kinde/management-api-js
[LINK: @kinde/management-api-js](https://github.com/kinde-oss/management-api-js)
Server Component example:
Route Handler example:

## Organizations

### Create organizations

To create an organization from your app, you can use the CreateOrgLink component.

### Sign in to organizations

You can have your users sign in to a specific organization by setting the orgCode param in the LoginLink and RegisterLink components.
If the orgCode is not specified and the user belongs to multiple organizations, they will be prompted to choose which organization to sign in to during the login or register flow.

## Self Serve Portal

To allow your users to be sent to the self-serve portal, you can use the PortalLink component.
Check here for information on enabling self-serve portal for Organizations .
Check here for information on enabling self-serve portal for users .
To use our self-serve portal API please see Get self-serve portal link .
[LINK: self-serve portal for Organizations](https://docs.kinde.com/build/self-service-portal/self-serve-portal-for-orgs/)
[LINK: self-serve portal for users](https://docs.kinde.com/build/self-service-portal/self-serve-portal-for-users/)
[LINK: Get self-serve portal link](https://docs.kinde.com/kinde-apis/frontend/)

### subNav

The subNav="" property allows you to set the area of the portal you want the user to land on. By default, it will send users to their profile.

### returnUrl

The returnUrl property is the URL to redirect the user to after they have completed their actions in the portal. The url must be an absolute url to work correctly.

## Analytics

### UTM tags

UTM tags can be used with the LoginLink and RegisterLink components to track auth traffic from its origin. You can then track the tags on the Analytics dashboard from within the Kinde app.

## Internationalization

You can set the language you wish your users to see when they hit the login flow by including the lang attribute as a part of the authUrlParams when using the LoginLink and RegisterLink components.

## Audience

An audience is the intended recipient of an access token - for example the API for your application. The audience argument can be passed to the Kinde client to request an audience be added to the provided token.
You can request multiple audiences by providing a white space separated list
For details on how to connect, see Register an API .
[LINK: Register an API](/developer-tools/your-apis/register-manage-apis/)

## Working with subdomains

In the case you have a custom domain and you would like to start the authentication flow from a URL like auth .mysite.com and you want to redirect to a URL like app .mysite.com , all you have to do is set the KINDE_COOKIE_DOMAIN to match the domain.
If the URL you want to start the authentication flow from and the URL you want to redirect to don’t share the same domain, then this will not work.

## Working with preview URLs

Our Kinde Next.js SDK currently requires that these environment variables KINDE_SITE_URL , KINDE_POST_LOGOUT_REDIRECT_URL , and KINDE_POST_LOGIN_REDIRECT_URL are defined, and that the callback URLs and logout redirect URLs are added to your app in Kinde.
To add Vercel’s dynamically generated URLs you can either securely use our API to add them on the fly or you can use wildcard URLs . It should be noted that whilst wildcards are more convenient it is not as secure as explicitly adding the url to the allowlist via API as we outline below.
Add the following to your next.config.js .
This ensures Vercel uses its generated preview URLs to populate the three Kinde variables.
- Make sure the above values match your application (e.g. “/dashboard” for KINDE_POST_LOGIN_REDIRECT_URL )
- Also make sure variables are not set for the preview environment in your Vercel project. If they are, they will be overridden by the new variables in the next.config.js file.

### Add callback URLs and logout redirect URLs to Kinde dynamically

Create a script that will run each time a new preview is deployed by Vercel, which will add the newly generated URL to Kinde.
You need to create a machine to machine (M2M) application to connect to the Kinde Management API .
[LINK: machine to machine (M2M)](/developer-tools/kinde-api/connect-to-kinde-api/)
[LINK: Kinde Management API](/kinde-apis/management/)
- Create a Machine to machine (M2M) app. In Kinde, go to Settings > Applications and click on Add application . Give your application a name and select Machine to machine (M2M) . Select Save . On the next screen, take note of the Client ID and Client secret values and add them to your .env.local file as KINDE_M2M_CLIENT_ID and KINDE_M2M_CLIENT_SECRET . On the same screen, click on APIs on the left menu. Authorize your M2M application to access the Kinde Management API by selecting the three dots ( ... ) and clicking Authorize application . Once the application is authorized, select the three dots ( ... ) again and this time select Manage scopes . Since we will be adding callback and redirect URLs dynamically via the Kinde Management API, you will need to toggle the switch for create:application_redirect_uris and create:application_logout_uris . Select Save .
Create a Machine to machine (M2M) app.
- In Kinde, go to Settings > Applications and click on Add application .
- Give your application a name and select Machine to machine (M2M) .
- Select Save .
- On the next screen, take note of the Client ID and Client secret values and add them to your .env.local file as KINDE_M2M_CLIENT_ID and KINDE_M2M_CLIENT_SECRET .
- On the same screen, click on APIs on the left menu.
- Authorize your M2M application to access the Kinde Management API by selecting the three dots ( ... ) and clicking Authorize application .
- Once the application is authorized, select the three dots ( ... ) again and this time select Manage scopes .
- Since we will be adding callback and redirect URLs dynamically via the Kinde Management API, you will need to toggle the switch for create:application_redirect_uris and create:application_logout_uris .
- Select Save .
- In your application source code, create a folder at the top level called scripts .
In your application source code, create a folder at the top level called scripts .
- Within that folder, create a file called add-urls-to-kinde.js and add the following code: async function getAuthToken () { try { const response = await fetch ( ` ${ process . env . KINDE_ISSUER_URL } /oauth2/token ` , { method : " POST " , headers : { " Content-Type " : " application/x-www-form-urlencoded " , Accept : " application/json " } , body : new URLSearchParams ( { client_id : process . env . KINDE_M2M_CLIENT_ID , client_secret : process . env . KINDE_M2M_CLIENT_SECRET , grant_type : " client_credentials " , audience : ` ${ process . env . KINDE_ISSUER_URL } /api ` } ) } ) ; if ( ! response . ok ) { throw new Error ( ` Failed to get auth token: ${ response . statusText } ` ) ; } const data = await response . json () ; return data . access_token ; } catch ( error ) { console . error ( " Error getting auth token: " , error ) ; throw error ; } } async function addLogoutUrlToKinde ( token ) { try { const response = await fetch ( ` ${ process . env . KINDE_ISSUER_URL } /api/v1/applications/ ${ process . env . KINDE_CLIENT_ID } /auth_logout_urls ` , { method : " POST " , headers : { Authorization : ` Bearer ${ token } ` , Accept : " application/json " , " Content-Type " : " application/json " } , body : JSON . stringify ( { urls : [ ` https:// ${ process . env . VERCEL_URL } ` ] } ) } ) ; if ( ! response . ok ) { throw new Error ( ` Failed to add logout URL to Kinde: ${ response . statusText } ` ) ; } const responseData = await response . json () ; console . log ( ` SUCCESS: Logout URL added to Kinde: ${ process . env . VERCEL_URL } ` , responseData ) ; } catch ( error ) { console . error ( " Failed to add logout URL to Kinde " , error ) ; throw error ; } } async function addCallbackUrlToKinde ( token ) { try { const response = await fetch ( ` ${ process . env . KINDE_ISSUER_URL } /api/v1/applications/ ${ process . env . KINDE_CLIENT_ID } /auth_redirect_urls ` , { method : " POST " , headers : { Authorization : ` Bearer ${ token } ` , Accept : " application/json " , " Content-Type " : " application/json " } , body : JSON . stringify ( { urls : [ ` https:// ${ process . env . VERCEL_URL } /api/auth/kinde_callback ` ] } ) } ) ; if ( ! response . ok ) { throw new Error ( ` Failed to add callback URL to Kinde: ${ response . statusText } ` ) ; } const responseData = await response . json () ; console . log ( ` SUCCESS: Callback URL added to Kinde: ${ process . env . VERCEL_URL } /api/auth/kinde_callback ` , responseData ) ; } catch ( error ) { console . error ( " Failed to add callback URL to Kinde " , error ) ; throw error ; } } ( async () => { if ( process . env . VERCEL == 1 ) { try { const authToken = await getAuthToken () ; await addCallbackUrlToKinde ( authToken ) ; await addLogoutUrlToKinde ( authToken ) ; } catch ( error ) { console . error ( " Script failed: " , error ) ; } } } )() ;
Within that folder, create a file called add-urls-to-kinde.js and add the following code:
- In your package.json , add a postbuild script that will run the /scripts/add-urls-to-kinde.js file after Vercel builds your app. " scripts " : { " dev " : " next dev " , " build " : " next build " , " start " : " next start " , " lint " : " next lint " , " postbuild " : " node ./scripts/add-urls-to-kinde.js " }
In your package.json , add a postbuild script that will run the /scripts/add-urls-to-kinde.js file after Vercel builds your app.
- Commit these changes. The next deploy will add the newly created preview URLs to your Kinde application.
Commit these changes. The next deploy will add the newly created preview URLs to your Kinde application.

## Health check

To check your configuration, the SDK exposes an endpoint with your settings.
Note : The client secret will indicate only if the secret is set or not set correctly.
/api/auth/health

## State not found error

### Solution

- Confirm that the domain you start the auth flow from is different from the domain you are redirected to after the auth flow is complete. If this is not the case, see the explanation.
- Dynamically set the KINDE_SITE_URL and KINDE_POST_LOGIN_REDIRECT_URL when working with vercel preview domains.
If you are using Vercel, you can set the KINDE_SITE_URL and KINDE_POST_LOGIN_REDIRECT_URL dynamically.

### Explanation

The State not found error in production is usually a result of a mismatch between a few variables.
- KINDE_SITE_URL and/or KINDE_POST_LOGIN_REDIRECT_URL
- The domain you are on e.g. your-app-projects.vercel.app
- Callback URL set on the Kinde dashboard
If you set KINDE_SITE_URL=https:// your-app-projects.vercel.app and KINDE_POST_LOGIN_REDIRECT_URL=https:// your-app-projects.vercel.app/dashboard .
And you also set your Callback URL to be your-app-\*.vercel.app/api/auth/kinde_callback . You should be able to click login and complete the auth flow.
However if you start the auth flow from a Vercel preview domain your-app-PREVIEW-projects.vercel.app and complete the auth flow, you will be redirected to your-app-projects.vercel.app/api/auth/kinde_callback which is NOT the same as the domain you started the auth flow on.
The error happens because when you start the auth flow, a state cookie is set which needs to be checked against when you return back to your app. In this case, you are NOT being redirect to the app you started the flow on, but rather another domain where the app is running which does not have the state cookie.
Since there is a state cookie mismatch, the auth flow is aborted for security reasons.
The reason why you are redirected to the wrong domain because is likely because your KINDE_POST_LOGIN_REDIRECT_URL environment variable is static and is set for all your deployments/domains.
You should set the KINDE_POST_LOGIN_REDIRECT_URL dynamically based on the domain you initiating the auth flow from.

## Debug mode

In debug mode you will see more logs in your console that may help with debugging.

## Migration guide

Changes when moving from the previous version.
handleAuth - is now imported from “@kinde-oss/kinde-auth-nextjs/server”
getKindeServerSession - functions returned from getKindeServerSession now return promises

## Related articles

- Next.js Pages Router SDK SDKs and APIs
[LINK: Next.js Pages Router SDK SDKs and APIs](/developer-tools/sdks/backend/nextjs-prev-sdk/)

### Next.js Pages Router SDK

SDKs and APIs

## Useful links

- Join the community Get support from the Kinde team and expert users in the Kinde community Join via Slack or Discord

### Join the community

Get support from the Kinde team and expert users in the Kinde community
Join via Slack or Discord
- Contact support Chat to support through the Kinde help widget, or send a question via email Send an email

### Contact support

Chat to support through the Kinde help widget, or send a question via email
Send an email
- Browse the docs
- See what’s new
- View our guides
- Read our blog
- Request a feature
- System status

--------------------
# Developer Portal
**URL:** https://portal.airbyte.com
**Page Title:** portal.airbyte.com deprecation
--------------------

To increase security, Airbyte is migrating to use in-app Applications to secure access to the Airbyte API. As a result, we're removing the portal.airbyte.com site, which has previously been used for API key management.
API keys generated from the previous Portal will stop working on August 15, 2024.

## Migration Steps

In order to access these applications, open your workspace and navigate to Settings -> Workspace -> Applications in order to create an Application. From there, you can use the Client ID and Secret tied to that application to request an access token. These expire quickly (3 minutes in Cloud) and so should be refreshed regularly.
Airbyte recommends using the SDKs/Terraform provider, as it is supported natively through client credentials auth and the token is automatically refreshed.
See Authentication for more information on creating an Application and generating a token for testing from the UI or Get an Access Token for using your created application for getting an access token via the Airbyte API.
Updated 11 months ago
Updated 11 months ago

--------------------
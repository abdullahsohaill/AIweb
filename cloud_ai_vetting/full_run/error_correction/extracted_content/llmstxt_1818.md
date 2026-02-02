# llms.txt
**URL:** https://docs.meshconnect.com/llms.txt
**Page Title:** 
--------------------

### (Raw Extraction Fallback)

# Mesh

## Docs

- [Best UX Practices & Examples](https://docs.meshconnect.com/advanced/best-ux-practices.md)
- [Configuring Transfer Options](https://docs.meshconnect.com/advanced/configuring-transfer-options.md)
- [Intelligent Provider Filtering in Mesh Link](https://docs.meshconnect.com/advanced/intelligent-provider-filtering.md)
- [Enabling Multi-Language Support for Link](https://docs.meshconnect.com/advanced/language.md): This guide explains how to configure Mesh Link to support multiple languages, allowing you to provide a localized experience for your users.
- [Mesh Link SDK Events](https://docs.meshconnect.com/advanced/link-ui-events.md)
- [Mesh Managed Tokens (MMT)](https://docs.meshconnect.com/advanced/mesh-managed-tokens.md): This guide explains how to implement Mesh Managed Tokens (MMT), our recommended approach for handling user authentication to create a secure and seamless return user experience.
- [Paylinks](https://docs.meshconnect.com/advanced/paylinks.md)
- [Managing Sub-Clients](https://docs.meshconnect.com/advanced/sub-client-branding.md)
- [Verifying Self-Hosted Wallets](https://docs.meshconnect.com/advanced/verifying-self-hosted-wallets.md): Using Mesh Verify for wallet verification
- [Generate Auth token](https://docs.meshconnect.com/api-reference/account-management/auth-token/generate-auth-token.md): Get a short lived token for initializing request calls for Registered client API.
- [Get Main Client callback urls](https://docs.meshconnect.com/api-reference/account-management/main-clients/get-main-client-callback-urls.md): Get information about Main Client Allowed Link URLs.
- [Update Main Client callback urls](https://docs.meshconnect.com/api-reference/account-management/main-clients/update-main-client-callback-urls.md): Update information about Main Client Allowed Link URLs. Allowed Link URLs of Main Client will only be used for those Registered clients,
that don't have any Allowed Link URLs specified.
- [Add new Registered client](https://docs.meshconnect.com/api-reference/account-management/registered-clients/add-new-registered-client.md): Create new Registered client with specified data. Client will be created without Logo URL.
In order to specify a Logo URL, send separate Update Registered Logo request along with id of just created client.
- [Delete Registered client](https://docs.meshconnect.com/api-reference/account-management/registered-clients/delete-registered-client.md): Delete Registered client by id.
- [Get all Registered clients](https://docs.meshconnect.com/api-reference/account-management/registered-clients/get-all-registered-clients.md): Get information about all Registered clients.
- [Get Registered client](https://docs.meshconnect.com/api-reference/account-management/registered-clients/get-registered-client.md): Get information about the Registered client of specified identifier.
- [Remove Registered client Logo](https://docs.meshconnect.com/api-reference/account-management/registered-clients/remove-registered-client-logo.md): Remove logo of Registered client.
- [Update Registered client](https://docs.meshconnect.com/api-reference/account-management/registered-clients/update-registered-client.md): Update information about already Registered client by client id. This request does not support updating client Logo URL.
In order to update a Logo URL, send separate Update Registered Logo request along with id of the client.
- [Update Registered client Logo](https://docs.meshconnect.com/api-reference/account-management/registered-clients/update-registered-client-logo.md): Adds or update a logo for Registered client.
Allowed file extensions are ".png", ".jpg", ".jpeg".
Allowed file MIME types are "image/png", "image/jpeg", "image/jpg".
Maximum file size is 5MB.
Upload logo as form data with key 'logoFile'.
- [Get account balance](https://docs.meshconnect.com/api-reference/balance/get-account-balance.md): Get real-time account fiat balances.
- [Get aggregated portfolio fiat balances](https://docs.meshconnect.com/api-reference/balance/get-aggregated-portfolio-fiat-balances.md): Get cached aggregated fiat balances from all connected integrations.
- [Get health status](https://docs.meshconnect.com/api-reference/managed-account-authentication/get-health-status.md): Get the list of supported institutions and their health statuses.
- [Get Link token with parameters](https://docs.meshconnect.com/api-reference/managed-account-authentication/get-link-token-with-parameters.md): Get a short lived, one-time use token for initializing a Link session using the client-side SDKs
- [Refresh auth token](https://docs.meshconnect.com/api-reference/managed-account-authentication/refresh-auth-token.md): Refresh auth token of the connected institution.
Some institutions do not require tokens to be refreshed.
            
The following institutions require custom flows:
            
WeBull: AuthToken should be provided along with the RefreshToken
            
Vanguard: security settings may activate MFA, requiring user action.
If MFA is triggered, a second refresh request should be sent.
Second request should contain MFA code and access token obtained from initial response
- [Remove connection](https://docs.meshconnect.com/api-reference/managed-account-authentication/remove-connection.md): Remove connection to the financial institution and erase all related data completely.
- [Retrieve the list of all available integrations.](https://docs.meshconnect.com/api-reference/managed-account-authentication/retrieve-the-list-of-all-available-integrations.md): Returns a list of integrations with details including the integration ID, name, type,
DeFi wallet provider ID, and categories.
- [Get deposit address](https://docs.meshconnect.com/api-reference/managed-transfers/get-deposit-address.md): Get or generate a cryptocurrency deposit address that can be used to transfer assets to the financial institution
- [Get integrations](https://docs.meshconnect.com/api-reference/managed-transfers/get-integrations.md): **Get supported integrations list.**

---
Get the list of all integrations supported by Mesh to perform transfers, including which tokens and networks are supported.
- [Get deposit addresses](https://docs.meshconnect.com/api-reference/managed-transfers/get-list-of-deposit-addresses.md): Get or generate a cryptocurrency deposit address that can be used to transfer assets to the financial institution
- [Get networks](https://docs.meshconnect.com/api-reference/managed-transfers/get-networks.md): **Get supported networks list.**

---
Get the list of all networks supported by Mesh to perform transfers, including which tokens and integrations are supported.

The response always includes validation data:
- `addressPattern`: The regex pattern for validating addresses on this network
- `contractAddress`: For each token, the contract address (if applicable) to enable ERC20 contract address validation
- [Get supported tokens list](https://docs.meshconnect.com/api-reference/managed-transfers/get-supported-tokens-list.md): Get the list of all tokens supported by Mesh to perform transfers, including which networks and integrations are supported.
- [Get transfers initiated by Mesh](https://docs.meshconnect.com/api-reference/managed-transfers/get-transfers-initiated-by-mesh.md): Get cryptocurrency transfers initiated by Mesh on exchanges or self-custody wallets.
- [Get aggregated portfolio](https://docs.meshconnect.com/api-reference/portfolio/get-aggregated-portfolio.md): Get the aggregated portfolio of the user containing market values.
- [Get holdings.](https://docs.meshconnect.com/api-reference/portfolio/get-holdings.md): Obtain assets from the connected investment account. Performs realtime API call to the underlying integration.
- [Get holdings values.](https://docs.meshconnect.com/api-reference/portfolio/get-holdings-values.md): Obtain assets from the connected investment account and return total value and performance.
Performs realtime API call to the underlying integration.
- [Get deposit address](https://docs.meshconnect.com/api-reference/transfers/get-deposit-address.md): Get or generate a cryptocurrency deposit address that can be used to transfer assets to the financial institution
- [Get details of asset](https://docs.meshconnect.com/api-reference/transfers/get-details-of-asset.md): Get details of the asset for deposit or withdrawal. For example, several exchanges support same tokens over multiple
blockchains, and thus require the name of chain to be supplied for transfers. This endpoint allows getting such details.
- [Get transfer details](https://docs.meshconnect.com/api-reference/transfers/get-transfer-details.md): Get details of a specific transfer (withdrawals or deposits) executed from an exchange.
Only supports Exchange integrations.
- [Get transfer history](https://docs.meshconnect.com/api-reference/transfers/get-transfer-history.md): Get entire history of cryptocurrency transfers (withdrawals or deposits) executed from an exchange.
Only supports Exchange integrations.
- [Verify account identity.](https://docs.meshconnect.com/api-reference/verify/verify.md): Returns basic profile data of the user's exchange account.
Available data varies by exchange and linked account.
- [Get wallet verifications for user and address.](https://docs.meshconnect.com/api-reference/verify/wallet.md)
- [Manual](https://docs.meshconnect.com/manual.md)
- [Overview](https://docs.meshconnect.com/overview.md)
- [null](https://docs.meshconnect.com/supported-tokens.md)
- [null](https://docs.meshconnect.com/testing/error-dictionary.md)
- [Sandbox](https://docs.meshconnect.com/testing/sandbox.md): Learn about the Sandbox environment, its features, limitations, and how to use it for API testing.
- [Testnets](https://docs.meshconnect.com/testing/testnets.md)
- [null](https://docs.meshconnect.com/testing/troubleshooting-link.md)
- [Transfer Webhooks](https://docs.meshconnect.com/testing/webhooks.md)


--------------------
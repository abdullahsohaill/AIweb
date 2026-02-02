# REST Countries API
**URL:** https://restcountries.com
**Page Title:** REST Countries
--------------------


## REST Countries

- View on GitLab
- Issues
- REST Countries 🇵🇪 About this Project Important Information REST Countries Contributing Donations Fields (mandatory) API Endpoints Using this Project Endpoints Latest added Enpoint Independent All Name Full Name Code List of codes Currency Demonym Language Capital city Calling code Region Subregions Translation Filter Response REST Countries Typed API Package Similar projects
- REST Countries 🇵🇪
- About this Project Important Information
- Important Information
- REST Countries
- Contributing
- Donations
- Fields (mandatory)
- API Endpoints Using this Project
[LINK: API Endpoints](#api-endpoints)
- Using this Project
[LINK: Using this Project](#api-endpoints-using-this-project)
- Endpoints Latest added Enpoint Independent All Name Full Name Code List of codes Currency Demonym Language Capital city Calling code Region Subregions Translation Filter Response REST Countries Typed API Package Similar projects
- Latest added Enpoint Independent
- Independent
- All
- Name
- Full Name
- Code
- List of codes
- Currency Demonym
- Demonym
- Language
- Capital city
[LINK: Capital city](#endpoints-capital-city)
- Calling code
- Region
- Subregions
- Translation
- Filter Response
- REST Countries Typed API Package
[LINK: REST Countries Typed API Package](#endpoints-rest-countries-typed-api-package)
- Similar projects

## REST Countries 🇵🇪

Get information about countries via a RESTful API
Current version: 3.1

## About this Project

This project is inspired on restcountries.eu by Fayder Florez. Although the original project has now
moved to
a subscription base API, this project is still Open Source and Free to use.

## Important Information

- The structure of V2 has been reverted to its original form from the Original Project to maintain
compatibility.
[LINK: Original Project](https://github.com/apilayer/restcountries/)
- Only the latest version will receive updates and improvements.

## REST Countries

You can access API through https://restcountries.com/v3.1/all but in order to get a faster response,
you should filter the results by the fields you need.
Like

## Contributing

Any help is always welcome! Just edit the relevant file and create a new Merge Request or you can
also
donate using Patreon or PayPal .

## Donations

This are getting out of control (in a positive way).
I’m getting about 4 million hits each day and that means CPU ussage (sometimes at 99%) and also
bandwidth consumption (120 GB per day! ) so costs have obviously increased. Please , consider
making a donation on Patreon or PayPal . This will help me pay the server’s bills

## Fields (mandatory)

You can check the FIELDS.md file to get a description for each field (thanks to
@ePascalC!). You must specify the fields you need (up to 10 fields) when calling the all endpoints.

## API Endpoints

## Using this Project

- Famosos
- Cultural Care
- Covidata
- Asendia
- Picker

## Endpoints

Below are described the REST endpoints available that you can use to search for countries

## Latest added Enpoint

### Independent

Now you can get all independent (or not independent) countries by calling this endpoint:
If you don’t specify the status, true will be taken as default. You can mix it with the fields filter like this:

## All

You must specify the fields you need (up to 10 fields) when calling the all endpoints,
otherwise you’ll get a bad request response. Please see this issue for more information. This applies to all versions.

## Name

Search by country name. If you want to get an exact match, use the next endpoint. It can be the
common or official value

## Full Name

Search by country’s full name. It can be the common or official value

## Code

Search by cca2, ccn3, cca3 or cioc country code (yes, any!)

## List of codes

Search by cca2, ccn3, cca3 or cioc country code (yes, any!)

## Currency

Search by currency code or name

### Demonym

Now you can search by how a citizen is called.

## Language

Search by language code or name

## Capital city

Search by capital city

## Calling code

In version 3, calling codes are in the idd object. There is no implementation
to search by calling codes in V3.

## Region

Search by region (replace X with the version you want to use)

## Subregions

You can search by subregions (replace X with the version you want to use)

## Translation

You can search by any translation name

## Filter Response

You can filter the output of your request to include only the specified fields.

## REST Countries Typed API Package

Yusif Aliyev from Azerbaijan created an npm package which provides TypeScript support for the REST Countries API. Everyone can use
the package for their own purpose.
This package offers full type and autocomplete support for anyone using
JavaScript or TypeScript. Users no longer need to spend time reading
documentation or manually writing API URLs and types. You can easily use
all the package’s functionalities by calling its functions.
He is also open to contributing further improvements.
You can find the code here
[LINK: here](https://github.com/yusifaliyevpro/countries)

## Similar projects

- REST Countries (original project)
[LINK: REST Countries](https://github.com/apilayer/restcountries)
- Countries of the world
- REST Countries Node.js
[LINK: REST Countries Node.js](https://github.com/aredo/restcountries)
- REST Countries Ruby
[LINK: REST Countries Ruby](https://github.com/davidesantangelo/restcountry)
- REST Countries Go
[LINK: REST Countries Go](https://github.com/alediaferia/gocountries)
- REST Countries Python
[LINK: REST Countries Python](https://github.com/SteinRobert/python-restcountries)
- world-currencies
[LINK: world-currencies](https://github.com/wiredmax/world-currencies)

--------------------
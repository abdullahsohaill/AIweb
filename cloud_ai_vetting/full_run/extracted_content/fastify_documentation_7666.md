# Fastify Documentation
**URL:** https://fastify.dev
**Page Title:** Fast and low overhead web framework, for Node.js | Fastify
--------------------


## Why

An efficient server implies a lower cost of the infrastructure, better responsiveness under load, and happy users. How can you efficiently handle the resources of your server, knowing that you are serving the highest number of requests possible, without sacrificing security validations and handy development?
Enter Fastify. Fastify is a web framework highly focused on providing the best developer experience with the least overhead and a powerful plugin architecture. It is inspired by Hapi and Express and as far as we know, it is one of the fastest web frameworks in town.

## Who is using Fastify?

Fastify is proudly powering a large ecosystem of organizations and products out there with over 10 million downloads per month . Checkout our affiliate companies.

### Sponsors

Would you like to sponsor Fastify financially? Support us on GitHub or Open Collective .
[LINK: GitHub](https://github.com/sponsors/fastify)

## Core features

These are the main features and principles on which Fastify has been built:
- Highly performant: as far as we know, Fastify is one of the fastest web frameworks in town, depending on the code complexity we can serve up to 30 thousand requests per second.
- Extensible: Fastify is fully extensible via its hooks, plugins, and decorators.
- Schema-based: even if it is not mandatory we recommend using JSON Schema to validate your routes and serialize your outputs. Internally Fastify compiles the schema in a highly performant function.
- Logging: logs are extremely important but are costly; we chose the best logger to almost remove this cost, Pino !
[LINK: Pino](https://github.com/pinojs/pino)
- Developer friendly: the framework is built to be very expressive and help developers in their daily use, without sacrificing performance and security.
- TypeScript ready: we work hard to maintain a TypeScript type declaration file so we can support the growing TypeScript community.

## Quick start

Get Fastify with NPM:
Then create server.js and add the following content:
- ESM
- CJS
Finally, launch the server with:
and test it with:

## Using CLI

Get the fastify-cli to create a new scaffolding project:
[LINK: fastify-cli](https://github.com/fastify/fastify-cli)
Or to create a TypeScript project:

## Request/Response validation and hooks

Fastify can do much more than this. For example, you can easily provide input and output validation using JSON Schema and perform specific operations before the handler is executed:
- ESM
- CJS

## TypeScript Support

Fastify is shipped with a typings file, but you may need to install @types/node , depending on the Node.js version you are using. The following example creates a http server. We pass the relevant typings for our http version used. By passing types we get correctly typed access to the underlying http objects in routes. If using http2 we would pass <http2.Http2Server, http2.Http2ServerRequest, http2.Http2ServerResponse> . For https pass http2.Http2SecureServer or http.SecureServer instead of Server. This ensures within the server handler we also get http.ServerResponse with correct typings on reply.res .
- TypeScript
Visit the Documentation to learn more about all the features that Fastify has to offer.
[LINK: Documentation](/docs/latest/)

## A fast web framework

Leveraging our experience with Node.js performance, Fastify has been built from the ground up to be as fast as possible . Have a look at our benchmarks section to compare Fastify performance to other common web frameworks.
Check out our benchmarks

## Ecosystem

Fastify has an ever-growing ecosystem of plugins. There is probably already a plugin for your favorite database or template language. Have a look at the Ecosystem page to navigate through the currently available plugins. Can't you find the plugin you are looking for? No problem, it's very easy to write one !
[LINK: it's very easy to write one](/docs/latest/Reference/Plugins/)
Explore 308 plugins

## Meet The Team

In alphabetical order

## Lead Maintainers

Matteo Collina
Tomas Della Vedova
KaKa Ng
Manuel Spigolon
James Sumners

## Collaborators

Aras Abbasi
Harry Brundage
Dan Castillo
Gürgün Dayıoğlu
Carlos Fuentes
Vincent Le Goff
Luciano Mammino
Jean Michelet
Luis Orbaiceta
Igor Savin
Evan Shortiss
Maksim Sinik
Frazer Smith

## Past Collaborators

Tommaso Allevi
Ethan Arrowood
Ayoub El Khattabi
Çağatay Çalı
Cemre Mengu
David Clements
Dustin Deus
Rafael Gonzaga
Salman Mitha
Trivikram Kamat
Nathan Woltman

## Acknowledgments

This project is kindly sponsored by :
- NearForm
- Platformatic
Past Sponsors:
- LetzDoIt
- Microsoft
Also thanks to:
- The amazing Fastify community
[LINK: The amazing Fastify community](https://github.com/fastify/fastify/graphs/contributors)
We are an At Large project at the OpenJS Foundation

--------------------
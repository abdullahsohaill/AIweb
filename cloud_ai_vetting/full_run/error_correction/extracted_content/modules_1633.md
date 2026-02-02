# Modules
**URL:** https://docs.nestjs.com/modules
**Page Title:** Modules | NestJS - A progressive Node.js framework
--------------------

- Modules
[LINK: Modules](https://docs.nestjs.com/modules#modules)
- Feature modules
[LINK: Feature modules](https://docs.nestjs.com/modules#feature-modules)
- Shared modules
[LINK: Shared modules](https://docs.nestjs.com/modules#shared-modules)
- Module re-exporting
[LINK: Module re-exporting](https://docs.nestjs.com/modules#module-re-exporting)
- Dependency injection
[LINK: Dependency injection](https://docs.nestjs.com/modules#dependency-injection)
- Global modules
[LINK: Global modules](https://docs.nestjs.com/modules#global-modules)
- Dynamic modules
[LINK: Dynamic modules](https://docs.nestjs.com/modules#dynamic-modules)

### Modules

A module is a class that is annotated with the @Module() decorator. This decorator provides metadata that Nest uses to organize and manage the application structure efficiently.
Every Nest application has at least one module, the root module , which serves as the starting point for Nest to build the application graph . This graph is an internal structure that Nest uses to resolve relationships and dependencies between modules and providers. While small applications might only have a root module, this is generally not the case. Modules are highly recommended as an effective way to organize your components. For most applications, you'll likely have multiple modules, each encapsulating a closely related set of capabilities .
The @Module() decorator takes a single object with properties that describe the module:
The module encapsulates providers by default, meaning you can only inject providers that are either part of the current module or explicitly exported from other imported modules. The exported providers from a module essentially serve as the module's public interface or API.
In our example, the CatsController and CatsService are closely related and serve the same application domain. It makes sense to group them into a feature module. A feature module organizes code that is relevant to a specific feature, helping to maintain clear boundaries and better organization. This is particularly important as the application or team grows, and it aligns with the SOLID principles.
Next, we'll create the CatsModule to demonstrate how to group the controller and service.
Above, we defined the CatsModule in the cats.module.ts file, and moved everything related to this module into the cats directory. The last thing we need to do is import this module into the root module (the AppModule , defined in the app.module.ts file).
Here is how our directory structure looks now:
In Nest, modules are singletons by default, and thus you can share the same instance of any provider between multiple modules effortlessly.
Every module is automatically a shared module . Once created it can be reused by any module. Let's imagine that we want to share an instance of the CatsService between several other modules. In order to do that, we first need to export the CatsService provider by adding it to the module's exports array, as shown below:
Now any module that imports the CatsModule has access to the CatsService and will share the same instance with all other modules that import it as well.
If we were to directly register the CatsService in every module that requires it, it would indeed work, but it would result in each module getting its own separate instance of the CatsService . This can lead to increased memory usage since multiple instances of the same service are created, and it could also cause unexpected behavior, such as state inconsistency if the service maintains any internal state.
By encapsulating the CatsService inside a module, such as the CatsModule , and exporting it, we ensure that the same instance of CatsService is reused across all modules that import CatsModule . This not only reduces memory consumption but also leads to more predictable behavior, as all modules share the same instance, making it easier to manage shared states or resources. This is one of the key benefits of modularity and dependency injection in frameworks like NestJS—allowing services to be efficiently shared throughout the application.
Explore your graph with NestJS Devtools Graph visualizer Routes navigator Interactive playground CI/CD integration Sign up

## Explore your graph with NestJS Devtools

- Graph visualizer
- Routes navigator
- Interactive playground
- CI/CD integration
As seen above, Modules can export their internal providers. In addition, they can re-export modules that they import. In the example below, the CommonModule is both imported into and exported from the CoreModule , making it available for other modules which import this one.
A module class can inject providers as well (e.g., for configuration purposes):
However, module classes themselves cannot be injected as providers due to circular dependency .
If you have to import the same set of modules everywhere, it can get tedious. Unlike in Nest, Angular providers are registered in the global scope. Once defined, they're available everywhere. Nest, however, encapsulates providers inside the module scope. You aren't able to use a module's providers elsewhere without first importing the encapsulating module.
When you want to provide a set of providers which should be available everywhere out-of-the-box (e.g., helpers, database connections, etc.), make the module global with the @Global() decorator.
The @Global() decorator makes the module global-scoped. Global modules should be registered only once , generally by the root or core module. In the above example, the CatsService provider will be ubiquitous, and modules that wish to inject the service will not need to import the CatsModule in their imports array.
Dynamic modules in Nest allow you to create modules that can be configured at runtime. This is especially useful when you need to provide flexible, customizable modules where the providers can be created based on certain options or configurations. Here's a brief overview of how dynamic modules work.
This module defines the Connection provider by default (in the @Module() decorator metadata), but additionally - depending on the entities and options objects passed into the forRoot() method - exposes a collection of providers, for example, repositories. Note that the properties returned by the dynamic module extend (rather than override) the base module metadata defined in the @Module() decorator. That's how both the statically declared Connection provider and the dynamically generated repository providers are exported from the module.
If you want to register a dynamic module in the global scope, set the global property to true .
The DatabaseModule can be imported and configured in the following manner:
If you want to in turn re-export a dynamic module, you can omit the forRoot() method call in the exports array:
The Dynamic modules chapter covers this topic in greater detail, and includes a working example .
[LINK: working example](https://github.com/nestjs/nest/tree/master/sample/25-dynamic-modules)

### Support us

Nest is an MIT-licensed open source project. It can grow thanks to the support of these awesome people. If you'd like to join them, please read more here .

### Join our Newsletter

Subscribe to stay up to date with the latest Nest updates, features, and videos!

--------------------
# https://docs.digitalocean.com/products/app-platform/how-to/create-apps/
**URL:** https://docs.digitalocean.com/products/app-platform/how-to/create-apps
**Page Title:** How to Create Apps in App Platform | DigitalOcean Documentation
--------------------


## How to Create Apps in App Platform

Validated on 10 May 2024 • Last edited on 27 Jan 2026
App Platform is a fully managed Platform-as-a-Service (PaaS) that deploys applications from Git repositories or container images. It automatically builds, deploys, and scales components while handling all underlying infrastructure.
App Platform retrieves your app’s code from your linked repository or container registry, detects the type of language the app is written in, and deploys the app into an appropriate container environment. App Platform hosts the app at a public URL provided by DigitalOcean and can automatically redeploy the app when it detects changes in the repo.
App Platform supports deployment from the following source code management services:
- GitHub
- GitLab
- Bitbucket
- DOCR
- Docker Hub
- GitHub Container Registry
Creating an App Platform app involves two steps:
- Choose a deployment source.
- Review and configure resource settings (such as the app’s name, region, size, instance type, instance sizes, environment variables, and HTTP routes).
You can change the configuration and add more services, static sites, and databases after you create the app.
[LINK: Owner or Maintainer permissions-role](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization)

## Create Resource From Source Code Using Automation

To create an app using the CLI or API, provide a path to an app spec file (JSON or YAML) as the argument for the --spec flag using the CLI, or provide a spec as a JSON object in the spec field of the App Create API request.
- Install doctl , the official DigitalOcean CLI.
[LINK: Install doctl](https://docs.digitalocean.com/reference/doctl/how-to/install/)
- Create a personal access token and save it for use with doctl .
[LINK: Create a personal access token](https://docs.digitalocean.com/reference/api/create-personal-access-token/)
- Use the token to grant doctl access to your DigitalOcean account. doctl auth init
- Finally, run doctl apps create . Basic usage looks like this, but you can read the usage docs for more details: doctl apps create [ flags ] The following example creates an app in a project named example-project using an app spec located in a directory called /src/your-app.yaml . Additionally, the command returns the new app’s ID, ingress information, and creation date: doctl apps create --spec src/your-app.yaml --format ID,DefaultIngress,Created
[LINK: read the usage docs](https://docs.digitalocean.com/reference/doctl/reference/apps/create/)
- Create a personal access token and save it for use with the API.
[LINK: Create a personal access token](https://docs.digitalocean.com/reference/api/create-personal-access-token/)
- Send a POST request to https://api.digitalocean.com/v2/apps .
[LINK: https://api.digitalocean.com/v2/apps](https://docs.digitalocean.com/reference/api/digitalocean//#operation/apps_create)

### cURL

Using cURL:

### Python

Using PyDo , the official DigitalOcean API client for Python:
[LINK: PyDo](https://github.com/digitalocean/pydo)

## Create Resource From Source Code Using the Control Panel

To create an app using the DigitalOcean Control Panel , click the Create button and then select App Platform from the dropdown menu.
On the Choose a deployment source screen, select the code repository service your app resides on. If you have not previously created an app on App Platform, the repository service prompts you to provide DigitalOcean with read permissions to your account.
Select the app’s repo from the Repository dropdown and then select the branch to deploy from in the Branch dropdown menu.
The Source Directory is the directory inside the repo to build the app from. The default is the repo’s root directory. If you’re deploying from a monorepo or a container image registry, see Deploy from a Monorepo or How to Deploy from Container Images for more information on how to deploy apps using these options.
If you don’t want App Platform to redeploy the app when it detects changes, clear the Autodeploy box.
After you select the app’s repo and branch, click Next . App Platform retrieves your app’s code.
App Platform inspects the code and app resources, and selects an appropriate runtime environment (such as Node, or Ruby). If you need to override this, upload a Dockerfile to your branch and restart the app creation process.
[LINK: Dockerfile](https://docs.docker.com/engine/reference/builder/)

## Configure Resource Settings

Apps include two types of deployable resources: app resources for running code, and database resources for managed databases.
App resources are made up of components , which define how code is built, deployed, and run. Supported component types include web services, workers, jobs, and static sites. Web services, workers, and jobs run in containers from a repository or container image, while static sites are hosted from a directory of static files on DigitalOcean’s CDN.
The Resource settings table displays the configuration settings for each component, some of which the detection system auto-fills. Click Edit beside the component you want to change.
You can configure the following settings:
- Name: A unique name for the component.
Name: A unique name for the component.
- Resource type: The type of component to deploy (web service, static site, or worker service). This field determines which additional configuration options appear on this screen.
Resource type: The type of component to deploy (web service, static site, or worker service). This field determines which additional configuration options appear on this screen.
- Instance size: The amount of memory (RAM), CPUs, and bandwidth allocated to the component. You can choose shared or dedicated CPUs. Shared CPUs share their processing power with other DigitalOcean users. Dedicated CPUs are dedicated solely to your app. We recommend dedicated CPUs for more resource-intensive applications that require consistent high performance and autoscaling.
Instance size: The amount of memory (RAM), CPUs, and bandwidth allocated to the component. You can choose shared or dedicated CPUs. Shared CPUs share their processing power with other DigitalOcean users. Dedicated CPUs are dedicated solely to your app. We recommend dedicated CPUs for more resource-intensive applications that require consistent high performance and autoscaling.
- Containers: Configure the component’s scaling settings. The instance size you select determines the scaling options available. For more details, see How to Scale Apps in App Platform .
Containers: Configure the component’s scaling settings. The instance size you select determines the scaling options available. For more details, see How to Scale Apps in App Platform .
- Build command: Add a custom build command to run before the app is deployed. This is useful for compiling assets, installing dependencies, or running tests before deployment.
Build command: Add a custom build command to run before the app is deployed. This is useful for compiling assets, installing dependencies, or running tests before deployment.
- Run command: For web and worker services only. You can specify custom run commands for the application to run after deployment. If no run commands are specified, the default run command for your app’s language is used, such as npm start for a Node.js app. For Dockerfile-based builds, entering a run command overrides the Dockerfile’s entrypoint.
Run command: For web and worker services only. You can specify custom run commands for the application to run after deployment. If no run commands are specified, the default run command for your app’s language is used, such as npm start for a Node.js app. For Dockerfile-based builds, entering a run command overrides the Dockerfile’s entrypoint.
- Public HTTP port: For web services only. The port that the app receives HTTP requests on. The default port is 8080 .
Public HTTP port: For web services only. The port that the app receives HTTP requests on. The default port is 8080 .
- Internal ports: For web services only. The port that the app receives internal requests on.
Internal ports: For web services only. The port that the app receives internal requests on.
- HTTP request routes: For web services and static sites only. The URL path where the app can be accessed, such as your-app-v3cl4.ondigitalocean.app/api . If not specified, the app is accessible from the provided hostname’s root.
HTTP request routes: For web services and static sites only. The URL path where the app can be accessed, such as your-app-v3cl4.ondigitalocean.app/api . If not specified, the app is accessible from the provided hostname’s root.
- Environment variables: Key-value pairs that are available to your app at runtime. Use them to store configuration values, secrets, API keys, or other data that your app needs to access without hardcoding them into the source code. Environment variables can be defined at the component level and, in some cases, overridden per deployment environment. For example, you can provide connection details for an external database using environment variables.
Environment variables: Key-value pairs that are available to your app at runtime. Use them to store configuration values, secrets, API keys, or other data that your app needs to access without hardcoding them into the source code. Environment variables can be defined at the component level and, in some cases, overridden per deployment environment. For example, you can provide connection details for an external database using environment variables.
- Output Directory: For static sites only. An optional path to where the build assets are located, relative to the build context. If not set, App Platform automatically scans for these directory names: _static , dist , public , build .
Output Directory: For static sites only. An optional path to where the build assets are located, relative to the build context. If not set, App Platform automatically scans for these directory names: _static , dist , public , build .
App Platform uses cloud-native buildpacks to build components and applies the buildpack’s default build and run commands. See the cloud-native buildpack reference for details about supported buildpacks.

## Add a Database

In the Add a Database section, you can connect a database to your app.
- To provision a new dev database directly within your app, click Create dev database .
To provision a new dev database directly within your app, click Create dev database .
- To connect an existing DigitalOcean Managed Database, click Attach DigitalOcean database .
To connect an existing DigitalOcean Managed Database, click Attach DigitalOcean database .
- If your database is hosted outside of DigitalOcean, add environment variables to provide connection details in the Resource settings table.
If your database is hosted outside of DigitalOcean, add environment variables to provide connection details in the Resource settings table.
After connecting a database, App Platform automatically injects the necessary connection information into the relevant component’s environment variables.
For more information, see How to Manage Databases in App Platform .

## App-Level Environment Variables

App-level environment variables are defined at the app level and accessible by all resources in your app. They can be used for configuration values, secrets, API keys, or other data your app needs at build time or runtime.
To set app-level environment variables, in the App-level environment variables box, click Edit . Click Add environment variable , type a key and value, and then select a scope. Select the Encrypt checkbox to obscure the variable’s value in build, deployment, and application logs.
For dynamic, app-specific variables that your app can reference, see app-specific dynamic environment variables .

## Datacenter Region

In the Datacenter region section, you can choose the datacenter region to deploy your app into. Click the Choose a datacenter region dropdown menu and select a region. For performance purposes, it is best to select the region geographically closest to the app’s user base.
You cannot select a region for static sites. Static resources are served on DigitalOcean’s global CDN .

## Finalize

In the Finalize section, you can update the app’s name and project.
In the Choose a unique app name field, type a name for the app. In the Select a project dropdown menu, you can select an existing project or create a new project. If you create a new project, you can also select an environment for the project.
After you choose a name and project, click Create app .
App Platform creates the app using the selected settings and deploys it automatically. Once your app deploys, you can view the app at the URL at the top of the app’s Overview page.

### We can't find any results for your search.

Try using different keywords or simplifying your search terms.

## Product Docs

### We can't find any results for your search.

Try using different keywords or simplifying your search terms.

## Marketplace

## DigitalOcean Blog

## Community


--------------------
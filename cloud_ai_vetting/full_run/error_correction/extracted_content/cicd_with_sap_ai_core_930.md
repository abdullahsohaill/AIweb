# CI/CD with SAP AI Core
**URL:** https://community.sap.com/t5/technology-blogs-by-sap/ci-cd-with-sap-ai-core/ba-p/13708965
**Page Title:** CI/CD with SAP AI Core - SAP Community
--------------------

- SAP Community
- Products and Technology
- Technology
- Technology Blog Posts by SAP
- CI/CD with SAP AI Core

## CI/CD with SAP AI Core

- Subscribe to RSS Feed
- Mark as New
- Mark as Read
- Bookmark
- Printer Friendly Page
- Report Inappropriate Content
- SAP Managed Tags
- Machine Learning
- Python
- SAP AI Core
- Machine Learning Topic
- Python Programming Tool
- SAP AI Core SAP Business AI
SAP AI Core is the AI Workload Management Solution on SAP BTP. Its the place to be for Machine Learning Engineers in the SAP domain and brings a bunch of out-of the box features supporting in training and serving machine learning scenarios. To strengthen the development workflow with AI Core, I will introduce an example of how to use a CI/CD pipeline in a multi-stage development environment. It aims to accelerate testing processes and enhance the stability of your production environment.

## Szenario:

Anyone who starts developing machine learning content for AI Core knows the struggle: updating templates, building Docker containers, and testing the training or serving source code. This blog post provides an overview of how to minimize deployment time.
Operating within a three-stage landscape, our objective is to streamline the deployment of an end-to-end training/serving ML workflow. Each of the three instances resides in distinct subaccounts on BTP and is linked to dedicated object stores. Our deployment automation strategy revolves around crafting workflows in a development environment first, ensuring everything is fine-tuned before transitioning to production. We strictly segregate data between environments to enforce robust data protection measures.

## CI/CD Platforms:

I have worked with several of the aforementioned technologies, and each one has slight differences in how you execute scripts and manage environment variables. This blog demonstrates how to automate deployment on one platform, but the scripts available on GitHub can be adapted for use on other platforms.

## Development Workflow on SAP AI Core:

Again to recap: The below are the main steps in building custom ML Solutions in AI Core and how we want to simplify it.

### 1. Dockerize Source Code:

The very first step is to develop our training and serving code. This is done in a local environment using locally available test data stored in files.

### 2. Template Creation:

The AI Core-specific task involves creating a YAML-based template to orchestrate our workload. This can be quite challenging and involves several steps to configure it as desired. In an upcoming blog post, I will provide a deep dive into template creation. Some important aspects to consider for production are using environment variables and secrets, accessing and writing files via the storage gateway to object stores, and specifying the infrastructure to use (resource plan, multiplicity, etc.).

### 3. Actual Deployment:

The actual deployment involves pushing the template to a synchronized Git repository, creating artifacts, configurations, and then performing the respective deployment or execution. These tasks can be particularly cumbersome when executed manually step-by-step, especially when done through the user interface of the AI Launchpad.

## CI/CD Principles used:

### 1. Git as sole truth of deployment state

The first important principle is to use the Git repository as the single source of truth for all source code-related items. We do this by specifying three branches, one for each stage. These branches are linked to the platform and represent its state. This approach ensures versioning of deployments and modifications in the source code, templates, and configurations, thereby eliminating mistakes.

### 2. Automate everything up to one click

The deployment process consists of many individual tasks, all of which can be summarized in a deployment script. We utilize the AI Core SDK because it is the most convenient way to interact with the RESTful API.

### 3. Deployment Configuration as file

Most importantly, we use a deployment configuration file to precisely define how and what we want to deploy to the platform when executing our pipeline. This principle allows us to specify different configurations for multiple environments. The configuration file is defined in JSON, as many of the payloads are also JSON-based, making it more convenient compared to the widely used YAML.

### Prerequisites:

It is required to have the Git-Sync enabled for the branches you want to deploy to. For my case this means:
- Creating the Git Repository Credentials per Subaccount
- Creating the Application linked to the necessary branch per Subaccount
- Creating the "default" Object Store Secret per Subaccount and Resource Group
- Creating the Docker Registry Credentials per Subaccount
- (Optional) Creating generic secrets used

### Configuration Schema:

Below is the rough configuration schema I use. Here, I specify all artifacts, executions, and deployments I want to be created upon deployment. Specifically for the executables, we need to define parameter and artifact bindings, paying attention to additional details. For example, the artifact may be enriched with a "key" field, which is then used to map it to the input artifact binding. The "wait for status" field determines at which status we should follow the logs, which can be convenient. All other fields visible, such as name, kind, URL, and scenario_id of an artifact, are the fields leveraged when creating the objects themselves.
The automation is designed to support the deployment of multiple objects and also to view the logs of multiple executables, though currently, the logs are viewed sequentially. Typically, I would use one executable in the configuration for rapid testing and then include the entire configuration when moving between stages. This approach speeds up script execution, and only the necessary deployment can be debugged as needed.

## Source Code for the Python CI/CD Script:

At a high level, the script progresses through three phases. The first phase involves manually syncing with the Git repository to ensure all new templates are up to date. Next, the script proceeds to create executions and deployments one by one using the configuration JSON file. Finally, it monitors and reports on the status of these executions and deployments, providing an output of the logs.
Reviewing logs in AI Launchpad can be a tedious task. I find it much more satisfying to have the logs displayed in proper order within a console environment.
The code for the pipeline supports several optional features. For instance, it can clean up the tenant by deleting all previous deployments and executions, or it can prevent duplicate artifact or configuration creations. This is particularly useful when deploying fixes multiple times, as creating individual new configurations can clutter the resource group and diminish usability.

### CI/CD Pipeline Setup:

The CI/CD Script shown can be run locally, but maximises its utility deployed on a CI/CD Platform. In my demonstration, I'll illustrate how to set it up with GitHub Actions.
An important feature we rely on to determine which tenant to deploy the content to is environment secrets, typically created in the repository settings. For my example, I've configured secrets for three branches, and the CI pipeline will run upon commits to these branches. Consequently, pushing to the dev branch triggers deployment to the development environment, initiating a pull request from dev to test results in deployment to the test environment upon completion, and vice versa for the production environment. Additionally, we can incorporate steps for unit/integration testing and approvals.
In action, upon pushing my local changes, the pipeline is triggered, and within approximately 20 seconds, the changes are deployed and scheduled for execution.
Here's how the repository will be structured:
The project structure includes a .github directory for the pipeline's YAML markup, a cicd directory containing the pipeline code, configuration.json, and a requirements.txt file specifying additional dependencies. The templates folder holds WorkflowTemplate and ServingTemplate markup, synced with AI Core. At the root level, Python files and a Dockerfile are present as the source code, with potential for additional structuring as the project grows.
The YAML configuration at the end can be adjusted as required. For this blog example, I utilize environment variables created as secrets in three environments (dev, tst, prd) and execute identical steps. Leveraging the GitHub Actions ubuntu-latest image, we employ checkout to retrieve the code, setup-python to establish a valid Python environment, and then execute custom commands. This includes pip install to install pipeline dependencies and the execution of our pipeline script. Jobs are triggered upon a push to any of the specified branches.

### Multi Resource Group Setup:

A final note on facilitating multi-team and project collaboration through this workflow: AI Core provides developers with the opportunity to segregate teams' work using resource groups. I highly recommend leveraging this approach for the CI setup as well. To maintain efficiency, I suggest having an individual instance of a CI Pipeline per resource group. This allows teams to make changes independently and have different deployment schedules. Ultimately, it's as simple as creating a new Git repository and setting up the three branches to connect to another set of resource groups in the environment.
Hope this blog post gave you an idea on how to make use of CI Pipelines in SAP AI Core! Find all the shown code pieces in one harmonized Github repository for you to try out. Feel free to leave a comment!
[LINK: Github](https://github.com/fyx99/CI-CD-with-AI-Core)
- Expert Insights​
You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.
- Comment
- SAP Databricks CLI: Unlocking Automation and Efficiency in Data Engineering in Technology Blog Posts by SAP 15m ago
- BIB Replication: Employee Central to S/4 in Technology Blog Posts by SAP Friday
- SAP BTP - APIM - Domain-Centric Routing Pattern (DCRP): Governing APIs via CPI Provider - Part I in Technology Blog Posts by Members Friday
[LINK: SAP BTP - APIM - Domain-Centric Routing Pattern (DCRP): Governing APIs via CPI Provider - Part I](/t5/technology-blog-posts-by-members/sap-btp-apim-domain-centric-routing-pattern-dcrp-governing-apis-via-cpi/ba-p/14312788)
- New ESAC (CQC) Pilot for Customers: Deployment Readiness Check for the Integrated Toolchain in Technology Blog Posts by SAP Friday
- Sneak Peek in to SAP Analytics Cloud release for Q1 2026 in Technology Blog Posts by SAP Thursday

--------------------
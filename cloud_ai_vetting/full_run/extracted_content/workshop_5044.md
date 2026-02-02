# workshop
**URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/db0f23ea-2442-4962-9a54-04dcdab7de59/en-US
**Page Title:** Guidance for Multi-Provider Generative AI Gateway on AWS
--------------------


## Select your cookie preferences

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

## Customize cookie preferences

### Essential

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

### Performance

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

### Functional

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

### Advertising

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.
Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the AWS Cookie Notice .

## Unable to save cookie preferences

We will only store essential cookies at this time, because we were unable to save your cookie preferences. If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

## Settings

## Settings

The AWS Solution Library now offers Guidance for Multi-Provider Generative AI Gateway, helping customers deploy and manage a centralized gateway using LiteLLM on AWS to streamline their LLM interactions. This solution provides organizations with a single, secure API interface to standardize access across multiple AI providers, including Amazon Bedrock . Through HashiCorp Terraform templates, the solution enables automated deployment on Amazon ECS or Amazon EKS , complete with production-ready features including usage tracking, access control, and cost management capabilities.

## Workshop Experience

This workshop provides hands-on exploration of the solution's capabilities through interactive exercises and real-world scenarios.
AWS Event Participants : The solution is pre-deployed in your workshop environment. You'll explore its features and capabilities without needing to deploy infrastructure. Self-Paced Learners : You'll deploy the complete solution in your own AWS account, then explore the same hands-on exercises.
We'll cover the specific setup steps for your workshop path in the Launch the Workshop Environment section later.

## Target audience

This workshop is intended mainly for Machine Learning Scientists/Engineers, Solution Architects, Data Scientists/Engineers, Prompt Engineers, Developers, and technical Founders.
This is a 400 level workshop. Participants should have basic familiarity with AWS services, command-line interfaces, and container technologies. A general understanding of cloud infrastructure concepts, domain management, and generative AI will be helpful for successful completion of this workshop.

## Duration

AWS Event : Approximately 1 hour (hands-on exploration of pre-deployed solution) Self-Paced : Approximately 2-3 hours (including deployment time)

## Cost

For self-paced learners running this workshop in your own AWS accounts, you are responsible for the cost of the AWS services used while running this Guidance. As of March, 2025 the cost for running this
Guidance with the default settings in the us-east-1 region is approximately under $380 per month .
We recommend creating a budget through AWS Cost Explorer to
help manage costs. Prices are subject to change. For full details, refer to the pricing webpage for each AWS service used in this Guidance.
[LINK: budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html)
For detailed cost estimates, refer Cost section for both ECS and EKS deployments.

## Supported Regions

As of March, 2025 'Guidance for Running Generative AI Gateway on AWS' is currently available for deployment in the following AWS Regions:
us-east-1, us-east-2, us-west-1, us-west-2, eu-west-3, ca-central-1, sa-east-1, eu-central-1, eu-west-1, eu-west-2, eu-west-3, eu-north-1, eu-south-1, eu-south-2, eu-central-2.

## Prerequisites

For self-paced learners, this section outlines the prerequisites required before deploying the GenAI Gateway in your AWS Account.
Please make sure you have the required permissions in your own self-managed AWS accounts to create, update and configure the below prerequisites.
- You will need an Integrated Development Environment (IDE) local/remote. For eg - leveraging AWS IDE Toolkits , AWS Cloudshell or similar IDE of your choice
[LINK: AWS IDE Toolkits](https://aws.amazon.com/developer/tools/)
- Required CLI Tools - Installation of necessary command line utilities
- Public Domain in Amazon Route 53 - Registration or configuration of a domain name
- Public Certificate via AWS Certificate Manager (ACM) - SSL/TLS certificate for secure communication
- Domain Ownership Validation - Verification of domain control for the certificate
- Amazon Bedrock Model Access - Grant access to foundational models you plan to use via GenAI Gateway
- Clone source code from GitHub repository - Download the required source code and configuration files

--------------------
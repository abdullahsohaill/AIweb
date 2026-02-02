# truss
**URL:** https://truss.baseten.co
**Page Title:** Developing a Model on Baseten - Baseten
--------------------

- Overview
- Quick start
- Why Baseten
- How Baseten works
- Concepts
- Overview Your first model Deploy custom Docker images Implementation Deploy and iterate Performance optimization Secrets Data and storage Python driven configuration for models 🆕
- Overview
- Your first model
- Deploy custom Docker images
- Implementation
- Deploy and iterate
- Performance optimization
- Secrets
- Data and storage
- Python driven configuration for models 🆕
- Concepts
- Deployments
- Environments
- Resources
- Autoscaling
- Concepts
- Call your model
- Streaming
- Async inference
- Integrations
- Overview
- Training on Baseten
- Getting started
- Lifecycle
- Management
- Loading Checkpoints
- Serving your trained model
- Organization settings
- Access control
- Teams 🆕
- API keys
[LINK: API keys](/organization/api-keys)
- Secrets
- Restricted environments
- Metrics
- Status and health
- Secure model inference
- Tracing
- Billing and usage
- Deployments
- Inference
- Support
- Return to Baseten

## ​ What does it mean to develop a model?

- Packaging your model code and weights :
Wrap your trained model into a structured project that includes your inference logic and dependencies.
- Configuring the model environment :
Define everything needed to run your model—from Python packages to system dependencies and secrets.
- Deploying and iterating quickly :
Push your model to Baseten in development mode and make live edits with instant feedback.

## ​ Development flow on Baseten

- Initialize a new model project using the Truss CLI.
- Add your model logic to a Python class (model.py), specifying how to load and run inference.
- Configure dependencies in a YAML or Python config.
- Deploy the model in development mode using truss push.
- Iterate fast with truss watch—live-reload your dev deployment as you make changes.
- Test and tune the model until it’s production-ready.
- Promote the model to production when you’re ready to scale.

## ​ What is Truss?

- Scaffold a new model project
- Serve models locally or in the cloud
- Package your code, config, and model files
- Push to Baseten for deployment
- Model frameworks like PyTorch, transformers, and diffusers
- Inference engines like TensorRT-LLM, SGLang, vLLM
- Serving technologies like Triton
- Any package installable with pip or apt

## ​ From model to server: the key components

- A Model class : This is where your model is loaded, preprocessed, run, and the results returned.
- A configuration file ( config.yaml or Python config): Defines the runtime environment, dependencies, and deployment settings.
- Optional extra assets , like model weights, secrets, or external packages.

## ​ Development vs. other deployments

- Development deployment Meant for iteration and testing. It supports live-reloading for quick feedback loops and will only scale to one replica , no autoscaling.
- All others deployments Stable, autoscaled, and ready for live traffic but don’t support live-reloading .
Was this page helpful?
[LINK: Previous](/development/model-apis/deprecation)
- What does it mean to develop a model?
- Development flow on Baseten
- What is Truss?
- From model to server: the key components
- Development vs. other deployments

--------------------
# llms.txt
**URL:** https://docs.ionq.com/llms.txt
**Page Title:** 
--------------------

### (Raw Extraction Fallback)

# IonQ Quantum Cloud Documentation

## Docs

- [null](https://docs.ionq.com/CLAUDE.md)
- [null](https://docs.ionq.com/GEMINI.md)
- [Get Backends](https://docs.ionq.com/api-reference/v0.3/backends/get-backends.md): Retrieve a list of all available backends.
- [Get a Characterization](https://docs.ionq.com/api-reference/v0.3/characterizations/get-a-characterization.md): This endpoint retrieves a characterization.
- [Get All Backend Characterizations](https://docs.ionq.com/api-reference/v0.3/characterizations/get-all-backend-characterizations.md): This endpoint retrieves an array of all available backend characterizations, with pagination.
- [Get the Most Recent Backend Characterization](https://docs.ionq.com/api-reference/v0.3/characterizations/get-the-most-recent-backend-characterization.md): This endpoint retrieves the most recent backend characterization data available.
- [API Core Concepts](https://docs.ionq.com/api-reference/v0.3/core-concepts.md)
- [v0.3 Error Codes](https://docs.ionq.com/api-reference/v0.3/error-codes.md)
- [Introduction](https://docs.ionq.com/api-reference/v0.3/introduction.md)
- [Cancel a Job](https://docs.ionq.com/api-reference/v0.3/jobs/cancel-a-job.md): Cancel the execution of a single job by ID.
- [Cancel many Jobs](https://docs.ionq.com/api-reference/v0.3/jobs/cancel-many-jobs.md): Cancel the execution of many jobs at once by passing a list of jobs.
- [Create a Job](https://docs.ionq.com/api-reference/v0.3/jobs/create-a-job.md): To submit a program to be simulated or executed on our quantum hardware, `POST` it to the `jobs` endpoint.
- [Delete a Job](https://docs.ionq.com/api-reference/v0.3/jobs/delete-a-job.md): Permanently delete a job from our service. This cannot be undone.
- [Delete many Jobs](https://docs.ionq.com/api-reference/v0.3/jobs/delete-many-jobs.md): Permanently remove many jobs from our platform. This cannot be undone.
- [Get a specific Job](https://docs.ionq.com/api-reference/v0.3/jobs/get-a-specific-job.md): Retrieve a specific job by UUID.
- [Get a Job's output](https://docs.ionq.com/api-reference/v0.3/jobs/get-a-specific-jobs-output.md): Retrieve a specific job's results by UUID.
- [Get Jobs](https://docs.ionq.com/api-reference/v0.3/jobs/get-jobs.md): **NOTE**: If request filters are provided, this endpoint will limit responses to 1 or more specific jobs based on those filters.<br /><br />
This endpoint retrieves all jobs this API key is authorized to view.

- [Migrating from old versions](https://docs.ionq.com/api-reference/v0.3/migrating-from-old-versions.md)
- [Multicircuit Jobs](https://docs.ionq.com/api-reference/v0.3/multicircuit-jobs.md): This guide covers everything from setting up a multicircuit job, submitting it to IonQ's backend, and retrieving the results.
- [Using native gates with the IonQ API](https://docs.ionq.com/api-reference/v0.3/native-gates-api.md): Learn how to use our hardware-native gateset to run a circuit with the IonQ API
- [Get an Organization’s Report](https://docs.ionq.com/api-reference/v0.3/reports/get-an-organizations-report.md): Get a usage report for the given organization from the start_date and end_date, detailing how much usage went to each QPU during that period. If no start_date or end_date are provided, period defaults to last 30 days until current time.
- [Writing Quantum Programs](https://docs.ionq.com/api-reference/v0.3/writing-quantum-programs.md)
- [Get a Characterization](https://docs.ionq.com/api-reference/v0.4/backends/get-a-characterization.md): Retrieve detailed performance data for a characterization.
- [Get a Backend](https://docs.ionq.com/api-reference/v0.4/backends/get-backend-by-name.md): Retrieve detailed information about a specific backend.
- [Get Backends](https://docs.ionq.com/api-reference/v0.4/backends/get-backends.md): List all available backends including QPUs and simulators.
- [Get All Backend Characterizations](https://docs.ionq.com/api-reference/v0.4/backends/get-characterizations.md): Retrieve historical characterizations for a backend.
- [API v0.4 Reference](https://docs.ionq.com/api-reference/v0.4/introduction.md): The IonQ Quantum Cloud API lets you submit quantum circuits, manage jobs, and access quantum computing resources programmatically. 
- [Cancel a job](https://docs.ionq.com/api-reference/v0.4/jobs/cancel-job.md): Stop the execution of job in queue.
- [null](https://docs.ionq.com/api-reference/v0.4/jobs/cancel-jobs.md): Cancel multiple jobs simultaneously.
- [null](https://docs.ionq.com/api-reference/v0.4/jobs/create-job.md): Submit a quantum circuit to run on a backend.
- [null](https://docs.ionq.com/api-reference/v0.4/jobs/delete-job.md): Permanently remove a job and its associated data.
- [null](https://docs.ionq.com/api-reference/v0.4/jobs/delete-jobs.md): Permanently remove multiple jobs and their data.
- [null](https://docs.ionq.com/api-reference/v0.4/jobs/get-job.md): Retrieve detailed information about a specific job.
- [null](https://docs.ionq.com/api-reference/v0.4/jobs/get-job-cost.md): Retrieve billing information for a specific job.
- [null](https://docs.ionq.com/api-reference/v0.4/jobs/get-job-estimate.md): Retrieve cost estimate for a job.
- [null](https://docs.ionq.com/api-reference/v0.4/jobs/get-jobs.md): List all jobs in your project with optional filtering.
- [null](https://docs.ionq.com/api-reference/v0.4/jobs/get-jobs-probabilities-aggregated.md): Retrieve aggregated probability results from jobs.
- [Migrating to API v0.4](https://docs.ionq.com/api-reference/v0.4/migration-from-v0.3.md): See what's new in API v0.4 and how to migrate from v0.3.
- [null](https://docs.ionq.com/api-reference/v0.4/sessions/create-session.md): Create a new session for quantum computing jobs.
- [null](https://docs.ionq.com/api-reference/v0.4/sessions/end-session.md): End a session by its id and cancel any incomplete jobs in queue
- [null](https://docs.ionq.com/api-reference/v0.4/sessions/get-session.md): Retrieve detailed information about a specific session.
- [null](https://docs.ionq.com/api-reference/v0.4/sessions/get-sessions.md): List and filter all sessions in your organization.
- [Get current key](https://docs.ionq.com/api-reference/v0.4/util/whoami.md): Gets information about the current token.
- [null](https://docs.ionq.com/guides/cloud-usage.md)
- [Connecting a SAML Identity Provider](https://docs.ionq.com/guides/connecting-saml-identity-providers.md): Enhance security and simplify user management by authenticating with your SAML-based SSO provider
- [Direct API Submissions](https://docs.ionq.com/guides/direct-api-submission.md): Learn how to submit jobs directly to the IonQ API v0.4
- [IonQ API Key Management with dotenv Integration](https://docs.ionq.com/guides/dotenv-project-api-keys.md): Discover how to effortlessly manage IonQ API keys across various projects by leveraging dotenv's automatic loading feature, enhancing security and codebase cleanliness.
- [Error Mitigation - Debiasing](https://docs.ionq.com/guides/error-mitigation-debiasing.md): Getting started with IonQ's built-in error mitigation
- [Native Gates](https://docs.ionq.com/guides/getting-started-with-native-gates.md): Getting started with IonQ's hardware-native gateset
- [Hosted Hybrid Service](https://docs.ionq.com/guides/hosted-hybrid-service.md): Run hybrid execution loops using functions managed by IonQ's Cloud.
- [Managing API keys](https://docs.ionq.com/guides/managing-api-keys.md): Learn how to create and manage your IonQ API keys for secure access through SDKs and APIs.
- [QPU Submission Checklist](https://docs.ionq.com/guides/qpu-submission-checklist.md): Things to do before submitting to IonQ's hardware systems.
- [Simulation with Noise Models](https://docs.ionq.com/guides/simulation-with-noise-models.md): Getting started with hardware noise model simulation
- [IonQ Documentation](https://docs.ionq.com/index.md): Welcome to IonQ's developer documentation! Get started, learn advanced techniques, and browse through our reference materials.
- [Amazon Braket](https://docs.ionq.com/partners/amazon-braket.md): Learn how to connect to IonQ products and services through AWS Braket
- [Azure Quantum](https://docs.ionq.com/partners/azure-quantum.md)
- [Google Cloud](https://docs.ionq.com/partners/google.md)
- [qBraid](https://docs.ionq.com/partners/qbraid.md): Learn how to connect to IonQ products and services through qBraid
- [Getting started with Cirq](https://docs.ionq.com/sdks/cirq/index.md): Learn how to use the Cirq SDK to submit quantum circuits to IonQ's simulators and quantum computers.
- [Using native gates with Cirq](https://docs.ionq.com/sdks/cirq/native-gates-cirq.md): Learn how to use our hardware-native gateset to run a circuit with Cirq
- [CUDA-Q](https://docs.ionq.com/sdks/cuda-q.md): Learn how to use NVIDIA's CUDA Quantum to submit quantum circuits to IonQ's simulators and quantum computers.
- [Quantum SDKs](https://docs.ionq.com/sdks/index.md): SDKs allow access to IonQ resources directly from within your code environment
- [PennyLane](https://docs.ionq.com/sdks/pennylane/index.md): Learn how to use PennyLane to submit quantum circuits to IonQ's simulators and quantum computers.
- [Using native gates with PennyLane](https://docs.ionq.com/sdks/pennylane/native-gates-pennylane.md): Learn how to use our hardware-native gateset to run a circuit with PennyLane
- [Getting started with qBraid](https://docs.ionq.com/sdks/qbraid/index.md): Learn how to use the qBraid-SDK to submit quantum circuits to IonQ's simulators and quantum computers.
- [Using native gates with qBraid](https://docs.ionq.com/sdks/qbraid/native-gates-qbraid.md): Learn how to use our hardware-native gateset to run a circuit with qBraid
- [Using debiasing with Qiskit](https://docs.ionq.com/sdks/qiskit/error-mitigation-qiskit.md): Learn how to use IonQ's error mitigation techniques with Qiskit
- [Getting started with Qiskit](https://docs.ionq.com/sdks/qiskit/index.md): Learn how to use the Qiskit SDK to submit quantum circuits to IonQ's simulators and quantum computers.
- [Compilation and native gates with Qiskit](https://docs.ionq.com/sdks/qiskit/native-gates-qiskit.md): Learn how to use our supported QIS gateset or hardware-native gateset to run a circuit with Qiskit
- [TensorFlow Quantum](https://docs.ionq.com/sdks/tensorflow.md): Learn how to use TensorFlow Quantum to connect your ML workflows to IonQ's simulators and quantum computers.
- [Your Account](https://docs.ionq.com/user-manual/accounts.md): Learn how to manage your IonQ account, including API keys, security settings, and access controls.
- [Backends](https://docs.ionq.com/user-manual/backends.md): Trapped-ion QPU hardware and QPU software simulators
- [Glossary](https://docs.ionq.com/user-manual/glossary.md): An glossary of IonQ Platform terminology
- [Introduction](https://docs.ionq.com/user-manual/introduction.md): Welcome to the IonQ Quantum Cloud
- [Jobs](https://docs.ionq.com/user-manual/jobs.md): Jobs are tasks running on IonQ systems, usually containing a circuit to run on a QPU.
- [Organizations](https://docs.ionq.com/user-manual/organizations.md)
- [Platform Systems](https://docs.ionq.com/user-manual/platform-systems.md): An overview of some of the systems that make up the IonQ Quantum Cloud Platform
- [Projects](https://docs.ionq.com/user-manual/projects.md): Projects are collaborative workspaces created in an organization to manage teams and resources.

## Optional

- [Join our Slack](https://join.slack.com/t/ionqcommunity/shared_invite/zt-2ohj4fkvb-ErVKebhkwaP7S~lt2Gq0_w)
- [Example Notebooks](https://github.com/ionq-samples/)
- [Other Resources](https://ionq.com/resources)


--------------------
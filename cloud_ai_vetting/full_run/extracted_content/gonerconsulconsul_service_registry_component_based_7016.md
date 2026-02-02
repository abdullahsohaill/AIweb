# goner/consul](./consul) - Service registry component based on [consul
**URL:** https://www.consul.io
**Page Title:** Consul | HashiCorp Developer
--------------------


## Service Networking Automations Across Clouds

- Install
- Tutorials
- Documentation

## What is Consul?

Consul is a service networking solution that enables teams to manage secure network connectivity between services, across on-prem, hybrid cloud, and multi-cloud environments and runtimes. Consul offers service discovery, service mesh, identity-based authorization, L7 traffic management, and secure service-to-service encryption.
[LINK: Learn more about Consul](/consul/docs/intro)

## Get Started

Learn how to use Consul for service discovery and service mesh operations.
- Get started with Consul on VMs
- Get started with Consul on Kubernetes
- Migrate a monolith with Consul and Nomad

## Sandbox

- Consul sandbox The Consul sandbox contains preinstalled tools and services for you to experiment with Consul.

## Introduction to Consul: Architecture and Concepts

- Control plane architecture Consul provides a control plane that enables you to register, access, and secure services deployed across your network.
- Data plane architecture Consul can deploy gateways and sidecar proxies in an application's data plane to help you secure, observe, and manage application traffic.
- Concept: Consul catalog The Consul catalog API tracks registered services and their locations for both service discovery and service mesh use cases.
- Concept: Cluster consensus Consul ensures a consistent state using the Raft protocol. A quorum, or a majority of server agents with one leader, agree to state changes before committing to the state log.
- Concept: Gossip communication Consul agents manage membership in datacenters and WAN federations using the Serf protocol, also called gossip communication.

## Consul Fundamentals

- Consul editions and releases Consul releases include Enterprise and Community editions. Additional tool binaries for managing Consul on specific runtimes and cloud providers is also available.
- How to install Consul Install Consul to get started with service discovery and service mesh. Follow the installation instructions to download the precompiled binary, or use Go to compile from source.
- Run Consul in developer mode Consul can deploy gateways and sidecar proxies in an application's data plane to help you secure, observe, and manage application traffic.
- Explore the Consul HTTP API The Consul HTTP API is a RESTful interface for Consul that exposes endpoints for both Consul operations and service networking functions that return JSON payloads.
- Explore the Consul CLI TThe Consul CLI is a wrapper for the HTTP API that allows you to interact with Consul from a terminal session.
- Explore the Consul UI The Consul UI allows you to interact with Consul using a browser-based graphical user interface.
- Identity in Consul In a datacenter, Consul uses identity to associate agents, configurations, and services on different nodes that may have different names but are otherwise identical.
- Consul agent basics The Consul agent is a long running daemon that operates on a node. It is a core unit of Consul operations.
- Service and health check basics Consul agents require service definitions in order to register services into the Consul catalog.
- Configuration entry basics Configuration entries explicitly define many of Consul's security, traffic, and cluster management behaviors.
- Consul Terraform provider basics You can use the official Terraform provider to configure your Consul cluster's ACLs, configuration entries, intentions, and more.

## Popular Use Cases

- 34min Register your services to Consul Deploy Consul client agents on your virtual machine workloads. Register  services to Consul and set up health checks. Consul
- Consul
- 25min Securely connect your services with Consul service mesh Deploy Consul service mesh and secure your applications using Envoy. Consul
- Consul
- 25min Access services in your service mesh Use Consul API Gateway to enable external access to services inside the mesh. Consul
- Consul
- 5 tutorials Connect services Register services and health checks to Consul. Consul
- Consul
- 4 tutorials Control network traffic Control service traffic patterns with canary deployments, service splitters, chaos engineering practices, and Consul API Gateway. Consul
- Consul
- 4 tutorials Secure services Secure service to service traffic in Consul service mesh using service intentions, both at L4 and L7 level, and Access Control Lists (ACLs) to avoid unidentified traffic. Include new services in Consul service mesh gradually using permissive mTLS. Consul
- Consul
- 4 tutorials Observe your network Consul observability features enhance your service mesh capabilities with  enriched metrics, logs, and distributed traces so you can improve performance  and debug your distributed services with precision. Consul
- Consul
- 2 tutorials Network automation Automate infrastructure changes based on changes to the Consul catalog using Consul-Terraform-Sync and  learn how Consul's built-in load balancing features help applications automatically adapt to changes in services. Consul
- Consul
- 4 tutorials Implement multi-tenancy Manage service tenancy with admin partitions, namespace, and cluster peering. Consul
- Consul

## Get Certified

- 3 tutorials Prepare for the Consul Associate (003) certification exam Prepare for your Consul Associate certification exam. Choose to follow an in-depth guide or to review select exam topics depending on the kind of preparation support you need. Then review sample questions to learn what to expect on exam day. Consul
- Consul

--------------------
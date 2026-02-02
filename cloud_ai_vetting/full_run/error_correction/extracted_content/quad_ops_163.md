# Quad Ops
**URL:** https://trly.github.io/quad-ops
**Page Title:** quad-ops | quad-ops
--------------------


## quad-ops #

## GitOps for Quadlet #

A cross-platform GitOps framework for container management with native service integration
Quad-Ops is a tool that helps you manage container deployments in a GitOps workflow. It watches Git repositories for standard Docker Compose files and automatically converts them into native service definitions for your platform:
- Linux : systemd + Podman Quadlet
[LINK: Podman Quadlet](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html)
- macOS : launchd (planned)

## What Makes Quad-Ops Different #

While Quad-Ops uses Docker Compose as its configuration format, there are some key differences from traditional Docker Compose deployments:
- GitOps-Based : Changes to containers are driven by Git repositories, not manual commands
- Cross-Platform : Automatically adapts to your platform’s native service manager (systemd on Linux, launchd on macOS)
- Native Integration : Containers are managed by your platform’s service manager, not a separate daemon
- Platform-Agnostic Models : Uses platform-neutral service definitions that render to platform-specific formats
- Automated Dependencies : Service relationships are automatically converted to native dependency directives
- Intelligent Restarts : Only restarts services that have changed and their dependents

## Key Features: #

- Monitor multiple Git repositories for container configurations
- Supports standard Docker Compose files (services, networks, volumes, secrets)
- Works in both system-wide and user (rootless) modes
- Automates deployment and management of container infrastructure

## How Quad-Ops Works #

Quad-Ops bridges the gap between Docker Compose and systemd by converting familiar Docker Compose configurations into Podman Quadlet units:
[LINK: Podman Quadlet](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html)

### The Conversion Process #

- Git Synchronization - Monitors repositories for Docker Compose file changes
- File Processing - Reads docker-compose.yml files and associated environment files
- Unit Generation - Converts services, volumes, and networks to .container , .volume , and .network Quadlet units
- systemd Integration - Loads units into systemd for native service management
- Dependency Resolution - Maps depends_on relationships to systemd After / Requires directives

### Why This Approach? #

- Familiar Configuration - Use standard Docker Compose files you already know
- systemd Benefits - Leverage systemd’s robust service management, logging, and dependency handling
- GitOps Workflow - All changes tracked in Git with rollback capability
- Podman Integration - Daemonless, rootless container execution with enhanced security

## Docker Compose Feature Support #

Quad-Ops converts Docker Compose version 3.x+ configurations into systemd-managed containers through Podman Quadlet . The following matrix shows which Docker Compose features are supported and how they’re implemented.
[LINK: Podman Quadlet](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html)

### Feature Support Matrix #

This matrix describes Docker Compose feature support for systemd-managed containers through Quad-Ops conversion:
✅ Native Quadlet Support - Features that map directly to Podman Quadlet directives for optimal systemd integration.
[LINK: Podman Quadlet](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html)
⚠️ PodmanArgs Implementation - Features implemented using Quadlet’s PodmanArgs directive, providing full functionality with some limitations.
❌ Unsupported - Docker-specific features incompatible with systemd container management.

## Compose Extensions #

Quad-Ops extends Docker Compose with powerful capabilities:
- Cross-project dependencies ( x-quad-ops-depends-on ) - Declare dependencies on services in other projects
- Environment secrets mapping for secure credential handling
- Strict naming validation - Project and service names follow Docker Compose specification exactly
- Volume extensions for advanced mount options
- Build extensions for enhanced build configurations
See Docker Compose Support for complete configuration examples and Cross-Project Dependencies for multi-project architectures.
[LINK: Docker Compose Support](docs/container-management/docker-compose-support)
[LINK: Cross-Project Dependencies](docs/container-management/cross-project-dependencies)

--------------------